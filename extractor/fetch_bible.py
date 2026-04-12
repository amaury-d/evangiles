#!/usr/bin/env python3
"""Fetch Bible verses from the GetBible API and store them in a local SQLite database.

Usage:
    python3 extractor/fetch_bible.py [TRANSLATION]

Without TRANSLATION, enabled translations from data/translations.json are fetched.
TRANSLATION can be one code or a comma-separated list, for example "ls1910,darby".
See https://api.getbible.net/v2/translations.json for the full list.
"""

from __future__ import annotations

import json
import sqlite3
import sys
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "bible.db"
TRANSLATIONS_CONFIG = ROOT / "data" / "translations.json"

API_BASE = "https://api.getbible.net/v2"
USER_AGENT = "evangiles-refresh/1.0"

# Mapping from harmony.json book slugs to GetBible book numbers
BOOKS = {
    "matthieu": 40,
    "marc": 41,
    "luc": 42,
    "jean": 43,
    "actes": 44,
}


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def configured_translations() -> tuple[list[dict[str, Any]], str]:
    config = json.loads(TRANSLATIONS_CONFIG.read_text(encoding="utf-8"))
    translations = [
        translation
        for translation in config["translations"]
        if translation.get("enabled", True)
    ]
    default = config["default"]
    if not any(translation["code"] == default for translation in translations):
        raise SystemExit(f"Default translation {default!r} is not enabled in {TRANSLATIONS_CONFIG}")
    return translations, default


def selected_translations() -> tuple[list[dict[str, Any]], str]:
    translations, default = configured_translations()
    by_code = {translation["code"]: translation for translation in translations}
    if len(sys.argv) <= 1 or not sys.argv[1].strip():
        return translations, default

    selected_codes = [code.strip() for code in sys.argv[1].split(",") if code.strip()]
    selected: list[dict[str, Any]] = []
    for code in selected_codes:
        selected.append(
            by_code.get(
                code,
                {
                    "code": code,
                    "label": code,
                    "language": "unknown",
                    "enabled": True,
                },
            )
        )
    return selected, selected_codes[0]


def main() -> None:
    translations, default_translation = selected_translations()
    codes = ", ".join(translation["code"] for translation in translations)

    print(f"Fetching translation(s): {codes}")

    tmp_db = DB.with_suffix(".db.tmp")
    if tmp_db.exists():
        tmp_db.unlink()

    conn = sqlite3.connect(tmp_db)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS versets")
    cursor.execute("""
        CREATE TABLE versets (
            translation TEXT NOT NULL,
            evangeliste TEXT,
            chapitre_id INTEGER,
            verset_id INTEGER,
            titre TEXT,
            texte TEXT,
            UNIQUE(translation, evangeliste, chapitre_id, verset_id)
        )
    """)
    cursor.execute("""
        CREATE INDEX versets_lookup
        ON versets (translation, evangeliste, chapitre_id, verset_id)
    """)
    cursor.execute("DROP TABLE IF EXISTS translations")
    cursor.execute("""
        CREATE TABLE translations (
            code TEXT PRIMARY KEY,
            label TEXT,
            language TEXT
        )
    """)
    cursor.execute("DROP TABLE IF EXISTS metadata")
    cursor.execute("""
        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()

    for translation in translations:
        code = translation["code"]
        cursor.execute(
            "INSERT INTO translations (code, label, language) VALUES (?, ?, ?)",
            (code, translation.get("label", code), translation.get("language", "")),
        )

        for book_slug, book_nr in BOOKS.items():
            url = f"{API_BASE}/{code}/{book_nr}.json"
            print(f"  {code}: {book_slug} ({url})")
            data = fetch_json(url)

            for chapter in data["chapters"]:
                chapter_nr = chapter["chapter"]
                for verse in chapter["verses"]:
                    text = verse["text"].strip()
                    if text:
                        cursor.execute(
                            "INSERT INTO versets (translation, evangeliste, chapitre_id, verset_id, titre, texte) "
                            "VALUES (?, ?, ?, ?, '', ?)",
                            (code, book_slug, chapter_nr, verse["verse"], text),
                        )

        conn.commit()

    cursor.execute(
        "INSERT INTO metadata (key, value) VALUES ('default_translation', ?)",
        (default_translation,),
    )
    cursor.execute(
        "INSERT INTO metadata (key, value) VALUES ('translations', ?)",
        (",".join(translation["code"] for translation in translations),),
    )
    conn.commit()
    conn.close()
    tmp_db.replace(DB)

    print(f"Done. Wrote {DB.relative_to(ROOT)} (translation(s): {codes})")


if __name__ == "__main__":
    main()
