# Let's Quiz

### [letsquiz.pythonanywhere.com/](https://letsquiz.pythonanywhere.com/) [![Website letsquiz.pythonanywhere.com](https://img.shields.io/website-up-down-green-red/http/letsquiz.pythonanywhere.com.svg)](http://letsquiz.pythonanywhere.com/)

This is an online quiz organizing website project, developed using Python's web framework Django.<br>
For front-end designing I have used Twitter's front-end library Bootstrap4.

[![GitHub release](https://img.shields.io/github/release/akashgiricse/lets-quiz.svg)](https://img.shields.io/bower/vpre/bootstrap.svg)
[![GitHub issues](https://img.shields.io/github/issues/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/issues)
[![GitHub forks](https://img.shields.io/github/forks/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/network)
[![GitHub stars](https://img.shields.io/github/stars/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/stargazers)
[![GitHub license](https://img.shields.io/github/license/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/blob/master/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Current Features

### Site access features:

- User must be logged in to access the Quiz.
- For signup user is required to give _username_, _first name_, _last name_, _e-mail address_ and _password_.
- For login the user will be required to enter _username_ and _password_ only.

### Features of the quiz:

- All questions are multiple choice question.
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect.

### Leaderboard features:

- Leaderboard is a shorted list according to the score obtained by the users.
- If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.
- Leaderboard is open to all. No login required.

### Administrative features:

- Only admin can add questions.
- Admin can add questions and modify them until they are not marked as _Has been published?_
- Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
- Admin can search questions by question text or choice text.
- Admin can filter questions based on whether the questions have been published or not.

## Getting started with development

Dependencies:

- Python 3.6.x
- Django 1.11.x
- Ubuntu 17.04 or later or Linux Mint 18.2 or later

### 1. Clone this repository

```bash
git clone https://github.com/akashgiricse/lets-quiz.git
cd lets_quiz
```

### 2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

### 3. Create the virtualenv

```bash
## run following command from `lets_quiz` directory
pipenv shell
```

### 4. Install python packages

```bash
pip install -r requirements.txt
```

### 5. Setup the database

_TODO - Add instructions for this when I start using MySQL database._

### 6. Run database migrations

```bash
cd lets_quiz
python manage.py migrate
```

### 7. Create superuser

```bash
python manage.py createsuperuser
```

### 8. Run development server

```bash
python manage.py runserver
```

## Contribute

- Issue Tracker: [Issues](https://github.com/akashgiricse/lets-quiz/issues)
- Source Code: [Download zip: Release v1.0.1](https://github.com/akashgiricse/lets-quiz/archive/1.0.1.zip)

## Contributors

- [Akash Giri](https://github.com/akashgiricse)

## Support

- If you are having issues, please let me know.<gr>
  I have a mailing list located at: contact@akashgiri.com

## License

MIT License

Copyright (c) 2018 Akash Giri.
