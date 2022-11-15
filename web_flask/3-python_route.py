#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""


from flask import Flask


app = Flask(__name__)


app.route('/', strict_slashes=False)


def hello():
    """  display 'Hello HBNB!' """
    return 'Hello HBNB!'


app.route('/hbnb', strict_slashes=False)


def hbnb():
    """  /hbnb: display “HBNB” """
    return 'HBNB'


app.route('/c/<text>', strict_slashes=False)


def c(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    par = text.replace('_', '')
    return 'C {}'.format(par)


app.route('/python/(<text>)', strict_slashes=False)


def python(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    par = text.replace('_', '')
    return 'Python {}'.format(par)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
