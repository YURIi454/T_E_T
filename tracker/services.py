import requests

from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_mess_telega(chat_id, message):
    """ Отправка сообщения в телеграм. """

    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
