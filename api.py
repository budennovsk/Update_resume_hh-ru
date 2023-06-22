import requests
from config import MY_ID_RESUME, ACCESS_TOKEN


class Update:
    """ Класс обновления резюме через телеграм"""

    @classmethod
    def update_resume(cls):
        """ Поднятие резюме списка резюме 5 шт. """
        for id_resume in MY_ID_RESUME.split(','):
            URL = f'https://api.hh.ru/resumes/{id_resume}/publish/'

            header = {
                'Authorization': f'Bearer {ACCESS_TOKEN}',
                'User-Agent': 'api-test-agent'
            }

            response = requests.post(url=URL, headers=header)
            return response.status_code
