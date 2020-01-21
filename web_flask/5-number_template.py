#!/usr/bin/python3
""" Module 5-number_template

Script that starts a Flask web aplication
, some routes, get a parameters and
default parameters and integer param,
and use of templates.
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def number(n):
    """ Returns the number page"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """ Returns the number_template page"""
    return render_template("5-number.html", n=n)


app.url_map.strict_slashes = False
app.run(host="0.0.0.0", debug=False)
