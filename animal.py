from random import random


class Animal():
    def __init__(self, species, age, name, gender, weight, life_expectancy,
                 food_type, gestation_period, newborn_weight, average_weight,
                 food_weight_ratio, weight_age_ratio):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.alive = True
        self.life_expectancy = life_expectancy
        self.food_type = food_type
        self.gestation_period = gestation_period
        self.newborn_weight = newborn_weight
        self.average_weight = average_weight
        self.food_weight_ratio = food_weight_ratio
        self.weight_age_ratio = weight_age_ratio

    def grow(self):
        self.age += 1
        self.food_weight_ratio += 0.5

    def eat(self):
        if self.weight < self.average_weight:
            self.weight += self.food_weight_ratio / 10

    def should_die(self):
        chance_of_dying = self.age / self.life_expectancy
        num = random()
        if num < chance_of_dying:
            self.alive = False
