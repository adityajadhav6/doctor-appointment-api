# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all code to container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run db.py to initialize database
RUN python models/db.py

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
