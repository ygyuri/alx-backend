#!/usr/bin/env python3

"""
Module for handling user locale preference.
"""

from flask import Flask, render_template, request, g
from typing import List


app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES: List[str] = ['en', 'fr', 'es']
    BABEL_DEFAULT_LOCALE: str = 'en'


@app.before_request
def before_request():
    """
    Function to set the user's preferred locale.
    """
    g.locale = get_locale()


def get_locale() -> str:
    """
    Function to retrieve the user's preferred locale.
    The order of priority is:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    # Locale from user settings (dummy implementation)
    # Replace this with actual user settings retrieval
    # user_locale = get_user_locale()
    # if user_locale and user_locale in Config.LANGUAGES:
    #     return user_locale

    # Locale from request header
    locale = request.headers.get('Accept-Language')
    if locale:
        for lang in locale.split(','):
            lang = lang.split(';')[0]
            if lang in Config.LANGUAGES:
                return lang

    # Default locale
    return Config.BABEL_DEFAULT_LOCALE


@app.route('/')
def index():
    """
    Route for rendering the index page.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()

