#!/bin/bash
#python manage.py makemigrations
#python manage.py migrate
#python manage.py collectstatic
#/usr/sbin/crond -s
uwsgi --stop uwsgi.pid
uwsgi uwsgi.ini 
#/usr/sbin/sshd -D
tail -f /dev/null
