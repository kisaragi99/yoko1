DOCKER=docker-compose

.PHONY: init up down clean

init:
	$(DOCKER) up -d --build

up:
	$(DOCKER) up -d

down:
	$(DOCKER) down --remove-orphans

clean:
	@rm -rf data
