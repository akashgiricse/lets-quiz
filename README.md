# Let's quiz
This is an online quiz organizing website project, developed using Python's web framework Django.<br>
For front-end designing I have used Twitter's front-end library Bootstrap4.

[![GitHub release](https://img.shields.io/github/release/akashgiricse/lets-quiz.svg)](https://img.shields.io/bower/vpre/bootstrap.svg)
[![GitHub issues](https://img.shields.io/github/issues/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/issues)
[![GitHub forks](https://img.shields.io/github/forks/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/network)
[![GitHub stars](https://img.shields.io/github/stars/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/stargazers)
[![GitHub license](https://img.shields.io/github/license/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/blob/master/LICENSE)

## Current Features

### Site access features:

* Quiz can be accessed only if the user is logged in.
* For signup user is required to give *username*, *e-mail* and *password*.
* For login the user will be required to enter *username* and *password* only.

### Features of the quiz:

* Every question is multiple choice question.
* Every question is displayed only once per user.
* Questions are displayed randomly for every user.
* If the user presses refresh or go back to the previous page, there will be a new question for the user and the question he/she was on will be counted as attempted.
* A message is displayed after every attempted question whether the answer was correct or incorrect.


### Leaderboard features:

* Leaderboard is a shorted list according to the score obtained by the user.
* If two users have same score, the user who has signed up earlier will have good ranking than the one who joines late.
* Leaderboard is open to all. No login required.

### Administrative features:

* Only admin can add questions.
* Admin can add questions and modify them until they are not marked as *Has been published?*
* Once a question has been published, it can neither be modify nor can be accessed. Admin can only see a list of questions.
* Admin can search questions by question text or choice text.
* Admin can filter questions based on whether the questions have been published or not.


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

### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

### 3. Create the virtualenv
```bash
## run following command from `lets_quiz` directory
mkvirtualenv lets_quiz -a "$(pwd)" -p python3.6
```

### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step
workon lets_quiz
cd ..
pip install -r requirements.txt
```

### 5. Setup the database
*TODO - Add instructions for this when I start using MySQL database.*

### 6. Run database migrations
```bash
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
- Source Code: [Download zip file here](https://github.com/akashgiricse/lets-quiz/archive/master.zip)

## Contributors

* [Akash Giri](https://github.com/akashgiricse)

## Support

* If you are having issues, please let me know.<gr>
I have a mailing list located at: buggyrango@gmail.com

## License

[![GitHub license](https://img.shields.io/github/license/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/blob/master/LICENSE)

Copyright (c) 2018 Akash Giri.
