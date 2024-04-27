"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest

from wtforms.validators import ValidationError

from hw1_registration import app


# Вопрос по правильности организации тестирования: Учел ошибку прошлого ДЗ, где ловил исключения через try except,
# а пользователю отправлял 200 статус. Тут сначала думал ловить ошибку 400, но понял, что не понятно будет на какое
# именно поле будет реагировать тест Тогда добавил в валидатор сообщения и стал искать эти сообщения, но возникает
# вопрос, Валидатор наверно выкидывает какое-то исключение, но я его не вижу нигде кроме статуса 400, исключения где-
# то появляются или нет? Верно ли вообще так тестировать? Правильно ли что словарь с данными повторяется с
# незначительными изменениями в каждом тесте и это дубляж кода? Так и должно быть?
class RegistrationForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        cls.app = app.test_client()
        cls.base_url = "/registration"

    def setUp(self):
        self.post_data = {
            "email": "boris@mail.ru",
            "phone": 9852000338,
            "name": "Boris B.A.",
            "address": "Москва,Ягодная, 8к3, 129",
            "index": 45789,
            "comment": "some user inf",
        }

    def test_all_correct(self):
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("200" in request.status)

    def test_email_empty(self):
        self.post_data["email"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("Форма почты пуста" in request.data.decode())

    def test_email_incorrect(self):
        self.post_data["email"] = "borismail.ru"
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("некорректный формат почты" in request.data.decode())

    def test_phone_none(self):
        self.post_data["phone"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("номер пуст" in request.data.decode())

    def test_phone_incorrect(self):
        self.post_data["phone"] = 98520003389
        request = self.app.post(self.base_url, data=self.post_data)
        # Если правильно понимаю исключение возникает в файле hw2 и почему то я не могу его отловить?????
        # with self.assertRaises(ValidationError):
        #     request = self.app.post(self.base_url, data=post_data)

        self.assertTrue("номер некорректен" in request.data.decode())

    def test_name_none(self):
        self.post_data["name"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("Имя не заполнено" in request.data.decode())

    def test_address_none(self):
        self.post_data["address"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("адрес пуст" in request.data.decode())

    def test_index_none(self):
        self.post_data["index"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("индекс пуст" in request.data.decode())

    def test_comment_none(self):
        self.post_data["comment"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("200" in request.status)


if __name__ == "__main__":
    unittest.main()
