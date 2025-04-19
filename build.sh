# Bash script to build and run the docker container for the Python application
#!/bin/bash
# Exit on error
set -e

# Build the Docker image
#docker build -t hello-python .
#docker build -f Dockerfile.light -t hello-python .
#docker build -f Dockerfile.ubuntu -t hello-python .
#docker build --pull=false -f Dockerfile.ubuntu -t hello-python .
docker build --pull=false -f Dockerfile.debian -t hello-python .

# Run the Docker container
docker run -it hello-python

# Run the Docker container
#docker run -p 5000:5000 hello-python
#docker run -it -p 5000:5000 hello-python

