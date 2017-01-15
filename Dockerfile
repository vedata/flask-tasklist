# This is a Flask Image

FROM python:2.7.10
MAINTAINER Vedat Karaaslan <vedat.karaaslan@ruv.de>

COPY start.sh /
COPY requirements.txt /

RUN apt-get update && apt-get install -y \
    python-pip

RUN pip install -r requirements.txt && \
    git clone https://github.com/vedata/flask-tasklist.git

ENTRYPOINT ./start.sh
