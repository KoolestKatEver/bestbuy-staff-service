# Use the official Python 3.11 image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (including bestbuy-staff-service.py)
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "bestbuy-staff-service.py"]
