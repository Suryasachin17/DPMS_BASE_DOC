FROM python:3.10

WORKDIR /app

# Install system dependencies first
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install cryptography  # Explicitly install cryptography

COPY . .

CMD ["python", "app.py"]