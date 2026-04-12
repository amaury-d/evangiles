# Consignes du dépôt

## Structure du projet

Ce dépôt contient un site Jekyll intitulé "Mon harmonie des Évangiles". La configuration est dans `_config.yml`. Les modèles et fragments HTML sont dans `_layouts/` et `_includes/`. Les styles Sass sont dans `_sass/` et `assets/main.scss`. Les contenus Markdown se trouvent à la racine, dans `annexes/` et dans `evangiles/`. La bibliographie est dans `_bibliography/references.bib`.

Les scripts Python de `extractor/` génèrent les chapitres harmonisés à partir de `bible.db` et `extractor/harmonie.py`. Considérez `evangiles/chapitre_*.md` et `_site/` comme des sorties générées : modifiez les sources, puis reconstruisez le site.

## Commandes de build, test et développement

- `bundle install` : installe les dépendances Ruby déclarées dans `Gemfile`.
- `make` : lance le build par défaut, régénère le contenu nécessaire puis exécute `jekyll build`.
- `make serve` : démarre un serveur Jekyll local pour relire le site.
- `make clean` : supprime les chapitres générés, les caches Jekyll et `_site/`.
- `make trous` : exécute `extractor/trous.py` pour repérer des données manquantes ou incomplètes.
- `make publish` : synchronise `_site/` vers le chemin Dropbox local configuré ; réservé au mainteneur.

Pour lancer Jekyll manuellement : `bundle exec jekyll build` ou `bundle exec jekyll serve`.

## Style et conventions de nommage

Les pages Markdown utilisent un en-tête YAML avec `layout`, `title`, `permalink`, `has_children` et `nav_order`. Gardez des noms descriptifs en minuscules. Les chapitres générés suivent `evangiles/chapitre_<numéro>-<slug>.md`.

Les scripts Python utilisent une indentation de 4 espaces. Conservez le style éditorial français, les accents et la terminologie existante. Limitez les changements Sass à `assets/main.scss` ou aux partiels de `_sass/`.

## Validation

Il n'existe pas de suite de tests automatisés dédiée. Validez avec `make`, puis relisez le résultat avec `make serve`. Pour un extracteur, lancez le script concerné, par exemple `python3 extractor/compare.py`, puis reconstruisez les pages affectées.

## Commits et pull requests

L'historique actuel ne montre qu'un commit initial ; aucune convention stricte n'est établie. Utilisez des messages courts à l'impératif, par exemple `Corrige les notes sur la Galilée`.

Une pull request doit décrire le changement de contenu ou de génération, lister les commandes de validation exécutées et signaler les fichiers générés inclus. Ajoutez des captures d'écran lorsque la mise en page, les cartes, les images ou la navigation sont modifiées.

## Instructions pour les agents

Ne modifiez pas `_site/` directement. Préférez le Markdown, les modèles Jekyll, le Sass, la bibliographie ou les données d'extraction, puis régénérez avec `make`.
