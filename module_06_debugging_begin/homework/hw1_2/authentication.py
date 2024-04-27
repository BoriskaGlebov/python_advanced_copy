"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

2. К нам пришли сотрудники отдела безопасности и сказали, что, согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, является ли пароль хорошим по новым стандартам безопасности.
"""

import getpass
import hashlib
import logging
import re
import time

logger = logging.getLogger("password_checker")
with open("/usr/share/dict/words", "r") as file:
    all_word = filter(
        lambda x: len(x) > 4, file.read().split()
    )  # выбираю слова длинне 4 символов
    all_word = map(lambda x: x.lower(), all_word)  # все слова в нижний регистр перевожу
    # all_word = sorted(all_word) #я думал что поиск регулярным выражением
    # лучше из отсортированного списка слов, но для set это же не важно наверное?
    all_word = set(
        all_word
    )  # сет убирает почти 2000 слов из поиска, на 0.01 быстрее программа стала))))))))))
    all_word = "|".join(
        all_word
    ).lower()  # строка в качетсве паттерна для поиска в регулярном выражении


def is_strong_password(password: str) -> bool:
    res = re.findall(all_word, password.lower())
    if not res:
        return False
    else:
        print(res)
        return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()
    start = time.time()
    if not password:
        logger.warning("Вы ввели пустой пароль.")
        print(f"Время работы: {time.time() - start}")
        return False
    elif is_strong_password(password):
        print(f"Время работы: {time.time() - start}")
        logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)
    print(f"Время работы: {time.time() - start}")
    return False


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="stderr.txt",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)
# Отчего-то долго идет первый запуск, не понятно.
# Как я понимаю при запуске у меня открывается файл со словами и
# все операции с ним проводятся
# Потом времени тратится именно на
# моменте когда происходит первый анализ регулярным выражением,
# а потот почему-то на это время не тратится
# Я ничего не понял, как сделать алгоритм со сложностью O(log n) ,
# поэтому получилось как я понимаю O(n).
# Как пример оптимизации в чате предложили алгоритм бинарного
# поиска, но внятно понять, как разделять слова для поиска я не понял!
