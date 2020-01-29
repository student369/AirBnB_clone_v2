#!/usr/bin/python3
"""
python program that deploys an hbnb site with places
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb')
def filter_display():
    """
    return a webpage
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    users = storage.all("User")
    return render_template('100-hbnb.html', states=states, users=users,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(self):
    """
    teardown
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
