#!/usr/bin/env python3
'''A simple flask app to translate languages'''

from flask import Flask, g, render_template, request
from flask_babel import Babel
from flask_cors import CORS


myapp = Flask(__name__)
cors = CORS(myapp, resources={r"/*": {'origins': "*"}})
babel = Babel(myapp)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


myapp.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Gets the best language match from user request"""
    if request.args.get('locale') is not None:
        lang = request.args.get('locale')
        if lang in myapp.config['LANGUAGES']:
            return lang
    else:
        return request.accept_languages.best_match(myapp.config['LANGUAGES'])


@myapp.route('/', methods=['GET'], strict_slashes=False)
def home():
    """returns the home page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    myapp.run()
