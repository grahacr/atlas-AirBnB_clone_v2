#!/usr/bin/python3
"""
"""


#!/usr/bin/python3
"""module for starting Flask app with 3 routes"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_list():
    """render html template for states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
