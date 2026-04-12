#!/usr/bin/env python3
"""Build enriched site data from harmony config and the local Bible database."""

from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "bible.db"
CONFIG = ROOT / "data" / "harmony.json"
OUTPUT = ROOT / "src" / "data" / "harmony.generated.json"
ASSETS_SOURCE = ROOT / "assets"
ASSETS_DEST = ROOT / "public" / "assets"


def main() -> None:
    if not DB.exists():
        raise SystemExit("Missing bible.db. Run python3 extractor/fetch_bible.py first.")

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    generated = {
        "schema": config["schema"],
        "books": config["books"],
        "chapters": [],
    }

    for chapter in config["chapters"]:
        generated_chapter = {k: v for k, v in chapter.items() if k != "sections"}
        generated_chapter["slug"] = f"chapitre-{chapter['number']}-{chapter['id']}"
        generated_chapter["sections"] = []

        for section in chapter["sections"]:
            generated_section = dict(section)
            generated_section["passages"] = build_passages(conn, section.get("refs", {}))
            generated_chapter["sections"].append(generated_section)

        generated["chapters"].append(generated_chapter)

    validate_images(generated)
    copy_assets()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(generated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def build_passages(conn: sqlite3.Connection, refs_by_book: dict[str, list[list[int]]]) -> list[dict[str, Any]]:
    passages: list[dict[str, Any]] = []
    for book, refs in refs_by_book.items():
        for chapter_id, start_verse, end_verse in refs:
            rows = conn.execute(
                """
                SELECT verset_id, titre, texte
                FROM versets
                WHERE evangeliste = ?
                  AND chapitre_id = ?
                  AND verset_id >= ?
                  AND verset_id <= ?
                ORDER BY verset_id ASC
                """,
                (book, chapter_id, start_verse, end_verse),
            ).fetchall()
            if not rows:
                raise SystemExit(f"Missing verses for {book} {chapter_id}:{start_verse}-{end_verse}")

            passages.append(
                {
                    "book": book,
                    "chapter": chapter_id,
                    "startVerse": start_verse,
                    "endVerse": end_verse,
                    "title": rows[0]["titre"],
                    "verses": [
                        {
                            "number": row["verset_id"],
                            "title": row["titre"],
                            "text": row["texte"],
                        }
                        for row in rows
                    ],
                }
            )
    return passages


def validate_images(generated: dict[str, Any]) -> None:
    image_names: set[str] = set()
    for chapter in generated["chapters"]:
        image_names.update((chapter.get("images") or {}).keys())
        for section in chapter["sections"]:
            image_names.update((section.get("images") or {}).keys())

    missing = sorted(name for name in image_names if not (ASSETS_SOURCE / name).exists())
    if missing:
        raise SystemExit("Missing assets: " + ", ".join(missing))


def copy_assets() -> None:
    ASSETS_DEST.mkdir(parents=True, exist_ok=True)
    for path in ASSETS_SOURCE.iterdir():
        if path.is_file() and path.name != "main.scss":
            shutil.copy2(path, ASSETS_DEST / path.name)


if __name__ == "__main__":
    main()
