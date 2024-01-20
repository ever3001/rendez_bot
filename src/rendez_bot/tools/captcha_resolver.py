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

import easyocr


class CaptchaResolver:
    @classmethod
    def resolve_captcha_img_to_text(cls, image_path) -> str:
        reader = easyocr.Reader(
            ["en", "fr"]
        )  # this needs to run only once to load the model into memory
        results = reader.readtext(image_path)
        return " ".join([result[1] for result in results])
