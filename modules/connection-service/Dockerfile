FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc g++ libpq-dev libgeos-c1v5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

ENV FLASK_APP=wsgi.py
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
