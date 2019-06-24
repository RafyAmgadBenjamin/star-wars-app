"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import star_wars_app.views
