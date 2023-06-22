# DataFrame Attributes

# 1. Index: Represents the row labels of the DataFrame.
# Allows for efficient indexing and retrieval of rows based on their labels.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the index
index = df.index

print("\nThe Name of the index is:")
print(index)


# 2. Column: Represents the column labels of the DataFrame.
# Provides a way to access and manipulate data in specific columns of the DataFrame.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the columns
columns = df.columns
print("\nThe Columns of the DataFrame are:")
print(columns)


# 3. Values: Returns the actual data stored in the DataFrame as a NumPy array.
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the values
values = df.values
print("\nThe Values of the DataFrame are:")
print(values)


# 4. Shape: Returns a tuple representing the dimensions of the DataFrame (number of rows, number of columns).

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the shape
shape = df.shape
print("\nThe Shape of the DataFrame is:")
print(shape)


# 5. Size: Returns the total number of elements in the DataFrame,
# which is equal to the product of the shape.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the size
size = df.size
print("\nThe Size of the DataFrame is:")
print(size)


# 6. Dtype: Returns the data type of the elements in the DataFrame.
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the data types
dtypes = df.dtypes
print("\nThe Data Types of the DataFrame are:")
print(dtypes)


# 7. Empty: Indicates whether the DataFrame is empty or not.
import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame()

# Check if the DataFrame is empty
is_empty = df.empty
print("\nIs the DataFrame empty?")
print(is_empty)


# 8. Ndim: Returns the number of dimensions of the DataFrame.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the number of dimensions
ndim = df.ndim
print("\nThe Number of Dimensions of the DataFrame is:")
print(ndim)


# 9. Column.name: Returns the name of a specific column in the DataFrame.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the name of a specific column
column_name = df['Name'].name
print("\nThe Name of the 'Name' Column is:")
print(column_name)


# 10. Index.type: Returns the type of the index used in the DataFrame,
# such as 'RangeIndex' or 'MultiIndex'.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the type of the index
index_type = df.index.__class__.__name__
print("\nThe Type of the Index is:")
print(index_type)


# 11. Index.name: Returns the name of the index of the DataFrame, if specified.

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Access the name of the index
index_name = df.index.name
print("\nThe Name of the Index is:")
print(index_name)
