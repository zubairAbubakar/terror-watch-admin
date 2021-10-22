FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client

RUN pip install -r requirements.txt
COPY . /app
