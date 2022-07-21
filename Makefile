DOCKER=docker-compose
DB=python3 manage.py

.PHONY: init up down makemigrations migrate

init:
	@$(DOCKER) up -d --build

up:
	@$(DOCKER) up -d

down:
	@$(DOCKER) down --remove-orphans

makemigrations:
	@$(DB) makemigrations adminloader

migrate:
	@$(DB) migrate adminloader
