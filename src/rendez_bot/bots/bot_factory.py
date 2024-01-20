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

from enum import IntEnum

from rendez_bot.bots.generic_bot import GenericBot
from rendez_bot.bots.city_implementation import ParisBot, ValDeMarneBot
from rendez_bot.config.config import Config
from rendez_bot.telegram.telegram_bot import TelegramBot


class BotTypeEnum(IntEnum):
    MEURTHE_ET_MOSELLE = 54
    PARIS = 75
    VAL_DE_MARNE = 94


class BotFactory:
    @classmethod
    def get_bot(
        cls, bot_type: BotTypeEnum, config: Config, telegram_bot: TelegramBot
    ) -> GenericBot:
        if bot_type == BotTypeEnum.PARIS:
            return ParisBot(config=config, telegram_bot=telegram_bot)
        if bot_type == BotTypeEnum.VAL_DE_MARNE:
            return ValDeMarneBot(config=config, telegram_bot=telegram_bot)
        else:
            raise NotImplementedError(
                f"The bot type {bot_type} is not implemented yet."
            )
