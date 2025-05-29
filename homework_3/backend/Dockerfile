# # Use official Python image
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Expose the port Flask will run on
# EXPOSE 8080

# # Set environment variable to allow Flask to run in any environment
# ENV FLASK_ENV=production

# # Start the app using gunicorn (recommended for production)
# CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

# Base image with Python and ffmpeg
FROM python:3.11-slim

# Install system dependencies (ffmpeg, etc.)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements2.txt .
RUN pip install -r requirements2.txt

# Copy the rest of the code into the container
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port Cloud Run will listen on
EXPOSE 8080

# Run the app on port 8080 for Cloud Run
#CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
CMD ["python", "app.py"]