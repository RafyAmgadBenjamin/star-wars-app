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
    url = 'https://swapi.co/api/people/'
    reponse = requests.get(url, params={'search': name})
    DeserializedResponse = json.loads(reponse.content)
    charactersList = mapResponseToCharacterModel(DeserializedResponse)
    return json.dumps([ob.__dict__ for ob in charactersList])

#I need to map the data to an object 
def mapResponseToCharacterModel(characters):
    charactersList = []
    for character in characters['results']:
        name = character['name']
        gender = character['gender']
        id = getIdFromUrl(character['url'])
        singleCharacter =  getCharacterInfo(id)
        species = getCharacterSpecies(singleCharacter)
        averageLifeSpan = getAverageLifeSpan(singleCharacter)
        films = getCharacterFilms(singleCharacter)
        homeWorld = getCharacterHomeworld(singleCharacter)
        characterTemp = starwarCharacter(name,gender,"human",averageLifeSpan,homeWorld,films)
        charactersList.append(characterTemp)
        del characterTemp
    return charactersList




def getIdFromUrl(url):
   return url.split('/')[-2]

def getCharacterInfo(id):
    return swapi.get_person(id)
   
def getCharacterFilms(character):
    films = character.get_films()
    filmsNames = []
    for film in films.items:
        filmsNames.append(film.title)
    return filmsNames



def getCharacterSpecies(character):
     return character.get_species().items[0].name

def getCharacterHomeworld(character):
     return character.get_homeworld().name

def getAverageLifeSpan(character):
    return character.get_species().items[0].average_lifespan

