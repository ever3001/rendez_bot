import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from rendez_bot.bots.generic_bot import GenericBot
from rendez_bot.tools.captcha_resolver import CaptchaResolver


from time import sleep


class ParisBot(GenericBot):
    def execute_bot(self):
        try:
            self.driver.get("https://www.ppoletrangers.interieur.gouv.fr/?motif=rensej")

            ########################################################
            # 01 page: Renouvellement du titre de séjour form
            ########################################################
            # Fill the form
            nom = self.driver.find_element(By.ID, "nom")
            nom.send_keys(self.config.personal_info.last_name)
            prenom = self.driver.find_element(By.ID, "prenom")
            prenom.send_keys(self.config.personal_info.first_name)
            agdref = self.driver.find_element(By.ID, "agdref")
            agdref.send_keys(self.config.visa_info.visa_number)
            naissance = self.driver.find_element(By.ID, "naissance")
            naissance.send_keys(self.config.personal_info.birthdate)
            validite = self.driver.find_element(By.ID, "validite")
            validite.send_keys(self.config.visa_info.validity_date)

            # Captcha
            # open file in write and binary mode
            captcha_img_path = os.path.join(os.getcwd(), "captcha.png")
            with open(captcha_img_path, "wb") as file:
                # identify image to be captured
                l = self.driver.find_element(By.ID, "captchaimg")
                file.write(l.screenshot_as_png)
                captcha_string = CaptchaResolver.resolve_captcha_img_to_text(
                    captcha_img_path
                )
                print(captcha_string)
                captchacode = self.driver.find_element(By.ID, "captchacode")
                captchacode.send_keys(captcha_string)

            # Click in the submit button
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        finally:
            self.driver.quit()
