import unittest

from animal import Animal


class Animal_test(unittest.TestCase):

    def setUp(self):
        self.my_animal = Animal("bear", 5, "puh", "m", 150, 10)

    def test_init(self):
        self.assertEqual(self.my_animal.species, "bear")
        self.assertEqual(self.my_animal.age, 5)
        self.assertEqual(self.my_animal.name, "puh")
        self.assertEqual(self.my_animal.gender, "m")
        self.assertEqual(self.my_animal.weight, 150)
        self.assertTrue(self.my_animal.alive)
        self.assertEqual(self.my_animal.life_expectancy, 10)

    def test_grow(self):
        self.my_animal.grow()
        self.assertEqual(self.my_animal.age, 6)
        self.assertEqual(self.my_animal.weight, 151)

    def test_eat(self):
        self.my_animal.eat()
        self.assertEqual(self.my_animal.weight, 151)

    def test_should_die(self):
        flag_die = False
        flag_alive = False
        for i in range(0, 100):
            self.my_animal.should_die()
            if not self.my_animal.alive:
                flag_die = True
            else:
                flag_alive = True
        self.assertTrue(flag_die and flag_alive)

if __name__ == '__main__':
    unittest.main()
