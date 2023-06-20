#!/bin/bash

celery --app=tasks.celery beat --loglevel=INFO
celery --app=tasks.celery worker --loglevel=debug
