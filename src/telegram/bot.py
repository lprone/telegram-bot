from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from src.telegram.handler.question import question
from src.telegram.handler.start import start


class TelegramBot:

    def __init__(self, token):
        self.token = token

    def run(self):
        app = ApplicationBuilder().token(self.token).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, question))
        app.run_polling()
