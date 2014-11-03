from random import random


class Animal:
    def __init__(self, species, age, name, gender, weight, life_expectancy):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.alive = True
        self.life_expectancy = life_expectancy

    def grow(self):
        self.age += 1
        self.weight += 1

    def eat(self):
        self.weight += 1

    def should_die(self):
        chance_of_dying = self.age / self.life_expectancy
        num = random()
        if num < chance_of_dying:
            self.alive = False
