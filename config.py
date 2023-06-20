import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
MY_ID_RESUME = os.environ.get('MY_ID_RESUME')
TG_BOT_KEY = os.environ.get('TG_BOT_KEY')
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

MY_ID_BOT = os.environ.get('MY_ID_BOT')
REDISUSER = os.environ.get('REDISUSER')
REDIS_PASS = os.environ.get('REDIS_PASS')
