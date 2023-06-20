# Creating Series in Pandas


# General (Direct Method):
# - Series is a one-dimensional labeled array in Pandas.
# - It can be created directly by passing data and index.
# - Syntax: pd.Series(data, index)
# Example: Creating Series using the General Method

import pandas as pd

# Create a list of data
data = [10, 20, 30, 40, 50]

# Create a list of index labels
index = ['a', 'b', 'c', 'd', 'e']

# Create a Series by passing both data and index
s = pd.Series(data, index)

# Print the Series
print(s)


# Creating Series from a List:
# - Pass a list as the data argument to create a Series.
# - Index is automatically generated as integers starting from 0.
# Example: Creating Series from a List

import pandas as pd

# Create a list of data
data = [10, 20, 30, 40, 50]

# Create a Series from the list
s = pd.Series(data)

# Print the Series
print(s)


# Creating Series from a Tuple:
# - Pass a tuple as the data argument to create a Series.
# - Index is automatically generated as integers starting from 0.
# Example: Creating Series from a Tuple

import pandas as pd

# Create a tuple of data
data = (10, 20, 30, 40, 50)

# Create a Series from the tuple
s = pd.Series(data)

# Print the Series
print(s)


# Creating Series from a Set:
# - Pass a set as the data argument to create a Series.
# - Index is automatically generated as integers starting from 0.
import pandas as pd

# Define a set of data
data = {10, 20, 30, 40, 50}

# Convert the set to a list
data_list = list(data)

# Create a Series from the list
s = pd.Series(data_list)

# Print the Series
print(s)


# Creating Series from a Dictionary:
# - Pass a dictionary as the data argument to create a Series.
# - Keys of the dictionary become the index of the Series.
# - Values of the dictionary become the data of the Series.
# - Example: pd.Series({'A': 10, 'B': 20, 'C': 30})

import pandas as pd

# Define a dictionary of special dishes
special_dishes = {
    'Main Course': 'Spicy Butter Chicken',
    'Appetizer': 'Garlic Prawns',
    'Soup': 'Tom Yum',
    'Salad': 'Caprese Salad',
    'Dessert': 'Tiramisu'
}

# Create a Series from the dictionary
s = pd.Series(special_dishes)

# Print the Series
print(s)
