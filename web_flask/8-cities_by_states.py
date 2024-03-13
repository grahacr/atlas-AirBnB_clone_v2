#!/usr/bin/python3
"""
module for displaying States
"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """teardown function to close storage"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """render html template for states"""
    states = storage.all("State").values()
    return render_template('8-cities_by_state.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
