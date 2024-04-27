"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask
import re

app = Flask(__name__)


@app.route("/max_number/<path:num>")
def max_number(num: str):
    """
    Поиск максимального числа в строке через /число/
    :param num: строка с endpoint
    :return: максимальное число
    """
    all_num = re.findall(r"(?<=/)[+-]?\d+[.]?\d*(?=/|\Z)", num)
    if all_num:
        rez = max(all_num, key=lambda x: float(x))
        return f"Максимальное переданное число <i>{rez}</i>"
    else:
        return f"Нет чисел в запросе"


if __name__ == "__main__":
    app.run(debug=True)
