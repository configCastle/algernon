FROM python:3.8

WORKDIR /app

ADD . /app

RUN python setup.py develop

EXPOSE 8080

CMD [ "./entrypoint.sh" ]
