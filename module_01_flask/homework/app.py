import datetime
from flask import Flask
from random import choice
import re
import os

app = Flask(__name__)
cars = [
    "Chevrolet",
    "Renault",
    "Ford",
    "Lada",
]
cats = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин",
]

count_num = 0


def word_from_book() -> list:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    book_file = os.path.join(base_dir, "simple.txt")

    with open(book_file, "r", encoding="UTF-8") as book:
        res = book.read()
        out = re.findall(r"[А-Яа-яA-Za-z]+", res)
        return out


@app.route("/hello_world")
def hello_world():
    return "Hello World"


@app.route("/cars")
def cars_str():
    global cars
    cars_list = ", ".join(cars)
    return f"Вот список имеющихся машин: {cars_list}"


@app.route("/cats")
def random_cats():
    return f"Вывожу рандомную кошку {choice(cats)}"


@app.route("/get_time/now")
def time_count():
    current_time = datetime.datetime.now().time().strftime("%X")
    return f"Точное время: {current_time}"


@app.route("/get_time/future")
def test_function():
    future_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%X")
    return f"Точное время через час {future_time}"


@app.route("/get_random_word")
def random_word():
    out = choice(word_from_book())
    return f"Вывожу ранодомное слово из книги: {out}"


@app.route("/counter")
def counter_funk():
    global count_num
    count_num += 1
    out_str = f"Вы посетили сайт {count_num} раз"
    return out_str


@app.route("/")
def index():
    return (
        "<h4><a href='/hello_world'>/hello_world</a></h4>"
        "<h4><a href='/cars'>/cars</a></h4>"
        "<h4><a href='/get_time/now'>/get_time/now</a></h4>"
        "<h4><a href='/get_random_word'>/get_random_word</a></h4>"
        "<h4><a href='/get_time/future'>/get_time/future</a></h4>"
        "<h4><a href='/counter'>/counter</a><h4>"
        "<h4><a href='/get_random_word'>/get_random_word</a></h4>"
    )


if __name__ == "__main__":
    app.run(debug=True)
