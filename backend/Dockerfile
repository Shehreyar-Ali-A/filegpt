# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY poetry.lock pyproject.toml /code/

# Install tesseract
RUN apt update && apt install -y tesseract-ocr && apt install -y libtesseract-dev

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-root --no-dev

# Copy the current directory contents into the container at /code
COPY . /code/

# Expose both port 8080 for HTTP and port 443 for HTTPS
EXPOSE 8080
EXPOSE 443

# Install Nginx and copy SSL certificate files
RUN apt-get update && apt-get install -y nginx openssl
COPY nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key
COPY nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt

# Remove the default Nginx configuration file
RUN rm /etc/nginx/sites-enabled/default

# Copy the Nginx configuration file for the Django app
COPY nginx/nginx.conf /etc/nginx/sites-enabled/

# Start Nginx and run the Django development server
CMD ["nginx", "-g", "daemon off;"]
