#!/usr/bin/python3
"""
Starts a Flask web application
"""


import os
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ removes current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ displays 9-states.html """
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ displays 9-states.html by id """
    states = storage.all("State")
    try:
        state = states[id]
    except:
        state = None
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
