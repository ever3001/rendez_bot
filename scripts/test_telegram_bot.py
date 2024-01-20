#!/usr/bin/env python

from rendez_bot.config.config import Config
from rendez_bot.telegram.telegram_bot import TelegramBot


def main():
    config = Config.parse_json_file()
    telegram_bot = TelegramBot(
        token=config.telegram.token, chat_id=config.telegram.chat_id
    )
    message = "Bonjour 🥐"
    telegram_bot.send_message(message)


if __name__ == "__main__":
    main()
