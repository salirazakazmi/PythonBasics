class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(f"{dog.name} is a {dog.species}.")
