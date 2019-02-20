"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""

import json
from admin.settings import DEFAULT_LANGUAGE


# TODO add guide on how to add languages
class DataSet:
    participants = {}
    q_set_de_ = None
    q_set_en_ = None
    q_set_es_ = None
    q_set_fr_ = None

    def __init__(self):
        try:
            with open('survey/question_set_de.json') as file:
                self.q_set_de_ = json.load(file)
        except FileNotFoundError:
            print('Language: German not available!')
        try:
            with open('survey/question_set_en.json') as file:
                self.q_set_en_ = json.load(file)
        except FileNotFoundError:
            print('Language: English not available!')
        try:
            with open('survey/question_set_es.json') as file:
                self.q_set_es_ = json.load(file)
        except FileNotFoundError:
            print('Language: Spanish not available!')
        try:
            with open('survey/question_set_fr.json') as file:
                self.q_set_fr_ = json.load(file)
        except FileNotFoundError:
            print('Language: French not available!')
        return

    def get_participant(self, chat_id):
        return self.participants[chat_id]

    def add_participant(self, user):
        self.participants[user.chat_id] = user
        return

    def return_question_set_by_language(self, lang):
        if lang == 'de' and self.q_set_de_ is not None:
            return self.q_set_de_
        elif lang == 'en' and self.q_set_en_ is not None:
            return self.q_set_en_
        elif lang == 'es' and self.q_set_es_ is not None:
            return self.q_set_es_
        elif lang == 'fr' and self.q_set_fr_ is not None:
            return self.q_set_fr_
        else:
            return self.return_question_set_by_language(DEFAULT_LANGUAGE)
