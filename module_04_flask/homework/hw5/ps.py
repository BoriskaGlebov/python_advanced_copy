"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from flask import Flask

import subprocess
import shlex
from flask import request
import string

app = Flask(__name__)


# Надеюсь я тут верно понял, что пользователь пишет команду в endpoint http://localhost:5000/ps?arg=a&aarg=u......
# Все это я могу или в браузере вводить или в postman и мой скрипт должен эту команду отработать и результат вывести
# пользователю в браузере! Сложности возникают с небезопасными командами, я предположил, что любая команда не
# начинающаяся с aux не безопасна поэтому ее не обрабатывать, надеюсь верно понял
@app.route("/ps", methods=["GET"])
def ps():
    base_url = request.endpoint
    print(base_url)
    user_cmd = request.args.getlist("arg")
    print(user_cmd)
    user_cmd_cleaned = [shlex.quote(s) for s in user_cmd]
    print(user_cmd_cleaned)
    command_str = f"{base_url} {' '.join(user_cmd_cleaned)}"
    print(command_str)
    command = shlex.split(command_str)
    print(command)
    res = subprocess.run(command, capture_output=True)
    print(res.returncode)
    if res.returncode != 0:
        return f"Какая-то ошибка ", 500
    output = res.stdout.decode()
    return f"<pre> {output} </pre>"
    # return string.Template(f'<pre> {output} </pre>').substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)
