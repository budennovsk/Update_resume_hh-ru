from celery import Celery
from config import REDIS_HOST, REDIS_PORT
from api import Update

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')



def send_resume():
    print("выполнено")
    res = Update()
    print(res)
    res.update_resume()


celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.send_resume',
        'schedule': 30.0,
    },
}
celery.conf.timezone = 'UTC'
