import time # for sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

condition = True

while condition:
    browser = webdriver.Chrome()
    browser.get('https://www.ppoletrangers.interieur.gouv.fr/?motif=rensej')

    nom = browser.find_element_by_id("nom")
    prenom = browser.find_element_by_id("prenom")
    agdref = browser.find_element_by_id("agdref")
    naissance = browser.find_element_by_id("naissance")
    validite = browser.find_element_by_id("validite")

    nom.send_keys(data.get("nom"))
    prenom.send_keys(data.get("prenom"))
    agdref.send_keys(data.get("agdref"))
    naissance.send_keys(data.get("naissance"))
    validite.send_keys(data.get("validite"))

    browser.find_element_by_xpath("//button[@type='submit']").click()

    nationalite = Select(browser.find_element_by_name('nationalite'))
    nationalite.select_by_visible_text(data.get("nationalite"))
    arrdt = Select(browser.find_element_by_name('arrdt'))
    arrdt.select_by_visible_text(data.get("arrdt"))

    browser.find_element_by_xpath("//input[@type='submit']").click()

    text = "Nous ne sommes pas en mesure de traiter votre demande."

    if (text in browser.page_source):
        browser.quit()
    else:
        condition = False
        #open tab
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # Load a page 
        browser.get('https://youtu.be/M3CSWLFL5u8')
        break
    time.sleep(data.get("time_in_secs"))