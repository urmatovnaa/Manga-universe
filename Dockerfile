FROM python:3.10-alpine
WORKDIR /main/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /main/
RUN pip install -r requirements.txt
COPY . /main/