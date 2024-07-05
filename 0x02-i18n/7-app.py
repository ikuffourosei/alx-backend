#!/usr/bin/env python3
'''A simple flask app to translate languages'''

from flask import Flask, g, render_template, request
from flask_babel import Babel
from flask_cors import CORS
from pytz import timezone
import pytz

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
    url_locale = request.args.get('locale')
    if url_locale and url_locale in myapp.config['LANGUAGES']:
        return url_locale
    user_locale = getattr(g, 'user', None)
    if user_locale and user_locale.get('locale') in myapp.config['LANGUAGES']:
        return user_locale['locale']
    best_match = request.accept_languages.best_match(myapp.config['LANGUAGES'])
    if best_match:
        return best_match
    else:
        return myapp.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """Gets the timezone"""
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            zone = timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError as e:
            pass

    user_timezone = getattr(g, 'user', None)
    if user_timezone:
        try:
            zone = timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError as e:
            pass
    return myapp.config['BABEL_DEFAULT_TIMEZONE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets the user based on the id"""
    id = request.args.get('login_as')
    if id is not None and int(id) in users.keys():
        return users[int(id)]
    return None


@myapp.before_request
def before_request():
    """Action to do before a client request"""
    user = get_user()
    if user is not None:
        g.user = user


@myapp.route('/', methods=['GET'], strict_slashes=False)
def home():
    """returns the home page"""
    return render_template('7-index.html')


if __name__ == '__main__':
    myapp.run()
