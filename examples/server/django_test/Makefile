DOCKER_IMAGE:=django_test

build:
	docker build --tag ${DOCKER_IMAGE} .
run:
	docker run --rm -it --publish 8000:8000 ${DOCKER_IMAGE}
shell:
	docker run --rm -it \
		--publish 8000:8000 \
		--volume ${PWD}:/app/:ro \
		${DOCKER_IMAGE} \
		/bin/bash

install_local:
	pip install django
	django-admin startproject mysite
	# edit `mysite/settings.py` to have `ALLOWED_HOSTS = ['*']`
run_local:
	python3 mysite/manage.py runserver 0.0.0.0:8000