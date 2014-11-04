import unittest

from zoo import Zoo
from animal import Animal


class Zoo_test(unittest.TestCase):

    def setUp(self):
        self.my_animal = Animal("bear", 5, "puh", "m", 150, 10)
        self.my_zoo = Zoo()

    def test_init(self):


if __name__ == '__main__':
    unittest.main()
