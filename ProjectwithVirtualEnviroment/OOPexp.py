# Inheritence

class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add(Self, para1):
        name = "abcdedf"
        print("Add Employee Method", para1, Self.name, " and without self", name)

class EmployeeHR(Employee):
    def __init__(self, name, age, hireby):
        super().__init__(name, age)
        self.hireby = hireby


employee2 = EmployeeHR('xyz', 40, 'faisal')

print(employee2.name)
print(employee2.age)

employee2.add("Employee 2")

        
