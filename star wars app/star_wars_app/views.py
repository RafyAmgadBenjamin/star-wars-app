"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from star_wars_app import app

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
    return render_template(
        'characters.html',
        title='characters',
        year=datetime.now().year)
