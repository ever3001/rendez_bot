# MIT License

# Copyright (c) 2020 Ever ATILANO (ever.developer3001@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time # for sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

## All data for the form
data = {
    "nom"           : "Pierre",         # Nom (e.g. Pierre)
    "prenom"        : "KONG",           # Prenom (e.g. KONG)
    "agdref"        : "1234567891",     # N° de votre titre de séjour (e.g. 1234567891)
    "naissance"     : "15/06/1998",     # Date de naissance (jj/mm/aaaa) (e.g. 15/06/1998)
    "validite"      : "20/09/2030",     # Date d'expiration du titre de séjour(jj/mm/aaaa) (e.g. 20/09/2030)
    "nationalite"   : "MEXICAINE",      # Nationalité (e.g. MEXICAINE)
    "arrdt"         : "12",             # Arrondissement (e.g. 12)
    "time_in_secs"  : 30                # Temps pour reviser la page web en secondes
}

while True:
    # New instance for Chrome
    browser = webdriver.Chrome()
    # Open the webpage
    browser.get('https://www.ppoletrangers.interieur.gouv.fr/?motif=rensej')
    # Save the window opener (current window, do not mistaken with tab... not the same)
    main_window = browser.current_window_handle
    ################################################## Fill all the first form
    nom = browser.find_element_by_id("nom")
    nom.send_keys(data.get("nom"))
    prenom = browser.find_element_by_id("prenom")
    prenom.send_keys(data.get("prenom"))
    agdref = browser.find_element_by_id("agdref")
    agdref.send_keys(data.get("agdref"))
    naissance = browser.find_element_by_id("naissance")
    naissance.send_keys(data.get("naissance"))
    validite = browser.find_element_by_id("validite")
    validite.send_keys(data.get("validite"))
    # Click in the submit button
    browser.find_element_by_xpath("//button[@type='submit']").click()
    ##################################################

    ################################################## Fill all the second form
    nationalite = Select(browser.find_element_by_name('nationalite'))
    nationalite.select_by_visible_text(data.get("nationalite"))
    arrdt = Select(browser.find_element_by_name('arrdt'))
    arrdt.select_by_visible_text(data.get("arrdt"))
    # Click in the submit button
    browser.find_element_by_xpath("//input[@type='submit']").click()
    ##################################################

    # Text to find when there is an error
    text = "Nous ne sommes pas en mesure de traiter votre demande."

    # If text error exist in webpage
    if (text in browser.page_source):
        # Print in console that we didn't have the rd
        print("Pas de chance pour trouver un rendez-vous ='(")
        # Close the browser
        browser.quit()
        # Retry in some seconds
        time.sleep(data.get("time_in_secs"))
    else:
        # Open tab and trigger the alarm
        browser.execute_script("window.open('http://soundbible.com/mp3/analog-watch-alarm_daniel-simion.mp3', '_blank')")
        break