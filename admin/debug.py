"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""

from admin.settings import DEBUG


def debug(flag, text, log=False):
    if DEBUG is False:
        return

    print(flag + ':\t' + text)
    if log:
        with open('log.txt', 'a') as f:
            f.write(flag + '\t\t' + text + '\n')
    return
