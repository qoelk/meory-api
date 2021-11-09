FROM python:3.8-slim-buster
WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY . /backend
RUN pip install -r requirements.txt
