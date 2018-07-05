PWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

PYTESTOPTS=


all: build

lockfiles:
	cd python2; pipenv --python 2 lock;
	cd python3; pipenv --python 3 lock;
	pipenv --python 3 lock;

build:
	docker build -t="dskard/tew:python2" -f python2/Dockerfile .
	docker build -t="dskard/tew:python3" -f python3/Dockerfile .
	docker build -t="dskard/tew:dev" .

build-ubuntu:
	docker build -t="dskard/tew:python3-u16" -f python3-u16/Dockerfile .

build-deb9slim:
	docker build -t="dskard/tew:python3-deb9slim" python3-deb9slim

test:
	docker run -it --rm \
	  --name=tew-test \
	  --user=$(shell id -u):$(shell id -g) \
	  --volume=${PWD}:/opt/shared/tew \
	  --workdir=/opt/shared/tew \
	  -e "PATH=/opt/shared/tew:/usr/local/bin:/usr/bin:/bin" \
	  dskard/tew:dev \
	  pytest ${PYTESTOPTS} /opt/shared/tew/test

run:
	docker run -it --rm \
	  --name=tew-test \
	  --user=$(shell id -u):$(shell id -g) \
	  --volume=${PWD}:/opt/shared/tew \
	  --workdir=/opt/shared/tew \
	  -e "PATH=/opt/shared/tew:/usr/local/bin:/usr/bin:/bin" \
	  dskard/tew:dev \
	  ${COMMAND}


.PHONY: build test run
