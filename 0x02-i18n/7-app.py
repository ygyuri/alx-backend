#!/usr/bin/env python3

"""
Module for handling user time zone preference.
"""

from flask import Flask, render_template, request, g
from typing import Optional
import pytz
from babel import dates


app = Flask(__name__)


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
    # Time zone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Time zone from user settings (dummy implementation)
    # Replace this with actual user settings retrieval
    # user_timezone = get_user_timezone()
    # if user_timezone:
    #     try:
    #         pytz.timezone(user_timezone)
    #         return user_timezone
    #     except pytz.exceptions.UnknownTimeZoneError:
    #         pass

    # Default to UTC
    return 'UTC'


@app.route('/')
def index():
    """
    Route for rendering the index page.
    """
    return render_template('7-index.html', now=get_current_time())


def get_current_time() -> str:
    """
    Function to get the current time in the user's preferred time zone.
    """
    return dates.format_datetime(dates.datetime.now(pytz.timezone(g.timezone)), locale=Config.BABEL_DEFAULT_LOCALE)


if __name__ == '__main__':
    app.run()

