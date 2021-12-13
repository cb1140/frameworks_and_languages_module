DOCKER_IMAGE:=client


build:
	docker build --tag ${DOCKER_IMAGE} .

test:
	docker run --rm ${DOCKER_IMAGE}

run:
	docker run --rm -it --publish 8001:80 ${DOCKER_IMAGE}
	