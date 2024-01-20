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

import logging
import requests
from pydantic import BaseModel


class TelegramBot(BaseModel):
    token: str
    chat_id: str

    def send_message(self, message: str):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={message}"
        r = requests.get(url)
        logging.debug(r.json())

    def test_bot(self):
        url = f"https://api.telegram.org/bot{self.token}/getMe"
        r = requests.get(url)
        logging.debug(r.json())
