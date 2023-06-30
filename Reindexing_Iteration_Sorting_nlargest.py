# Reindexing in Python Pandas

# Reindexing in Python Pandas refers to the process of creating a new DataFrame or Series with a different index
# It allows us to change the row labels (index) and column labels of a DataFrame or Series, either by adding new labels, reordering existing labels, or filling missing labels with appropriate values
# If new labels are introduced that did not exist in the original index, Pandas will assign NaN (Not a Number) values to the corresponding rows or columns where data is not available

# Example: Changing the order of rows or columns

import pandas as pd

# Create a Series with integer index
s = pd.Series([10, 20, 30, 40], index=[3, 1, 2, 4])

print("Original Series:")
print(s)

# Reindex the Series with a new order of index values
s_reindexed = s.reindex([1, 2, 3, 4])

print("\nReindexed Series:")
print(s_reindexed)

# Example: Changing the order of rows or columns

import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3], 
        'B': [4, 5, 6], 
        'C': [7, 8, 9]
        }
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Reindex the DataFrame columns in a new desired order
new_order = ['B', 'C', 'A']
df_reindexed = df[new_order]

print("\nReindexed DataFrame:")
print(df_reindexed)

# Iteration in Python Pandas

# Iteration in Python Pandas allows you to loop over the elements of a DataFrame or Series to perform operations or access data

# Example: Using items()

import pandas as pd

# Define the data as a dictionary
data = {
    'Name': ["Jane", "Tarzan", "James"],
    'Age': [18, 19, 22],
    'Course': ['MCS', 'CS', 'BA'],
    'Marks': [400, 450, 478],
}

# Create a DataFrame using the data dictionary
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original df:")
print(df)

# Iterate over the columns of the DataFrame
for c_n, c_data in df.items():
    # c_n represents the column name, and c_data represents the column data as a Series object
    print(f"\nc_n: {c_n}")  # Print the column name
    print(f"c_data:\n{c_data}")  # Print the column data

    # You can perform operations or analysis on each column here
    # This loop allows you to access and process each column individually

    # Example: Calculate the maximum value in the current column
    max_value = c_data.max()
    print(f"Maximum value in the column: {max_value}")

# The loop iterates over each column, allowing you to work with columns individually

# Example: Using iterrows()
import pandas as pd

# Create a dictionary with column names as keys and corresponding data as values
data = {
    'Name': ["Jane", "Tarzan", "James"],
    'Age': [18, 19, 22],
    'Subject': ['MCS', 'CS', 'BA'],
    'Grade': ['A', 'A', 'B']
}

# Create a DataFrame using the dictionary
df = pd.DataFrame(data)

print("Original df:")
print(df)

# Iterate over each row in the DataFrame
for i, row in df.iterrows():
    # Access individual values from each row using column names
    name = row['Name']
    age = row['Age']
    subject = row['Subject']
    grade = row['Grade']
    
    # Print a customized message for each row
    print(f"Hi {name}, you scored {grade} in {subject}")
    
# Example: using itertuples()

import pandas as pd

# Create a dictionary with column names as keys and corresponding data as values
data = {
    'Name': ["Jane", "Tarzan", "James"],
    'Age': [18, 19, 22],
    'Subject': ['MCS', 'CS', 'BA'],
    'Grade': ['A', 'A', 'B']
}

# Create a DataFrame using the dictionary
df = pd.DataFrame(data)

print("Original df:")
print(df)

# Iterate over each row in the DataFrame
for row in df.itertuples():
    # Access individual values from each row using attribute names
    name = row.Name
    age = row.Age
    subject = row.Subject
    grade = row.Grade
    
    # Print a customized message for each row
    print(f"Hi {name}, you scored {grade} in {subject}")

# Sorting in Python Pandas

# Sorting in pandas refers to arranging the rows or columns of a DataFrame or Series in a particular order based on specified criteria
# Sorting can be done in ascending or descending order

# Example: Uisng sort_values()

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Emily', 'Michael', 'Sarah'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [50000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

# Sort the DataFrame by 'Age' column in descending order
sorted_by_age = df.sort_values('Age', ascending=False)

print("Sorted DataFrame by Age (Descending Order):")
print(sorted_by_age)

# Sort the DataFrame by multiple columns
sorted_by_multiple_columns = df.sort_values(['Age', 'Salary'], ascending=[False, True])

print("\nSorted DataFrame by Age and Salary (Descending Order for Age, Ascending Order for Salary):")
print(sorted_by_multiple_columns)


# Example: Using sort_index()

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Emily', 'Michael', 'Sarah'],
    'Age': [25, 30, 30, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
}

df = pd.DataFrame(data, index=[2, 3, 1, 0])

print("Original DataFrame:")
print(df)

# Sort the DataFrame by index in ascending order
sorted_by_index_asc = df.sort_index()

print("\nSorted DataFrame by Index (Ascending Order):")
print(sorted_by_index_asc)

# Sort the DataFrame by index in descending order
sorted_by_index_desc = df.sort_index(ascending=False)

print("\nSorted DataFrame by Index (Descending Order):")
print(sorted_by_index_desc)


# nlargest and nsmallest

# The nlargest and nsmallest methods in pandas are used to retrieve the top n largest or smallest values from a Series or DataFrame based on a specified column or multiple columns

# Example

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Emily', 'Michael', 'Sarah'],
    'Age': [25, 30, 35, 40],
    'Score': [90, 85, 92, 88],
}

df = pd.DataFrame(data)

# Retrieve the top 2 rows with the largest 'Score'
top_scores = df.nlargest(2, 'Score')

print("Top 2 Scores:")
print(top_scores)

# Retrieve the bottom 3 rows with the smallest 'Age'
bottom_ages = df.nsmallest(3, 'Age')

print("\nBottom 3 Ages:")
print(bottom_ages)
