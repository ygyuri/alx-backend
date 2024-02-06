#!/usr/bin/env python3
"""
Module for mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import List, Dict, Union

class Config:
    """
    Class for Flask Babel configuration.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users: Dict[int, Dict[str, Union[str, None]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id: int) -> Union[Dict[str, Union[str, None]], None]:
    """
    Get user information based on user ID.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """
    Execute before all other functions.
    """
    user_id = request.args.get("login_as")
    g.user = get_user(int(user_id)) if user_id else None

@app.route("/")
def index() -> str:
    """
    Return welcome message or default message based on login status.
    """
    return render_template("5-index.html")

if __name__ == "__main__":
    app.run(debug=True)
