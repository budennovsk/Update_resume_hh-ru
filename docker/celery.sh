#!/bin/bash


celery --app=tasks.celery worker --loglevel=INFO -P solo
#celery --app=tasks.celery beat --loglevel=INFO
celery --app=tasks.celery flower --loglevel=INFO
