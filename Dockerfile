# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY oilandgas_company.db /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
