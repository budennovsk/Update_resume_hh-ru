import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
MY_ID_RESUME = os.environ.get('MY_ID_RESUME')
TG_BOT_KEY = os.environ.get('TG_BOT_KEY')