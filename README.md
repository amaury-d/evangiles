# Mon harmonie des Évangiles

Ce dépôt contient la reconstruction du site <https://evangiles.decre.me/> : une harmonisation personnelle des Évangiles pensée pour une lecture quotidienne, chronologique, annotée et illustrée.

Le projet garde la base de données locale `bible.db`, alimentée par `extractor/fetch_bible.py`, et génère un site statique Astro.

## Nouveau pipeline

1. `data/translations.json` déclare les traductions bibliques supportées.
2. `extractor/fetch_bible.py` récupère ces traductions depuis l'API GetBible et reconstruit `bible.db`.
3. `data/harmony.json` décrit l'harmonie : chapitres, sections, dates, lieux, images, notes et références bibliques.
4. `data/greek_terms.json` décrit les mots-clés grecs et les variantes textuelles à surligner.
5. `scripts/build_site_data.py` lit `data/harmony.json`, `data/translations.json` et `bible.db`, puis génère `src/data/harmony.generated.json`.
6. Astro lit ces données et produit le site statique dans `dist/`.

`src/data/harmony.generated.json`, `public/assets/` et `dist/` sont générés. La source éditable principale est `data/harmony.json`.

## Structure

- `data/harmony.json` : configuration source de l'harmonie.
- `data/translations.json` : liste des traductions à construire et traduction par défaut.
- `data/greek_terms.json` : dictionnaire local des notions grecques à surligner.
- `bible.db` : base SQLite locale des versets bibliques, avec une colonne `translation`.
- `extractor/fetch_bible.py` : script de régénération multi-traduction de `bible.db` depuis GetBible.
- `scripts/build_site_data.py` : génération des données enrichies pour Astro.
- `src/` : pages, composants et styles du nouveau site.
- `assets/` : images sources.
- `assets/maps/` : source cartographique libre et futures cartes dérivées.
- `public/assets/` : copie générée des images pour Astro.
- `dist/` : site statique généré.

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

Reconstruit `bible.db` avec `extractor/fetch_bible.py`. À utiliser avec prudence, car ce script remplace la base locale.

Sans argument, la commande récupère toutes les traductions activées dans `data/translations.json`. Pour reconstruire une traduction précise :

```sh
make refresh-bible TRANSLATION=darby
```

Pour reconstruire plusieurs traductions précises :

```sh
make refresh-bible TRANSLATION=ls1910,darby
```

## Traductions et mots grecs

Pour ajouter une traduction, ajoutez une entrée dans `data/translations.json` avec `code`, `label`, `language` et `enabled`, puis lancez :

```sh
make refresh-bible
npm run build
```

Le sélecteur de traduction est rendu côté Astro et bascule les passages avec un petit script client. Le choix est mémorisé dans `localStorage` et ajouté à l'URL lors d'un changement manuel via `?traduction=...`.

Pour ajouter un mot-clé grec, ajoutez une entrée dans `data/greek_terms.json`. Les champs importants sont `id`, `lemma`, `transliteration`, `labels`, `short_definition`, `long_definition` et `notes`. Les `labels` sont les mots ou expressions complets détectés dans les traductions, par exemple `royaume de Dieu`, `foi` ou `truth`.

Le surlignage est heuristique : il ne prétend pas faire un alignement grec mot-à-mot. Il sert de repère de lecture et pourra être remplacé plus tard par un alignement lexical plus précis.

## Cartes

Les anciennes cartes `assets/carte*.jpg` sont appelées à être remplacées. La nouvelle base cartographique libre est `assets/maps/sources/Holy_sites_of_Jesus_in_Palestine.svg`, téléchargée depuis Wikimedia Commons et publiée sous licence CC0 1.0.

Les cartes dérivées doivent être placées dans `assets/maps/generated/`, idéalement en SVG. Elles peuvent ensuite être référencées depuis `data/harmony.json`, par exemple `maps/generated/chapitre-06-judee.svg`. Le build copie récursivement `assets/` vers `public/assets/`.

## Publication

Le site généré est statique. Il peut être auto-hébergé en servant `dist/`, ou publié via GitHub Pages. Le workflow `.github/workflows/deploy-pages.yml` construit le site avec GitHub Actions et publie `dist/` sur GitHub Pages lorsque la fonctionnalité Pages est configurée pour utiliser les Actions.
