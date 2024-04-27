"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""

import datetime
import json
import logging
import random
import shlex
import subprocess
import time
from itertools import groupby
from typing import List
import re

logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2**31), 2**31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


def counter_log():
    # я пробовал читать файл и фильтровать через filter,regex они были долгие, а вот grep оказался быстрее
    # Как можно было сделать это средствами python? быстро
    cmd = 'grep -e "Enter measure_me" -e "Leave measure_me" count.log'
    args_correct = shlex.split(cmd)
    proc = subprocess.Popen(args=args_correct, stdout=subprocess.PIPE)
    time_compare = []
    for line in proc.stdout.readlines():
        time_str = json.loads(line.decode().strip())["time"]
        time_format = datetime.datetime.strptime(time_str, "%H:%M:%S")
        time_compare.append(time_format)
    res = []
    for num, el in enumerate(time_compare[::2]):
        start = el
        end = time_compare[num * 2 + 1]
        different = (end - start).seconds
        res.append(different)
    out = sum(res) / len(res)
    return out

    # Этот способ совсем чтото долгий
    # with open('count.log', 'r') as file:
    #     # lines=file.read()
    #     find_str = re.finditer(r'.*(?:Enter measure_me|Leave measure_me).*', file.read())
    # for el in find_str:
    #     print(el.group())


if __name__ == "__main__":
    # logging.basicConfig(level="DEBUG",
    #                     format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
    #                     datefmt='%H:%M:%S',
    #                     filename='count.log')
    # for it in range(15):
    #     data_line = get_data_line(10 ** 3)
    #     measure_me(data_line)
    print(counter_log())

    # наверно это все можно сделать быстрее и проще, но что-то в голову не пришло совсем
