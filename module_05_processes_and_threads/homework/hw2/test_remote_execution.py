import unittest
from remote_execution import app


class CodeForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        cls.app = app.test_client()
        cls.base_url = "/run_code"

    def setUp(self):
        self.post_data = {"code": "print('hello_world')", "timeout": "5"}

    def test_simple_code(self):
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue("hello_world" in request.data.decode())

    def test_empty_code(self):
        self.post_data["code"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue(
            "Invalid input" in request.data.decode() and request.status_code == 400
        )

    def test_empty_timeout(self):
        self.post_data["timeout"] = ""
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue(
            "Invalid input" in request.data.decode() and request.status_code == 400
        )

    def test_uncorrect_timeout(self):
        self.post_data["timeout"] = "sdf"
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue(
            "Invalid input" in request.data.decode() and request.status_code == 400
        )

    def test_timeout_work(self):
        self.post_data["code"] = "import time;time.sleep(5);print('Hello world!')"
        self.post_data["timeout"] = "4"
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue(
            "Ваш код слишком долго выполнялся" in request.data.decode()
            and request.status_code == 400
        )

    def test_prlimit_work(self):
        self.post_data["code"] = (
            "from subprocess import run\n" "run(['./kill_the_system.sh'])"
        )
        self.post_data["timeout"] = "4"
        request = self.app.post(self.base_url, data=self.post_data)
        self.assertTrue(
            "BlockingIOError" in request.data.decode() and request.status_code == 200
        )


if __name__ == "__main__":
    unittest.main()
