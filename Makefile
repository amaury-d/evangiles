all: build

node_modules: package-lock.json
	npm install

maps: assets/maps/generated/chapitre-02-naissance-jeunesse.svg assets/maps/generated/chapitre-03-debut-ministere-judee.svg assets/maps/generated/chapitre-04-bethanie.svg assets/maps/generated/chapitre-05-galilee.svg assets/maps/generated/chapitre-06-judee-samarie.svg assets/maps/generated/chapitre-07-galilee.svg assets/maps/generated/chapitre-07-traversee-lac.svg assets/maps/generated/chapitre-08-jerusalem.svg

assets/maps/generated/chapitre-02-naissance-jeunesse.svg assets/maps/generated/chapitre-03-debut-ministere-judee.svg assets/maps/generated/chapitre-04-bethanie.svg assets/maps/generated/chapitre-05-galilee.svg assets/maps/generated/chapitre-06-judee-samarie.svg assets/maps/generated/chapitre-07-galilee.svg assets/maps/generated/chapitre-07-traversee-lac.svg assets/maps/generated/chapitre-08-jerusalem.svg: assets/maps/sources/Holy_sites_of_Jesus_in_Palestine.svg assets/maps/sources/Jerusalem_in_70_map.svg scripts/generate_maps.py
	python3 scripts/generate_maps.py

data: maps src/data/harmony.generated.json src/pages/annexes

src/data/harmony.generated.json: data/harmony.json data/translations.json bible.db scripts/build_site_data.py assets maps
	python3 scripts/build_site_data.py

src/pages/annexes: annexes scripts/build_annexes.py
	python3 scripts/build_annexes.py

build: node_modules data
	npm run build

serve: node_modules
	npm run dev

refresh-bible:
	python3 extractor/fetch_bible.py $(TRANSLATION)

clean:
	rm -rf dist .astro public/assets src/data/harmony.generated.json src/data/annexes.generated.json src/pages/annexes
