FROM python:3.12.4-alpine

WORKDIR /app

COPY requirements.txt ./

RUN apk add --no-cache make gcc g++
RUN python -m pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del make gcc g++

COPY . /app
ENTRYPOINT sh /app/entrypoint.sh