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
It is intended to conduct surveys/studies that strech over longer time periods.
Since there was no similar tool around to conduct those type of studies we
developed one on our own. The messaging app Telegram seemed fitting, because of
its decent API and popularity. The bot is written in python3 and uses this
[API](https://github.com/python-telegram-bot/python-telegram-bot).

[Here](https://telegram.org/blog/bot-revolution) is the official
telegram info about bots and how you can set up your own.

For a detailed guide on how to use this bot visit the **Wiki**!

## Features:

- Multi language support
- Studies are created in the easy to use json format
- Variable question-block scheduling
- Custom keyboards
- Condition based questions
- Timezone support
- Backup database
- Data storing in easy to use csv files
- Editor for creating surveys

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
