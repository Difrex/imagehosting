FROM python:3.6

COPY ./config /opt/app/config
COPY ./utils /opt/app/utils
COPY ./imagehosting /opt/app/imagehosting
ADD manage.py /opt/app
ADD requirements.txt /opt/app

RUN pip install -r /opt/app/requirements.txt

RUN chown -R nobody:nogroup /opt/app

ADD ./docker/docker-entrypoint.sh /usr/local/bin

WORKDIR /opt/app

EXPOSE 8080

USER nobody

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
