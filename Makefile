all: build

node_modules: package-lock.json
	npm install

GENERATED_MAPS = \
	assets/maps/generated/chapitre-02-naissance-jeunesse.svg \
	assets/maps/generated/chapitre-03-debut-ministere-judee.svg \
	assets/maps/generated/chapitre-04-bethanie.svg \
	assets/maps/generated/chapitre-05-galilee.svg \
	assets/maps/generated/chapitre-06-judee-samarie.svg \
	assets/maps/generated/chapitre-07-galilee.svg \
	assets/maps/generated/chapitre-07-traversee-lac.svg \
	assets/maps/generated/chapitre-08-jerusalem.svg \
	assets/maps/generated/chapitre-09-galilee-phenicie.svg \
	assets/maps/generated/chapitre-09-galilee-jerusalem.svg \
	assets/maps/generated/chapitre-10-samarie.svg \
	assets/maps/generated/chapitre-11-jerusalem.svg \
	assets/maps/generated/chapitre-11-peree-jericho.svg \
	assets/maps/generated/chapitre-12-bethanie-ephraim.svg \
	assets/maps/generated/chapitre-13-bethanie-jerusalem.svg \
	assets/maps/generated/chapitre-13-passion.svg \
	assets/maps/generated/chapitre-14-jerusalem-emmaus.svg \
	assets/maps/generated/chapitre-14-galilee.svg \
	assets/maps/generated/chapitre-15-ascension.svg

maps: $(GENERATED_MAPS)

$(GENERATED_MAPS): assets/maps/sources/Holy_sites_of_Jesus_in_Palestine.svg assets/maps/sources/Jerusalem_premier_siecle.JPG scripts/generate_maps.py
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
