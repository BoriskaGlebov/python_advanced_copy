"""Модуль тестировщик"""

import unittest

from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt


class Decrypt(unittest.TestCase):
    """
    Класс конструткор тестов
    """

    def setUp(self):
        self.tests: list[tuple[str, str]] = [
            ("абра-кадабра.", "абра-кадабра"),
            ("абраа..-кадабра", "абра-кадабра"),
            ("абраа..-.кадабра", "абра-кадабра"),
            ("абра--..кадабра", "абра-кадабра"),
            ("абрау...-кадабра", "абра-кадабра"),
            ("абра........", ""),
            ("абр......a.", "a"),
            ("1..2.3", "23"),
            (".", ""),
            ("1.......................", ""),
        ]

    def test_decrypt(self):
        """
        Тесты
        :return:
        """
        for el in self.tests:
            with self.subTest(el):
                res = decrypt(el[0])
                self.assertEqual(res, el[1])
