all: build

node_modules: package-lock.json
	npm install

data: src/data/harmony.generated.json src/pages/annexes

src/data/harmony.generated.json: data/harmony.json data/translations.json bible.db scripts/build_site_data.py assets
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
