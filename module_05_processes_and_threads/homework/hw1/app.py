"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""

import os
import shlex
import signal
import subprocess
from subprocess import CalledProcessError
import time
from typing import List

import psutil
from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    cmd_str = f"lsof -i :{str(port)}"
    cmd_correct = shlex.split(cmd_str)
    try:
        process_port_finder = subprocess.check_output(cmd_correct).decode()
    except CalledProcessError as ex:
        return []
    lines = process_port_finder.splitlines()[1:]
    pids: List[int] = [int(line.split()[1]) for line in lines]
    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    print(len(psutil.pids()))  # сколько процессов до завершения нужного мне
    pids: List[int] = get_pids(port)
    if pids:
        for pid in pids:
            proc = psutil.Process(pid)
            os.kill(pid, signal.SIGKILL)
            # proc.terminate()
            proc.wait()
            print(
                len(psutil.pids())
            )  # Сколько процессов осталось. Проверяю что только один был завершен


# os.kill(pid, signal.SIGKILL) пробовал так, но не получилось реализовать ожидание завершения процесса!
# если добавить time.sleep то получается , но мне кажется это костыль? как нужно было это сделать через os.kill?????


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)

    app.run(port=port)


if __name__ == "__main__":
    run(5000)
    # free_port(5000)
    # print(get_pids(5000))
