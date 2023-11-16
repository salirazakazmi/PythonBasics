# List:

# A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [].


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: "apple"

# Modifying elements
fruits[1] = "orange"

# Adding elements
fruits.append("grape")

# Removing elements
fruits.remove("cherry")

# Iterating through a list
for fruit in fruits:
    print(fruit)
