# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY src/ .

# Create a non-root user for security (optional but recommended)
RUN useradd -m demo
USER demo

# Command to run the application
CMD ["python", "main.py"]

# Instructions to build and run the Docker container
# To build the Docker image, run:
# docker build -t hello-python .
# To run the Docker container, use:
# docker run -it hello-python
