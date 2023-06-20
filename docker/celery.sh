#!/bin/bash

celery -A app.tasks.celery beat --loglevel=INFO
celery -A app.tasks.celery worker --loglevel=debug"
