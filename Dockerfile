# Use the latest Ubuntu base image
FROM ubuntu:24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .

# Copy the Flask application file
COPY /src/main.py .

# Install Python dependencies
#RUN pip3 install --no-cache-dir -r requirements.txt

# Install dependencies with override flag
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Define the default command to run the Flask app
CMD ["python3", "main.py"]
