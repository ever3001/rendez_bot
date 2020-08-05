# Python script pour prendre un rendez-vous au commissariat de Paris
Avec la situation du corona, c'est presque impossible de pouvoir faire un **rendez-vous au commissariat de Paris** pour le renouvellement du titre de séjour. Donc, j'ai créé un petit script qui remplis les formulaires du page web de la [préfecture de police de paris](https://www.ppoletrangers.interieur.gouv.fr/?motif=rensej) chaque **30 secondes** pour voir s’il y a de la disponibilité dans le site. Si le bot trouve un rendez-vous, il va sonner une alarme. Le script a besoin de Python 3 et Selenium pour travailler.

## Installer Python
[Utilisation de Python sur Windows](https://docs.python.org/fr/3/using/windows.html)
[Utilisation de Python sur Linux](https://docs.python.org/fr/3/using/unix.html#on-linux)

## Installer Selenium
[Guide complet en anglais](https://selenium-python.readthedocs.io/installation.html)
### Installer Selenium pour Python
```bash
# installer selenium
pip install selenium
```
### Installer driver pour navigateur web

| Navigateur | Liens vers les pilotes de navigateur web                              |
|------------|-----------------------------------------------------------------------|
| Chrome:    | https://sites.google.com/a/chromium.org/chromedriver/downloads        |
| Edge:      | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Firefox:   | https://github.com/mozilla/geckodriver/releases                       |
| Safari:    | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          |

## Remplir les informations
Il faut remplir les informations suivantes pour les formulaires (de la ligne 10 à la ligne 18 du fichier [rdv_visa.py](./rdv_visa.py)).

```python
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
```

## Lancer le script
```bash
python rdv_visa.py
```