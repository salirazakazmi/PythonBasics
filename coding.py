
# name = input("Enter your name:")


# # print(f) -- formatted string
# print(f"my name is {name}") 

# print("my full name is :", name)


# file open at write mode

# file_path = "example.txt"  # Replace with the path to your desired file

# with open(file_path, 'w') as file:
#     file.write(name)

# file.close

# file open at append mode
# name ="\n" + name 
# with open(file_path, 'a') as file:
#     file.write(name)

# file.close

# Exception Handling

try:
    value = int(input("Enter an integer: "))
    result = 10 / value
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An exception of type {type(e).__name__} occurred: {e}")
else:
    print(f"The result is: {result}")



# pointer is not supported in Python, 

x = 42
print(id(x))  # Prints the unique identifier of the integer object


