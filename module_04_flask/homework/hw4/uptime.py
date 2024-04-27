"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

import datetime
import subprocess
from sys import platform

from flask import Flask
from flask import request

app = Flask(__name__)


# Скрипт работает на обеих системах, но есть нюансы и вопросы На линекс вроде все быстро и хорошо, а так как она у
# меня на английском языке то еще и с кодировкой проблем нет от слова совсем Но вот винда!!!!!!!!! Не понятно почему
# оно время uptime системы не всегда обнуляется при перезагрузке или выключении компа, хотя вроде все считает
# нормально при тех показаниях, что есть in windows have method systeminfo | find "Время после перезагрузки", но в
# subprocess не могу предать именно так команду, приходиться вытаскивать вывод из команды systeinfo Верно ли я делаю
# или что-то не то тут. Ну и код в линекс работает в разы быстрее чем в виндовс!!!!!!
@app.route("/uptime", methods=["GET"])
def uptime() -> str:
    uptime_correct = "Ничего не покажу"
    if "linux" == platform:
        res = subprocess.run(["uptime", "-p"], capture_output=True)
        uptime_correct = res.stdout.decode()
    else:
        res = subprocess.run(["systeminfo"], capture_output=True)
        data = res.stdout.decode(encoding="CP866", errors="ignore")
        for el in data.split("\n"):
            if el.startswith("Время"):
                time = el.split(":", maxsplit=1)[1].replace(",", "").strip()
                # получаю чистую строку даты из systeminfo
                start = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M:%S")
                # преобразую строку в datetime формат
                now_time = datetime.datetime.now().replace(microsecond=0)
                uptime_correct = now_time - start
                # нахожу разницу времени с последеенего запуска и в таком формате выдает верно 2 дня
    return f"Current uptime is {uptime_correct}"


if __name__ == "__main__":
    app.run(debug=True)
