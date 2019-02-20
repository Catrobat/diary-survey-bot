"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""

# List of chat_ids that are admins
ADMINS = ['0x0', '0x0']

# Debug mode on/off
DEBUG = True

# /delete_me command enabled/disabled
DELETE = True

# For testing purposes. Sets all block scheduling to x seconds.
# To deactivate set it to False (0)
QUICK_TEST = 15

# Default language if something goes wrong.
DEFAULT_LANGUAGE = 'de'

# Default timezone if something goes wrong.
DEFAULT_TIMEZONE = 'Europe/Vienna'

# OR    - One condition is enough
# AND   - All conditions must hold
CONDITION_SCHEME = 'OR'

# Scheduling intervals for question blocks.
# IMPORTANT: If you choose intervals, make sure they are at least 30min!
# Todo: add documentation
SCHEDULE_INTERVALS = {
                        "RANDOM_1": ["08:00", "12:00"],
                        "RANDOM_2": ["13:00", "15:00"],
                        "RANDOM_3": ["16:00", "20:00"],
                        "0700": "07:00",
                        "0800": "08:00",
                        "0900": "09:00",
                        "1000": "10:00",
                        "1100": "11:00",
                        "1200": "12:00",
                        "1300": "13:00",
                        "1400": "14:00",
                        "1500": "15:00",
                        "1600": "16:00",
                        "1700": "17:00",
                        "1800": "18:00",
                        "1900": "19:00",
                        "2000": "20:00",
                        "2100": "21:00"
                     }

INFO_TEXT = {
                "de": "https://github.com/Catrobat/diary-survey-bot",
                "en": "https://github.com/Catrobat/diary-survey-bot",
                "fr": "https://github.com/Catrobat/diary-survey-bot",
                "es": "https://github.com/Catrobat/diary-survey-bot"
            }

STOP_TEXT = {
                "de": "Vielen Dank für deine Teilnahme! "
                      "Wenn du möchtest würden wir uns über eine Nachricht freuen,"
                      " warum du nicht mehr weitermachen willst. Falls du es dir anders"
                      " überlegst, kannst du jederzeit wieder teilnehmen, indem du uns eine"
                      " Nachricht mit \"/start\" schickst.",
                "en": "Thank you for your participation! If "
                      "you want to, we would appreciate a message "
                      "why you don't feel like continuing the study. "
                      "Anyway, if you change your mind, you can resume "
                      "by sending us a message with the word \"/start\".",
                "es": "Gracias por tu participación. Si lo deseas, sería de gran utilidad"
                      " si nos haces saber por qué no deseas continuar con el estudio."
                      " De todas maneras, si cambias de opinión y deseas seguir participando,"
                      " envíanos un mensaje que diga: \"/start\"",
                "fr": "Merci beaucoup pour ta participation. Si tu le souhaites,"
                      " envoie-nous un message donnant les raisons pour lesquelles"
                      " tu préfères arrêter de participer. Si tu changes d'avis, envoie-nous"
                      " un message avec le mot \"/start\", tu pourras recommencer tout de suite."
            }
