# Mon harmonie des Évangiles

Ce dépôt contient le code source du site <https://evangiles.decre.me/>, une harmonisation personnelle des Évangiles sous forme chronologique, datée et annotée.

Le site combine :

- les textes bibliques de la TOB 2010 ;
- une structure d'harmonisation maintenue en Python ;
- des pages Markdown générées automatiquement ;
- un site statique publié avec Jekyll et le thème `just-the-docs`.

## Fonctionnement général

Le flux de génération est le suivant :

1. `extractor/fetch_tob.py` récupère les textes de Matthieu, Marc, Luc, Jean et Actes depuis `lire.la-bible.net`, puis les stocke dans la base SQLite `bible.db`.
2. `extractor/harmonie.py` décrit l'ordre harmonisé : chapitres, sections, dates, lieux, images, notes et références de versets.
3. `extractor/compare.py` lit `bible.db` et `extractor/harmonie.py`, puis génère les fichiers `evangiles/chapitre_*.md`.
4. Jekyll transforme les pages Markdown, les annexes, les styles et la bibliographie en site statique dans `_site/`.

Les fichiers `_site/` et `evangiles/chapitre_*.md` sont donc des sorties générées. Pour modifier le fond, il faut généralement changer `extractor/harmonie.py`, les annexes Markdown, les assets ou les modèles Jekyll, puis reconstruire.

## Structure du dépôt

- `about.md` : page d'accueil publiée à la racine du site.
- `evangiles/index.md` : entrée de navigation des chapitres harmonisés.
- `annexes/` : pages complémentaires.
- `extractor/` : scripts Python de récupération, harmonisation et diagnostic.
- `assets/` : images, cartes et Sass principal.
- `_layouts/`, `_includes/`, `_sass/` : personnalisation Jekyll.
- `_bibliography/references.bib` : sources affichées via `jekyll-scholar`.
- `_site/` : site généré.

## Installation

Prérequis :

- Ruby `3.3.6` ou une version compatible `>= 3.1` et `< 4.0` ;
- Bundler ;
- Python 3 ;
- dépendances Python utilisées par l'extraction : `requests` et `beautifulsoup4`.

Installer les dépendances Ruby :

```sh
bundle install
```

Le fichier `.ruby-version` permet à `rbenv`, `asdf` ou `mise` de sélectionner Ruby `3.3.6`. Avec `rbenv`, par exemple :

```sh
rbenv install 3.3.6
rbenv local 3.3.6
gem install bundler
bundle install
```

`Gemfile.lock` est versionné pour conserver les versions de gems qui construisent le site. Si vous devez le régénérer, supprimez-le puis relancez `bundle install`.

## Commandes utiles

```sh
make
```

Reconstruit le site. Si les chapitres générés sont absents, `make` lance aussi `extractor/compare.py`.

```sh
make serve
```

Démarre un serveur Jekyll local pour relire le site, généralement sur <http://127.0.0.1:4000/>. N'ouvrez pas `_site/index.html` directement en `file://` : le thème utilise des chemins absolus comme `/assets/...`, qui nécessitent un serveur HTTP à la racine de `_site`.

```sh
make clean
```

Supprime les chapitres générés, `_site/` et les caches Jekyll.

```sh
make trous
```

Lance un diagnostic des versets présents dans `bible.db` mais non couverts par l'harmonisation.

```sh
make publish
```

Synchronise `_site/` vers le chemin Dropbox local configuré dans le `Makefile`. Cette commande est spécifique à la machine du mainteneur.

## Régénérer les textes bibliques

La base `bible.db` est ignorée par Git. Pour la recréer :

```sh
python3 extractor/fetch_tob.py
```

Ce script fait des requêtes réseau vers `lire.la-bible.net` et reconstruit la table `versets`. À utiliser avec prudence, car il dépend de la structure HTML du site source et des conditions d'utilisation de la traduction.

## Modifier l'harmonisation

Pour changer l'ordre, les titres, les dates, les lieux, les images ou les notes des chapitres, modifier `extractor/harmonie.py`, puis exécuter :

```sh
make clean
make
```

Relire ensuite les pages générées dans `evangiles/chapitre_*.md` ou lancer `make serve`.

## Notes

La page d'accueil précise que la datation et les cartes servent à inscrire les textes dans une temporalité et des lieux, sans prétendre dessiner un Jésus historique. Les droits d'utilisation des images et textes doivent rester un point d'attention lors de toute mise à jour.
