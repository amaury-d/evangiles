# -*- coding: utf-8 -*-

import requests
import sqlite3
import random
import time
import re
import unicodedata
from bs4 import BeautifulSoup

import sqlite3

DB='bible.db'

# Connect to the database
conn = sqlite3.connect(DB,detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, timeout=10.0, isolation_level=None)

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute("DROP TABLE IF EXISTS versets")
cursor.execute('CREATE TABLE versets ( \
    evangeliste TEXT, \
    chapitre_id INTEGER, \
    verset_id INTEGER, \
    titre TEXT, \
    texte TEXT, \
    UNIQUE(evangeliste, chapitre_id, verset_id) \
)')

chapitres ={
    "matthieu": 28,
    "marc": 16,
    "luc": 24,
    "jean": 21,
    "actes": 28,
}
# Commit the changes to the database
conn.commit()

def insert_verset(evangeliste:str, chapitre_id:int, titre:str, verset_id:int,texte:str):
    texte=unicodedata.normalize("NFKD", texte.strip())
    if len(texte):
        cursor.execute('INSERT INTO versets (evangeliste, chapitre_id, titre, verset_id, texte) VALUES (?, ?, ?, ?, ?)', (evangeliste, chapitre_id, titre, verset_id, texte))
        print(f"{evangeliste} {chapitre_id}:{verset_id} {texte}")


for evangeliste, chapitre_max in chapitres.items():
    for chapitre_id in range(1, chapitre_max+1):
        print(f"Evangeliste {evangeliste}")
        print(f"Chapitre {chapitre_id}")

        # Send a request to the website
        url = f'https://lire.la-bible.net/lecture/{evangeliste}/{chapitre_id}/1/TOB'
        response = requests.get(url)

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find an element in the HTML content
        tob = [element for element in soup.find_all('li', class_="liste__traduction") if element.get('rel')=='TOB'][0]
        zone_versets = tob.find("div", class_="zone_versets")

        titre=''
        for element in zone_versets.find_all(["span","p"]):
            classe = element["class"][0] if element.has_attr('class') else None

            if classe == "titre4":
                titre = element.get_text().strip()
                print(f"Titre {titre}")

            elif classe == "verset":
                raw_text = element.get_text().replace('\n', ' ').strip()
                if resultat := re.search(
                    r"^(?P<verset_id>\d+)(?P<texte>[^\d+]+)", raw_text
                ):
                    insert_verset(evangeliste, chapitre_id, titre, int(resultat['verset_id']), resultat['texte'])
                # print(element.prettify())

        conn.commit()

        time.sleep(random.random() + 0.1)

# Close the connection
conn.close()
