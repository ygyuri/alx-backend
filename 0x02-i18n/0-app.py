#!/usr/bin/env python3

"""
Module for displaying the current time based on inferred time zone.
"""

from flask import Flask, render_template, g
from typing import Optional
import pytz
from babel import dates
from flask_babel import Babel, _
from flask_babel import lazy_gettext as _l


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app.
    """
    BABEL_DEFAULT_LOCALE: str = 'en'


@app.before_request
def before_request():
    """
    Function to set the user's preferred time zone.
    """
    g.timezone = get_timezone()


def get_timezone() -> str:
    """
    Function to retrieve the user's preferred time zone.
    The order of priority is:
    1. Time zone from URL parameters
    2. Time zone from user settings
    3. Default to UTC
    """
    # Simulated logic for getting time zone from user settings or URL parameters
    # This part can be replaced with actual logic
    return 'UTC'


@app.route('/')
def index():
    """
    Route for rendering the index page.
    """
    current_time = get_current_time()
    return render_template('index.html', current_time=current_time)


def get_current_time() -> str:
    """
    Function to get the current time in the user's preferred time zone.
    """
    user_timezone = pytz.timezone(g.timezone)
    current_time = dates.format_datetime(dates.datetime.now(user_timezone), locale=Config.BABEL_DEFAULT_LOCALE)
    return current_time


if __name__ == '__main__':
    app.run()

