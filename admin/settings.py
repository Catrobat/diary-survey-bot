# List of chat_ids that are admins
ADMINS = ['0x0', '0x0']

# Debug mode on/off
DEBUG = True

# /delete command enabled/disabled
DELETE = True

# For testing purposes. Sets all block scheduling to x seconds.
# To deactivate set it to False (0)
QUICK_TEST = 5

# Default language if something goes wrong.
DEFAULT_LANGUAGE = 'de'

# Default timezone if something goes wrong.
DEFAULT_TIMEZONE = 'Europe/Vienna'

# OR    - One condition is enough
# AND   - All conditions must hold
CONDITION_SCHEME = 'OR'

# Scheduling intervals for question blocks.
SCHEDULE_INTERVALS = {
                        "RANDOM_1": ["08:00", "12:00"],
                        "RANDOM_2": ["13:00", "15:00"],
                        "RANDOM_3": ["16:00", "20:00"]
                     }

INFO_TEXT = {
                "de": "pokemon@uni-graz.at",
                "en": "pokemon@uni-graz.at",
                "fr": "pokemon@uni-graz.at",
                "es": "pokemon@uni-graz.at"
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





