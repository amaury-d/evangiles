#!/usr/bin/env python3
"""Fetch Bible verses from the GetBible API and store them in a local SQLite database.

Usage:
    python3 extractor/fetch_bible.py [TRANSLATION]

TRANSLATION defaults to "ls1910" (Louis Segond 1910).
Other examples: "darby", "kjv", "asv".
See https://api.getbible.net/v2/translations.json for the full list.
"""

from __future__ import annotations

import json
import sqlite3
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "bible.db"

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


def main() -> None:
    translation = sys.argv[1] if len(sys.argv) > 1 else "ls1910"

    print(f"Fetching translation: {translation}")

    tmp_db = DB.with_suffix(".db.tmp")
    if tmp_db.exists():
        tmp_db.unlink()

    conn = sqlite3.connect(tmp_db)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS versets")
    cursor.execute("""
        CREATE TABLE versets (
            evangeliste TEXT,
            chapitre_id INTEGER,
            verset_id INTEGER,
            titre TEXT,
            texte TEXT,
            UNIQUE(evangeliste, chapitre_id, verset_id)
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

    for book_slug, book_nr in BOOKS.items():
        url = f"{API_BASE}/{translation}/{book_nr}.json"
        print(f"  {book_slug} ({url})")
        data = fetch_json(url)

        for chapter in data["chapters"]:
            chapter_nr = chapter["chapter"]
            for verse in chapter["verses"]:
                text = verse["text"].strip()
                if text:
                    cursor.execute(
                        "INSERT INTO versets (evangeliste, chapitre_id, verset_id, titre, texte) "
                        "VALUES (?, ?, ?, '', ?)",
                        (book_slug, chapter_nr, verse["verse"], text),
                    )

        conn.commit()

    # Store metadata about the translation
    cursor.execute(
        "INSERT INTO metadata (key, value) VALUES ('translation', ?)", (translation,)
    )
    conn.commit()
    conn.close()
    tmp_db.replace(DB)

    print(f"Done. Wrote {DB.relative_to(ROOT)} (translation: {translation})")


if __name__ == "__main__":
    main()
