#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return a given string"""
    return render_template("7-states_list.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
