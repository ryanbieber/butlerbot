# Makefile for managing Docker Compose and PostgreSQL with a local mount

DOCKER_COMPOSE_FILE=docker-compose.yml

.PHONY: up down

# Start Docker Compose services
up:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d --build --force-recreate

# Stop Docker Compose services
down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down
