import unittest
from freezegun import freeze_time

from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app


class HelloWorld(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/hello-world/"

    # я вот тут не понял. Я передаю в username любую строку и он воспримет ее как имя по0льзователя, это я и проверяю?
    def test_username(self):
        username = "хорошей среды"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn(username, response_str)

    @freeze_time("2012-01-16")
    def test_day_monday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("понедельника", response_str)

    @freeze_time("2012-01-17")
    def test_day_tuesday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("вторника", response_str)

    @freeze_time("2012-01-18")
    def test_day_wednesday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("среды", response_str)

    @freeze_time("2012-01-19")
    def test_day_thursday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("четверга", response_str)

    @freeze_time("2012-01-20")
    def test_day_friday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("пятницы", response_str)

    @freeze_time("2012-01-21")
    def test_day_saturday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("субботы", response_str)

    @freeze_time("2012-01-22")
    def test_day_sunday(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_str = response.data.decode()
        self.assertIn("воскресенья", response_str)
