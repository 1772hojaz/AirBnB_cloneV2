#!/usr/bin/python3
"""display n is a number only if n is an integer"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """display Python followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if typeof(n)==int:
        return '{} is a number'.formart(n)
    else:
        pass
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)