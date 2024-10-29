# Use the official image as a parent image
FROM python:3.13-slim

# Set the working directory
ENV APP_HOME=/app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]