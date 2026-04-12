#!/usr/bin/env python3
"""Migrate the legacy Python harmony data to JSON configuration."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY_EXTRACTOR = ROOT / "extractor"
OUTPUT = ROOT / "data" / "harmony.json"
BOOKS = ("matthieu", "marc", "luc", "jean", "actes")


def main() -> None:
    sys.path.insert(0, str(LEGACY_EXTRACTOR))
    from harmonie import harmonie  # type: ignore

    chapters = []
    for chapter_index, legacy_chapter in enumerate(harmonie, start=1):
        chapter = {
            "id": legacy_chapter["titre_short"],
            "number": chapter_index,
            "title": legacy_chapter["titre"],
            "sections": [],
        }
        copy_optional_fields(legacy_chapter, chapter)

        for section_index, legacy_section in enumerate(legacy_chapter["contenu"], start=1):
            section = {
                "id": f"{chapter['id']}-{section_index}",
                "title": legacy_section["titre"],
                "refs": refs_by_book(legacy_section["contenu"]),
            }
            copy_optional_fields(legacy_section, section)
            chapter["sections"].append(section)

        chapters.append(chapter)

    payload = {
        "schema": 1,
        "books": list(BOOKS),
        "chapters": chapters,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def copy_optional_fields(source: dict, target: dict) -> None:
    for field in ("date", "lieu", "notes", "images"):
        if field in source:
            target[field] = source[field]


def refs_by_book(raw_refs: list | None) -> dict[str, list[list[int]]]:
    if raw_refs is None:
        return {}

    refs: dict[str, list[list[int]]] = {}
    for book, groups in zip(BOOKS, raw_refs):
        if not groups:
            continue
        refs[book] = [list(group) for group in groups if group]
    return refs


if __name__ == "__main__":
    main()
