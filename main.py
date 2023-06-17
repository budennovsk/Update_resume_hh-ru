from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

storage = MemoryStorage()
bot = Bot(token=TG_BOT_KEY)
disDot = Dispatcher(bot, storage=storage)


class Update:
    """ Класс обновления резюме через телеграм"""

    @classmethod
    def update_resume(cls):
        """ Поднятие резюме """

        URL = f'https://api.hh.ru/resumes/{MY_ID_RESUME}/publish/'

        header = {
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            'User-Agent': 'api-test-agent'
        }

        response = requests.post(url=URL, headers=header)
        if response.status_code == 204:
            return 204
        if response.status_code == 403:
            raise Exception('Ошибка авторизации Access Token')
        return response.status_code

@disDot.message_handler(commands=["start"])
async def start_command(message: types.Message):
    """
       Обработка команды /start. Приветствие пользователя и предложение выбрать
       действие.
       """
    if message.chat.type == types.ChatType.PRIVATE:
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=2,
                                                    resize_keyboard=True)
        up_button = types.KeyboardButton('/up')

        keyboard_markup.add(up_button)
        await message.reply('Привет! Что вы хотите сделать?',
                            reply_markup=keyboard_markup)


@disDot.message_handler(commands=['up'])
async def up_resume(message: types.Message):
    """
    Обработка команды /up для поднятия резюме
    """

    try:
        up = Update.update_resume()
        if up == 204:
            await message.reply('Резюме обновлено')
        if message.from_id != 646576220:
            await message.reply('Ты не местный, я вызываю копов')
        else:
            await message.reply(f'Резюме не обновлено\n'
                                f'Ошибка: {up}')

    except Exception as e:
        await message.reply(f'Ошибка системы {e}')


@disDot.message_handler()
async def allComands(message: types.Message):
    """ Обработка команд неверных"""
    await message.reply('Введите команду /up')


if __name__ == '__main__':
    executor.start_polling(disDot)
