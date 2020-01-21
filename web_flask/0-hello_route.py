#!/usr/bin/python3
""" Module 0-hello_route

Script that starts a Flask web aplication.
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """ Returns the index page"""
    return "Hello HBNB!"


app.run(host="0.0.0.0", debug=False)
