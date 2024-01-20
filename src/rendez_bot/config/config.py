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

import json
import logging
import os
from pydantic import BaseModel

DEFAULT_CONFIG_FILE_PATH = os.path.join(os.getcwd(), "config.json")
DEFAULT_CONFIG_TEMPLATE_FILE_PATH = os.path.join(os.getcwd(), "config.template.json")


class TelegramCfg(BaseModel):
    token: str
    chat_id: str


class PersonalInfoCfg(BaseModel):
    last_name: str
    first_name: str
    birthdate: str
    nationality: str
    address: str
    postal_code: str
    city: str


class VisaCfg(BaseModel):
    visa_number: str
    validity_date: str


class Config(BaseModel):
    telegram: TelegramCfg
    personal_info: PersonalInfoCfg
    visa_info: VisaCfg

    @classmethod
    def parse_json_file(cls, path=DEFAULT_CONFIG_FILE_PATH):
        with open(path, "r") as json_file:
            data = json.load(json_file)
            logging.debug(f"Parsed data:\r\n{data}")
            return cls(**data)

    @classmethod
    def create_config_json_file_template(cls, path=DEFAULT_CONFIG_TEMPLATE_FILE_PATH):
        # Create template object
        config_obj = cls(
            telegram=TelegramCfg(
                token="YOUR_TELEGRAM_TOKEN",
                chat_id="YOUR_CHAT_ID",
            ),
            personal_info=PersonalInfoCfg(
                last_name="YOUR_LAST_NAME",
                first_name="YOUR_FIRST_NAME",
                birthdate="YOUR_BIRTHDATE",
                nationality="YOUR_NATIONALITY",
                address="YOUR_ADDRESS",
                postal_code="YOUR_POSTAL_CODE",
                city="YOUR_CITY",
            ),
            visa_info=VisaCfg(
                visa_number="YOUR_VISA_NUMBER",
                validity_date="YOUR_VALIDITY_DATE",
            ),
        )

        # Write template into the file
        with open(path, "w") as config_file:
            json.dump(config_obj.model_dump(), config_file)
