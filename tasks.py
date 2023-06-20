from celery import Celery
from config import REDIS_HOST, REDIS_PORT, REDISUSER, REDIS_PASS
from api import Update


celery = Celery('tasks', broker=f'redis://{REDISUSER}:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}',
                broker_connection_retry_on_startup=True)

celery.conf.CELERYD_MAX_TASKS_PER_CHILD = 1


@celery.task
def send_resume():
    res = Update()
    result = res.update_resume()
    if result == 204:
        return 'Обновлено'
    elif result == 429:
        return 'Резюме не обновлено'
    else:
        raise Exception('Ошибка запроса')


celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.send_resume',
        'schedule': 30.0,
    },
}
celery.conf.timezone = 'UTC'
