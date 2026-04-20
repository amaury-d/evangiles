# Graph Report - /Users/amaury/git/evangiles  (2026-04-20)

## Corpus Check
- 6 files · ~938,440 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 115 nodes · 194 edges · 21 communities detected
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 50 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]

## God Nodes (most connected - your core abstractions)
1. `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` - 22 edges
2. `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie` - 16 edges
3. `Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale)` - 16 edges
4. `Jérusalem` - 15 edges
5. `Galilée` - 12 edges
6. `Carte Chapitre 7 : Ministère en Galilée` - 11 edges
7. `build_annexes.main — converts annexes/*.md and .bib to Astro pages` - 9 edges
8. `Judée` - 9 edges
9. `Carte Chapitre 6 : Jésus et Jean en Judée` - 8 edges
10. `Holy Sites of Jesus in Palestine (base cartographique CC0)` - 8 edges

## Surprising Connections (you probably didn't know these)
- `astro.config.mjs — Astro site configuration` --conceptually_related_to--> `Mon harmonie des Évangiles (project overview)`  [INFERRED]
  astro.config.mjs → README.md
- `build_annexes.main — converts annexes/*.md and .bib to Astro pages` --shares_data_with--> `src/pages/annexes/apocryphes.md — Astro annexe on apocryphal gospels`  [EXTRACTED]
  scripts/build_annexes.py → src/pages/annexes/apocryphes.md
- `build_annexes.main — converts annexes/*.md and .bib to Astro pages` --shares_data_with--> `src/pages/annexes/bibliographie.md — Astro bibliography annexe`  [EXTRACTED]
  scripts/build_annexes.py → src/pages/annexes/bibliographie.md
- `build_annexes.main — converts annexes/*.md and .bib to Astro pages` --shares_data_with--> `src/data/annexes.generated.json — generated annexe index`  [EXTRACTED]
  scripts/build_annexes.py → src/data/annexes.generated.json
- `build_site_data.main — reads harmony.json, queries DB, writes generated JSON` --shares_data_with--> `src/data/harmony.generated.json — generated enriched harmony data`  [EXTRACTED]
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

### Community 0 - "Community 0"
Cohesion: 0.17
Nodes (22): Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif), Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie, Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale), Carte routière moderne de la région de Génézareth / Mer de Galilée, Béthanie, Bethphagé, Bethsaïde, Capharnaüm (+14 more)

### Community 1 - "Community 1"
Cohesion: 0.15
Nodes (17): bible.db — SQLite multi-translation Bible database, build_site_data.build_passages — queries bible.db for multi-translation passages, build_site_data.main — reads harmony.json, queries DB, writes generated JSON, build_site_data.validate_images — checks assets exist, fetch_bible.configured_translations — reads enabled translations from config, fetch_bible.main — orchestrates DB rebuild from GetBible, fetch_bible.py — GetBible API extractor, fetch_bible.selected_translations — filters by CLI args (+9 more)

### Community 2 - "Community 2"
Cohesion: 0.23
Nodes (12): annexes/apocryphes.md — legacy Jekyll annex on apocryphal gospels, src/data/annexes.generated.json — generated annexe index, annexes/harmonie.md — legacy Jekyll harmony source annex, annexes/index.md — legacy Jekyll annexe index, annexes/marc.md — legacy Jekyll annex on the Gospel of Mark, build_annexes.bib_to_markdown — formats bib entries as markdown list, build_annexes.main — converts annexes/*.md and .bib to Astro pages, build_annexes.parse_bib — parses .bib files into dicts (+4 more)

### Community 3 - "Community 3"
Cohesion: 0.32
Nodes (12): Carte Chapitre 3 : Début du ministère en Judée, Carte Chapitre 4 : Jean le Baptiste à Béthanie, Carte Chapitre 5 : Jésus en Galilée, Carte Chapitre 6 : Jésus et Jean en Judée, Holy Sites of Jesus in Palestine (base cartographique CC0), Aïnon, Béthanie au-delà du Jourdain, Désert de Judée (+4 more)

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (10): Carte Chapitre 2 : Naissance et jeunesse de Jésus, Carte Chapitre 8 : Jérusalem au temps du Second Temple, Bethléem, Égypte, Jérusalem, Mont des Oliviers, Nazareth, Piscine de Bethesda (+2 more)

### Community 5 - "Community 5"
Cohesion: 0.42
Nodes (10): Carte Chapitre 7 : Ministère en Galilée, Carte Chapitre 7 : Traversée du lac, Cana, Capharnaüm, Gadara, Galilée, Lac de Tibériade, Naïn (+2 more)

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (6): assets/maps/README.md — map sources and conventions, build_site_data.copy_assets — copies assets/ to public/assets/, Jerusalem_premier_siecle.JPG — Jerusalem 1st century raster source, Holy_sites_of_Jesus_in_Palestine.svg — CC0 cartographic base, public/assets/maps/README.md — (copy) map sources and conventions, Rationale: only CC0 map sources allowed

### Community 7 - "Community 7"
Cohesion: 0.83
Nodes (3): generate_map(), generate_raster_map(), main()

### Community 8 - "Community 8"
Cohesion: 0.5
Nodes (4): Plan de Jérusalem au premier siècle — Temple, Antonia, murs, citadelle, Forteresse Antonia (Jérusalem 1er siècle), Temple de Jérusalem (1er siècle), Thème : Jérusalem au 1er siècle

### Community 9 - "Community 9"
Cohesion: 0.5
Nodes (4): Désert de Judée — paysage aride et rocheux, La Terre Sainte à l'époque du Nouveau Testament — carte générale, Thème : désert et lieu de retraite spirituelle, Thème : Terre Sainte au Nouveau Testament

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (2): astro.config.mjs — Astro site configuration, Mon harmonie des Évangiles (project overview)

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (2): build_annexes.py — Jekyll-to-Astro annexe converter, Rationale: annexes/ are a Jekyll legacy migrated to Astro via build_annexes.py

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (2): AGENTS.md — repository instructions for agents, CLAUDE.md — project guidance for Claude Code

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (1): build_site_data.py — generates harmony.generated.json

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (1): Return (frontmatter dict, body) from a Jekyll markdown file.

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (1): Parse a .bib file into a list of entries with key/value fields.

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (1): Convert parsed bib entries to a markdown list.

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (1): data/greek_terms.json — Greek theological term definitions

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (1): google7be578b7e788ac0e.html — Google Search Console verification

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (1): Rationale: use numbered markers by default, arrows only for explicit movement

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (1): Rationale: Jerusalem JPG embedded in SVG to allow sharp overlays without degrading source labels

## Knowledge Gaps
- **36 isolated node(s):** `astro.config.mjs — Astro site configuration`, `fetch_bible.py — GetBible API extractor`, `GetBible API — external Bible verse API`, `Rationale: fetch_tob.py is legacy single-translation scraper superseded by fetch_bible.py`, `build_annexes.py — Jekyll-to-Astro annexe converter` (+31 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 10`** (2 nodes): `astro.config.mjs — Astro site configuration`, `Mon harmonie des Évangiles (project overview)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (2 nodes): `build_annexes.py — Jekyll-to-Astro annexe converter`, `Rationale: annexes/ are a Jekyll legacy migrated to Astro via build_annexes.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (2 nodes): `AGENTS.md — repository instructions for agents`, `CLAUDE.md — project guidance for Claude Code`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `build_site_data.py — generates harmony.generated.json`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `Return (frontmatter dict, body) from a Jekyll markdown file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (1 nodes): `Parse a .bib file into a list of entries with key/value fields.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `Convert parsed bib entries to a markdown list.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (1 nodes): `data/greek_terms.json — Greek theological term definitions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `google7be578b7e788ac0e.html — Google Search Console verification`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `Rationale: use numbered markers by default, arrows only for explicit movement`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `Rationale: Jerusalem JPG embedded in SVG to allow sharp overlays without degrading source labels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` connect `Community 0` to `Community 9`, `Community 3`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `Jérusalem` connect `Community 4` to `Community 0`, `Community 9`, `Community 3`, `Community 8`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `Galilée` connect `Community 5` to `Community 0`, `Community 9`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` (e.g. with `Thème : itinéraires de Jésus dans les Évangiles` and `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie`) actually correct?**
  _`Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie` (e.g. with `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` and `Thème : itinéraires de Jésus dans les Évangiles`) actually correct?**
  _`Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale)` (e.g. with `Carte 4 — Itinéraires entre Galilée et Jérusalem (ministère tardif)` and `Carte 5 — Derniers voyages vers Jérusalem via Pérée et Samarie`) actually correct?**
  _`Carte 6 — Galilée, Judée et vue aérienne de Jérusalem (entrée triomphale)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Jérusalem` (e.g. with `Judée` and `La Terre Sainte à l'époque du Nouveau Testament — carte générale`) actually correct?**
  _`Jérusalem` has 3 INFERRED edges - model-reasoned connections that need verification._