#!/usr/bin/python3
"""
flask application that will display a page for hbnb
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def filter_display():
    """
    display a webpage with popover-filters
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """
    cleanup function
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
