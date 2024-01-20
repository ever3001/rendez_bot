import logging

from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By

from rendez_bot.bots.generic_bot import GenericBot

RVD_URL = "https://rdv-etrangers-94.interieur.gouv.fr"


class ValDeMarneBot(GenericBot):
    def execute_bot(self):
        try:
            self.driver.get(RVD_URL)

            ########################################################
            # 1/4 : Code postal de résidence
            ########################################################
            CPId = self.driver.find_element(By.ID, "CPId")
            CPId.send_keys(self.config.personal_info.postal_code)

            # Click in the "Continuer" button
            self.driver.find_element(By.XPATH, "//input[@value='Continuer']").click()

            ########################################################
            # 2/4 : Motif de votre visite
            ########################################################
            motive_checkbox = self.driver.find_element(
                By.XPATH, "//input[@value='30']"
            ).click()

            # Click in the continuer button
            self.driver.find_element(By.ID, "nextButtonId").click()
            now_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            sleep(1)

            # If alert popup means that there is no rdv. So just accept the alert and go on
            found_rdv = False
            try:
                alert_obj = self.driver.switch_to.alert
                alert_msg = alert_obj.text
                logging.debug(f"Alert shows following message: {alert_msg}")

                if "Aucun rendez-vous" not in alert_msg:
                    found_rdv = False

                alert_obj.accept()
            except Exception as e:
                pass
            # If there is a rdv send a message
            if found_rdv:
                self.telegram_bot.send_message(
                    f"""
                        GO GO GO ! RDV displonible dans la prefecture de Val-de-Marne {RVD_URL}
                        Code Postal : {self.config.personal_info.postal_code}
                        RDV Trouve a {now_string}.
                        C'est parti !
                    """
                )
        finally:
            self.driver.quit()
