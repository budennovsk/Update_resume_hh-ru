from celery import Celery
from config import REDIS_HOST, REDIS_PORT, REDISUSER, REDIS_PASS
from api import Update


celery = Celery('tasks', broker=f'redis://{REDISUSER}:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}',
                broker_connection_retry_on_startup=True)

CELERYD_MAX_TASKS_PER_CHILD = 1  # 单work最多任务使用数
CELERYD_CONCURRENCY = 3  # 单worker最大并发数
CELERYD_MAX_MEMORY_PER_CHILD = 2000 # 单任务可占用2G内存
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 * 3
CELERYD_HIJACK_ROOT_LOGGER = False


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
