from src.common.env import telegram_token
from src.telegram.bot import TelegramBot


if __name__ == "__main__":

    telegram_bot = TelegramBot(telegram_token)

    telegram_bot.run()

