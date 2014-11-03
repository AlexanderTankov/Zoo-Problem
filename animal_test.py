import unittest

from animal import Animal


class Animal_test(unittest.TestCase):

    def setUp(self):
        self.my_animal = Animal("bear", 5, "puh", "m", 150)

    def test_init(self):
        self.assertEqual(self.my_animal.species, "bear")
        self.assertEqual(self.my_animal.age, 5)
        self.assertEqual(self.my_animal.name, "puh")
        self.assertEqual(self.my_animal.gender, "m")
        self.assertEqual(self.my_animal.weight, 150)

if __name__ == '__main__':
    unittest.main()
