FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dns/ ./dns/
COPY google.py facebook.py ./

EXPOSE 5000/udp 8000 8001
