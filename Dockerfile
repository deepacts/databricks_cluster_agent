FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
ENV PORT=8080
EXPOSE 8080

# Start FastAPI server
CMD ["python3", "app.py"]
