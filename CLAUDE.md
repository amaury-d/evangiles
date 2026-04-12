# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Static site presenting a personal chronological harmony of the Gospels (Matthew, Mark, Luke, John, Acts). Built with Astro, fed from a SQLite database of TOB Bible verses and a hand-curated harmony configuration.

The site is in French. Published at https://evangiles.decre.me/.

## Build pipeline

The data flows in one direction:

1. `bible.db` (SQLite, committed) contains TOB verses, populated by `extractor/fetch_tob.py`
2. `data/harmony.json` is the **single source of truth** for the harmony: chapter order, sections, biblical references, dates, places, images, and notes
3. `scripts/build_site_data.py` reads both, validates images and verses, writes `src/data/harmony.generated.json` and copies `assets/` to `public/assets/`
4. Astro reads the generated JSON and produces the static site in `dist/`

**Generated files** (do not edit directly): `src/data/harmony.generated.json`, `public/assets/`, `dist/`, `.astro/`

## Commands

```sh
npm install              # install Node dependencies
make                     # full build: generate data + build Astro site
make serve               # dev server (runs build_site_data.py first via predev hook)
make clean               # remove all generated outputs
make refresh-bible       # re-scrape TOB into bible.db (fragile, use sparingly)
npm run build            # just Astro build (runs build_site_data.py via prebuild hook)
```

## Validation

Run `npm run build` before concluding any change. For data changes, check that `scripts/build_site_data.py` reports no missing verses or images.

## Data format

In `data/harmony.json`, biblical references are keyed by book slug (`matthieu`, `marc`, `luc`, `jean`, `actes`) and use triplets `[chapter, start_verse, end_verse]`. The `bible.db` table is `versets` with columns `evangeliste`, `chapitre_id`, `verset_id`, `titre`, `texte`.

## Astro site structure

- `src/layouts/BaseLayout.astro` — HTML shell, imports global CSS
- `src/components/SiteShell.astro` — sidebar navigation + main content slot
- `src/components/SectionBlock.astro` — renders one harmony section (metadata, images, passages, notes)
- `src/components/Passage.astro` — renders verses for a single biblical passage
- `src/pages/index.astro` — home page with chapter index
- `src/pages/evangiles/[chapter].astro` — dynamic route generating one page per chapter via `getStaticPaths`
- `src/styles/main.css` — global styles

## Deployment

GitHub Actions workflow `.github/workflows/deploy-pages.yml` builds and publishes `dist/` to GitHub Pages.
