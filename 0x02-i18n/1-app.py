#!/usr/bin/env python3
'''A simple flask app'''
from flask import Flask, request, g, render_template
from flask_babel import Babel
from flask_cors import CORS


myapp = Flask(__name__)
babel = Babel(myapp)
cors = CORS(myapp, resources={r"/*": {'origins': '*'}})


class Config:
    LANGUAGES = ["en", "fr"]


myapp.config.from_object(Config)


@babel.localeselector
def get_locale() -> str | None:
    return request.accept_languages.best_match(myapp.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


@myapp.route('/', methods=['GET'], strict_slashes=False)
def home():
    return render_template('1-index.html')


if __name__ == '__main__':
    myapp.run()
