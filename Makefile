.PHONY: build
build:
	$(MAKE) clean
	$(MAKE) prepare-dir
	python scripts/main.py

.PHONY: prepare-dir
prepare-dir:
	mkdir output output/assets
	cp assets/* output/assets

.PHONY: clean
clean:
	rm -rf output
