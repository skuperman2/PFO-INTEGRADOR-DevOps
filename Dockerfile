# Dockerfile for EcomData Quart App
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
	&& pip install --no-cache-dir hypercorn

# Copy the rest of the application code
COPY . .

# Expose port (default Quart port)
EXPOSE 5000

# Set environment variables for Quart
ENV QUART_APP=app:app
ENV QUART_ENV=production
ENV PORT=5000
ENV HYPERCORN_WORKERS=1

# Add entrypoint script and create a non-root user to run the app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Create a non-root user and ensure app ownership
RUN adduser --disabled-password --gecos "" appuser || true \
	&& chown -R appuser:appuser /app

USER appuser

# Entrypoint will initialize the SQLite DB (create tables) then exec the CMD
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

# Use Hypercorn (ASGI server) for production; expand workers env var via shell
CMD ["sh", "-c", "hypercorn app:app --bind 0.0.0.0:5000 --workers ${HYPERCORN_WORKERS:-1}"]
