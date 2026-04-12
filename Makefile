all: _site

evangiles/chapitre_*.md: extractor bible.db
	rm -f evangiles/chapitre_*.md
	python3 extractor/compare.py

Gemfile.lock: Gemfile
	bundle install

_site: Gemfile.lock Gemfile _bibliography _layouts *.html  *.md *.yml assets evangiles/chapitre_*.md
	bundle exec jekyll build

serve: Gemfile.lock _site
	bundle exec jekyll serve

bible.db:
	python3 extractor/fetch_tob.py

trous:
	python3 extractor/trous.py

publish: _site
	rsync -av --delete _site/ /Users/amaury/Library/CloudStorage/Dropbox/backup-server/static-sites/evangiles/

clean:
	rm -f evangiles/chapitre_*.md
	find . -name '__pycache__' -type d -delete
	rm -rf _site .jekyll-cache .jekyll-metadata
