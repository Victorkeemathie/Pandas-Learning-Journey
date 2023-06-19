# Pandas Data Structures

# 1. Series:
#    - A one-dimensional labeled array capable of holding any data type.
#    - Similar to a column in a spreadsheet or a database table.
#    - Can be created from a list, array, or dictionary.

# Exanple: 
# Creating Series Data Structures:

import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)



# 2. DataFrame:
#    - A two-dimensional labeled data structure, like a table or spreadsheet.
#    - Consists of rows and columns, where each column can have a different data type.
#    - Can be created from various sources such as CSV files, Excel sheets, databases, or dictionaries.
# Example:
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['John', 'Emma', 'Ryan'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Sydney']}
df = pd.DataFrame(data)
print(df)


# 3. Index:
#    - An immutable array or an ordered set representing the labels of rows or columns in a Series or DataFrame.
#    - Allows for efficient data alignment and retrieval.
#    - Can be customized based on the requirements.
# Example:
import pandas as pd

# Create a Series with a custom index
data = [10, 20, 30]
index = ['A', 'B', 'C']
s = pd.Series(data, index=index)
print(s)


# 4. Panel:
#    - A three-dimensional data structure.
#    - Contains multiple DataFrames.
#    - Less commonly used compared to Series and DataFrame.
# NB: The pd.Panel() constructor has been deprecated since pandas version 0.20.0, and it is no longer a valid way to create a panel DataFrame.

# Key Operations on Data Structures:

# 1. Indexing and Selection:
#    - Accessing specific elements or subsets of data using various indexing techniques.
#    - Examples: loc, iloc, boolean indexing.

# 2. Data Manipulation:
#    - Performing operations to modify, filter, or transform data.
#    - Examples: filtering rows based on conditions, adding or removing columns, data aggregation, etc.

# 3. Data Alignment:
#    - Aligning data based on indexes or labels, ensuring consistency across different data structures.
#    - Enables performing operations on datasets with different shapes and indexes.

# 4. Missing Data Handling:
#    - Dealing with missing or null values in datasets.
#    - Provides methods to handle missing data, such as filling, dropping, or interpolating.

# 5. Grouping and Aggregation:
#    - Grouping data based on certain criteria and computing summary statistics.
#    - Enables performing operations on subsets of data based on specific conditions.

# Pandas is a versatile library that simplifies data manipulation and analysis tasks in Python. Its rich set of functionalities makes it a popular choice for working with structured data.

