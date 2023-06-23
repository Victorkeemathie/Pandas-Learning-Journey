# Function Application

# Function Application in Pandas refers to the process of applying functions to manipulate data in a DataFrame or Series.
# It allows for efficient and flexible data transformation and analysis.

# 1. Element-wise Function Application:
# Element-wise function application applies a function to each individual element in a DataFrame or Series.
# By using built-in functions or custom functions, you can perform computations or transformations on each element independently.
# This operation is particularly useful when you need to apply specific calculations or transformations to each element of the data.
# Example:

import pandas as pd

# Create a DataFrame
data = {
    'A': [2, 4, 6, 8, 10],
    'B': [1, 3, 5, 7, 9]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Define a custom function to multiply a number by 2
def multiply_by_2(x):
    return x * 2

# Apply the multiply_by_2 function to each element of the DataFrame
df = df.applymap(multiply_by_2)
print("\nAfter Element-wise Function Application (Multiply by 2):")
print(df)

# Series Example:

import pandas as pd

# Create a Series of strings
s = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])
print("Original Series:")
print(s)

# Define a custom function to capitalize the first letter of each string
def capitalize_first_letter(x):
    return x.capitalize()

# Apply the capitalize_first_letter function to each element of the Series
s = s.apply(capitalize_first_letter)
print("\nAfter Element-wise Function Application (Capitalize First Letter):")
print(s)


# 2. Row or Column-wise Function Application:
# Row or column-wise function application applies a function along either the rows or columns of a DataFrame.
# By specifying the axis parameter as 0 (default) for column-wise or 1 for row-wise, the function is applied across the specified axis.
# This operation allows you to perform computations or transformations that involve multiple elements within each row or column.

# Example:

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Emily', 'Michael'],
    'Hours_Worked': [40, 35, 45],
    'Hourly_Rate': [20, 25, 18]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Define a custom function to calculate the total weekly salary (Hours_Worked * Hourly_Rate) for each row
def calculate_weekly_salary(row):
    return row['Hours_Worked'] * row['Hourly_Rate']

# Apply the calculate_weekly_salary function row-wise using apply() with axis=1
df['Weekly_Salary'] = df.apply(calculate_weekly_salary, axis=1)
print("\nAfter Row-wise Function Application (Weekly Salary Calculation):")
print(df)


# Example involving Series:

import pandas as pd

# Create a Series
data = ['apple', 'banana', 'cherry', 'durian']
s = pd.Series(data)
print("Original Series:")
print(s)

# Apply the str.upper() function column-wise using apply()
s_upper = s.apply(str.upper)
print("\nAfter Column-wise Function Application (Uppercase Conversion):")
print(s_upper)


# Example 2:

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Emily', 'Michael', 'Sarah'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


def capitalize(x):
    return x.upper()


# Apply the 'capitalize' function element-wise to the 'Name' and 'City' columns using 'applymap()'
df[['Name', 'City']] = df[['Name', 'City']].applymap(capitalize)


print("\nAfter Column-wise Function Application (Capitalized City Names):")
print(df)


# 3. Table-wise Function Application:
# Table-wise function application applies a function to the entire DataFrame or Series, considering the complete data structure.
# It calculates aggregate statistics or performs complex operations that involve the entire dataset.
# Examples include calculating summary statistics like mean, median, or standard deviation for the entire dataset.
# Example:

# Example:

import pandas as pd

# Create a DataFrame
data = {
    'Country': ['USA', 'Canada', 'Germany', 'France'],
    'Population': [331002651, 37742154, 83783942, 65273511],
    'GDP (USD)': [21439453, 17371243, 41588418, 30159594]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


# Define a custom function to calculate the average GDP per capita
def calculate_average_gdp_per_capita(row):
    return row['GDP (USD)'] / row['Population']


# Apply the custom function to the entire DataFrame using 'apply()' with axis=1
average_gdp_per_capita = df.apply(calculate_average_gdp_per_capita, axis=1)

print("\nAverage GDP per Capita:")
print(average_gdp_per_capita)


# Add a new column 'Avg GDP per Capita' to the DataFrame
df['Avg GDP per Capita'] = average_gdp_per_capita

print("\nUpdated DataFrame with Additional Column:")
print(df)
