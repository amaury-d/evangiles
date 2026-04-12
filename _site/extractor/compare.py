# -*- coding: utf-8 -*-

import sqlite3
from harmonie import harmonie
from typing import List

OUTPUT='evangiles'
DB='bible.db'

conn = sqlite3.connect(DB, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, timeout=10.0, isolation_level=None)
cur = conn.cursor()

dernier_titre=None

def fetch_versets(evangeliste: str, chapitre_id: int, start_verset_id: int, end_verset_id:int) -> str:
    dernier_titre=None

    cur.execute("SELECT verset_id, titre, texte FROM versets WHERE evangeliste=? AND chapitre_id=? AND verset_id>=? AND verset_id<=? ORDER BY verset_id ASC", (evangeliste, chapitre_id, start_verset_id, end_verset_id))
    versets=''
    for row in cur.fetchall():
        verset_id, titre, texte=row

        if dernier_titre!=titre:
            versets+=f"### {evangeliste.capitalize()} _{chapitre_id}:{verset_id}_ : {titre}\n<br/>"
            dernier_titre=titre
        versets+=f"<sup>{verset_id}</sup> {texte}\n"
    return versets


# console = Console()
# def prt_md(texte:str='')->None:
    # console.print(Markdown(texte))



def prt_md(texte:str='')->None:
    file_h.write(f"{texte}\n")

def prt_header_file(file_id:int, titre:str, perma_id:str) -> None:
    prt_md("---")
    prt_md("layout: page")
    prt_md(f"title: \"{file_id}. {titre}\"")
    prt_md(f"permalink: /{OUTPUT}/{perma_id}.html")
    prt_md(f"nav_order: {file_id}")
    prt_md("parent: Evangiles")
    prt_md("---")
    prt_md()


def prt_header_section(infos) -> None:  # sourcery skip: extract-method
    if 'images' in infos:
        for image, description in infos['images'].items():
            prt_md(f"![{description}](../assets/{image})" + '{:.centered}')
            prt_md()
            prt_md("{:.image-caption}")
            prt_md(f"*{description}*")

    cartouche_header_printed=False
    for field_name in ['date', 'lieu']:
        if field_name in infos:
            if not cartouche_header_printed:
                prt_md("> info \"\"")
                cartouche_header_printed=True
            field_value = infos[field_name]
            prt_md(f"> **{field_name.capitalize()}**: {field_value}")
            prt_md('>')


def prt_footer_section(infos) -> None:  # sourcery skip: extract-method
    if 'notes' in infos:
        prt_md("> note \"\"")

        for note in infos["notes"]:
            prt_md(f"> - {note}")

file_id=0
for chapitre in harmonie:

    file_id=file_id+1
    perma_id=f"chapitre_{file_id}-{chapitre['titre_short']}"
    with open(f"{OUTPUT}/{perma_id}.md", 'w', encoding='utf-8') as file_h:
        prt_header_file(file_id, chapitre['titre'], perma_id)
        prt_md(f"# {chapitre['titre']}")
        prt_md()

        prt_header_section(chapitre)

        for section in chapitre['contenu']:
            prt_md(f"## {section['titre']}")
            prt_md()

            prt_header_section(section)

            evangiles = {
                'marc':section['contenu'][1],
                'luc':section['contenu'][2],
                'matthieu':section['contenu'][0],
                'jean':section['contenu'][3],
                'actes':section['contenu'][4],
            }

            for evangeliste, id_grps in evangiles.items():
                if not id_grps: continue
                for ids in id_grps:
                    if not ids: continue
                    chapitre_id, start_verset_id, end_verset_id = ids
                    texte = fetch_versets(evangeliste, chapitre_id, start_verset_id, end_verset_id)
                    prt_md(f"{texte}")
                    prt_md()

            prt_footer_section(section)
        prt_footer_section(chapitre)

conn.close()