"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from subprocess import TimeoutExpired
from wtforms.validators import InputRequired

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired()])


def run_python_code_in_subproccess(code: str, timeout: int):
    """
    создания процесса с кодом
    :param code:
    :param timeout:
    :return:
    """
    start_code = "prlimit --nproc=1:1 python -c"
    with subprocess.Popen(
        f'{start_code} "{code}"',
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        encoding="utf8",
        stderr=subprocess.PIPE,
    ) as proc:
        try:
            stdout, stderr = proc.communicate("asdas", timeout=timeout)
            if stdout:
                return stdout
            else:
                print(stderr)
                return stderr
        except TimeoutExpired as ex:
            print(ex)
            proc.kill()

            return "Ваш код слишком долго выполнялся", 400


@app.route("/run_code", methods=["POST"])
def run_code() -> (str, int):
    """
    Запуск кода
    :return: (ответ на запрос , статус код)
    """
    form = CodeForm()
    if form.validate_on_submit():
        input_code = form.code.data
        input_timeout = form.timeout.data
        res = run_python_code_in_subproccess(input_code, int(input_timeout))
        return res
    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
