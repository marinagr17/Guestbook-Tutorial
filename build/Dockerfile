# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \   
    default-libmysqlclient-dev \             
    build-essential \                        
    pkg-config \                             
    && rm -rf /var/lib/apt/lists/*  

COPY app/ .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8800

CMD ["./entrypoint.sh"]
