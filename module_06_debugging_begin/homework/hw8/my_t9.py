"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""

import re
from typing import List
from collections import Counter


def my_t9(input_numbers: str) -> List[str]:
    keyboard: dict = {
        "2": r"[abc]{1}",
        "3": r"[def]{1}",
        "4": r"[ghi]{1}",
        "5": r"[jkl]{1}",
        "6": r"[mno]{1}",
        "7": r"[pqrs]{1}",
        "8": r"[tuv]{1}",
        "9": r"[wxyz]{1}",
    }
    pattern = r"\b("
    for num in input_numbers:
        pattern += keyboard[num]
    else:
        pattern += r")\|"
    with open("words", "r") as file:
        all_word = file.readlines()
        all_word = map(lambda x: x.strip().lower(), all_word)
        all_word = set(
            all_word
        )  # сет убирает почти 2000 слов из поиска, на 0.01 быстрее программа стала))))))))))
        all_word = "|".join(
            all_word
        ).lower()  # строка в качетсве паттерна для поиска в регулярном выражении4
        res = re.findall(pattern, all_word)
        return res


if __name__ == "__main__":
    numbers: str = str(input("Введите цифры = "))
    words: List[str] = my_t9(numbers)
    # words: List[str] = my_t9(str(22736368))
    print(*words, sep="\n")
