# -*- coding: utf-8 -*-
# Detecteur de "trous" dans l'harmonie

import sqlite3
from harmonie import harmonie

harmonie.append({
        'titre': 'Ignore me',
        'contenu': [
            {
                'titre': 'Prologue des actes',
                'contenu': [ None, None, None, None, [[1, 1, 5]]],
            },
                        {
                'titre': 'Conclusions Jean',
                'contenu': [ None, None, None, [[20,30,31],[21,25,25]], None],
            },
        ]
})

DB='bible.db'

conn = sqlite3.connect(DB, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, timeout=10.0, isolation_level=None)
cur = conn.cursor()

def is_verset_in_harmonie(db_evangeliste:str,db_chapitre_id:int, db_verset_id:int) -> bool:
    for ha_chapitre in harmonie:
        for ha_section in ha_chapitre['contenu']:
            ha_versets = {
                'matthieu':ha_section['contenu'][0],
                'marc':ha_section['contenu'][1],
                'luc':ha_section['contenu'][2],
                'jean':ha_section['contenu'][3],
                'actes':ha_section['contenu'][4],
            }
            if ha_versets[db_evangeliste]:
                for ha_ids in ha_versets[db_evangeliste]:
                    if not ha_ids: continue
                    ha_chapitre_id, ha_start_verset_id, ha_end_verset_id = ha_ids
                    if ha_chapitre_id==db_chapitre_id and db_verset_id>=ha_start_verset_id and db_verset_id<=ha_end_verset_id:
                        return True
    return False

cur.execute("SELECT evangeliste, chapitre_id, verset_id FROM versets ORDER BY evangeliste, chapitre_id, verset_id ASC")
for row in cur.fetchall():
    db_evangeliste, db_chapitre_id, db_verset_id=row
    if not is_verset_in_harmonie(db_evangeliste, db_chapitre_id, db_verset_id):
        print(f"{db_evangeliste.capitalize()} {db_chapitre_id}:{db_verset_id} missing")

