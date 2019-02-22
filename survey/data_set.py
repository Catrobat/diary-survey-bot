"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""

import json
from admin.settings import DEFAULT_LANGUAGE


class DataSet:
    participants = {}
    q_set_de = None
    q_set_en = None
    q_set_es = None
    q_set_fr = None

    def __init__(self):
        try:
            with open('survey/question_set_de.json') as file:
                self.q_set_de = json.load(file)
        except FileNotFoundError:
            print('Language: German not available!')
        try:
            with open('survey/question_set_en.json') as file:
                self.q_set_en = json.load(file)
        except FileNotFoundError:
            print('Language: English not available!')
        try:
            with open('survey/question_set_es.json') as file:
                self.q_set_es = json.load(file)
        except FileNotFoundError:
            print('Language: Spanish not available!')
        try:
            with open('survey/question_set_fr.json') as file:
                self.q_set_fr = json.load(file)
        except FileNotFoundError:
            print('Language: French not available!')
        return

    def get_participant(self, chat_id):
        return self.participants[chat_id]

    def add_participant(self, user):
        self.participants[user.chat_id] = user
        return

    def return_question_set_by_language(self, lang):
        if lang == 'de' and self.q_set_de is not None:
            return self.q_set_de
        elif lang == 'en' and self.q_set_en is not None:
            return self.q_set_en
        elif lang == 'es' and self.q_set_es is not None:
            return self.q_set_es
        elif lang == 'fr' and self.q_set_fr is not None:
            return self.q_set_fr
        else:
            return self.return_question_set_by_language(DEFAULT_LANGUAGE)
