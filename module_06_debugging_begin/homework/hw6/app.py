"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""

import logging
from typing import Optional

from flask import Flask, render_template, url_for
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/dogs")
def dogs():
    return "Страница с пёсиками"


@app.route("/cats")
def cats():
    return "Страница с котиками"


@app.route("/cats/<int:cat_id>")
def cat_page(cat_id: int):
    return f"Страница с котиком {cat_id}"


@app.route("/index")
def index():
    return "Главная страница"


@app.route("/manage")
def manage():
    return "Главная страница manage"


@app.route("/asdasd", methods=["POST"])
def manager():
    return "Главная страница manage"


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    methods = rule.methods if rule.methods is not None else ()
    return len(defaults) >= len(arguments)


@app.errorhandler(404)
def handle_exception(e: 404):
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    out_mess = ""
    for el in links:
        mes = f'<p><a href="http://localhost:5000{el[0]}">/{el[1]}</a></p>'
        out_mess += mes
    return out_mess, 404


if __name__ == "__main__":
    app.run(debug=True)
