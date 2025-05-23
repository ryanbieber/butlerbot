FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
ENV PYTHONPATH=/app
RUN uv sync --frozen --no-cache

ENTRYPOINT ["uv", "run", "src/main.py"]
