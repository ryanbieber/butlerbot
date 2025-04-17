# Makefile for managing Docker Compose and PostgreSQL with a local mount

DOCKER_COMPOSE_FILE=docker-compose.yml
POSTGRES_DATA=./postgres-data

.PHONY: up down clean postgres

# Start Docker Compose services
up:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

# Stop Docker Compose services
down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

# Start PostgreSQL with a local mount
postgres: $(POSTGRES_DATA)
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d postgres

# Create the local mount directory for PostgreSQL
$(POSTGRES_DATA):
	mkdir -p $(POSTGRES_DATA)

# Clean up the local mount directory
clean:
	rm -rf $(POSTGRES_DATA)