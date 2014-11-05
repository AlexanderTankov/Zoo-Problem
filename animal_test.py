import unittest

from animal import Animal


class Animal_test(unittest.TestCase):

    def setUp(self):
        self.my_animal = Animal("bear", 5, "puh", "m", 150, 10, "carnivore", 0, 1, 200, 5, 2)

    def test_init(self):
        self.assertEqual(self.my_animal.species, "bear")
        self.assertEqual(self.my_animal.age, 5)
        self.assertEqual(self.my_animal.name, "puh")
        self.assertEqual(self.my_animal.gender, "m")
        self.assertEqual(self.my_animal.weight, 150)
        self.assertTrue(self.my_animal.alive)
        self.assertEqual(self.my_animal.life_expectancy, 10)
        self.assertEqual(self.my_animal.food_type, "carnivore")
        self.assertEqual(self.my_animal.gestation_period, 0)
        self.assertEqual(self.my_animal.newborn_weight, 1)
        self.assertEqual(self.my_animal.average_weight, 200)
        self.assertEqual(self.my_animal.food_weight_ratio, 5)
        self.assertEqual(self.my_animal.weight_age_ratio, 2)

    def test_grow(self):
        self.my_animal.grow()
        self.assertEqual(self.my_animal.age, 6)
        self.assertEqual(self.my_animal.food_weight_ratio, 5.5)

    def test_success_eat(self):
        self.my_animal.eat()
        self.assertEqual(self.my_animal.weight, 150.5)

    def test_fail_eat(self):
        my_fat_animal = Animal("bear", 5, "puh", "m", 150, 10, "carnivore", 0, 1, 150, 5, 2)
        my_fat_animal.eat()
        self.assertEqual(self.my_animal.weight, 150)

    def test_should_die(self):
        flag_die = False
        flag_alive = True
        for i in range(0, 100):
            self.my_animal.should_die()
            if not self.my_animal.alive:
                flag_die = True
            else:
                flag_alive = True
        self.assertTrue(flag_die and flag_alive)

if __name__ == '__main__':
    unittest.main()
