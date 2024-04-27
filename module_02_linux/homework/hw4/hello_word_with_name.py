"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from datetime import datetime
from flask import Flask
import locale
import sys

locale.setlocale(locale.LC_ALL, "")

app = Flask(__name__)

weekdays_tuple = (
    "Хорошего понедельника",
    "Хорошего вторника",
    "Хорошей среды",
    "Хорошего четверга",
    "Хорошей пятницы",
    "Хорошей субботы",
    "Хорошего воскресенья",
)
weekdays_list = [
    "Хорошего понедельника",
    "Хорошего вторника",
    "Хорошей среды",
    "Хорошего четверга",
    "Хорошей пятницы",
    "Хорошей субботы",
    "Хорошего воскресенья",
]
weekdays_dict = {
    1: "Хорошего понедельник",
    2: "Хорошего вторник",
    3: "Хорошей среда",
    4: "Хорошего четверг",
    5: "Хорошей пятница",
    6: "Хорошей суббота",
    7: "Хорошего воскресенье",
}


@app.route("/hello-world/<user_name>")
def hello_world(user_name: str):
    """
    Вывод сообщения приветствия с указанием дня недели
    :param user_name: ися пользователя
    :return: строка с выводом
    """

    weekday = datetime.today().weekday()
    print(sys.getsizeof(weekdays_tuple))
    print(sys.getsizeof(weekdays_list))
    print(sys.getsizeof(weekdays_dict))
    # Так мне показалось веселее))))
    # week_day = datetime.strftime(datetime.now(), '%A')
    # return f'Привет, <i>{user_name}</i>! <b>{week_day}</b> отличный день для Python'
    return f"Привет, <i>{user_name}</i>! <b>{weekdays_tuple[weekday]}</b>!"


if __name__ == "__main__":
    app.run(debug=True)
