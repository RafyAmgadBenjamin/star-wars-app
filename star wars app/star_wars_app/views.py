"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from star_wars_app import app
from flask import request
import swapi

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/characters')
def characters():
    """Renders the about page."""
    #Integrate with SWAPI API
    characters = swapi.get_all("people")
    return render_template(
        'characters.html',
        title='characters',
        characters=characters.items)


@app.route('/single-character')
def getsingleCharacterInfo():

    #//reponse = requests.get('https://swapi.co/api/people/1/')
    singleCharacter = request.args.get('character', None)

    return render_template('character.html',
                           title = "star wars character",
                           data=singleCharacter)