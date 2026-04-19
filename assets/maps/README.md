# Cartes

Ce dossier contient les sources et futures cartes générées du projet.

## Source géographique principale

- Fichier : `sources/Holy_sites_of_Jesus_in_Palestine.svg`
- Source : Wikimedia Commons, `File:Holy sites of Jesus in Palestine.svg`
- URL : https://commons.wikimedia.org/wiki/File:Holy_sites_of_Jesus_in_Palestine.svg
- Licence : Creative Commons CC0 1.0 Universal Public Domain Dedication
- Auteur/source indiqués sur Commons : un.org, via `File:Map of Israel, neighbours and occupied territories.svg`

Cette source est utilisable, modifiable et redistribuable sans demander d'autorisation. Elle sert de base vectorielle libre pour produire les cartes épurées du site.

## Organisation

- `sources/` : fichiers sources externes conservés avec leur provenance.
- `generated/` : cartes dérivées créées pour ce site, par chapitre ou par section.

Les cartes dérivées doivent rester sobres : fond clair, régions et lieux nécessaires au récit, peu de détails secondaires. Privilégier le SVG pour faciliter les variantes et les mises en évidence.

## Génération

Les cartes scriptées sont régénérées avec :

```sh
python3 scripts/generate_maps.py
```

La carte `generated/chapitre-02-naissance-jeunesse.svg` reprend le fond CC0 et ajoute les lieux numérotés du chapitre 2. Elle est référencée depuis `data/harmony.json` avec le chemin `maps/generated/chapitre-02-naissance-jeunesse.svg`.

La carte `generated/chapitre-03-debut-ministere-judee.svg` reprend la même convention pour le début du ministère : repères numérotés, sans trajet reconstruit.
