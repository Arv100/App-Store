# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Django app runs on
EXPOSE 8000

# Run Django's collectstatic command (optional, but recommended for production)
RUN python manage.py collectstatic --noinput

# Run the Django app with Gunicorn (recommended for production)
CMD ["gunicorn", "appstore.wsgi:application", "--bind", "0.0.0.0:8000"]
