import unittest
from redirect import Redirect


class RedirectTest(unittest.TestCase):
    def setUp(self):
        self.stdout_file = open("stdout.txt", "w")
        self.stderr_file = open("stderr.txt", "w")

    def test_stdout(self):
        with Redirect(stdout=self.stdout_file) as file:
            print("Hello stdout.txtz")
        with open("stdout.txt", "r") as stdout_file:
            file_inf = stdout_file.read()
            self.assertEqual("Hello stdout.txtz\n", file_inf)

    def test_stderr(self):
        with Redirect(stderr=self.stderr_file) as file:
            raise Exception("Hello stderr.txt")
        with open("stderr.txt", "r") as stdout_file:
            file_inf = stdout_file.read()
            self.assertTrue("Hello stderr.txt" in file_inf)

    def test_stdout_in_stderr(self):
        with Redirect(stdout=self.stderr_file, stderr=self.stderr_file) as file:
            print("Hello stdout.txtz")
            raise Exception("Hello stderr.txt")
        with open("stderr.txt", "r") as stdout_file:
            file_inf = stdout_file.read()
            self.assertTrue("Hello stdout.txtz" in file_inf)
            self.assertTrue("Hello stderr.txt" in file_inf)

    def test_clear(self):
        with self.assertRaises(Exception):
            with Redirect(stdout=None, stderr=None) as file:
                print("Hello stdout.txtz")
                raise Exception("Hello stderr.txt")

    def tearDown(self):
        self.stdout_file.close()
        self.stderr_file.close()


if __name__ == "__main__":
    # unittest.main()
    # зачем нужна конструкия ниже и почему файл test_results.txt не появляется нигде?
    with open("test_results.txt", "a") as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
