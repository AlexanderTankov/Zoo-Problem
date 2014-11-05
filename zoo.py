import random
import json
from animal import Animal


class Zoo():

    INCOME_FROM_ANIMAL = 60
    FOOD_KIND = {"carnivore": 4, "herbivore": 2}
    NEW_BORN_BABY_WEIGHT = 3

    @staticmethod
    def load(file_name):
        my_file = open(file_name, 'r')
        my_zoo = json.load(my_file)
        my_file.close()
        result = Zoo(my_zoo["capacity"], "budged")
        animals_arr = my_zoo["animals"]
        for animals in animals_arr:
            temp_animal = Animal(
                my_zoo["species"],
                my_zoo["age"],
                my_zoo["name"],
                my_zoo["gender"],
                my_zoo["weight"],
                my_zoo["life_expectancy"],
                my_zoo["food_type"],
                my_zoo["gestation_period"],
                my_zoo["newborn_weight"],
                my_zoo["average_weight"],
                my_zoo["food_weight_ratio"],
                my_zoo["weight_age_ratio"]
                )
            result.animals.append(temp_animal)
        return result

    def __init__(self, capacity, budged):
        self.capacity = capacity
        self.budged = budged
        self.animals = []

    def add_new_animal(self, new_animal):
        if self.capacity == len(self.animals):
            raise ValueError("The zoo is full")
        for animal in self.animals:
            is_names_equal = animal.name == new_animal.name
            is_species_equal = animal.species == new_animal.species
            if is_species_equal and is_names_equal:
                raise ValueError("Choose another name for the new animal")
        self.animals.append(new_animal)

    def daily_income(self):
        income = self.INCOME_FROM_ANIMAL * len(self.animals)
        self.budged += income

    def daily_outcome(self):
        total = 0
        for animal in self.animals:
            if animal.food_type in self.FOOD_KIND:
                total += self.FOOD_KIND[animal.food_type] * animal.food_weight_ratio
        self.budged -= total

    def death(self, animal):
        if animal in self.animals:
            animal.should_die()
            if not animal.alive:
                self.animals.remove(animal)

    def get_same_type_animals(self, animal):
        one_kind = []
        for couple in self.animals:
            if couple.species == animal.species:
                one_kind.append(couple)
        return one_kind

    def can_cocatenate(self, male, female):
        if male.gender == "m" and female.gender == "f":
            return (female in self.get_same_type_animals(male))

    def concatenate_names(self, male, female):
        if male.gender == "m" and female.gender == "f":
            return male.name + female.name

    def get_baby_gender(self):
        if random.random() > 0.5:
            return "m"
        return "f"

    def get_baby_gestation(self, baby_gender, female):
        if baby_gender == "m":
            return 0
        else:
            return female.gestation_period

    def born_animal(self, male, female):
        if self.can_cocatenate(male, female):
            baby_gender = self.get_baby_gender()
            baby_gestation = self.get_baby_gestation(baby_gender, female)
            animal_baby = Animal(male.species, 0, self.concatenate_names(male, female),
                                 baby_gender, self.NEW_BORN_BABY_WEIGHT,
                                 male.life_expectancy, male.food_type, baby_gestation,
                                 self.NEW_BORN_BABY_WEIGHT, self.NEW_BORN_BABY_WEIGHT, 1, 2)
            self.animals.append(animal_baby)
