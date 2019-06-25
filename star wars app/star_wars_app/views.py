"""
Routes and views for the flask application.
"""

from datetime import datetime
from star_wars_app.starwarCharacter import starwarCharacter
from flask import render_template
from star_wars_app import app
from flask import request
#import character
import swapi
import json
import requests 


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/characters')
def characters():
    """Renders the about page."""
    #Integrate with SWAPI API
    characters = swapi.get_all("people")
    return render_template('characters.html',
        title='characters',
        characters=characters.items)


@app.route('/single-character')
def getsingleCharacterInfo():

    singleCharacter = request.args.get('character', None)
    
    return render_template('character.html',
                           title = "star wars character",
                           data=singleCharacter)


@app.route('/character/<name>')
def searchCharacter(name):
    p = starwarCharacter("rafy","male","human",120,"earth","star wars from earth")
    p.get_name()
   
    #endPointUrl = "https://swapi.co/api/people/?search=" + name
    #reponse = requests.get(endPointUrl)
    url = 'https://swapi.co/api/people/'
    reponse = requests.get(url, params={'search': name})
    #temp = json.loads(reponse.content, object_hook=lambda d:namedtuple('X', d.keys())(*d.values()))
    DeserializedResponse = json.loads(reponse.content)
    mapResponseToCharacterModel(DeserializedResponse)


#I need to map the data to an object 
def mapResponseToCharacterModel(characters):
    for character in characters['results']:
        character['name']
        character['gender']
        id = getIdFromUrl(character['url'])
        getCharacterInfo(id)




def getIdFromUrl(url):
   return url.split('/')[-2]

def getCharacterInfo(id):
    character = swapi.get_person(id)
    species = character.get_species()
    films = character.get_films()
    homeWorld = character.get_homeworld()




