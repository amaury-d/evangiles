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
TRANSLATIONS_CONFIG = ROOT / "data" / "translations.json"
OUTPUT = ROOT / "src" / "data" / "harmony.generated.json"
ASSETS_SOURCE = ROOT / "assets"
ASSETS_DEST = ROOT / "public" / "assets"


def main() -> None:
    if not DB.exists():
        raise SystemExit("Missing bible.db. Run python3 extractor/fetch_bible.py first.")

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    translations_config = json.loads(TRANSLATIONS_CONFIG.read_text(encoding="utf-8"))
    translations = [
        translation
        for translation in translations_config["translations"]
        if translation.get("enabled", True)
    ]
    default_translation = translations_config["default"]
    if not any(translation["code"] == default_translation for translation in translations):
        raise SystemExit(f"Default translation {default_translation!r} is not enabled in {TRANSLATIONS_CONFIG}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    ensure_multi_translation_schema(conn)

    generated = {
        "schema": config["schema"],
        "books": config["books"],
        "defaultTranslation": default_translation,
        "translations": translations,
        "chapters": [],
    }

    for chapter in config["chapters"]:
        generated_chapter = {k: v for k, v in chapter.items() if k != "sections"}
        generated_chapter["slug"] = f"chapitre-{chapter['number']}-{chapter['id']}"
        generated_chapter["sections"] = []

        for section in chapter["sections"]:
            generated_section = dict(section)
            generated_section["passages"] = build_passages(
                conn,
                section.get("refs", {}),
                translations,
                default_translation,
            )
            generated_chapter["sections"].append(generated_section)

        generated["chapters"].append(generated_chapter)

    validate_images(generated)
    copy_assets()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(generated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def ensure_multi_translation_schema(conn: sqlite3.Connection) -> None:
    columns = {
        row["name"]
        for row in conn.execute("PRAGMA table_info(versets)").fetchall()
    }
    if "translation" not in columns:
        raise SystemExit(
            "bible.db uses the old single-translation schema. "
            "Run make refresh-bible to rebuild it."
        )


def build_passages(
    conn: sqlite3.Connection,
    refs_by_book: dict[str, list[list[int]]],
    translations: list[dict[str, Any]],
    default_translation: str,
) -> list[dict[str, Any]]:
    passages: list[dict[str, Any]] = []
    for book, refs in refs_by_book.items():
        for chapter_id, start_verse, end_verse in refs:
            default_rows = fetch_passage_rows(
                conn,
                default_translation,
                book,
                chapter_id,
                start_verse,
                end_verse,
            )
            if not default_rows:
                raise SystemExit(f"Missing verses for {book} {chapter_id}:{start_verse}-{end_verse}")

            passage_translations: dict[str, Any] = {}
            for translation in translations:
                code = translation["code"]
                rows = fetch_passage_rows(
                    conn,
                    code,
                    book,
                    chapter_id,
                    start_verse,
                    end_verse,
                )
                fallback = False
                if len(rows) != len(default_rows):
                    rows = default_rows
                    fallback = code != default_translation

                passage_translations[code] = {
                    "title": rows[0]["titre"],
                    "fallback": fallback,
                    "fallbackTranslation": default_translation if fallback else None,
                    "verses": [
                        {
                            "number": row["verset_id"],
                            "title": row["titre"],
                            "text": row["texte"],
                        }
                        for row in rows
                    ],
                }

            passages.append(
                {
                    "book": book,
                    "chapter": chapter_id,
                    "startVerse": start_verse,
                    "endVerse": end_verse,
                    "translations": passage_translations,
                }
            )
    return passages


def fetch_passage_rows(
    conn: sqlite3.Connection,
    translation: str,
    book: str,
    chapter_id: int,
    start_verse: int,
    end_verse: int,
) -> list[sqlite3.Row]:
    return conn.execute(
        """
        SELECT verset_id, titre, texte
        FROM versets
        WHERE translation = ?
          AND evangeliste = ?
          AND chapitre_id = ?
          AND verset_id >= ?
          AND verset_id <= ?
        ORDER BY verset_id ASC
        """,
        (translation, book, chapter_id, start_verse, end_verse),
    ).fetchall()


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
    if ASSETS_DEST.exists():
        shutil.rmtree(ASSETS_DEST)
    ASSETS_DEST.mkdir(parents=True, exist_ok=True)
    for path in ASSETS_SOURCE.rglob("*"):
        if path.is_file() and path.name != "main.scss":
            target = ASSETS_DEST / path.relative_to(ASSETS_SOURCE)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)


if __name__ == "__main__":
    main()
