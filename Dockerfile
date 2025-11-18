# Dockerfile for EcomData Quart App
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (default Quart port)
EXPOSE 5000

# Set environment variables for Quart
ENV QUART_APP=app:app
ENV QUART_ENV=production

# Start the Quart app
CMD ["python", "-m", "quart", "run", "--host", "0.0.0.0", "--port", "5000"]
