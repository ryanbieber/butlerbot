# Makefile for Docker build and run with auto-restart

IMAGE_NAME=butlerbot
CONTAINER_NAME=butlerbot

.PHONY: build run down

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run container with auto-restart
run:
	docker run -d \
		--name $(CONTAINER_NAME) \
		--restart always \
		$(IMAGE_NAME)

# Stop and remove container
down:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
