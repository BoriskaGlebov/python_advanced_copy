"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

import datetime
import calendar
import locale
from flask import Flask

locale.setlocale(locale.LC_ALL, "")

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    """
    Добавляет трауты в конккретную дату
    :param date:  дата
    :param number: сколько потратил
    :return: сообщение о том что все добавилось корректно
    """
    try:
        if len(date) == 8:
            correct_date = datetime.date(int(date[0:4]), int(date[4:6]), int(date[6:8]))
            year = correct_date.year
            month = correct_date.month
            expense = number
            if year in storage:
                if month in storage[year]:
                    storage[year][month] += expense
                    storage[year]["total"] += expense
                else:
                    storage[year][month] = expense
                    storage[year]["total"] += expense
            else:
                storage.setdefault(year, {}).setdefault(month, {})
                storage[year].setdefault("total", 0)
                storage[year][month] = expense
                storage[year]["total"] += expense
            print(storage)
            return f"В <b>{correct_date}</b> было потрачено <b>{expense}</b> рублей "
        raise Exception("Дата неправильной длинны")
    except (TypeError, ValueError, Exception) as ex:
        return f"<h3>{str(ex)}, ошибка ввода данных</h3>"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    """
    Вывод суммарных трат за год
    :param year: год
    :return:  Вывод суммарных трат за год
    """
    if year in storage:
        year_expense = storage[year].get("total", 0)
        return f"За указанный год <b>{year}</b> потрачено <b>{year_expense}</b> рублей"
    else:
        return f"За указанный год <b>{year}</b> потрачено <b>0</b> рублей"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    """
    Вывод суммарных трат в кокретном месяце и всего за конкретный год
    :param year: год
    :param month: месяц
    :return: сообщение с информацией
    """
    if year in storage:
        year_expense = storage[year].get("total", 0)
        month_expense = storage[year].get(month, 0)
        return (
            f"В этом году <b>{year}</b> было потрачено "
            f"<b>{year_expense}</b> из них в месяце "
            f"<b>{calendar.month_name[month]}</b> - <b>{month_expense}</b> рублей"
        )
    else:
        return (
            f"В этом году <b>{year}</b> было потрачено "
            f"<b>0</b> рублей из них в месяце <b>{calendar.month_name[month]}</b> - <b>0</b> рублей"
        )


@app.route("/")
def default():
    """Для тестирования удобно"""
    return (
        '<h3><a href = "/add/<date>/<int:number>"> сохранение информации о совершённой в рублях трате за какой-то день </a></h3>'
        '<h3><a href = "/calculate/<int:year>"> получение суммарных трат за указанный год </a></h3>'
        '<h3><a href = "/calculate/<int:year>/<int:month>"> получение суммарных трат за указанные год и месяц. </a></h3>'
    )


if __name__ == "__main__":
    app.run(debug=True)
