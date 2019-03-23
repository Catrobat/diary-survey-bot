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
# Instead of intervals you can also define fixed events.
# IMPORTANT: If you choose intervals, make sure they are at least 30min!
# Intervals:    "KEYWORD": ["hh:mm", "hh:mm"]
# fixed event:  "KEYWORD": ["hh:mm"]
SCHEDULE_INTERVALS = {
    "random (08-10)": ["08:00", "10:00"],
    "random (11-13)": ["11:00", "13:00"],
    "random (15-18)": ["15:00", "18:00"],
    "random (19-22)": ["19:00", "22:00"],
    "05:00": "05:00",
    "05:30": "05:30",
    "06:00": "06:00",
    "06:30": "06:30",
    "07:00": "07:00",
    "07:30": "07:30",
    "08:00": "08:00",
    "08:30": "08:30",
    "09:00": "09:00",
    "09:30": "09:30",
    "10:00": "10:00",
    "10:30": "10:30",
    "11:00": "11:00",
    "11:30": "11:30",
    "12:00": "12:00",
    "12:30": "12:30",
    "13:00": "13:00",
    "13:30": "13:30",
    "14:00": "14:00",
    "14:30": "14:30",
    "15:00": "15:00",
    "15:30": "15:30",
    "16:00": "16:00",
    "16:30": "16:30",
    "17:00": "17:00",
    "17:30": "17:30",
    "18:80": "18:30",
    "18:30": "18:30",
    "19:00": "19:00",
    "19:30": "19:30",
    "20:00": "20:00",
    "20:30": "20:30",
    "21:00": "21:00",
    "21:30": "21:30",
    "22:00": "22:00",
    "22:30": "22:30"
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
