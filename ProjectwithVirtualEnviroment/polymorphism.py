
# Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This is an abstract method

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says Quack!"

# Create objects of different animal types
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Daffy")

# Create a function that works with any animal
def animal_speak(animal):
    print(animal.speak())

# Call the function with different animal objects
animal_speak(dog)
animal_speak(cat)
animal_speak(duck)
