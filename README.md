# Rendez-bot : Votre Assistant de Rendez-vous

## Introduction

Rendez-bot est né durant la crise du COVID-19, face à la difficulté de prendre des rendez-vous au commissariat de Paris pour le renouvellement du titre de séjour. Ce bot a été conçu pour surveiller les disponibilités et alerter l'utilisateur via Telegram dès qu'un créneau se libère.

L'objectif est de faciliter la prise de rendez-vous dans différents commissariats. Si une disponibilité est détectée, une alerte est immédiatement envoyée.

Pour découvrir les bots disponibles, consultez la section [Liste de Bots](./README.md#liste-de-bots).

## Prérequis

- Python version 3.9 ou ultérieure
- Navigateur Google Chrome
- Un bot Telegram (https://www.youtube.com/watch?v=aQaCoVn7NbA)

## Installation

Exécutez la commande suivante pour installer :

```bash
pip install .
```

## Configuration

Créez un fichier `config.json` contenant les informations nécessaires à l'exécution du script. Un modèle `config.template.json` est disponible dans ce dépôt. Copiez et modifiez ce modèle selon vos besoins.

## Guide d'Utilisation

### Test du bot Telegram

Testez le bot Telegram avant utilisation :

```bash
python scripts/test_telegram_bot.py

```

Un message "Bonjour 🥐" devrait apparaître sur Telegram.

### Lancement du bot

Pour démarrer le bot :

```bash
rendez_bot

```

## Contribution

Votre aide est la bienvenue pour étendre la couverture des préfectures. Les contributions sous forme de pull requests sont appréciées. Les implémentations spécifiques à chaque préfecture se trouvent dans `bots/city_implementation`. Pour exemple, consultez le bot de [Val-de-Marne](https://chat.openai.com/c/src/rendez_bot/bots/city_implementation/val_de_marne_94_bot.py).

## Liste de Bots

### Disponibles

- ✅ Val-de-Marne (94)

### Instables

- ⚠️ Paris (75)

### Indisponibles

- ❌ Ain (01)
- ❌ Aisne (02)
- ❌ Allier (03)
- ❌ Alpes-de-Haute-Provence (04)
- ❌ Hautes-Alpes (05)
- ❌ Alpes-Maritimes (06)
- ❌ Ardèche (07)
- ❌ Ardennes (08)
- ❌ Ariège (09)
- ❌ Aube (10)
- ❌ Aude (11)
- ❌ Aveyron (12)
- ❌ Bouches-du-Rhône (13)
- ❌ Calvados (14)
- ❌ Cantal (15)
- ❌ Charente (16)
- ❌ Charente-Maritime (17)
- ❌ Cher (18)
- ❌ Corrèze (19)
- ❌ Côte-d'Or (21)
- ❌ Côtes-d'Armor (22)
- ❌ Creuse (23)
- ❌ Dordogne (24)
- ❌ Doubs (25)
- ❌ Drôme (26)
- ❌ Eure (27)
- ❌ Eure-et-Loir (28)
- ❌ Finistère (29)
- ❌ Corse-du-Sud (2A)
- ❌ Haute-Corse (2B)
- ❌ Gard (30)
- ❌ Haute-Garonne (31)
- ❌ Gers (32)
- ❌ Gironde (33)
- ❌ Hérault (34)
- ❌ Ille-et-Vilaine (35)
- ❌ Indre (36)
- ❌ Indre-et-Loire (37)
- ❌ Isère (38)
- ❌ Jura (39)
- ❌ Landes (40)
- ❌ Loir-et-Cher (41)
- ❌ Loire (42)
- ❌ Haute-Loire (43)
- ❌ Loire-Atlantique (44)
- ❌ Loiret (45)
- ❌ Lot (46)
- ❌ Lot-et-Garonne (47)
- ❌ Lozère (48)
- ❌ Maine-et-Loire (49)
- ❌ Manche (50)
- ❌ Marne (51)
- ❌ Haute-Marne (52)
- ❌ Mayenne (53)
- ❌ Meurthe-et-Moselle (54)
- ❌ Meuse (55)
- ❌ Morbihan (56)
- ❌ Moselle (57)
- ❌ Nièvre (58)
- ❌ Nord (59)
- ❌ Oise (60)
- ❌ Orne (61)
- ❌ Pas-de-Calais (62)
- ❌ Puy-de-Dôme (63)
- ❌ Pyrénées-Atlantiques (64)
- ❌ Hautes-Pyrénées (65)
- ❌ Pyrénées-Orientales (66)
- ❌ Bas-Rhin (67)
- ❌ Haut-Rhin (68)
- ❌ Rhône (69)
- ❌ Haute-Saône (70)
- ❌ Saône-et-Loire (71)
- ❌ Sarthe (72)
- ❌ Savoie (73)
- ❌ Haute-Savoie (74)
- ❌ Seine-Maritime (76)
- ❌ Seine-et-Marne (77)
- ❌ Yvelines (78)
- ❌ Deux-Sèvres (79)
- ❌ Somme (80)
- ❌ Tarn (81)
- ❌ Tarn-et-Garonne (82)
- ❌ Var (83)
- ❌ Vaucluse (84)
- ❌ Vendée (85)
- ❌ Vienne (86)
- ❌ Haute-Vienne (87)
- ❌ Vosges (88)
- ❌ Yonne (89)
- ❌ Territoire de Belfort (90)
- ❌ Essonne (91)
- ❌ Hauts-de-Seine (92)
- ❌ Seine-Saint-Denis (93)
- ❌ Val-d'Oise (95)
