class Zoo:
    INCOME_FROM_ANIMAL = 60
    MEAT = 4
    BAMBOO = 2

    def __init_(self, animals, capacity, budged):
        self.animals = []
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

    def death(self, animal):
        animal.should_die()
        if not self.anima.is_alive:
                self.animals.remove(animal)
                print("{} died.".format(animal.name))
    return self.animals
