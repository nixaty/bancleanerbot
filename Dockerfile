FROM python:3.12-slim

WORKDIR /bancleanerbot
COPY requirements.txt /bancleanerbot/
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

COPY . /bancleanerbot

CMD python main.py