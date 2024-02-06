#!/usr/bin/env python3
"""
Basic babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/')
def index():
    """
    Return html file in / route
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
