# lambda arguments: expression


# square = lambda x: x * x
# result = square(5)
# print(result)  # Output: 25


# numbers = [1, 4, 2, 7, 5]
# squared_numbers = list(map(lambda x: x * x, numbers))
# filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# sorted_numbers = sorted(numbers, key=lambda x: -x)

# print(squared_numbers)

# print(filtered_numbers)

# print(sorted_numbers)

# sorted_numbers1 = sorted(numbers)
# print(sorted_numbers1)

# filtered_numbers1 = list(filter(lambda x: x % 2 == 0, numbers))

doublethevalue = lambda x : x * x
print(doublethevalue(5))


powerof = lambda x,y : x ** y
print(powerof(5,3))


stringdisplay = lambda str: ( print(str) , print(str , 'abc ') )
stringdisplay("this is first string")


# factorial 

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
number = 5
result = factorial_recursive(number)
print(f"Function: The factorial of {number} is {result}")

# factorial with lambda

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Example usage:
number = 5
result = factorial(number)
print(f"lambda: The factorial of {number} is {result}")





