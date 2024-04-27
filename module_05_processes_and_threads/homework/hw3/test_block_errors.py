import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    # я так понимаю тут setup не нужен?
    # может лучше перед каждым тестом создавать нужный мне экземпляр класса?

    # @classmethod
    # def setUpClass(cls):
    #     cls.err_types = {ZeroDivisionError, TypeError}
    #     cls.block_err = BlockErrors(cls.err_types)

    def test_ignore_error(self):
        try:
            with BlockErrors({ZeroDivisionError, TypeError}):
                a = 1 / 0
        except:
            self.fail()

    def test_new_error(self):
        with self.assertRaises(TypeError):
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / "0"

    def test_different_level_error(self):
        try:
            with BlockErrors({TypeError}):
                with self.assertRaises(TypeError):
                    with BlockErrors({ZeroDivisionError}):
                        a = 1 / "0"
        except:
            self.fail()

    def test_ignore_subclass_error(self):
        try:
            with BlockErrors({Exception}):
                a = 1 / "0"
        except:
            self.fail()


if __name__ == "__main__":
    unittest.main()
