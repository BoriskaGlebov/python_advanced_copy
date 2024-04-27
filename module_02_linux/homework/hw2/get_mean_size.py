"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys

import os
from functools import reduce


def get_mean_size(ls_output: str) -> float | str:
    """
    Определяет средний размер файла в папке
    :param ls_output: данные из консоли
    :return: средний размер файла
    """
    len_inf = len(ls_output.split("\n")) - 2
    if len_inf and ls_output.startswith("total"):
        aver_size = round(
            (
                reduce(
                    lambda a, b: a + b,
                    map(lambda x: int(x.split()[4]), ls_output.split("\n")[1:-1]),
                )
            )
            / len_inf,
            2,
        )
        return aver_size
    return "Папка пуста/ или не существует"


if __name__ == "__main__":
    data: str = sys.stdin.read()
    print(data)
    mean_size: float = get_mean_size(data)
    print(mean_size)
