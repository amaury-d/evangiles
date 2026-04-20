import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "maps" / "sources" / "Holy_sites_of_Jesus_in_Palestine.svg"
JERUSALEM_RASTER_SOURCE = ROOT / "assets" / "maps" / "sources" / "Jerusalem_premier_siecle.JPG"
PAUL_JOURNEY_1_SOURCE = ROOT / "assets" / "maps" / "sources" / "Paul_the_Apostle,_first_missionary_journey.svg"
PAUL_JOURNEY_2_SOURCE = ROOT / "assets" / "maps" / "sources" / "Paul_the_Apostle,_second_missionary_journey.svg"
PAUL_JOURNEY_3_SOURCE = ROOT / "assets" / "maps" / "sources" / "Paul_the_Apostle,_third_missionary_journey.svg"
PAUL_JOURNEY_ROME_SOURCE = ROOT / "assets" / "maps" / "sources" / "Paul_the_Apostle,_fourth_missionary_journey_(Rome).svg"


COMMON_DEFS = """
  <defs>
    <marker id="ev-map-arrow" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#b6382d"/>
    </marker>
    <marker id="ev-map-callout-arrow" viewBox="0 0 10 10" refX="8.4" refY="5" markerWidth="3" markerHeight="3" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#4d4a41" fill-opacity="0.58"/>
    </marker>
    <style>
      .ev-map-title { font: 700 42px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; }
      .ev-map-subtitle { font: 400 24px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4d4a41; }
      .ev-map-route { fill: none; stroke: #b6382d; stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; marker-end: url(#ev-map-arrow); }
      .ev-map-place { fill: #2b2a25; fill-opacity: 0.58; stroke: #fffdf2; stroke-opacity: 0.8; stroke-width: 2.2; }
      .ev-map-place-probable { fill: #fffdf2; fill-opacity: 0.64; stroke: #2b2a25; stroke-opacity: 0.62; stroke-width: 1.5; }
      .ev-map-pin-number { font: 700 17px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #fffdf2; fill-opacity: 0.84; text-anchor: middle; dominant-baseline: central; }
      .ev-map-pin-number-dark { font: 700 17px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; fill-opacity: 0.78; text-anchor: middle; dominant-baseline: central; }
      .ev-map-label { font: 700 28px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; stroke: #fffdf2; stroke-width: 5; stroke-linejoin: round; paint-order: stroke; }
      .ev-map-small-label { font: 500 22px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; stroke: #fffdf2; stroke-width: 4; stroke-linejoin: round; paint-order: stroke; }
      .ev-map-note { font: 400 19px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4d4a41; }
      .ev-map-legend-box { fill: #fffdf2; fill-opacity: 0.88; stroke: #d6c9a7; stroke-width: 2; }
      .ev-map-title-compact { font: 700 22px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; }
      .ev-map-subtitle-compact { font: 400 14px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4d4a41; }
      .ev-map-note-compact { font: 400 12px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4d4a41; }
      .ev-map-pin-number-compact { font: 700 10px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #fffdf2; fill-opacity: 0.78; text-anchor: middle; dominant-baseline: central; }
      .ev-map-pin-number-dark-compact { font: 700 10px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; fill-opacity: 0.72; text-anchor: middle; dominant-baseline: central; }
      .ev-map-callout { fill: none; stroke: #4d4a41; stroke-opacity: 0.5; stroke-width: 1.2; stroke-linecap: round; marker-end: url(#ev-map-callout-arrow); }
    </style>
  </defs>
"""


CHAPTER_02_OVERLAY = """
  <g id="evangiles-chapitre-02-overlay">
    <rect x="742" y="1378" width="520" height="324" rx="8" class="ev-map-legend-box"/>
    <text x="770" y="1472" class="ev-map-title">Chapitre 2</text>
    <text x="770" y="1512" class="ev-map-subtitle">Naissance et jeunesse de Jésus</text>
    <text x="770" y="1554" class="ev-map-note">1. Jérusalem : annonce à Zacharie</text>
    <text x="770" y="1588" class="ev-map-note">2. Nazareth : annonces à Marie et Joseph</text>
    <text x="770" y="1622" class="ev-map-note">3. Bethléem : naissance, bergers et mages</text>
    <text x="770" y="1656" class="ev-map-note">4. Égypte : fuite et séjour</text>
    <text x="770" y="1690" class="ev-map-note">5. Jérusalem : Jésus au Temple à douze ans</text>

    <circle cx="700" cy="552" r="11" class="ev-map-place"/>
    <text x="700" y="552" class="ev-map-pin-number">2</text>

    <circle cx="652" cy="1264" r="11" class="ev-map-place"/>
    <text x="652" y="1264" class="ev-map-pin-number">3</text>

    <circle cx="664" cy="1144" r="11" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">1</text>

    <circle cx="696" cy="1144" r="11" class="ev-map-place"/>
    <text x="696" y="1144" class="ev-map-pin-number">5</text>

    <circle cx="656" cy="1060" r="9" class="ev-map-place-probable"/>

    <circle cx="156" cy="1694" r="11" class="ev-map-place"/>
    <text x="156" y="1694" class="ev-map-pin-number">4</text>
    <text x="184" y="1684" class="ev-map-label">Vers l'Égypte</text>
  </g>
"""


CHAPTER_03_OVERLAY = """
  <g id="evangiles-chapitre-03-overlay">
    <rect x="36" y="1328" width="572" height="260" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1382" class="ev-map-title">Chapitre 3</text>
    <text x="64" y="1422" class="ev-map-subtitle">Début du ministère en Judée</text>
    <text x="64" y="1474" class="ev-map-note">1. Jourdain : ministère de Jean le Baptiste</text>
    <text x="64" y="1508" class="ev-map-note">2. Jourdain : baptême de Jésus</text>
    <text x="64" y="1542" class="ev-map-note">3. Désert de Judée : quarante jours</text>

    <circle cx="840" cy="1138" r="11" class="ev-map-place"/>
    <text x="840" y="1138" class="ev-map-pin-number">1</text>

    <circle cx="876" cy="1138" r="11" class="ev-map-place"/>
    <text x="876" y="1138" class="ev-map-pin-number">2</text>

    <circle cx="736" cy="1304" r="11" class="ev-map-place"/>
    <text x="736" y="1304" class="ev-map-pin-number">3</text>
  </g>
"""


CHAPTER_04_OVERLAY = """
  <g id="evangiles-chapitre-04-overlay">
    <rect x="36" y="1328" width="610" height="250" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1382" class="ev-map-title">Chapitre 4</text>
    <text x="64" y="1422" class="ev-map-subtitle">Jean le Baptiste à Béthanie</text>
    <text x="64" y="1474" class="ev-map-note">1. Béthanie au-delà du Jourdain</text>
    <text x="64" y="1508" class="ev-map-note">Témoignage de Jean, agneau de Dieu,</text>
    <text x="64" y="1542" class="ev-map-note">André, Simon-Pierre et les premiers disciples.</text>

    <circle cx="860" cy="1138" r="11" class="ev-map-place"/>
    <text x="860" y="1138" class="ev-map-pin-number">1</text>
  </g>
"""


CHAPTER_05_OVERLAY = """
  <g id="evangiles-chapitre-05-overlay">
    <rect x="36" y="1298" width="610" height="304" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1352" class="ev-map-title">Chapitre 5</text>
    <text x="64" y="1392" class="ev-map-subtitle">Jésus en Galilée</text>
    <text x="64" y="1444" class="ev-map-note">1. Béthanie : appel de Philippe</text>
    <text x="64" y="1478" class="ev-map-note">2. Cana : noces et premier signe</text>
    <text x="64" y="1512" class="ev-map-note">3. Capharnaüm : court séjour</text>
    <text x="64" y="1556" class="ev-map-note">Les flèches suivent les déplacements indiqués</text>
    <text x="64" y="1588" class="ev-map-note">par Jean, sans reconstruire la route exacte.</text>

    <path class="ev-map-route" d="M 846 1122 C 840 930 812 748 772 612 C 746 526 722 482 704 456"/>
    <path class="ev-map-route" d="M 718 462 C 782 496 846 464 876 430"/>

    <circle cx="860" cy="1138" r="11" class="ev-map-place"/>
    <text x="860" y="1138" class="ev-map-pin-number">1</text>

    <circle cx="704" cy="456" r="11" class="ev-map-place"/>
    <text x="704" y="456" class="ev-map-pin-number">2</text>

    <circle cx="884" cy="426" r="11" class="ev-map-place"/>
    <text x="884" y="426" class="ev-map-pin-number">3</text>
  </g>
"""


CHAPTER_06_OVERLAY = """
  <g id="evangiles-chapitre-06-overlay">
    <rect x="36" y="1298" width="632" height="338" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1352" class="ev-map-title">Chapitre 6</text>
    <text x="64" y="1392" class="ev-map-subtitle">Jésus et Jean en Judée</text>
    <text x="64" y="1444" class="ev-map-note">1. Jérusalem : Pâque, Temple, Nicodème</text>
    <text x="64" y="1478" class="ev-map-note">2. Judée : Jésus demeure et baptise</text>
    <text x="64" y="1512" class="ev-map-note">3. Aïnon : Jean baptise encore</text>
    <text x="64" y="1546" class="ev-map-note">4. Sychar : rencontre en Samarie</text>
    <text x="64" y="1590" class="ev-map-note">Flèche : Jésus quitte la Judée pour la Galilée</text>
    <text x="64" y="1622" class="ev-map-note">en passant par la Samarie.</text>

    <path class="ev-map-route" d="M 690 1112 C 700 1014 696 940 684 884"/>
    <path class="ev-map-route" d="M 684 884 C 740 760 784 640 812 520"/>

    <circle cx="664" cy="1144" r="11" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">1</text>

    <circle cx="722" cy="1110" r="11" class="ev-map-place"/>
    <text x="722" y="1110" class="ev-map-pin-number">2</text>

    <circle cx="752" cy="940" r="11" class="ev-map-place-probable"/>
    <text x="752" y="940" class="ev-map-pin-number-dark">3</text>

    <circle cx="684" cy="884" r="11" class="ev-map-place"/>
    <text x="684" y="884" class="ev-map-pin-number">4</text>
  </g>
"""


CHAPTER_07_OVERLAY = """
  <g id="evangiles-chapitre-07-overlay">
    <rect x="36" y="1278" width="650" height="362" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1332" class="ev-map-title">Chapitre 7</text>
    <text x="64" y="1372" class="ev-map-subtitle">Ministère en Galilée</text>
    <text x="64" y="1424" class="ev-map-note">1. Galilée : proclamation et parcours</text>
    <text x="64" y="1458" class="ev-map-note">2. Capharnaüm : enseignements et guérisons</text>
    <text x="64" y="1492" class="ev-map-note">3. Lac de Tibériade : appels, foule, paraboles</text>
    <text x="64" y="1526" class="ev-map-note">4. Cana : guérison à distance</text>
    <text x="64" y="1560" class="ev-map-note">5. Naïn : fils de la veuve</text>
    <text x="64" y="1594" class="ev-map-note">6. Nazareth : rejet des habitants</text>
    <text x="64" y="1628" class="ev-map-note">7. Gadara : démoniaques</text>

    <circle cx="760" cy="420" r="11" class="ev-map-place"/>
    <text x="760" y="420" class="ev-map-pin-number">1</text>

    <circle cx="884" cy="426" r="11" class="ev-map-place"/>
    <text x="884" y="426" class="ev-map-pin-number">2</text>

    <circle cx="898" cy="500" r="11" class="ev-map-place"/>
    <text x="898" y="500" class="ev-map-pin-number">3</text>

    <circle cx="704" cy="456" r="11" class="ev-map-place"/>
    <text x="704" y="456" class="ev-map-pin-number">4</text>

    <circle cx="764" cy="666" r="11" class="ev-map-place"/>
    <text x="764" y="666" class="ev-map-pin-number">5</text>

    <circle cx="700" cy="552" r="11" class="ev-map-place"/>
    <text x="700" y="552" class="ev-map-pin-number">6</text>

    <circle cx="960" cy="610" r="11" class="ev-map-place-probable"/>
    <text x="960" y="610" class="ev-map-pin-number-dark">7</text>
    <text x="990" y="618" class="ev-map-small-label">Gadara ?</text>
  </g>
"""


CHAPTER_07_LAKE_OVERLAY = """
  <g id="evangiles-chapitre-07-lake-overlay">
    <rect x="36" y="1328" width="622" height="278" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1382" class="ev-map-title">Chapitre 7</text>
    <text x="64" y="1422" class="ev-map-subtitle">Traversée du lac</text>
    <text x="64" y="1474" class="ev-map-note">1. Rive ouest : départ en barque</text>
    <text x="64" y="1508" class="ev-map-note">2. Rive est : pays des Gadaréniens</text>
    <text x="64" y="1542" class="ev-map-note">3. Retour vers Capharnaüm</text>
    <text x="64" y="1584" class="ev-map-note">Les flèches suivent seulement l’aller-retour</text>

    <path class="ev-map-route" d="M 864 498 C 916 520 948 558 960 610"/>
    <path class="ev-map-route" d="M 946 596 C 922 534 904 472 884 426"/>

    <circle cx="850" cy="500" r="11" class="ev-map-place"/>
    <text x="850" y="500" class="ev-map-pin-number">1</text>

    <circle cx="960" cy="610" r="11" class="ev-map-place-probable"/>
    <text x="960" y="610" class="ev-map-pin-number-dark">2</text>

    <circle cx="884" cy="426" r="11" class="ev-map-place"/>
    <text x="884" y="426" class="ev-map-pin-number">3</text>
  </g>
"""


CHAPTER_08_OVERLAY = """
  <g id="evangiles-chapitre-08-overlay">
    <rect x="12" y="444" width="318" height="120" rx="8" class="ev-map-legend-box"/>
    <text x="28" y="476" class="ev-map-title-compact">Chapitre 8</text>
    <text x="28" y="498" class="ev-map-subtitle-compact">Jérusalem</text>
    <text x="28" y="526" class="ev-map-note-compact">1. Piscine de Bethesda : paralytique guéri</text>
    <text x="28" y="546" class="ev-map-note-compact">2. Temple : sabbat et controverse</text>

    <path class="ev-map-callout" d="M 354 108 L 342 98"/>
    <circle cx="354" cy="108" r="5" class="ev-map-place-probable"/>
    <text x="354" y="108" class="ev-map-pin-number-dark-compact">1</text>

    <path class="ev-map-callout" d="M 303 218 L 320 222"/>
    <circle cx="303" cy="218" r="5" class="ev-map-place"/>
    <text x="303" y="218" class="ev-map-pin-number-compact">2</text>
  </g>
"""


CHAPTER_09_GALILEE_NORD_OVERLAY = """
  <g id="evangiles-chapitre-09-galilee-nord-overlay">
    <rect x="36" y="1008" width="740" height="412" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1062" class="ev-map-title">Chapitre 9 (1/2)</text>
    <text x="64" y="1102" class="ev-map-subtitle">Galilée, Phénicie et Décapole</text>
    <text x="64" y="1154" class="ev-map-note">1. Capharnaüm : base du ministère, discours synagogue</text>
    <text x="64" y="1186" class="ev-map-note">2. Bethsaïde : envoi des disciples, multiplication pour 5000</text>
    <text x="64" y="1218" class="ev-map-note">3. Génézareth : guérisons dans la plaine</text>
    <text x="64" y="1250" class="ev-map-note">4. Tyr (Sidon hors carte) : fille de la Cananéenne guérie</text>
    <text x="64" y="1282" class="ev-map-note">5. Décapole : retour, multiplication pour 4000</text>
    <text x="64" y="1314" class="ev-map-note">6. Dalmanutha : pharisiens cherchent un signe</text>
    <text x="64" y="1346" class="ev-map-note">7. Césarée de Philippe : confession de Pierre</text>
    <text x="64" y="1386" class="ev-map-note">Flèches : Jésus vers Tyr et Sidon, retour par la Décapole.</text>

    <!-- Route: Capharnaüm → Tyr (northwest) -->
    <path class="ev-map-route" d="M 880 422 C 840 370 760 278 656 162"/>
    <!-- Route: Tyr → Décapole (return, southeast) -->
    <path class="ev-map-route" d="M 656 162 C 720 282 840 400 970 552"/>

    <!-- 1. Capharnaüm -->
    <circle cx="884" cy="426" r="11" class="ev-map-place"/>
    <text x="884" y="426" class="ev-map-pin-number">1</text>

    <!-- 2. Bethsaïde -->
    <circle cx="928" cy="400" r="11" class="ev-map-place"/>
    <text x="928" y="400" class="ev-map-pin-number">2</text>

    <!-- 3. Génézareth -->
    <circle cx="840" cy="462" r="11" class="ev-map-place"/>
    <text x="840" y="462" class="ev-map-pin-number">3</text>

    <!-- 4. Tyr -->
    <circle cx="650" cy="158" r="11" class="ev-map-place"/>
    <text x="650" y="158" class="ev-map-pin-number">4</text>

    <!-- 5. Décapole -->
    <circle cx="974" cy="556" r="11" class="ev-map-place-probable"/>
    <text x="974" y="556" class="ev-map-pin-number-dark">5</text>

    <!-- 6. Dalmanutha -->
    <circle cx="820" cy="508" r="11" class="ev-map-place-probable"/>
    <text x="820" y="508" class="ev-map-pin-number-dark">6</text>

    <!-- 7. Césarée de Philippe -->
    <circle cx="958" cy="163" r="11" class="ev-map-place"/>
    <text x="958" y="163" class="ev-map-pin-number">7</text>
  </g>
"""


CHAPTER_15_OVERLAY = """
  <g id="evangiles-chapitre-15-overlay">
    <rect x="36" y="1448" width="640" height="224" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1502" class="ev-map-title">Chapitre 15</text>
    <text x="64" y="1542" class="ev-map-subtitle">Ascension et Pentecôte</text>
    <text x="64" y="1594" class="ev-map-note">1. Mont des Oliviers : promesse du Saint Esprit, ascension</text>
    <text x="64" y="1628" class="ev-map-note">2. Jérusalem : rassemblement des disciples, Pentecôte</text>

    <!-- 1. Mont des Oliviers -->
    <circle cx="704" cy="1128" r="11" class="ev-map-place"/>
    <text x="704" y="1128" class="ev-map-pin-number">1</text>

    <!-- 2. Jérusalem -->
    <circle cx="664" cy="1144" r="11" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">2</text>
  </g>
"""


CHAPTER_14_JERUSALEM_OVERLAY = """
  <g id="evangiles-chapitre-14-jerusalem-overlay">
    <rect x="36" y="1358" width="660" height="302" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1412" class="ev-map-title">Chapitre 14 (1/2)</text>
    <text x="64" y="1452" class="ev-map-subtitle">Jérusalem et Emmaüs</text>
    <text x="64" y="1504" class="ev-map-note">1. Jérusalem : sépulcre vide, Marie de Magdala,</text>
    <text x="64" y="1536" class="ev-map-note">   Pierre et Jean, apparitions aux dix puis aux onze</text>
    <text x="64" y="1570" class="ev-map-note">2. Emmaüs : Jésus marche et se révèle aux deux disciples</text>
    <text x="64" y="1614" class="ev-map-note">Jésus apparaît sur la route</text>

    <!-- 1. Jérusalem -->
    <circle cx="664" cy="1144" r="11" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">1</text>

    <!-- 2. Emmaüs -->
    <circle cx="548" cy="1100" r="11" class="ev-map-place-probable"/>
    <text x="548" y="1100" class="ev-map-pin-number-dark">2</text>
  </g>
"""


CHAPTER_14_GALILEE_OVERLAY = """
  <g id="evangiles-chapitre-14-galilee-overlay">
    <rect x="36" y="1318" width="660" height="258" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1372" class="ev-map-title">Chapitre 14 (2/2)</text>
    <text x="64" y="1412" class="ev-map-subtitle">Galilée</text>
    <text x="64" y="1464" class="ev-map-note">1. Montagne de Galilée : apparition aux onze,</text>
    <text x="64" y="1496" class="ev-map-note">   grande commission</text>
    <text x="64" y="1530" class="ev-map-note">2. Lac de Tibériade : pêche miraculeuse,</text>
    <text x="64" y="1562" class="ev-map-note">   Jésus confie les brebis à Pierre</text>

    <!-- 1. Montagne de Galilée (lieu incertain) -->
    <circle cx="740" cy="524" r="11" class="ev-map-place-probable"/>
    <text x="740" y="524" class="ev-map-pin-number-dark">1</text>

    <!-- 2. Lac de Tibériade -->
    <circle cx="898" cy="500" r="11" class="ev-map-place"/>
    <text x="898" y="500" class="ev-map-pin-number">2</text>
  </g>
"""


CHAPTER_13_BETHANIE_OVERLAY = """
  <g id="evangiles-chapitre-13-bethanie-overlay">
    <rect x="36" y="1418" width="660" height="224" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1472" class="ev-map-title">Chapitre 13 (1/2)</text>
    <text x="64" y="1512" class="ev-map-subtitle">Béthanie et Jérusalem</text>
    <text x="64" y="1564" class="ev-map-note">1. Béthanie : Simon le lépreux, Lazare, onction de Jésus</text>
    <text x="64" y="1598" class="ev-map-note">2. Jérusalem : entrée triomphale, Temple, passion</text>
    <text x="64" y="1638" class="ev-map-note">Flèche : entrée triomphale depuis Béthanie.</text>

    <path class="ev-map-route" d="M 736 1148 C 718 1146 696 1145 668 1144"/>

    <!-- 1. Béthanie -->
    <circle cx="740" cy="1150" r="11" class="ev-map-place"/>
    <text x="740" y="1150" class="ev-map-pin-number">1</text>

    <!-- 2. Jérusalem -->
    <circle cx="664" cy="1144" r="11" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">2</text>
  </g>
"""


CHAPTER_13_PASSION_OVERLAY = """
  <g id="evangiles-chapitre-13-passion-overlay">
    <rect x="12" y="370" width="348" height="186" rx="8" class="ev-map-legend-box"/>
    <text x="28" y="402" class="ev-map-title-compact">Chapitre 13 (2/2)</text>
    <text x="28" y="424" class="ev-map-subtitle-compact">Jérusalem — Passion</text>
    <text x="28" y="450" class="ev-map-note-compact">1. Temple : enseignements, chasse des marchands</text>
    <text x="28" y="470" class="ev-map-note-compact">2. Gethsémani : prière, arrestation</text>
    <text x="28" y="490" class="ev-map-note-compact">3. Prétoire : Pilate et Hérode</text>
    <text x="28" y="510" class="ev-map-note-compact">4. Golgotha : crucifixion, mise au tombeau</text>

    <!-- 1. Temple -->
    <path class="ev-map-callout" d="M 303 218 L 320 222"/>
    <circle cx="303" cy="218" r="5" class="ev-map-place"/>
    <text x="303" y="218" class="ev-map-pin-number-compact">1</text>

    <!-- 2. Gethsémani (pied du Mont des Oliviers, est de la ville) -->
    <circle cx="432" cy="262" r="5" class="ev-map-place"/>
    <text x="432" y="262" class="ev-map-pin-number-compact">2</text>

    <!-- 3. Prétoire (palais d'Hérode, ouest) -->
    <circle cx="178" cy="248" r="5" class="ev-map-place-probable"/>
    <text x="178" y="248" class="ev-map-pin-number-dark-compact">3</text>

    <!-- 4. Golgotha (hors murs nord-ouest) -->
    <circle cx="148" cy="192" r="5" class="ev-map-place-probable"/>
    <text x="148" y="192" class="ev-map-pin-number-dark-compact">4</text>
  </g>
"""


CHAPTER_12_OVERLAY = """
  <g id="evangiles-chapitre-12-overlay">
    <rect x="36" y="1378" width="660" height="268" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1432" class="ev-map-title">Chapitre 12</text>
    <text x="64" y="1472" class="ev-map-subtitle">Béthanie et Éphraïm</text>
    <text x="64" y="1524" class="ev-map-note">1. Béthanie : Lazare malade puis ressuscité</text>
    <text x="64" y="1558" class="ev-map-note">2. Jérusalem : le sanhédrin décide de faire mourir Jésus</text>
    <text x="64" y="1592" class="ev-map-note">3. Éphraïm : Jésus se retire à l'écart</text>

    <!-- 1. Béthanie -->
    <circle cx="740" cy="1150" r="11" class="ev-map-place"/>
    <text x="740" y="1150" class="ev-map-pin-number">1</text>

    <!-- 2. Jérusalem (Sanhédrin) -->
    <circle cx="664" cy="1144" r="11" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">2</text>

    <!-- 3. Éphraïm -->
    <circle cx="715" cy="1015" r="11" class="ev-map-place"/>
    <text x="715" y="1015" class="ev-map-pin-number">3</text>
  </g>
"""


CHAPTER_11_JERUSALEM_OVERLAY = """
  <g id="evangiles-chapitre-11-jerusalem-overlay">
    <rect x="12" y="390" width="336" height="172" rx="8" class="ev-map-legend-box"/>
    <text x="28" y="422" class="ev-map-title-compact">Chapitre 11</text>
    <text x="28" y="444" class="ev-map-subtitle-compact">Jérusalem</text>
    <text x="28" y="470" class="ev-map-note-compact">1. Temple : Tabernacles, lumière du monde,</text>
    <text x="28" y="490" class="ev-map-note-compact">   femme adultère, fête de la Dédicace</text>
    <text x="28" y="514" class="ev-map-note-compact">2. Siloé : guérison de l'aveugle-né</text>

    <path class="ev-map-callout" d="M 303 218 L 320 222"/>
    <circle cx="303" cy="218" r="5" class="ev-map-place"/>
    <text x="303" y="218" class="ev-map-pin-number-compact">1</text>

    <path class="ev-map-callout" d="M 338 488 L 325 472"/>
    <circle cx="338" cy="488" r="5" class="ev-map-place"/>
    <text x="338" y="488" class="ev-map-pin-number-compact">2</text>
  </g>
"""


CHAPTER_11_PEREE_JERICHO_OVERLAY = """
  <g id="evangiles-chapitre-11-peree-jericho-overlay">
    <rect x="36" y="1318" width="650" height="258" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1372" class="ev-map-title">Chapitre 11</text>
    <text x="64" y="1412" class="ev-map-subtitle">Pérée et Jéricho</text>
    <text x="64" y="1464" class="ev-map-note">1. Pérée : divorce, richesses, annonce mort et résurrection</text>
    <text x="64" y="1498" class="ev-map-note">2. Jéricho : guérison d'aveugles, Zachée</text>
    <text x="64" y="1532" class="ev-map-note">3. Jéricho : parabole des 10 mines</text>
    <text x="64" y="1572" class="ev-map-note">Flèche : route de Pérée vers Jéricho.</text>

    <path class="ev-map-route" d="M 1016 1000 C 980 1030 920 1058 824 1086"/>

    <!-- 1. Pérée -->
    <circle cx="1018" cy="998" r="11" class="ev-map-place"/>
    <text x="1018" y="998" class="ev-map-pin-number">1</text>

    <!-- 2. Jéricho -->
    <circle cx="822" cy="1088" r="11" class="ev-map-place"/>
    <text x="822" y="1088" class="ev-map-pin-number">2</text>

    <!-- 3. Jéricho (parabole mines — adjacent) -->
    <circle cx="858" cy="1088" r="11" class="ev-map-place"/>
    <text x="858" y="1088" class="ev-map-pin-number">3</text>
  </g>
"""


CHAPTER_10_OVERLAY = """
  <g id="evangiles-chapitre-10-overlay">
    <rect x="36" y="1378" width="640" height="248" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1432" class="ev-map-title">Chapitre 10</text>
    <text x="64" y="1472" class="ev-map-subtitle">Samarie</text>
    <text x="64" y="1524" class="ev-map-note">1. Frontière samaritaine : guérison de dix lépreux</text>
    <text x="64" y="1558" class="ev-map-note">Un seul, Samaritain, revient rendre grâce.</text>
    <text x="64" y="1602" class="ev-map-note">Parabolus du juge inique et du pharisien</text>
    <text x="64" y="1636" class="ev-map-note">enseignées en route vers Jérusalem.</text>

    <!-- 1. Frontière Galilée / Samarie -->
    <circle cx="700" cy="720" r="11" class="ev-map-place"/>
    <text x="700" y="720" class="ev-map-pin-number">1</text>

    <text x="728" y="710" class="ev-map-small-label">Galilée ↑</text>
    <text x="728" y="738" class="ev-map-small-label">Samarie ↓</text>
  </g>
"""


CHAPTER_09_SAMARIE_JUDEE_OVERLAY = """
  <g id="evangiles-chapitre-09-samarie-judee-overlay">
    <rect x="36" y="1360" width="650" height="280" rx="8" class="ev-map-legend-box"/>
    <text x="64" y="1414" class="ev-map-title">Chapitre 9 (2/2)</text>
    <text x="64" y="1454" class="ev-map-subtitle">De la Galilée vers Jérusalem</text>
    <text x="64" y="1506" class="ev-map-note">1. Galilée : départ, face mise vers Jérusalem</text>
    <text x="64" y="1540" class="ev-map-note">2. Samarie : village refuse de recevoir Jésus</text>
    <text x="64" y="1574" class="ev-map-note">3. Béthanie : Jésus chez Marthe et Marie</text>
    <text x="64" y="1614" class="ev-map-note">Flèche : route de Galilée vers Jérusalem par la Samarie.</text>

    <!-- Route: Galilée → Samarie → Béthanie -->
    <path class="ev-map-route" d="M 800 488 C 780 640 752 760 722 868"/>
    <path class="ev-map-route" d="M 722 868 C 728 988 734 1082 740 1156"/>

    <!-- 1. Galilée (départ) -->
    <circle cx="802" cy="486" r="11" class="ev-map-place"/>
    <text x="802" y="486" class="ev-map-pin-number">1</text>
    <text x="830" y="476" class="ev-map-small-label">Galilée</text>

    <!-- 2. Samarie -->
    <circle cx="720" cy="870" r="11" class="ev-map-place"/>
    <text x="720" y="870" class="ev-map-pin-number">2</text>

    <!-- 3. Béthanie -->
    <circle cx="740" cy="1158" r="11" class="ev-map-place"/>
    <text x="740" y="1158" class="ev-map-pin-number">3</text>
  </g>
"""


MAPS = [
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-02-naissance-jeunesse.svg",
        "aria": "Naissance et jeunesse de Jésus",
        "overlay": CHAPTER_02_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-03-debut-ministere-judee.svg",
        "aria": "Début du ministère avec Jean le Baptiste en Judée",
        "overlay": CHAPTER_03_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-04-bethanie.svg",
        "aria": "Jean le Baptiste à Béthanie",
        "overlay": CHAPTER_04_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-05-galilee.svg",
        "aria": "Jésus en Galilée",
        "overlay": CHAPTER_05_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-06-judee-samarie.svg",
        "aria": "Jésus et Jean le Baptiste en Judée",
        "overlay": CHAPTER_06_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-07-galilee.svg",
        "aria": "Jésus en Galilée",
        "overlay": CHAPTER_07_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-07-traversee-lac.svg",
        "aria": "Traversée du lac de Tibériade",
        "overlay": CHAPTER_07_LAKE_OVERLAY,
    },
    {
        "source": JERUSALEM_RASTER_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-08-jerusalem.svg",
        "aria": "Jérusalem au temps du Second Temple",
        "overlay": CHAPTER_08_OVERLAY,
        "raster": True,
        "width": 464,
        "height": 598,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-09-galilee-phenicie.svg",
        "aria": "Galilée, Phénicie et Décapole — ministère de Jésus",
        "overlay": CHAPTER_09_GALILEE_NORD_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-09-galilee-jerusalem.svg",
        "aria": "De la Galilée vers Jérusalem par la Samarie",
        "overlay": CHAPTER_09_SAMARIE_JUDEE_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-15-ascension.svg",
        "aria": "Mont des Oliviers et Jérusalem — Ascension et Pentecôte",
        "overlay": CHAPTER_15_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-14-jerusalem-emmaus.svg",
        "aria": "Jérusalem et Emmaüs — résurrection et apparitions",
        "overlay": CHAPTER_14_JERUSALEM_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-14-galilee.svg",
        "aria": "Galilée — apparitions du Ressuscité",
        "overlay": CHAPTER_14_GALILEE_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-13-bethanie-jerusalem.svg",
        "aria": "Béthanie et entrée triomphale à Jérusalem",
        "overlay": CHAPTER_13_BETHANIE_OVERLAY,
    },
    {
        "source": JERUSALEM_RASTER_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-13-passion.svg",
        "aria": "Jérusalem — Temple, Gethsémani, Prétoire, Golgotha",
        "overlay": CHAPTER_13_PASSION_OVERLAY,
        "raster": True,
        "width": 464,
        "height": 598,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-12-bethanie-ephraim.svg",
        "aria": "Béthanie et Éphraïm — résurrection de Lazare",
        "overlay": CHAPTER_12_OVERLAY,
    },
    {
        "source": JERUSALEM_RASTER_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-11-jerusalem.svg",
        "aria": "Jérusalem — Tabernacles, aveugle-né, Dédicace",
        "overlay": CHAPTER_11_JERUSALEM_OVERLAY,
        "raster": True,
        "width": 464,
        "height": 598,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-11-peree-jericho.svg",
        "aria": "Pérée et Jéricho — enseignements et guérisons",
        "overlay": CHAPTER_11_PEREE_JERICHO_OVERLAY,
    },
    {
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-10-samarie.svg",
        "aria": "Frontière samaritaine — guérison des dix lépreux",
        "overlay": CHAPTER_10_OVERLAY,
    },
    {
        "source": PAUL_JOURNEY_1_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-16-paul-1er-voyage.svg",
        "aria": "Premier voyage missionnaire de Paul — Chypre et Galatie",
        "passthrough": True,
    },
    {
        "source": PAUL_JOURNEY_2_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-17-paul-2eme-voyage.svg",
        "aria": "Deuxième voyage missionnaire de Paul — Grèce et Asie Mineure",
        "passthrough": True,
    },
    {
        "source": PAUL_JOURNEY_3_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-18-paul-3eme-voyage.svg",
        "aria": "Troisième voyage missionnaire de Paul — Grèce et Asie Mineure",
        "passthrough": True,
    },
    {
        "source": PAUL_JOURNEY_ROME_SOURCE,
        "output": ROOT / "assets" / "maps" / "generated" / "chapitre-18-paul-rome.svg",
        "aria": "Voyage de Paul en prisonnier vers Rome",
        "passthrough": True,
    },
]


def copy_source_map(source_path: Path, output: Path, aria: str) -> None:
    import re
    output.parent.mkdir(parents=True, exist_ok=True)
    source = source_path.read_text(encoding="utf-8")
    generated = re.sub(r'<svg\b', f'<svg role="img" aria-label="{aria}"', source, count=1)
    output.write_text(generated, encoding="utf-8")
    print(f"Copied {output.relative_to(ROOT)}")


def generate_map(source: str, output: Path, aria: str, overlay: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    generated = source.replace("</svg>", f"{COMMON_DEFS}{overlay}\n</svg>")
    generated = generated.replace("<svg\n", f'<svg role="img" aria-label="{aria}"\n', 1)
    output.write_text(generated, encoding="utf-8")
    print(f"Generated {output.relative_to(ROOT)}")


def generate_raster_map(source_path: Path, output: Path, aria: str, overlay: str, width: int, height: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    image_data = base64.b64encode(source_path.read_bytes()).decode("ascii")
    generated = f"""<svg role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <title>{aria}</title>
  <image href="data:image/jpeg;base64,{image_data}" x="0" y="0" width="{width}" height="{height}" preserveAspectRatio="xMidYMid meet"/>
{COMMON_DEFS}{overlay}
</svg>
"""
    output.write_text(generated, encoding="utf-8")
    print(f"Generated {output.relative_to(ROOT)}")


def main() -> None:
    for map_config in MAPS:
        source_path = map_config.get("source", SOURCE)
        if map_config.get("passthrough"):
            copy_source_map(
                source_path,
                output=map_config["output"],
                aria=map_config["aria"],
            )
            continue
        if map_config.get("raster"):
            generate_raster_map(
                source_path,
                output=map_config["output"],
                aria=map_config["aria"],
                overlay=map_config["overlay"],
                width=map_config["width"],
                height=map_config["height"],
            )
            continue

        source = source_path.read_text(encoding="utf-8")
        if "</svg>" not in source:
            raise SystemExit(f"Invalid SVG source: {source_path}")

        generate_map(
            source,
            output=map_config["output"],
            aria=map_config["aria"],
            overlay=map_config["overlay"],
        )


if __name__ == "__main__":
    main()
