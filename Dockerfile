FROM python:3.8

WORKDIR /app

ADD . /app

RUN apt-get update && \
    apt-get install cmake flex bison -y

RUN python setup.py develop

EXPOSE 8080

CMD [ "./entrypoint.sh" ]
