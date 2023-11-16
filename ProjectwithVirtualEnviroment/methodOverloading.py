
# However, in Python, it's not possible to create multiple methods with the same name and 
# different parameter lists in a class.


class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

    def multiply(self, a, b, c=1):
        return a * b * c

# Example usage
math_ops = MathOperations()
result1 = math_ops.add(2, 3)
result2 = math_ops.add(2, 3, 4)
result3 = math_ops.multiply(2, 3)
result4 = math_ops.multiply(2, 3, 5)

print(result1)  # Output: 5
print(result2)  # Output: 9
print(result3)  # Output: 6
print(result4)  # Output: 30
