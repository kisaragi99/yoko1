.PHONY: init up down

init: up

up:
	docker-compose up -d --build

down:
	docker-compose down --remove-orphans
