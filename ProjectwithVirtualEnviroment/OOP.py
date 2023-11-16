

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

# Create objects (instances) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rocky", "Labrador")

# Access attributes and call methods
print(f"{dog1.name} is a {dog1.breed}. {dog1.bark()}")
print(f"{dog2.name} is a {dog2.breed}. {dog2.bark()}")
