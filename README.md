# diary-survey-bot 2.0

**This is the continuation of the original 
[diary-survey-bot](https://github.com/philippfeldner/diary-survey-bot).**  
**The continued development is part of my Bachelorthesis and the project will**  
**be maintained by the team of the [Catrobat](https://github.com/Catrobat) project.**


**Software-Design:** Philipp Feldner (Computer Science Student TU Graz)  
**Twitter/Telegram:** [@PhilippFeldner](https://twitter.com/PhilippFeldner)  
**Email:** [feldnerphilipp@gmail.com](mailto:feldnerphilipp@gmail.com)  
**Supervisors:**
[Univ.-Prof. Dipl.-Ing. Dr.techn. Wolfgang Slany](https://github.com/wslany), [Dr.techn. BSc MSc Bernadette Spieler](https://github.com/bernadettespieler)  




## Table of Contents:
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
  - [Question format](#question-format)
  - [Settings](#settings)
  - [Languages](#languages)
- [Technical details](#technical-details)
  - [Database](#database)
  - [CSV](#csv)
  - [Development](#development)


## Introduction:

This is a chat-bot for the messaging app [Telegram](https://telegram.org/).
It is intended to conduct surveys/studies that stretch over longer time periods.
Since there was no similar tool around to conduct those type of studies we
developed one on our own. The messaging app Telegram seemed fitting, because of
its decent API and popularity. The bot is written in python3 and uses this
[API](https://github.com/python-telegram-bot/python-telegram-bot).

[Here](https://telegram.org/blog/bot-revolution) is the official
telegram info about bots and how you can set up your own.

## Features:

- Multi language support
- Studies are created in the easy to use json format
- Variable question-block scheduling
- Custom keyboards
- Condition based questions
- Timezone support
- Backup database
- Data storing in easy to use csv files

## Usage:

To allow quick study creation I designed a format for question input that
is pretty easy to use and is based on the
[json notation](https://de.wikipedia.org/wiki/JavaScript_Object_Notation).
Json is a **markup language** similar to XML, that is easy to read for the
human and easy to translate for the machine. The whole format is basically
build as follows: We have multiple blocks that represent days. Within those
days we have smaller chucks that represent question-blocks that shall be
scheduled through out that day. Within those question-blocks are the questions
with a bunch of meta information that is explained later.

Currently there is support for english, german, french and spanish,
but with little python knowledge you will be able to add/remove other
languages. For every language create a file with the name format
**question_set_en.json** (en/de/es/fr) and place those files in the
survey folder.



### Question format:

Span a pair of **[ ]** from the very beginning of the file to the very end! Within
those braces place all the day elements. within **{ }** and separate them with
a colon.

#### Key description for day element:

- **day:** Represents the day of the study. Make sure to put the day elements in
ascending order.
- **blocks:** Contains a list of block elements.

*Example day:*
```
  {
    "day": 1,
    "blocks":
    [
      {
            -- Fill in block element --
      },
      {
            -- Fill in block element --
      }      
    ]
  }
```
#### Key description for block element:
- **time:** currently this element awaits a keyword, that is defined in
**SCHEDULE_INTERVALS** in the admin/settings.py file. There you can define
your own time intervals in the format **["hh:mm", "hh:mm"]**. Make sure to
make your **interval at least 30min long**. An option to schedule at a
certain time may be implemented in the future.
- **settings:** Here certain properties for a block can be set.
List of current options:
  - *MANDATORY:* Marks the block as mandatory. The next block is only getting
    scheduled when the current block is complete or a question contains
    the command: Q_ON
- **questions:** contains all the question elements of the block.

*Example block:*
```
{
  "time": "SAMPLE_TIME_KEYWORD",
  "settings": [["MANDATORY"]],
  "questions":
  [
    {
        -- Fill in question element --
    },
    {
        -- Fill in question element --
    }
  ]
}
```
#### Key description for question element:

- **text:** contains the message text, that shall be asked
- **choice:** contains nested lists of answer possibilities which are
used to create a custom keyboard within Telegram. Dynamic keyboards can be
created within the python file survey/keyboard_presets.py and have to be
registered in the CUSTOM_KEYBOARD dictionary.
- **condition:** Conditions can be used to give questions about certain requirements.
If a user does not fulfill given requirements the question will be skipped for him.
Multiple conditions are possible.
- **condition_required:** Previously defined conditions can be put here and
if the user does not fulfill them the question will be skipped for him.
- **commands:** Commands are basically signals for the program to trigger special
events. List of all (current) commands and their usage:  
  -  *FORCE_KB_REPLY:* The user has to choose an option from the Keyboard to proceed.  
  -  *Q_ON:* See BLOCK settings - MANDATORY  
  -  *COUNTRY:* Signals that the user will respond with his country:  Relevant for database.  
  -  *AGE:* Signals that the user will respond with his age:      Relevant for database.  
  -  *GENDER:* Signals that the user will respond with his gender:   Relevant for database.  
  -  *TIMEZONE:* Signals that the user will respond with his timezone: Relevant for database.
  - *["DATA", "DATA_NAME", "COMMAND"]:* Signals that a certain operation shall be executed onto a
    custom datastructure. (See Survey Specific Functions).

*Example question:*
```
{
  "text": "Sample Text",
  "choice": [
    ["Sample Choice 1"],
    ["Sample Choice 2"]
  ],
  "condition_required": ["#IDENTIFIER"],
  "condition": [["Sample Choice 1", "#IDENTIFIER"]],
  "commands": [["FORCE_KB_REPLY"],["COUNTRY"]]
}
```

### Settings:

Within the admin package you find a file settings.py.
This file is responsible for most of the settings you can take.
Custom keyboards are defined in survey/keyboard_presets.py

#### List of all elements in settings.py:
- **ADMINS:** A list with all admin chat_ids. Admin features are in development.
- **DEBUG:** Debug mode on/off (bool). For debugging purposes. If activated it
also stores the debug info to a log.txt file.
- **DELETE:** Activates (bool) the /delete_me command that allows the user to
withdraw himself from the study and deletes all his records, including csv and
database entries.
- **QUICK_TEST:** For testing purposes. If set to a different value than False
it reduces the time of the scheduling blocks to n seconds.
- **DEFAULT_LANGUAGE:** Default language if something goes wrong. It is
important that this language exists. Otherwise the program might crash.
- **DEFAULT_TIMEZONE:** Default timezone if something goes wrong. It is
important that this timezone is a timezone defined in
[pytz](https://pypi.python.org/pypi/pytz?).
Otherwise the program might crash.
- **SCHEDULE_INTERVALS:** A python dictionary that maps the Keywords from the
time value (question-blocks) to an interval format like this: 
KEYWORD: ["hh:mm","hh:mm"] with a minimum offset from 30min. 
Further more simple fixed schedules can be
defined as KEYWORD: "hh:mm".
- **INFO_TEXT:** A python dictionary that maps the info text for the /info to a
language abbreviation.
- **STOP_TEXT:** A python dictionary that maps the stop text for the /stop to a
language abbreviation.

#### Dynamic keyboards:

The survey/keyboard_presets.py file is meant to contain custom keyboards that
can be generated dynamically.

*Example: timezone keyboards*  
The user enters his current location (country) and this value is stored
to the DB. Afterwards the timezone keyboard gets generated from a dictionary
that maps every country and its (possibly multiple) timezones. When creating
dynamic keyboards register them in the CUSTOM\_KEYBOARD dictionary and I advice
you to use the prefix KB\_ for easier recognition.

#### Survey specific functions:
If your survey requires custom replies you can generate them via your
own python functions.
- **Step 1:** Gathering Data: Likely you want to make your questions
  depended on data from the users. Therefore every participant has
  their own dictionary of datastructures. Using the command field
  withing a question allows to create/delete a new datastructure.
  Use the format ["DATA", "DATA_NAME", "COMMAND"]. "DATA" is the key
  to recognize your intention. A unique "DATA_NAME" shall be chosen
  to identify the datastructure. "COMMAND" shall be replaced by either
  "ADD" or "CLR"(clear) to add the user response to the datastructure or
  delete the datastructure entirely.
- **Step 2:** Defining your own functions: Custom functions shall be
  defined within admin/survey_specific.py. Every function needs to
  have a *unique* string as identifier to invoke them within the json
  file. An example of how a function shall be registered:
  ```
  # Register your own functions here!
  # Define them above.
  def survey_function(user, data, function):
      if function == "baseline":
          return baseline_(data, user)
      elif function == "another_function":
          return another_function_(data, user)
  ```
  It makes sense to pass the parameters data and user to access
  user specific data. The return value *needs* to be stringified
  (str()) since it is going to be part of a message.
- **Step 3:** Invoking a function within the json files:
   <<DATA|data_name|function_name>> Placing this within a question
   message will invoke your function and replace it with your return
   value from this specific function.



#### Emojis in keyboards:
Emojis can simply be added as Unicode symbols into your text.
[Link](http://unicode.org/emoji/charts/full-emoji-list.html).

### Languages:
If you desire to add an additional language you need to follow those steps:
1. add an entry in the languages keyboard that you can find in the
 **keyboard_presets.py** file.
2. extend the set_language function in **participants.py** for your language.
3. add a member to the DataSet class (format: q_set_xx, xx: language abbreviation)
in the **data_set.py** file.
4. extend the DataSet Constructor for your language. (**data_set.py**)
5. extend the *return_question_set_by_language* function for your language 
(**data_set.py**)  
6. now you can write question_set_xx.json in the usual format and place them in
the *survey/* module

## Technical Details:

### Database:
To avoid data loss on restart I run a small
[sqlite3](https://docs.python.org/3/library/sqlite3.html)
database in the background, that stores the most basic
attributes of a user.

### CSV:
CSV (comma separated values) is a spreadsheet format that is suited
very well for storing survey data. Every user has his own sheet that
is named after his chat_id and stored in survey/data_incomplete. As
soon as a user has completed the survey the file gets copied to
survey/data_complete.

### Development:
This program was developed with the
[Pycharm IDE by Jetbrains](https://www.jetbrains.com/pycharm/)
and tested on a local machine. The telegram API is https based
so you might need to check if necessary ports are open.


