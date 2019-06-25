# Welcome to star wars Application

This is a simple documentation for star wars application.

## Application consists of:
-web API
-web pages

## web API:
**URL**:/api/character/<name>
**name**:Is the name of star wars character.
This API search for all the star wars character whose name include the searched text

## web pages
-Home page:
**URL:**/home
This page contains general information about star wars movies

-Characters page:
**URL:**/characters
This page list all the star wars characters

-Single character page:
**URL:**/single-character?character=
This page list single character general information after passing the single character URL as a parameter

-Contact page:
**URL:**/contact
This page list my contact information

## Testing
In this application I have applied testing concepts including **Unit testing**, **Integration Testing** and **Mocking Concepts**

##Getting started
```bash
cd start\ wars\ app
pip3 install -r requirements.txt
python3 runserver.py
```
