#!/usr/bin/env python

#   python script designed to facilitate booking appointments at French 
#   police departments for visa purposes.

#   Copyright (C) 2024  Ever ATILANO

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import logging

from time import sleep

from rendez_bot.__init__ import __version__ as rendez_bot_version
from rendez_bot.telegram.telegram_bot import TelegramBot
from rendez_bot.config.config import Config, DEFAULT_CONFIG_FILE_PATH
from rendez_bot.bots.bot_factory import BotFactory, BotTypeEnum

# Set up logging format and level
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(prog="rendez_bot")
    parser.add_argument(
        "-v", "--version", action="version", version=str(rendez_bot_version)
    )
    parser.add_argument(
        "-c",
        "--configuration_file",
        type=str,
        help="Path to the configuration file.",
        default=DEFAULT_CONFIG_FILE_PATH,
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        help="Time in seconds to wait before running the bot.",
        default=5,
    )
    args = parser.parse_args()
    return args


def get_bot_type_by_postal_code(postal_code: str) -> BotTypeEnum:
    """
    Get the bot type based on the postal code.

    Args:
        postal_code (str): The postal code.

    Returns:
        BotTypeEnum: The type of bot based on the postal code.
    """
    try:
        first_two_digits = postal_code[:2]
        return BotTypeEnum(int(first_two_digits))
    except ValueError as e:
        logging.error(e)
        raise NotImplementedError(f"The bot for {postal_code} is not implemented yet.")


def main():
    """
    The main function that initializes the bot and runs the appropriate bot based on the postal code.
    """
    args = parse_args()
    config = Config.parse_json_file(path=args.configuration_file)
    telegram_bot = TelegramBot(
        token=config.telegram.token, chat_id=config.telegram.chat_id
    )
    bot_type = get_bot_type_by_postal_code(config.personal_info.postal_code)

    while True:
        bot = BotFactory.get_bot(bot_type, config=config, telegram_bot=telegram_bot)
        bot.execute_bot()
        sleep(args.time)


if __name__ == "__main__":
    main()
