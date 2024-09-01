FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn app:app & python3 -m SessionGenerator
