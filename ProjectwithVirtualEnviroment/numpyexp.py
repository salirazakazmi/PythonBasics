#pip install numpy


# Use from when you want to import specific attributes (functions, variables, or classes) 
# example: from math import sqrt

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# # print(arr)

# print(arr[2] + arr[3])

# print(np.__version__)

# print(type(arr))

# -------------------------------------------------------------------------------------
# #2D array
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print("2D:", arr)

# print(arr.ndim)

# #3D array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print("3D:",arr)
# print(arr.ndim)

# --------------------------------------------------------------------------
# Revers the index -1 mean last index
# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[-2:-1])

# ------------------------------------------------------------------------------------------
# We use the array() function to create arrays, this function can take an optional argument: 
# dtype that allows us to define the expected data type of the array elements:

# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)

# -----------------------------------------------------------------------------
# Change data type from float to integer by using 'i' as parameter value:

# arr = np.array([1.1, 2.1, 3.1])

# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)


# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


# ----------------------------------------------- Copy and view ------------------------------
# arr = np.array([1, 2, 3, 4, 5])

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# -------------------------------------------------------------------------------------------
# Iteration / loop on array

# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)

# ------------------------------------------ Where or filter
# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)

# -------------------------------- Random Number --------------------
# from numpy import random
# x = random.randint(100)
# print(x)

# If you want to create your own website or build Python applications, check out W3Schools Spaces.
# CREATE A FREE PYTHON WEB SITE https://www.w3schools.com/spaces/index.php




# arr = np.array([1,2,3,4,5,6,7])
# print(arr[::3]) 