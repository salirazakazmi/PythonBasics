# OperatorOverloadingExample.py

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(2, 3)
v2 = Vector(1, 4)
result = v1 + v2
print(result)  # Calls the __add__ method, Output: Vector(3, 7)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return math.hypot(self.x, self.y) == math.hypot(other.x, other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(3, 4)
p2 = Point(1, 2)
print(p1 == p2)  # Calls the __eq__ method, Output: True

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"Student: {self.name}, Roll: {self.roll}"

# Example usage
student = Student("Alice", 101)
print(str(student))  # Calls the __str__ method, Output: "Student: Alice, Roll: 101"
