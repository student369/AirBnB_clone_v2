#!/usr/bin/python3
""" Module 2-c_route

Script that starts a Flask web aplication
, some routes and get a parameters.
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


@app.route("/c/<text>")
def c(text):
    """ Returns the C page"""
    text = text.replace("_", " ")
    return "C {:s}".format(text)


app.run(host="0.0.0.0", debug=False)
