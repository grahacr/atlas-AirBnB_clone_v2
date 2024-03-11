#!/usr/bin/python3
"""module for starting Flask app"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """function for returning script when root is visited"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """function for returning script when hbnb is visited"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
