.PHONY: all
all:
	$(MAKE) build
	$(MAKE) docker

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

.PHONY: docker
docker:
	docker build -t wizard-changelog:local .
	docker run --rm --name "wizard-changelog" -p 8888:8080 wizard-changelog:local
