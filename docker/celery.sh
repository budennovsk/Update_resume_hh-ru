#!/bin/bash


celery --app=tasks.celery worker --loglevel=INFO --max-tasks-per-child=1
#celery --app=tasks.celery beat --loglevel=INFO
celery --app=tasks.celery flower --loglevel=INFO
