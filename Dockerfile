# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# Copy the requirements file and install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project code
COPY . .

# Expose the default Django port
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
