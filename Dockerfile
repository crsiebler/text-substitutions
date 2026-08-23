# Use the official Python image as the base image
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Install the package and development tools used by the Makefile test targets
COPY pyproject.toml README.md LICENSE ./
COPY pysubstitutor/ ./pysubstitutor/
RUN pip install --no-cache-dir ".[dev]"

# Copy application data and tests
COPY data/ /app/data/
COPY tests/ /app/tests/

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Explicitly set the entrypoint
ENTRYPOINT ["python", "-m", "pysubstitutor"]
