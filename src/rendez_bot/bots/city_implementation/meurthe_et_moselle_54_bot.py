import logging

from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By

from rendez_bot.bots.generic_bot import GenericBot

RVD_URL = "https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/3771"


class ValDeMarneBot(GenericBot):
    def execute_bot(self):
        try:
            pass
        finally:
            self.driver.quit()
