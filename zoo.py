class Zoo():

    INCOME_FROM_ANIMAL = 60
    FOOD_KIND = {"carnivore": 4, "herbivore": 2}

    def __init__(self, capacity, budged):
        self.capacity = capacity
        self.budged = budged
        self.animals = []

    def add_new_animal(self, new_animal):
        if self.capacity == len(self.animals):
            raise ValueError("The zoo is full")
        for animal in self.animals:
            if animal.species == new_animal.species and animal.name == new_animal.name:
                raise ValueError("Choose another name for the new animal")
        self.animals.append(new_animal)

    def daily_income(self):
        income = self.INCOME_FROM_ANIMAL * len(self.animals)
        self.budged += income

    def daily_outcome(self):
        total = 0
        for animal in self.animals:
            if animal.food_type in self.FOOD_KIND:
                total += self.FOOD_KIND[animal.food_type]
        self.budged -= total

    def death(self, animal):
        animal.should_die()
        if not animal.is_alive:
            self.animals.remove(animal)
