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

Par défaut, utiliser des repères numérotés. Une carte de chapitre suffit quand tous les épisodes se lisent à la même échelle. Créer plusieurs cartes, par section ou par groupe de sections, quand l’histoire change nettement de lieu, d’échelle ou d’enjeu géographique. Ajouter des flèches seulement quand le texte biblique décrit explicitement un déplacement ; éviter les trajets reconstruits à partir d’hypothèses géographiques.

## Génération

Les cartes scriptées sont régénérées avec :

```sh
python3 scripts/generate_maps.py
```

La carte `generated/chapitre-02-naissance-jeunesse.svg` reprend le fond CC0 et ajoute les lieux numérotés du chapitre 2. Elle est référencée depuis `data/harmony.json` avec le chemin `maps/generated/chapitre-02-naissance-jeunesse.svg`.

La carte `generated/chapitre-03-debut-ministere-judee.svg` reprend la même convention pour le début du ministère : repères numérotés, sans trajet reconstruit.

La carte `generated/chapitre-04-bethanie.svg` situe Béthanie au-delà du Jourdain, avec un repère unique puisque les épisodes localisés du chapitre se concentrent au même endroit.

La carte `generated/chapitre-05-galilee.svg` situe Béthanie, Cana et Capharnaüm. Elle utilise des flèches fines parce que Jean indique explicitement le départ vers la Galilée puis la descente à Capharnaüm.

La carte `generated/chapitre-06-judee-samarie.svg` situe Jérusalem, la Judée, Aïnon et Sychar. Elle utilise une flèche fine pour le départ de Judée vers la Galilée en passant par la Samarie, explicitement indiqué en Jean 4.

La carte `generated/chapitre-07-galilee.svg` donne une vue d’ensemble du ministère en Galilée : Capharnaüm, lac de Tibériade, Cana, Naïn, Nazareth et Gadara.

La carte `generated/chapitre-07-traversee-lac.svg` est attachée à la section de la traversée du lac. Elle utilise des flèches parce que l’aller-retour sur le lac est explicitement raconté.
