# Bash script to build and run the docker container for the Python application
#!/bin/bash
# Exit on error
set -e
# Build the Docker image
docker build -t hello-python .
# Run the Docker container
docker run -it hello-python

