#!/usr/bin/env python3
"""Generate Astro markdown pages from annexes/*.md and _bibliography/*.bib."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "annexes"
BIB_DIR = ROOT / "_bibliography"
DEST = ROOT / "src" / "pages" / "annexes"
ANNEXES_JSON = ROOT / "src" / "data" / "annexes.generated.json"
LAYOUT = "../../layouts/AnnexeLayout.astro"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter dict, body) from a Jekyll markdown file."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm, match.group(2)


def parse_bib(text: str) -> list[dict[str, str]]:
    """Parse a .bib file into a list of entries with key/value fields."""
    entries: list[dict[str, str]] = []
    for match in re.finditer(
        r"@(\w+)\{([^,]+),\s*(.*?)\n\}", text, re.DOTALL
    ):
        entry: dict[str, str] = {"_type": match.group(1), "_key": match.group(2)}
        for field in re.finditer(
            r"(\w+)\s*=\s*(?:\{(.*?)\}|(\w+))(?:,|\s*$)", match.group(3), re.DOTALL
        ):
            entry[field.group(1)] = (field.group(2) or field.group(3)).strip()
        entries.append(entry)
    return entries


def bib_to_markdown(entries: list[dict[str, str]]) -> str:
    """Convert parsed bib entries to a markdown list."""
    lines: list[str] = []
    for e in entries:
        parts: list[str] = []
        if e.get("author"):
            parts.append(e["author"])
        if e.get("title"):
            title = re.sub(r"[{}]", "", e["title"])
            # Clean LaTeX accents: {\'e} -> é, etc.
            title = re.sub(r"\\'e", "é", title)
            title = re.sub(r"\\'a", "à", title)
            title = re.sub(r"\\`e", "è", title)
            # Collapse whitespace from multi-line bib values
            title = " ".join(title.split())
            url = e.get("hidden_url", "")
            if url:
                parts.append(f"*[{title}]({url})*")
            else:
                parts.append(f"*{title}*")
        if e.get("publisher"):
            parts.append(e["publisher"])
        if e.get("year"):
            parts.append(str(e["year"]))
        if e.get("pages"):
            parts.append(f"p. {e['pages']}")
        lines.append("- " + ", ".join(parts))
    return "\n".join(lines) + "\n"


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)

    annexes: list[dict[str, str]] = []

    # Process markdown annexes
    for md_path in sorted(SOURCE.glob("*.md")):
        if md_path.name == "index.md":
            continue

        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        title = fm.get("title", md_path.stem.capitalize())

        # Skip Jekyll-specific content (liquid includes etc.)
        if "{% include" in body or "{% raw" in body:
            continue

        slug = md_path.stem
        annexes.append({"slug": slug, "title": title})

        astro_fm = f"---\nlayout: {LAYOUT}\ntitle: \"{title}\"\n---\n"
        (DEST / f"{slug}.md").write_text(astro_fm + body, encoding="utf-8")

    # Process bibliography
    for bib_path in sorted(BIB_DIR.glob("*.bib")):
        text = bib_path.read_text(encoding="utf-8")
        entries = parse_bib(text)
        if not entries:
            continue
        slug = "bibliographie"
        annexes.append({"slug": slug, "title": "Bibliographie"})
        body = bib_to_markdown(entries)
        astro_fm = f"---\nlayout: {LAYOUT}\ntitle: \"Bibliographie\"\n---\n"
        (DEST / f"{slug}.md").write_text(astro_fm + body, encoding="utf-8")

    # Generate index page
    links = "\n".join(
        f'        <li><a href="/annexes/{a["slug"]}/">{a["title"]}</a></li>'
        for a in annexes
    )
    index = f"""---
import BaseLayout from "../../layouts/BaseLayout.astro";
import SiteShell from "../../components/SiteShell.astro";
---

<BaseLayout title="Annexes">
  <SiteShell currentSlug="annexes">
    <section class="annexe-page">
      <h1>Annexes</h1>
      <ul class="annexe-list">
{links}
      </ul>
    </section>
  </SiteShell>
</BaseLayout>
"""
    (DEST / "index.astro").write_text(index, encoding="utf-8")

    # Generate JSON for sidebar navigation
    ANNEXES_JSON.write_text(
        json.dumps(annexes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Built {len(annexes)} annexe(s) → {DEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
