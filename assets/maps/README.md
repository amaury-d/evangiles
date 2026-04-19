# Cartes

Ce dossier contient les sources et futures cartes générées du projet.

## Source géographique principale

- Fichier : `sources/Holy_sites_of_Jesus_in_Palestine.svg`
- Source : Wikimedia Commons, `File:Holy sites of Jesus in Palestine.svg`
- URL : https://commons.wikimedia.org/wiki/File:Holy_sites_of_Jesus_in_Palestine.svg
- Licence : Creative Commons CC0 1.0 Universal Public Domain Dedication
- Auteur/source indiqués sur Commons : un.org, via `File:Map of Israel, neighbours and occupied territories.svg`

Cette source est utilisable, modifiable et redistribuable sans demander d'autorisation. Elle sert de base vectorielle libre pour produire les cartes épurées du site.

## Source Jérusalem

- Fichier : `sources/Jerusalem_premier_siecle.JPG`
- Source : Wikimedia Commons, `File:Jerusalem premier siècle.JPG`
- URL : https://commons.wikimedia.org/wiki/File:Jerusalem_premier_si%C3%A8cle.JPG
- Licence : Creative Commons Attribution-ShareAlike 3.0 ; GNU Free Documentation License 1.2+
- Auteur : Olevy

Cette source représente Jérusalem au premier siècle. Elle sert de fond pour le chapitre 8. Comme le fichier source est un JPG lisible mais peu détaillé, la carte dérivée l'encapsule dans un SVG généré afin d'ajouter des repères nets sans dégrader les libellés d'origine.

- Fichier : `sources/Jerusalem_in_70_map.svg`
- Source : Wikimedia Commons, `File:Jerusalem in 70 - map.svg`
- URL : https://commons.wikimedia.org/wiki/File:Jerusalem_in_70_-_map.svg
- Licence : Creative Commons Attribution-ShareAlike 3.0, 2.5, 2.0 et 1.0 ; GNU Free Documentation License 1.2+
- Auteur : TcfkaPanairjdde

Cette source représente Jérusalem en 70. Elle reste disponible comme source alternative pour les épisodes à Jérusalem du Ier siècle, en gardant les emplacements comme indicatifs et en conservant l'attribution dans les légendes ou la documentation.

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

La carte `generated/chapitre-08-jerusalem.svg` utilise la source de Jérusalem au premier siècle pour situer Bethesda et le Temple. Les repères sont indicatifs.
