import unittest

from module_03_ci_culture_beginning.homework.hw4.person import Person


class PersonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.person = Person("Boris", 2023, "ягодная 2,3")

    def test_get_age(self):
        res = self.person.get_age()
        self.assertEqual(res, 1)

    def test_get_name(self):
        expected_name = "Boris"
        res = self.person.get_name()
        self.assertEqual(res, expected_name)

    def test_set_name(self):
        expected_name = "Миша"
        self.person.set_name(expected_name)
        self.assertEqual(self.person.name, expected_name)

    def test_set_address(self):
        expexted_address = "Михневская, 35, 12"
        self.person.set_address(expexted_address)
        self.assertEqual(expexted_address, self.person.address)

    def test_get_address(self):
        expexted_address = "ягодная 2,3"
        res = self.person.get_address()
        self.assertEqual(expexted_address, res)

    def test_is_homeless(self):
        res = self.person.is_homeless()
        print(res)
        self.assertEqual(res, False)
