# Consignes du dépôt

## Structure du projet

Ce dépôt contient une refonte Astro du site "Mon harmonie des Évangiles". La source de l'harmonie est `data/harmony.json`. Les traductions bibliques supportées sont dans `data/translations.json`, les mots grecs à surligner dans `data/greek_terms.json`, et les versets viennent de la base SQLite multi-traduction `bible.db`, régénérable avec `extractor/fetch_bible.py`. Les scripts de transformation sont dans `scripts/`, et le site Astro est dans `src/`.

Les images sources sont dans `assets/`. `public/assets/`, `src/data/harmony.generated.json`, `dist/` et `.astro/` sont générés et ne doivent pas être modifiés directement.

## Commandes de développement

- `npm install` : installe les dépendances Node.
- `make` ou `npm run build` : génère les données enrichies puis construit le site dans `dist/`.
- `make serve` ou `npm run dev` : lance le serveur local Astro.
- `make clean` : supprime les sorties générées.
- `make refresh-bible` : reconstruit `bible.db` via `extractor/fetch_bible.py`; sans argument, récupère toutes les traductions activées, ou seulement `TRANSLATION=darby`.

## Style et conventions

Gardez `data/harmony.json` comme source éditable de l'ordre harmonisé, des notes, dates, lieux et images. Les références bibliques sont indexées par livre (`matthieu`, `marc`, `luc`, `jean`, `actes`) et utilisent des triplets `[chapitre, verset_debut, verset_fin]`. Ajoutez les traductions dans `data/translations.json` et les notions grecques dans `data/greek_terms.json`, pas dans les composants.

Les composants Astro vivent dans `src/components/`, les pages dans `src/pages/`, et le CSS global dans `src/styles/main.css`. Préférez des composants simples et lisibles : l'objectif est une expérience de lecture quotidienne, pas une application lourde.

## Validation

Avant de conclure une modification, exécutez :

```sh
npm run build
```

Pour les changements de données, vérifiez aussi que `scripts/build_site_data.py` ne signale ni verset manquant ni image absente.

## Publication

Le site produit est statique. Il peut être servi depuis `dist/` en auto-hébergement, ou publié via GitHub Pages avec `.github/workflows/deploy-pages.yml` si Pages est configuré pour utiliser GitHub Actions.
