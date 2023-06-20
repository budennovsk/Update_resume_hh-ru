#!/bin/bash


celery --app=tasks.celery worker --loglevel=INFO
#celery --app=tasks.celery beat --loglevel=INFO
#celery --app=tasks.celery flower --loglevel=INFO
chown -R nobody:nogroup /var/run/celery /var/log/celery

exec celery --app=tasks.celery worker \
            --loglevel=INFO --logfile=/var/log/celery/worker-example.log \
            --statedb=/var/run/celery/worker-example@%h.state \
            --hostname=worker-example@%h \
            --queues=celery.example -O fair \
            --uid=nobody --gid=nogroup