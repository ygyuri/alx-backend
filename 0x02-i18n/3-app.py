#!/usr/bin/env python3
"""
Module to Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """
    class for Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    return locale from request
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    Return home title and header according to
    language
    """
    return render_template("3-index.html",
                           title=gettext("home_title"),
                           header=gettext("home_header")
                           )


if __name__ == "__main__":
    app.run(debug=True)
