"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""

import json
import shlex
import subprocess
from datetime import datetime
from typing import Dict
from itertools import groupby
from collections import Counter

with open("skillbox_json_messages.log", "r") as file:
    read_file = file.read().split("\n")
    log_file: list[dict] = [json.loads(line) for line in read_file[:-1]]


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    log_file.sort(key=lambda x: x["level"])
    keys = []
    groups = []
    for key, group in groupby(log_file, key=lambda x: x["level"]):
        keys.append(key)
        groups.append(list(group))
    out_dict = {el: groups[num].__len__() for num, el in enumerate(keys)}
    return out_dict


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    log_file.sort(key=lambda x: x["time"])
    keys = []
    groups = []
    for key, group in groupby(log_file, key=lambda x: x["time"][:2]):
        keys.append(key)
        groups.append(list(group))
    out_dict: dict = {el: groups[num].__len__() for num, el in enumerate(keys)}
    max_hour = max(out_dict, key=out_dict.get)
    return max_hour


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """

    # Что-то через shlex split не вышел, я тут так записал команду
    cmd1 = ["grep", '"level": "CRITICAL"', "skillbox_json_messages.log"]
    cmd2 = ["grep", "-c", "-e", '"time": "05:[01]', "-e", '"time": "05:20:00']
    proc1 = subprocess.Popen(
        args=cmd1, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE
    )
    proc2 = subprocess.Popen(args=cmd2, stdin=proc1.stdout, stdout=subprocess.PIPE)
    proc1.stdout.close()
    res = int(proc2.stdout.read().decode().strip())
    return res


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    cmd1 = ["grep", "-c", r"\bdog\s", "skillbox_json_messages.log"]
    proc1 = subprocess.Popen(
        args=cmd1, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE
    )
    res = int(proc1.stdout.read().decode())
    return res


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    filtered_log = list(filter(lambda x: x["level"] == "WARNING", log_file))
    el_counter = Counter()
    for el_dict in filtered_log:
        res = Counter(el_dict["message"].strip().split())
        el_counter.update(res)
    res = el_counter.most_common(1)[0][0]
    return res


if __name__ == "__main__":
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f"{i}. {task_answer}")
