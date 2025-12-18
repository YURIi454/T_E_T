from celery import shared_task

from telega.services import send_telegram_message
from users.models import CustomUser


@shared_task
def send_telegram_reminder(user_id, message):
    """ Отправка сообщения в телеграм. """

    try:
        CustomUser.objects.get(id=user_id)
        chat_id = CustomUser.telega_id
        if chat_id:
            send_telegram_message(chat_id, message)
    except Exception as e:
        print(f"Ошибка: {e}")


@shared_task
def send_daily_reminders():
    """ Отправка напоминания в телеграм. """

    users = CustomUser.objects.filter(profile__telegram_chat_id__isnull=False)
    message = "Время выполнить Вашу привычку!"
    for user in users:
        send_telegram_reminder.delay(user.id, message)
