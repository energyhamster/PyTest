FROM python:3.10-alpine

ARG run_env
ENV env $run_env

LABEL "channel"="Hamster"
LABEL "creator"="Energy_hamster"

WORKDIR ./PyTest

VOLUME /allure_results

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN pip install pydantic[email]

COPY . .

CMD pytest -m "$env" -s -v tests/* --alluredir=allure_results