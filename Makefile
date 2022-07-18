DOCKER=docker-compose

.PHONY: init up down

init:
	@$(DOCKER) up -d --build

up:
	@$(DOCKER) up -d

down:
	@$(DOCKER) down --remove-orphans
