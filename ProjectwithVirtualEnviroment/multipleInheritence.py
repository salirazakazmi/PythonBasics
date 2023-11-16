
# Mutiple Inheritence

class Parent1:
    def method1(self):
        print("Method 1 from Parent1")

class Parent2:
    def method2(self):
        print("Method 2 from Parent2")

class Child(Parent1, Parent2):
    def child_method(self):
        print("Child's method")

# Create an instance of the Child class
child = Child()

# Call methods from Parent1
child.method1()  # Output: Method 1 from Parent1

# Call methods from Parent2
child.method2()  # Output: Method 2 from Parent2

# Call the child's own method
child.child_method()  # Output: Child's method
