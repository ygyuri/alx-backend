
"""
Module to Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import List


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


@babel.localeselector
def get_locale() -> str:
    """
    Return locale from request or default behavior.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    Return home title and header according to language
    """
    return render_template(
        "4-index.html",
        title=gettext("home_title"),
        header=gettext("home_header")
    )


if __name__ == "__main__":
    app.run(debug=True)
