from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "maps" / "sources" / "Holy_sites_of_Jesus_in_Palestine.svg"
OUTPUT = ROOT / "assets" / "maps" / "generated" / "chapitre-02-naissance-jeunesse.svg"


OVERLAY = """
  <defs>
    <filter id="ev-map-label-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feFlood flood-color="#fffdf2" flood-opacity="0.9"/>
      <feComposite in2="SourceGraphic" operator="out"/>
      <feGaussianBlur stdDeviation="3"/>
      <feComposite in2="SourceGraphic" operator="over"/>
    </filter>
    <style>
      .ev-map-title { font: 700 42px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; }
      .ev-map-subtitle { font: 400 24px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4d4a41; }
      .ev-map-place { fill: #2b2a25; stroke: #fffdf2; stroke-width: 6; }
      .ev-map-place-probable { fill: #fffdf2; stroke: #2b2a25; stroke-width: 4; }
      .ev-map-pin-number { font: 700 24px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #fffdf2; text-anchor: middle; dominant-baseline: central; }
      .ev-map-label { font: 700 28px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; filter: url(#ev-map-label-shadow); }
      .ev-map-small-label { font: 500 22px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #2b2a25; filter: url(#ev-map-label-shadow); }
      .ev-map-note { font: 400 19px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4d4a41; }
      .ev-map-legend-box { fill: #fffdf2; fill-opacity: 0.88; stroke: #d6c9a7; stroke-width: 2; }
    </style>
  </defs>
  <g id="evangiles-chapitre-02-overlay">
    <rect x="742" y="1378" width="520" height="324" rx="8" class="ev-map-legend-box"/>
    <text x="770" y="1472" class="ev-map-title">Chapitre 2</text>
    <text x="770" y="1512" class="ev-map-subtitle">Naissance et jeunesse de Jésus</text>
    <text x="770" y="1554" class="ev-map-note">1. Jérusalem : annonce à Zacharie</text>
    <text x="770" y="1588" class="ev-map-note">2. Nazareth : annonces à Marie et Joseph</text>
    <text x="770" y="1622" class="ev-map-note">3. Bethléem : naissance, bergers et mages</text>
    <text x="770" y="1656" class="ev-map-note">4. Égypte : fuite et séjour</text>
    <text x="770" y="1690" class="ev-map-note">5. Jérusalem : Jésus au Temple à douze ans</text>

    <circle cx="700" cy="552" r="18" class="ev-map-place"/>
    <text x="700" y="552" class="ev-map-pin-number">2</text>

    <circle cx="652" cy="1264" r="18" class="ev-map-place"/>
    <text x="652" y="1264" class="ev-map-pin-number">3</text>

    <circle cx="664" cy="1144" r="18" class="ev-map-place"/>
    <text x="664" y="1144" class="ev-map-pin-number">1</text>

    <circle cx="696" cy="1144" r="18" class="ev-map-place"/>
    <text x="696" y="1144" class="ev-map-pin-number">5</text>

    <circle cx="656" cy="1060" r="11" class="ev-map-place-probable"/>

    <circle cx="156" cy="1694" r="18" class="ev-map-place"/>
    <text x="156" y="1694" class="ev-map-pin-number">4</text>
    <text x="184" y="1684" class="ev-map-label">Vers l'Égypte</text>
  </g>
"""


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    if "</svg>" not in source:
        raise SystemExit(f"Invalid SVG source: {SOURCE}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    generated = source.replace("</svg>", f"{OVERLAY}\n</svg>")
    generated = generated.replace("<svg\n", '<svg role="img" aria-label="Naissance et jeunesse de Jésus"\n', 1)
    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
