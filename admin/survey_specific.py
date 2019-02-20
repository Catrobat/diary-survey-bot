"""
diary-survey-bot 2.0

Software-Design: Philipp Feldner
Documentation: https://github.com/Catrobat/diary-survey-bot

Telegram API:
https://github.com/python-telegram-bot/python-telegram-bot
"""


def baseline_(data, user):
    def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)
    return str(int(mean(data)) + 3000)

# def your_function(data, user):
#    return something


# Include your own functions here!
# Define them above.
def survey_function(user, data, function):
    if function == "baseline":
        return baseline_(data, user)
    # elif  function == "your_function":
    #    return your_function(data, user)



