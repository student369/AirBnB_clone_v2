#!/usr/bin/python3
""" Module 1-hbnb_route

Script that starts a Flask web aplication
and some routes.
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """ Returns the index page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Returns the hbnb page"""
    return "HBNB"


app.run(host="0.0.0.0", debug=False)
