# syntax=docker/dockerfile:1
FROM python:3.14.2-trixie

WORKDIR /app

COPY app/ .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["./entrypoint.sh"]
