#!/bin/bash

celery --app=tasks.celery worker --loglevel=INFO --concurrency 4 -P eventlet
#celery --app=tasks.celery beat --loglevel=INFO
#celery --app=tasks.celery flower --loglevel=INFO
