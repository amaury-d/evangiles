import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "maps" / "sources" / "Holy_sites_of_Jesus_in_Palestine.svg"
JERUSALEM_RASTER_SOURCE = ROOT / "assets" / "maps" / "sources" / "Jerusalem_premier_siecle.JPG"


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
]


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
