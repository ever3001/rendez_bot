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

from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver
import chromedriver_autoinstaller

from typing import Optional, Union, Any

from rendez_bot.telegram.telegram_bot import TelegramBot
from rendez_bot.config.config import Config


class GenericBot(BaseModel):
    config: Config
    telegram_bot: TelegramBot
    driver: Optional[Any] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Check if the current version of chromedriver exists
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()

    def execute_bot(self):
        raise NotImplementedError(
            "Please do not call this method directly. Use the inherited class method."
        )
