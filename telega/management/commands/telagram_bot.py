import os

from django.core.management import BaseCommand
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


class Command(BaseCommand):
    help = "Запуск бота телеграм"

    def handle(self, *args, **options):
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text('Привет! Я напомню о ваших привычках!')

        app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        app.add_handler(CommandHandler("start", start))

        app.run_polling()
