
from abc import ABC, abstractmethod

class EmployeeAbstract(ABC):
    @property
    @abstractmethod
    def name(Self):
        pass

    @abstractmethod
    def Retired(Self):
        pass

class Employee(EmployeeAbstract):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def add(Self, para1):
        name = "abcdedf"
        print("Add Employee Method", para1, Self.name, " and without self", name)

    # def Retired(Self, para1):
    #     print(para1)
    #     return super().Retired()
    
    @property
    def name(Self):
        return Self._name
    
    def Retired(Self):
        print("I am retired now")


employee2 = Employee('xyz', 44)

print(employee2.name)
print(employee2.age)

employee2.add("Employee 2")
# employee2.Retired("I am now 60")
employee2.Retired()

        
