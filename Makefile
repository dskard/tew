PWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

PYTESTOPTS=


all: build

build:
	docker build -t="dskard/tew:dev" .

test:
	docker run -it --rm \
	  --name=tew-test \
	  --user=$(shell id -u):$(shell id -g) \
	  --volume=${PWD}:/opt/shared/tew \
	  --workdir=/opt/shared/tew \
	  -e "PATH=/opt/shared/tew:/usr/local/bin:/usr/bin:/bin" \
	  dskard/tew:dev \
	  pytest ${PYTESTOPTS} /opt/shared/tew/test


.PHONY: build test
