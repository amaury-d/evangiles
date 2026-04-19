# CLAUDE.md

Guidance for Claude Code (claude.ai/code) working in this repo.

## Project overview

Static site: personal chronological Gospel harmony (Matthew, Mark, Luke, John, Acts). Built with Astro. Data from multi-translation SQLite Bible DB + hand-curated harmony config.

Site in French. Published at https://evangiles.decre.me/.

## Build pipeline

Data flows one direction:

1. `data/translations.json` declares enabled GetBible translations + default
2. `bible.db` (SQLite, committed) holds Bible verses with `translation` column, populated by `extractor/fetch_bible.py`
3. `data/harmony.json` — **single source of truth**: chapter order, sections, refs, dates, places, images, notes
4. `data/greek_terms.json` stores theological/Greek term definitions + detection labels
5. `scripts/build_site_data.py` reads inputs, validates images/verses, writes `src/data/harmony.generated.json`, copies `assets/` to `public/assets/`
6. Astro reads generated JSON, produces static site in `dist/`

**Generated files** (do not edit directly): `src/data/harmony.generated.json`, `public/assets/`, `dist/`, `.astro/`

## Commands

```sh
npm install              # install Node dependencies
make                     # full build: generate data + build Astro site
make serve               # dev server (runs build_site_data.py first via predev hook)
make clean               # remove all generated outputs
make refresh-bible       # rebuild bible.db from all enabled GetBible translations
make refresh-bible TRANSLATION=darby
npm run build            # just Astro build (runs build_site_data.py via prebuild hook)
```

## Validation

Run `npm run build` before concluding any change. For data changes, check `scripts/build_site_data.py` reports no missing verses or images.

## Data format

In `data/harmony.json`, refs keyed by book slug (`matthieu`, `marc`, `luc`, `jean`, `actes`), triplets `[chapter, start_verse, end_verse]`. `bible.db` table is `versets`, columns: `translation`, `evangeliste`, `chapitre_id`, `verset_id`, `titre`, `texte`.

## Astro site structure

- `src/layouts/BaseLayout.astro` — HTML shell, imports global CSS
- `src/components/SiteShell.astro` — sidebar nav + main content slot
- `src/components/SectionBlock.astro` — renders one harmony section (metadata, images, passages, notes)
- `src/components/Passage.astro` — renders verses for single biblical passage
- `src/pages/index.astro` — home page with chapter index
- `src/pages/evangiles/[chapter].astro` — dynamic route, one page per chapter via `getStaticPaths`
- `src/styles/main.css` — global styles

## Maps

Use `assets/maps/sources/Holy_sites_of_Jesus_in_Palestine.svg` as cartographic base. From Wikimedia Commons, CC0 1.0. Project-derived maps go in `assets/maps/generated/`, preferably SVG. Reference from `data/harmony.json` with paths relative to `assets/`, e.g. `maps/generated/chapitre-06-judee.svg`.

Generate scripted maps with `python3 scripts/generate_maps.py`. When generated SVG needs changes, update script — don't edit generated SVG by hand.

One chapter map when narrative stays same geographic scale. Multiple maps (by section or section group) when story changes place, scale, or geographic focus. Numbered markers by default. Arrows only when biblical text explicitly describes movement or route.

## Deployment

GitHub Actions `.github/workflows/deploy-pages.yml` builds + publishes `dist/` to GitHub Pages.

## Context Navigation (Graphify)

### 3-Layer Query Rule
1. **First:** query `graphify-out/graph.json` or `graphify-out/wiki/index.md`
   to understand code structure and connections
2. **Second:** query the Obsidian vault for decisions, progress, and project context
3. **Third:** only read raw code files when editing
   or when the first two layers don't have the answer

### When to rebuild the graph
- After structural changes (new modules, major refactors)
- Command: `graphify . --update` (only processes modified files)
- Graph is persistent — NO need to rebuild every session

### Do NOT
- Don't manually modify files inside `graphify-out/`
- Don't re-read entire codebase if graph already has the information