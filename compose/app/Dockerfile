FROM python:3.10.18-alpine
ENV PYTHONUNBUFFERED 1


USER root
WORKDIR /app
ADD . /app

RUN \
	  apk update \
	  && apk add make gcc libffi-dev openssl-dev python3-dev musl-dev supervisor postgresql-dev zsh \
      && pip install -r requirements/dev.txt

RUN mkdir /var/log/app


ENV PYTHONPATH /audicus
