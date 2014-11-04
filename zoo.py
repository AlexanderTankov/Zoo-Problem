class Zoo():
    INCOME_FROM_ANIMAL = 60
    MEAT = ['meat']
    GREENS = ['bamboo', 'foliage', 'grass']
    animals = []

    def __init__(self, capacity, budged):
        self.capacity = capacity
        self.budged = budged

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
        return income

    def daily_outcome(self):
        total = 0
        for animal in animals:
            if animal.type_food in GREENS:
                total += 2
            if animal.type_food in MEAT:
                total += 4
        self.budged -= total
        return total

    def death(self, animal):
        animal.should_die()
        if not animal.is_alive:
            self.animals.remove(animal)
            print("{} died.".format(animal.name))
    return self.animals
