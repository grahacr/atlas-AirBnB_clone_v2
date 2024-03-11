#!/usr/bin/python3
"""module for starting Flask app with 3 routes"""


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


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """function for taking in text as part of route"""
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
