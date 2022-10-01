
FROM arm64v8/python:3.6-buster
ENV TZ="America/Sao_Paulo"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    sshpass \
    dnsutils \
    git \
    sudo \
    net-tools \
    build-essential

WORKDIR /app

COPY . /app
RUN pip install -r requiremets.txt
CMD python3 api.py
