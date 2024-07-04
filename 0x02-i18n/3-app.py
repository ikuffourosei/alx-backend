#!/usr/bin/env python3
'''A simple flask app'''
from flask import Flask, g, request, render_template
from flask_babel import Babel, _
from flask_cors import CORS


myapp = Flask(__name__)
babel = Babel(myapp)
cors = CORS(myapp, resources={r"/*": {'origins': '*'}})


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


myapp.config.from_object(Config)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(myapp.config['LANGUAGES'])


@myapp.route('/', methods=['GET'], strict_slashes=False)
def home():
    return render_template('3-index.html')


if __name__ == '__main__':
    myapp.run()
