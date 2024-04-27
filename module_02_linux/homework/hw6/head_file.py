"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt:
hello world!

/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

import os.path

from flask import Flask

app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    """
    Чтение файла
    :param size: сколько символов прочитать
    :param relative_path: относительный путь к файлу
    :return: строка с абсолютным путем к файлу, количество символов которое удалось прочитаь и сам прочитанный текст
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_dir, relative_path)
    print(abs_path)
    if os.path.isfile(abs_path):
        with open(abs_path, "r", encoding="utf-8") as file:
            result_text = file.read(size)
            result_size = len(result_text)
        return f"<b>{abs_path}</b> {result_size}<br>{result_text}"
    else:
        return "<b>Такого файла не существует</b>"


if __name__ == "__main__":
    app.run(debug=True)
    avs = os.path.abspath("docs/simple.txt")
    print(os.path.isfile(avs))
