FROM		python:3.7-slim

RUN			apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN			apt -y install nginx

COPY		./requirements.txt /tmp/
RUN			pip install -r /tmp/requirements.txt

COPY		. /srv/amanda_clone
WORKDIR		/srv/amanda_clone/app

RUN			rm /etc/nginx/sites-enabled/default
RUN			cp /srv/amanda_clone/.config/dev_dooh/amanda_clone.nginx /etc/nginx/sites-enabled/

RUN			mkdir /var/log/gunicorn

CMD			/bin/bash
