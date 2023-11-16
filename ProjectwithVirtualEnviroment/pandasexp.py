# Pandas is a Python library used for working with data sets.

# pip install pandas

# import pandas

import pandas as pd

# # cars and passing are header of data
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

# print(pd.__version__)

# # ------------------------------------ SERIES
# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.
# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar)



# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)

# ----------------------------------------------------------------------------------
# You can also use a key/value object, like a dictionary, when creating a Series.

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)



# -------------------------------------------  DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)

# ------------------------ Loading files

# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# pd.options.display.max_rows = 10

# df = pd.read_csv('datafile.csv')

# print(df) 

# print(pd.options.display.max_rows) 

# The head() method returns the headers and a specified number of rows, starting from the top.
# print(df.head(10))

# IF ONLY head then return 5 rows + header, starting from 0
# print(df.head())


# print(df.tail()) 

#print(df.info()) 
# print( pd.to_datetime(df[5])  )


# df.corr()


# ================================== PLOTING
# pip install matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('datafile.csv')

df.plot()

plt.show()