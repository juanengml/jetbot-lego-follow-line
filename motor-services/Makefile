SHELL := /bin/bash
PROJECT_NAME = motor-service
APP_NAME:= motor-service
DOCKER_IMG := $(PROJECT_NAME):latest
DOCKER_RUN := docker run --rm -t -it 
# Docker tasks
help:
	@echo "usage: make <command> [VERSION=X.Y.Z]"
	@echo
	@echo "COMMANDS"   
	@echo "    help     Show this help"
	@echo "    format   Using black before commit to style code"
	@echo "    build    Build docker image from Dockerfile"
	@echo "    run      Run Container Service"
	@echo "    clean    Remove all Container, Image, Volume"
config:
	pip3 install black make curl

build:
	sudo docker build -t $(PROJECT_NAME) .

run:build
	sudo docker run --name $(PROJECT_NAME) -p 8080:8080 --device /dev/ttyUSB0:/dev/ttyUSB0  -d  $(DOCKER_IMG)

clean:
	sudo docker stop $(PROJECT_NAME)
	sudo docker rm $(PROJECT_NAME)
	sudo docker volume rm $(DOCKER_IMG) --force

# Docker black
format:
	python3 -m black motor.py api.py test_unit.py

test:
	python3 test_unit.py
	python3 test_integration.py

logs:
	sudo docker logs $(PROJECT_NAME)

stop:
	sudo docker stop  $(PROJECT_NAME)
start:
	sudo docker start $(PROJECT_NAME)
