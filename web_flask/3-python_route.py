#!/usr/bin/python3
""" Module 3-python_route

Script that starts a Flask web aplication
, some routes, get a parameters and
default parameters.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    """ Returns the index page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Returns the hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """ Returns the C page"""
    text = text.replace("_", " ")
    return "C {:s}".format(text)


@app.route("/python")
def python_default():
    """ Returns the Python page"""
    return "Python is cool"


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    """ Returns the Python page"""
    text = text.replace("_", " ")
    return "Python {:s}".format(text)


app.url_map.strict_slashes = False
app.run(host="0.0.0.0", debug=False)
