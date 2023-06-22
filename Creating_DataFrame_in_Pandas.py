# Notes on Pandas DataFrame Structure:

# DataFrame:
#   - A two-dimensional data structure in Pandas.
#   - Used to store and organize data in tabular form.
#   - Consists of rows and columns.

# Creating DataFrame:
# - General (Direct Method):
#     - Use a list, dictionary, or NumPy array to create a DataFrame.
#     - Syntax: pd.DataFrame(data)

# - Empty DataFrame:
#     - Create an empty DataFrame and then populate it with data.
#     - Syntax: pd.DataFrame()
# Example:

import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame()

# Add columns and corresponding data to the DataFrame
df['Name'] = ['John', 'Emma', 'Michael']
df['Age'] = [25, 30, 35]

# Print the DataFrame
print(df)


# - Lists:
#     - Create a DataFrame from a list.
#     - Each element in the list represents a row in the DataFrame.
#     - Syntax: pd.DataFrame(data, columns)
# Example:

import pandas as pd

# Creating a DataFrame with student names and marks
data = [["Joe", 79], ["Ali", 68], ["Grace", 80], ["Prisca", 90]]  # List of student names and marks
columns = ["Name", "Marks"]  # Column names for the DataFrame
df = pd.DataFrame(data, columns=columns)  # Create the DataFrame using the data and columns

# Print the DataFrame
print("Student Grades:")
print(df)


# - Dictionary of Lists:
#     - Create a DataFrame from a dictionary of lists.
#     - Each key-value pair represents a column in the DataFrame.
#     - Syntax: pd.DataFrame(data)
# Example:

import pandas as pd

# Define a dictionary containing the data
data_dict = {
                'Name': ["John", "Peter", "James", "Robert"],
                'Age': [20, 21, 25, 26],
                'City': ['Nairobi', 'Mombasa', 'Dodoma', 'Kampala'],
                'Job Title': ['Medic', 'Data Analyst', 'Nurse', 'Teacher']
            }

# Create a DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# Print the DataFrame
print(df)


# - Lists of Dictionaries:
#     - Create a DataFrame from a list of dictionaries.
#     - Each dictionary represents a row in the DataFrame.
#     - Syntax: pd.DataFrame(data)
# Example:

# Importing the pandas library
import pandas as pd

# Creating a list of dictionaries where each dictionary represents a row in the DataFrame
data_list = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Emma', 'Age': 30, 'City': 'London'},
    {'Name': 'Michael', 'Age': 35, 'City': 'Sydney'}
]

# Creating a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Printing the DataFrame
print(df)


# - Dictionary of Series:
#     - Create a DataFrame from a dictionary of Pandas Series objects.
#     - Each key-value pair represents a column in the DataFrame.
#     - Syntax: pd.DataFrame(data)
# Example:

import pandas as pd

# Create Pandas Series objects for each column
country_series = pd.Series(['Kenya', 'United States', 'Israel', 'Germany'])
capital_series = pd.Series(['Nairobi', 'Washington D.C.', 'Jerusalem', 'Berlin'])
currency_series = pd.Series(['KES', 'USD', 'ILS', 'EUR'])
continent_series = pd.Series(['Africa', 'North America', 'Asia', 'Europe'])

# Create a dictionary of Pandas Series
data_dict = {
                'Country': country_series,
                'Capital City': capital_series,
                'Currency': currency_series,
                'Continent': continent_series
            }

# Create DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# Print the DataFrame
print(df)


# Note: Replace "data" with the appropriate data source or variable name when creating a DataFrame.

# These are the basic methods to create a Pandas DataFrame structure. DataFrame provides a flexible and powerful way to work with data in a tabular format,
# enabling various data manipulation and analysis operations.
