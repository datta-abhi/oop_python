class Zoo:
    def __init__(self):
        self.animals = []  # note each instance of zoo is a list of animals

    def add_animals(self,name,species):
        animal = self.Animal(name,species)
        self.animals.append(animal)
    def display_animals(self):
        for a in self.animals:
            print('Name: {}, Species: {}'.format(a.name,a.species))
    # inner class
    class Animal:
        def __init__(self,name,species):
            self.name = name
            self.species = species

# creating the zoo
zoo = Zoo()
zoo.add_animals('Tiger','mammal')
zoo.add_animals('Peacock','bird')
zoo.add_animals('Crocodile','reptile')
zoo.display_animals()

print()

#using the same template to create a digital zoo
zoo1 = Zoo()
zoo1.add_animals('Iphone','smartphone')
zoo1.add_animals('Asus','Laptop')
zoo1.add_animals('Boat','earphones')
zoo1.display_animals()