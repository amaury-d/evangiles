all: build

node_modules: package-lock.json
	npm install

data: src/data/harmony.generated.json

src/data/harmony.generated.json: data/harmony.json bible.db scripts/build_site_data.py assets
	python3 scripts/build_site_data.py

build: node_modules
	npm run build

serve: node_modules
	npm run dev

migrate-harmony:
	python3 scripts/migrate_harmony.py

refresh-bible:
	python3 extractor/fetch_tob.py

clean:
	rm -rf dist .astro public/assets src/data/harmony.generated.json
