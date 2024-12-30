FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt ./

RUN apk add gcc musl-dev build-base linux-headers libffi-dev rust cargo openssl-dev git && \
    pip install setuptools-rust && \
    pip install --no-cache-dir -r requirements.txt

COPY *.py ./

CMD uvicorn main:app --host 0.0.0.0 --port 9000
