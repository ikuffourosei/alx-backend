#!/usr/bin/env python3
"""A simple flask app"""

from flask import Flask, render_template
from flask_cors import CORS


myapp = Flask(__name__)
cors = CORS(myapp, resources={r"/*": {"origin": "*"}})


@myapp.route('/', methods=['GET'], strict_slashes=False)
def view_page():
    """Displays the home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    myapp.run()
