# Mon harmonie des Évangiles

Ce dépôt contient la reconstruction du site <https://evangiles.decre.me/> : une harmonisation personnelle des Évangiles pensée pour une lecture quotidienne, chronologique, annotée et illustrée.

Le projet garde la base de données locale `bible.db`, alimentée par `extractor/fetch_tob.py`, et remplace progressivement l'ancien site Jekyll par un site statique Astro.

## Nouveau pipeline

1. `extractor/fetch_tob.py` récupère la TOB depuis `lire.la-bible.net` et reconstruit `bible.db`.
2. `data/harmony.json` décrit l'harmonie : chapitres, sections, dates, lieux, images, notes et références bibliques.
3. `scripts/build_site_data.py` lit `data/harmony.json` et `bible.db`, puis génère `src/data/harmony.generated.json`.
4. Astro lit ces données et produit le site statique dans `dist/`.

`src/data/harmony.generated.json`, `public/assets/` et `dist/` sont générés. La source éditable principale est `data/harmony.json`.

## Structure

- `data/harmony.json` : configuration source de l'harmonie.
- `bible.db` : base SQLite locale des versets TOB.
- `extractor/fetch_tob.py` : script conservé pour régénérer `bible.db`.
- `scripts/migrate_harmony.py` : migration ponctuelle depuis l'ancien `extractor/harmonie.py`.
- `scripts/build_site_data.py` : génération des données enrichies pour Astro.
- `src/` : pages, composants et styles du nouveau site.
- `assets/` : images sources.
- `public/assets/` : copie générée des images pour Astro.
- `dist/` : site statique généré.

Les anciens fichiers Jekyll restent présents comme référence pendant la migration, mais ils ne sont plus le chemin principal.

## Installation

Prérequis :

- Node.js 22 ou plus récent ;
- Python 3 avec SQLite inclus ;
- `bible.db` présent à la racine du dépôt.

Installer les dépendances :

```sh
npm install
```

## Commandes

```sh
make
```

Génère les données et construit le site Astro dans `dist/`.

```sh
make serve
```

Démarre le serveur de développement Astro, généralement sur <http://127.0.0.1:4321/>.

```sh
make clean
```

Supprime les sorties générées : `dist/`, `.astro/`, `public/assets/` et `src/data/harmony.generated.json`.

```sh
make refresh-bible
```

Reconstruit `bible.db` avec `extractor/fetch_tob.py`. À utiliser avec prudence, car ce script dépend de la structure HTML du site source.

```sh
make migrate-harmony
```

Régénère `data/harmony.json` depuis l'ancien `extractor/harmonie.py`. Cette commande est surtout utile tant que la migration n'est pas totalement finalisée.

## Publication

Le site généré est statique. Il peut être auto-hébergé en servant `dist/`, ou publié via GitHub Pages. Le workflow `.github/workflows/deploy-pages.yml` construit le site avec GitHub Actions et publie `dist/` sur GitHub Pages lorsque la fonctionnalité Pages est configurée pour utiliser les Actions.
