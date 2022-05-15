#!/usr/bin/python3
"""
Write a script that starts a Flask web application, update
"""
from cgitb import text
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ display “C ” followed by the value of the text variable"""
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)

if __name__ == '__main__':
    app.run(host="0.0.0.0")