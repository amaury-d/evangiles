# Graph Report - .  (2026-04-20)

## Corpus Check
- Large corpus: 53 files · ~660,841 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 125 nodes · 221 edges · 15 communities detected
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 50 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Gospel Journey Maps|Gospel Journey Maps]]
- [[_COMMUNITY_Build Pipeline & Data|Build Pipeline & Data]]
- [[_COMMUNITY_Chapter Maps (SVG)|Chapter Maps (SVG)]]
- [[_COMMUNITY_Annexes Migration|Annexes Migration]]
- [[_COMMUNITY_Map Generation|Map Generation]]
- [[_COMMUNITY_Jerusalem Sites|Jerusalem Sites]]
- [[_COMMUNITY_Judea & Desert|Judea & Desert]]
- [[_COMMUNITY_TOB Bible Extractor|TOB Bible Extractor]]
- [[_COMMUNITY_Agent Instructions|Agent Instructions]]
- [[_COMMUNITY_Astro Site Config|Astro Site Config]]
- [[_COMMUNITY_Annex Build Script|Annex Build Script]]
- [[_COMMUNITY_Astro Config (duplicate)|Astro Config (duplicate)]]
- [[_COMMUNITY_Site Data Generator|Site Data Generator]]
- [[_COMMUNITY_Greek Terms|Greek Terms]]
- [[_COMMUNITY_Google Verification|Google Verification]]

## God Nodes (most connected - your core abstractions)
1. `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` - 22 edges
2. `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie` - 16 edges
3. `Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale)` - 16 edges
4. `Jérusalem` - 15 edges
5. `Galilée` - 12 edges
6. `Carte Chapitre 7 : Ministère en Galilée` - 11 edges
7. `main()` - 10 edges
8. `main()` - 9 edges
9. `Judée` - 9 edges
10. `Carte Chapitre 6 : Jésus et Jean en Judée` - 8 edges

## Surprising Connections (you probably didn't know these)
- `copy_assets()` --shares_data_with--> `public/assets/maps/README.md — (copy) map sources and conventions`  [INFERRED]
  scripts/build_site_data.py → public/assets/maps/README.md
- `main()` --shares_data_with--> `src/pages/annexes/apocryphes.md — Astro annexe on apocryphal gospels`  [EXTRACTED]
  scripts/build_annexes.py → src/pages/annexes/apocryphes.md
- `main()` --shares_data_with--> `src/pages/annexes/bibliographie.md — Astro bibliography annexe`  [EXTRACTED]
  scripts/build_annexes.py → src/pages/annexes/bibliographie.md
- `main()` --shares_data_with--> `src/data/annexes.generated.json — generated annexe index`  [EXTRACTED]
  scripts/build_annexes.py → src/data/annexes.generated.json
- `main()` --shares_data_with--> `src/data/harmony.generated.json — generated enriched harmony data`  [EXTRACTED]
  scripts/build_site_data.py → src/data/harmony.generated.json

## Hyperedges (group relationships)
- **Main Data Build Pipeline** — translations_json, fetch_bible_script, bible_db, harmony_json, greek_terms_json, build_site_data_script, harmony_generated_json, generate_maps_script [EXTRACTED 1.00]
- **Jekyll-to-Astro Annexes Migration Pipeline** — annexes_marc_legacy, annexes_apocryphes_legacy, build_annexes_script, pages_annexes_marc, pages_annexes_apocryphes, pages_annexes_bibliographie, annexes_generated_json [EXTRACTED 1.00]
- **Map Generation Pipeline** — map_source_palestine_svg, map_source_jerusalem_jpg, generate_maps_script, assets_maps_readme [EXTRACTED 1.00]
- **Route narrative Chapitre 2 : Bethléem → Égypte → Nazareth → Jérusalem** — place_bethleem, place_egypte, place_nazareth, place_jerusalem [EXTRACTED 1.00]
- **Route narrative Chapitre 3 : Jourdain → Désert de Judée** — place_jourdain, place_desert_judee [EXTRACTED 1.00]
- **Route narrative Chapitre 5 : Béthanie → Cana → Capharnaüm** — place_bethanie_jourdain, place_cana, place_capharnaum [EXTRACTED 1.00]
- **Route narrative Chapitre 6 : Jérusalem → Judée → Samarie → Galilée** — place_jerusalem, place_judee, place_ainon, place_sychar, place_samarie, place_galilee [EXTRACTED 1.00]
- **Traversée du lac : Rive ouest → Rive est (Gadaréniens) → Capharnaüm** — place_rive_ouest_lac, place_rive_est_lac, place_capharnaum [EXTRACTED 1.00]
- **Lieux du ministère en Galilée (Chapitre 7)** — place_galilee, place_capharnaum, place_lac_tibériade, place_cana, place_nain, place_nazareth, place_gadara [EXTRACTED 1.00]
- **Sites de Jérusalem au Second Temple (Chapitre 8)** — place_jerusalem, place_piscine_bethesda, place_temple_jerusalem [EXTRACTED 1.00]
- **Toutes les cartes générées dérivent de la base Holy Sites** — map_ch02_naissance_jeunesse, map_ch03_debut_ministere_judee, map_ch04_bethanie, map_ch05_galilee, map_ch06_judee_samarie, map_ch07_galilee, map_ch07_traversee_lac, map_ch08_jerusalem, map_source_holy_sites [EXTRACTED 1.00]
- **Séquence cartographique des itinéraires évangéliques (Cartes 4-5-6)** — carte4_map, carte5_map, carte6_map, theme_gospel_journeys [INFERRED 0.95]
- **Groupe géographique : Mer de Galilée et environnants** — place_mer_galilee, place_galilee, vue_genezareth_photo, genezareth_roadmap, place_capernaum, place_bethsaide, place_tiberiade [INFERRED 0.90]
- **Groupe géographique : Jérusalem et ses environs immédiats** — place_jerusalem, place_bethanie, place_mont_oliviers, place_bethphage, place_vallee_cedron, jerusalem_premier_siecle_plan, place_antonia, place_temple [INFERRED 0.90]
- **Contexte géographique Nouveau Testament — Terre Sainte** — map_holy_land, carte4_map, carte5_map, carte6_map, theme_holy_land_nt, desert_judee_photo, jerusalem_premier_siecle_plan [INFERRED 0.85]

## Communities

### Community 0 - "Gospel Journey Maps"
Cohesion: 0.15
Nodes (25): Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif), Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie, Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale), Carte routière moderne de la région de Génézareth / Mer de Galilée, La Terre Sainte à l'époque du Nouveau Testament — carte générale, Béthanie, Bethphagé, Bethsaïde (+17 more)

### Community 1 - "Build Pipeline & Data"
Cohesion: 0.13
Nodes (21): bible.db — SQLite multi-translation Bible database, build_passages(), copy_assets(), ensure_multi_translation_schema(), fetch_passage_rows(), main(), validate_images(), configured_translations() (+13 more)

### Community 2 - "Chapter Maps (SVG)"
Cohesion: 0.21
Nodes (21): Carte Chapitre 2 : Naissance et jeunesse de Jésus, Carte Chapitre 3 : Début du ministère en Judée, Carte Chapitre 4 : Jean le Baptiste à Béthanie, Carte Chapitre 5 : Jésus en Galilée, Carte Chapitre 7 : Ministère en Galilée, Carte Chapitre 7 : Traversée du lac, Holy Sites of Jesus in Palestine (base cartographique CC0), Béthanie au-delà du Jourdain (+13 more)

### Community 3 - "Annexes Migration"
Cohesion: 0.18
Nodes (15): annexes/apocryphes.md — legacy Jekyll annex on apocryphal gospels, src/data/annexes.generated.json — generated annexe index, annexes/harmonie.md — legacy Jekyll harmony source annex, annexes/index.md — legacy Jekyll annexe index, annexes/marc.md — legacy Jekyll annex on the Gospel of Mark, bib_to_markdown(), main(), parse_bib() (+7 more)

### Community 4 - "Map Generation"
Cohesion: 0.23
Nodes (11): assets/maps/README.md — map sources and conventions, generate_map(), generate_raster_map(), main(), generate_maps.py — SVG map generator, Jerusalem_premier_siecle.JPG — Jerusalem 1st century raster source, Holy_sites_of_Jesus_in_Palestine.svg — CC0 cartographic base, public/assets/maps/README.md — (copy) map sources and conventions (+3 more)

### Community 5 - "Jerusalem Sites"
Cohesion: 0.31
Nodes (9): Plan de Jérusalem au premier siècle — Temple, Antonia, murs, citadelle, Carte Chapitre 8 : Jérusalem au temps du Second Temple, Forteresse Antonia (Jérusalem 1er siècle), Jérusalem, Piscine de Bethesda, Temple de Jérusalem (1er siècle), Temple de Jérusalem, Vallée du Cédron (+1 more)

### Community 6 - "Judea & Desert"
Cohesion: 0.38
Nodes (7): Désert de Judée — paysage aride et rocheux, Carte Chapitre 6 : Jésus et Jean en Judée, Aïnon, Judée, Samarie, Sychar (Samarie), Thème : désert et lieu de retraite spirituelle

### Community 7 - "TOB Bible Extractor"
Cohesion: 1.0
Nodes (0): 

### Community 8 - "Agent Instructions"
Cohesion: 1.0
Nodes (2): AGENTS.md — repository instructions for agents, CLAUDE.md — project guidance for Claude Code

### Community 9 - "Astro Site Config"
Cohesion: 1.0
Nodes (2): astro.config.mjs — Astro site configuration, Mon harmonie des Évangiles (project overview)

### Community 10 - "Annex Build Script"
Cohesion: 1.0
Nodes (2): build_annexes.py — Jekyll-to-Astro annexe converter, Rationale: annexes/ are a Jekyll legacy migrated to Astro via build_annexes.py

### Community 11 - "Astro Config (duplicate)"
Cohesion: 1.0
Nodes (0): 

### Community 12 - "Site Data Generator"
Cohesion: 1.0
Nodes (1): build_site_data.py — generates harmony.generated.json

### Community 13 - "Greek Terms"
Cohesion: 1.0
Nodes (1): data/greek_terms.json — Greek theological term definitions

### Community 14 - "Google Verification"
Cohesion: 1.0
Nodes (1): google7be578b7e788ac0e.html — Google Search Console verification

## Knowledge Gaps
- **32 isolated node(s):** `Return (frontmatter dict, body) from a Jekyll markdown file.`, `Parse a .bib file into a list of entries with key/value fields.`, `Convert parsed bib entries to a markdown list.`, `Mon harmonie des Évangiles (project overview)`, `CLAUDE.md — project guidance for Claude Code` (+27 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `TOB Bible Extractor`** (2 nodes): `fetch_tob.py`, `insert_verset()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Agent Instructions`** (2 nodes): `AGENTS.md — repository instructions for agents`, `CLAUDE.md — project guidance for Claude Code`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Astro Site Config`** (2 nodes): `astro.config.mjs — Astro site configuration`, `Mon harmonie des Évangiles (project overview)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Annex Build Script`** (2 nodes): `build_annexes.py — Jekyll-to-Astro annexe converter`, `Rationale: annexes/ are a Jekyll legacy migrated to Astro via build_annexes.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Astro Config (duplicate)`** (1 nodes): `astro.config.mjs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Site Data Generator`** (1 nodes): `build_site_data.py — generates harmony.generated.json`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Greek Terms`** (1 nodes): `data/greek_terms.json — Greek theological term definitions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Google Verification`** (1 nodes): `google7be578b7e788ac0e.html — Google Search Console verification`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` connect `Gospel Journey Maps` to `Chapter Maps (SVG)`, `Jerusalem Sites`, `Judea & Desert`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Why does `Jérusalem` connect `Jerusalem Sites` to `Gospel Journey Maps`, `Chapter Maps (SVG)`, `Judea & Desert`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `Galilée` connect `Chapter Maps (SVG)` to `Gospel Journey Maps`, `Judea & Desert`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` (e.g. with `Thème : itinéraires de Jésus dans les Évangiles` and `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie`) actually correct?**
  _`Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie` (e.g. with `Thème : itinéraires de Jésus dans les Évangiles` and `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)`) actually correct?**
  _`Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale)` (e.g. with `Thème : itinéraires de Jésus dans les Évangiles` and `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)`) actually correct?**
  _`Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Jérusalem` (e.g. with `Judée` and `La Terre Sainte à l'époque du Nouveau Testament — carte générale`) actually correct?**
  _`Jérusalem` has 3 INFERRED edges - model-reasoned connections that need verification._