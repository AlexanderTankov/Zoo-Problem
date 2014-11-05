import unittest

from zoo import Zoo
from animal import Animal


class Zoo_test(unittest.TestCase):

    def setUp(self):
        self.my_animal = Animal("bear", 5, "puh", "m", 150, 10, "carnivore", 0, 1, 200, 5, 2)
        self.my_zoo = Zoo(60, 1000)

    def test_init(self):
        self.assertEqual(self.my_zoo.capacity, 60)
        self.assertEqual(self.my_zoo.budged, 1000)
        self.assertEqual(self.my_zoo.animals, [])

    def test_success_add_new_animal(self):
        self.my_zoo.add_new_animal(self.my_animal)
        self.assertEqual(self.my_zoo.animals[0].species, "bear")

    def test_fail_add_new_animal_full_capacity(self):
        my_fail_zoo = Zoo(1, 1000)
        my_snd_animal = Animal("Tiger", 5, "Blq", "m", 150, 10, "carnivore", 0, 1, 200, 5, 2)
        my_fail_zoo.add_new_animal(self.my_animal)
        self.assertEqual(my_fail_zoo.animals[0].species, "bear")
        with self.assertRaises(ValueError):
            my_fail_zoo.add_new_animal(my_snd_animal)
            self.assertEqual("The zoo is full", str(self.assertRaises(ValueError).exception))

    def test_fail_add_new_animal_equal_name(self):
        my_fail_zoo = Zoo(1, 1000)
        my_snd_animal = Animal("Tiger", 5, "Blq", "m", 150, 10, "carnivore", 0, 1, 200, 5, 2)
        my_fail_zoo.add_new_animal(self.my_animal)
        self.assertEqual(my_fail_zoo.animals[0].species, "bear")
        with self.assertRaises(ValueError):
            my_fail_zoo.add_new_animal(my_snd_animal)
            self.assertEqual("Choose another name for the new animal", str(self.assertRaises(ValueError).exception))

    def test_daily_income_without_animals(self):
        self.my_zoo.daily_income()
        self.assertEqual(self.my_zoo.budged, 1000)

    def test_daily_income_with_animals(self):
        self.my_zoo.add_new_animal(self.my_animal)
        self.my_zoo.daily_income()
        self.assertEqual(self.my_zoo.budged, 1060)

    def test_daily_outcome(self):
        self.my_zoo.add_new_animal(self.my_animal)
        self.my_zoo.daily_outcome()
        self.assertEqual(self.my_zoo.budged, 980)

    def test_death(self):
        self.my_zoo.add_new_animal(self.my_animal)
        for i in range(1, 10):
            self.my_zoo.death(self.my_animal)
        self.assertEqual(self.my_zoo.animals, [])

if __name__ == '__main__':
    unittest.main()
