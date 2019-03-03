# Quran Tafseer API [![Codeship Status for Quran-Tafseer/tafseer_api](https://app.codeship.com/projects/8bc13660-dd1b-0136-eb69-5213487ae4ca/status?branch=master)](https://app.codeship.com/projects/317993) [![Build Status](https://travis-ci.org/Quran-Tafseer/tafseer_api.svg?branch=master)](https://travis-ci.org/Quran-Tafseer/tafseer_api) [![codecov](https://codecov.io/gh/EmadMokhtar/tafseer_api/branch/master/graph/badge.svg)](https://codecov.io/gh/EmadMokhtar/tafseer_api)

Quran Tafseer REST APIs and Quran Text

## Idea

The idea is to create one REST API for all Quran Tafseer/Interpretation for developers.
The idea came to me when I tried to search for REST API for Quran Tafseer/Interpretation I couldn't find one,
and each Quran application web/mobile has its own Quran Tafseer/Interpretation, so I thought it's a good idea
to create one.


## How to contribute and help the project

1. [Report Bugs](https://github.com/EmadMokhtar/tafseer_api/issues/new)
    * If you found a bug please report, it'll help the project to grow and improve.
1. [Suggest Ideas](https://github.com/EmadMokhtar/tafseer_api/issues/new)
    * If you have an innovative idea you feel it'll be awesome to add to the API, please share.
1. Use the API
    * Yes using the API will help the project, this is the reason I built this API 😉.
1. Spread the word
    * Share the API with your friends and community.
1. Write a wrapper or client for the API.
    * Please find the client list below.
1. [Donate](https://www.paypal.me/emadhabib/1)
    * You can help me in growing the project with any amount.
1. Check [translation help](https://github.com/EmadMokhtar/tafseer_api/labels/translation%20help) label, and help in documentation translation.
1. Check [help wanted](https://github.com/EmadMokhtar/tafseer_api/labels/help%20wanted) label, and help in developing the API.

## Development Stack

1. [Python](https://www.python.org/)
1. [Django](https://www.djangoproject.com/)
1. [Django REST Framework](http://www.django-rest-framework.org/)

## How to run locally

* Create a virtualenv
    `mkvirtualenv tafsser_api`
* Install dependencies
    `pip install -r requirements/requirements_dev.txt`
* Create .env file and add project settings

|   Setting    |    Example     |
| ------------- |:-------------:|
|   DEBUG    |    DEBUG=True     |
|   SECRET_KEY    |    SECRET_KEY=VeryVerySecret     |
|   DATABASE_URL    |    DATABASE_URL=sqlite:///db.sqlite3     |


* Run model migrations
    `python manage.py migrate`
* Run development server
    `python manage.py runserver`

## Clients

* [CSharp client](https://github.com/xh0/QuranTafseerCSharpClient) created by [Bassam Abd Elhamid](https://github.com/xh0)


## Quran Tafseer/Interpretation Sources

|   Tafseer    |   Soruce      | Language |
| ------------- |:-------------:|---------|
|التفسير الميسر| [Tanzil.net](http://tanzil.net/trans/) | العربية |
|تفسير الجلالي| [Tanzil.net](http://tanzil.net/trans/)     | العربية 
|تفسير السعدي| [Ayat](http://quran.ksu.edu.sa)| العربية 
|تفسير ابن كثير| [Ayat](http://quran.ksu.edu.sa)| العربية 
|تفسير الوسيط لطنطاوي| [Ayat](http://quran.ksu.edu.sa)| العربية 
|تفسير البغوي| [Ayat](http://quran.ksu.edu.sa)| العربية 
|تفسير القرطبي| [Ayat](http://quran.ksu.edu.sa)| العربية 
|تفسير الطبري| [Ayat](http://quran.ksu.edu.sa)|  العربية 
Arberry | [Tanzil.net](http://tanzil.net/trans/) | English |
Yusuf Ali | [Tanzil.net](http://tanzil.net/trans/) |English |
Keyzer | [Tanzil.net](http://tanzil.net/trans/) | Dutch |
Leemhuis | [Tanzil.net](http://tanzil.net/trans/) | Dutch |
Siregar | [Tanzil.net](http://tanzil.net/trans/) | Dutch |