
# # Python does not support function overloading in the same way that some other languages (like C++) do, 
# where you can have multiple functions with the same name but different parameter lists. 
# In Python, function overloading can be achieved in a different way using default arguments 
# and variable numbers of arguments.



def add(a, b, c=0):
    return a + b + c

# Example usage
result1 = add(2, 3)
result2 = add(2, 3, 4)

print(result1)  # Output: 5
print(result2)  # Output: 9
