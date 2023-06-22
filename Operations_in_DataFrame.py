# Operations in DataFrame

# 1. Column Selection
# Retrieve specific columns from a DataFrame using column labels or indices.
# Syntax: df['column_label'] or df.column_name
# Example:

import pandas as pd

# - Dictionary of Series
country_series = pd.Series(['Kenya', 'Tanzania', 'Nigeria'])
capital_series = pd.Series(['Nairobi', 'Dodoma', 'Abuja'])
mountain_series = pd.Series(['Mount Kenya', 'Mount Kilimanjaro', 'Aso Rock'])
height_series = pd.Series([5199, 5895, 400])

# Create a dictionary of Pandas Series
data_dict = {
    'Country': country_series,
    'Capital City': capital_series,
    'Highest Mountain': mountain_series,
    'Mountain Height': height_series
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# COlumn Selection: Select only one column from the DataFrame
selected_column = df['Highest Mountain']

# Print the selected column
print(selected_column)

# Column Selection: Select specific columns from the DataFrame
selected_columns = df[['Country',  'Highest Mountain']]

# Print the selected columns
print(selected_columns)


# 2. Column Addition
# Add new columns to a DataFrame or modify existing columns.
# Syntax: df['new_column'] = values or df['existing_column'] = modified_values
# Example:

import pandas as pd

# - Lists of Dictionaries
data_list = [
    {'Name': 'John', 'University': 'Harvard', 'Course': 'Computer Science'},
    {'Name': 'Emma', 'University': 'Oxford', 'Course': 'Mathematics'},
    {'Name': 'Michael', 'University': 'Stanford', 'Course': 'Physics'}
]

# Create DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Column Addition: Add new columns to the DataFrame
df['Location'] = ['Cambridge', 'Oxford', 'Palo Alto']
df['Faculty'] = ['Engineering', 'Science', 'Natural Sciences']

# Print the DataFrame
print(df)


# 3. Column Deletion
# Remove one or more columns from a DataFrame.
# Syntax: del df['column_label'] or df.drop(columns=['column_label'], inplace=True)
# Example:

import pandas as pd

# - Dictionary of Lists
data = {
    'Item': ['Bread', 'TV', 'Notebook'],
    'Category': ['Bakery', 'Electronics', 'School Supplies'],
    'Price': [2.99, 499.99, 1.99]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Column Deletion: Remove the 'Category' column from the DataFrame
df = df.drop(columns=['Category'])

# Print the DataFrame
print(df)

# 4. Row Selection
# Extract specific rows from a DataFrame based on conditions or row indices.
# Syntax: df[df['condition']] or df.loc[row_indices]
# Example:

import pandas as pd

# Create Pandas Series objects for each column
country_series = pd.Series(['Kenya', 'United States', 'Israel', 'Germany'])
capital_series = pd.Series(['Nairobi', 'Washington D.C.', 'Jerusalem', 'Berlin'])
currency_series = pd.Series(['KSH', 'USD', 'ILS', 'EUR'])
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

# Select a single row using index label
selected_row = df.loc[1]
print("Selected Row:")
print(selected_row)

# Select multiple rows using index labels
selected_rows = df.loc[[0, 2]]
print("Selected Rows:")
print(selected_rows)


# . Row Addition
# Append new rows to a DataFrame or concatenate multiple DataFrames vertically.
# Syntax: df.append(new_row) or pd.concat([df1, df2], axis=0)
# Example:

import pandas as pd

# 1. Create an empty DataFrame

df = pd.DataFrame(columns=["Programming Language", "Creator", "Year Created", "Paradigm", "Popularity", "Website", "License"])

# Add rows with information about the languages: Python, Java, JavaScript, C++
df.loc[0] = ["Python", "Guido van Rossum", 1991, "Object-oriented", "1", "python.org", "PSF License"]
df.loc[1] = ["Java", "James Gosling", 1995, "Object-oriented", "2", "java.com", "GPL License"]
df.loc[2] = ["JavaScript", "Brendan Eich", 1995, "Multi-paradigm", "4", "javascript.com", "Mozilla Public License"]
df.loc[3] = ["C++", "Bjarne Stroustrup", 1985, "Object-oriented", "3", "cplusplus.com", "GNU GPL License"]

# Add a new row containing information about the language R
df.loc[len(df)] = ["R", "Ross Ihaka and Robert Gentleman", 1993, "Multi-paradigm", "5", "r-project.org", "GNU GPL License"]

# Print the DataFrame
print(df)



# 6. Row Deletion
# Delete specific rows from a DataFrame based on conditions or row indices.
# Syntax: df.drop(index=index_value) or df.drop(df[df['condition']].index)
# Example:

import pandas as pd

# Define the list of fruit data
fruit_list = [
    ["Apple", "Red", "Sweet", "Round", "Europe", "Fall"],
    ["Banana", "Yellow", "Sweet", "Curved", "Southeast Asia", "Summer"],
    ["Orange", "Orange", "Sweet/Sour", "Round", "China", "Winter"],
    ["Grape", "Purple", "Sweet", "Round", "Italy", "Spring"],
    ["Mango", "Yellow", "Sweet", "Oval", "India", "Summer"],
    ["Strawberry", "Red", "Sweet", "Irregular", "United States", "Spring"]
]

# Define the column names
columns = ["Name", "Color", "Taste", "Shape", "Origin", "Seasons"]

# Create a DataFrame from the fruit_list using the defined columns
df = pd.DataFrame(fruit_list, columns=columns)

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Deleting a single row:
df = df.drop(1)  # Drop the row with index 1 (Banana)

# Print the DataFrame after deleting a single row
print("\nDataFrame after deleting a single row:")
print(df)

# Deleting multiple rows:
df = df.drop([0, 2, 4])  # Drop the rows with indices 0 (Apple), 2 (Orange), and 4 (Mango)

# Print the DataFrame after deleting multiple rows
print("\nDataFrame after deleting multiple rows:")
print(df)



# 7. Indexing
# Access and manipulate data in a DataFrame using index labels or row indices.
# Syntax: df.loc[row_labels] or df.iloc[row_indices] or boolean

# Example: .loc[] Method, boolean method:

import pandas as pd

# Dictionary containing information about the top 5 smartphones
smartphone_data = {
    "Apple": {
        "country_of_origin": "United States",
        "operating_system": "iOS",
        "processor": "A15 Bionic",
        "display_type": "OLED",
    },
    "Samsung": {
        "country_of_origin": "South Korea",
        "operating_system": "Android",
        "processor": "Snapdragon 8 Gen 1",
        "display_type": "AMOLED",
    },
    "Huawei": {
        "country_of_origin": "China",
        "operating_system": "HarmonyOS",
        "processor": "Kirin 9000",
        "display_type": "OLED",
    },
    "Microsoft Surface smartphones": {
        "country_of_origin": "United States",
        "operating_system": "Windows 11",
        "processor": "Intel Core i5",
        "display_type": "LCD",
    },
    "Nokia": {
        "country_of_origin": "Finland",
        "operating_system": "Android",
        "processor": "Snapdragon 8 Gen 1",
        "display_type": "OLED",
    },
}

# Create Series for each column using the provided data
name_series = pd.Series(["Apple", "Samsung", "Microsoft Surface", "Huawei", "Nokia"])
country_of_origin_series = pd.Series(["United States", "South Korea", "United States", "China", "Finland"])
processor_type_series = pd.Series(["A15 Bionic", "Snapdragon 8 Gen 1", "Intel Core i5", "Kirin 9000", "Snapdragon 8 Gen 1"])
operating_system_series = pd.Series(["iOS", "Android", "Windows 11", "HarmonyOS", "Android"])
display_type_series = pd.Series(["OLED", "AMOLED", "LCD", "OLED", "OLED"])

# Create a dictionary with column names as keys and corresponding series as values
data_dict = {
    "Name": name_series,
    "Country of Origin": country_of_origin_series,
    "Processor Type": processor_type_series,
    "Operating System": operating_system_series,
    "Display Type": display_type_series
}

# Create a DataFrame using the data dictionary
df = pd.DataFrame(data_dict)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Indexing of a specific row
print("\nIndexing of a specific row:")
print(df.loc[1])  # Access the row with index label 1

# Indexing of multiple rows
print("\nIndexing of multiple rows:")
print(df.loc[2:4])  # Access rows from index label 2 to 4 (inclusive)

# Indexing of a specific column
print("\nIndexing of a specific column:")
print(df["Name"])  # Access the "Name" column

# Indexing of multiple columns
print("\nIndexing of multiple columns:")
print(df[["Name", "Operating System"]])  # Access columns "Name" and "Operating System"

# Adding a column of prices
price_list = [250000, 200000, 170000, 150000, 120000]
df["Price"] = price_list

print("\nDataFrame after adding the 'Price' column:")
print(df)

# Accessing using boolean indexing for the phones that have prices greater than 180000
print("\nPhones with prices greater than 180000:")
print(df[df["Price"] > 180000])

# Accessing using boolean indexing for a specific row
print("\nAccessing a row using boolean indexing:")
print(df.loc[df["Name"] == "Samsung"])


# 8. Slicing
# Extract a subset of data from a DataFrame using row and column ranges.
# Syntax: df.loc[row_start:row_end, column_start:column_end] or df.iloc[row_start:row_end, column_start:column_end]

# 9. Arithmetic Operators
# Perform arithmetic operations (addition, subtraction, multiplication, division) on DataFrame columns.
# Syntax: df['result_column'] = df['column1'] + df['column2']
# Here we will discuss many Arithmwtic Operators and Arithmetic Fucntions

# Example 1: pow(x, y)
# Returns x raised to the power of y 

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'x': [2, 3], 'y': [2, 3]})

# Perform power operation on the DataFrame
df['Result'] = df['x'].pow(df['y'])

# Print the DataFrame
print(df)

# Example 2: exp(x)
# Returns the exponential value of x (e^x)

import pandas as pd
import math

# Create a DataFrame
df = pd.DataFrame({'x': [3, 6, 9]})

# Calculate the exponential value of the elements in the DataFrame
df['Result'] = df['x'].apply(math.exp)

# Print the DataFrame
print(df)

# Example 3: max(iterable)
# Returns the maximum value from an iterable
import pandas as pd

# Create a DataFrame with iterables
df = pd.DataFrame({
    'List_1': [2, 4, 6],
    'List_2': [1, 3, 5],
    'List_3': [7, 9, 11]
})

# Find the maximum value in each iterable column
max_values = df.max()

# Add a 'Result' column with the maximum values
df['Result'] = max_values.values

# Print the DataFrame
print(df)


# Example 4: min(iterable)
# Returns the minimum value from an iterable.

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'iterable': [5, 8, 2, 1, 9]})

# Find the minimum value in the DataFrame
min_num = df['iterable'].min()

# Print the minimum value
print(min_num)

# Example 5: round(x, n)
# Rounds the number x to n decimal places.


import pandas as pd

# Create Series for each column using the provided data
name_series = pd.Series(["Apple", "Samsung", "Microsoft Surface", "Huawei", "Nokia"])
country_of_origin_series = pd.Series(["United States", "South Korea", "United States", "China", "Finland"])
processor_type_series = pd.Series(["A15 Bionic", "Snapdragon 8 Gen 1", "Intel Core i5", "Kirin 9000", "Snapdragon 8 Gen 1"])
operating_system_series = pd.Series(["iOS", "Android", "Windows 11", "HarmonyOS", "Android"])
display_type_series = pd.Series(["OLED", "AMOLED", "LCD", "OLED", "OLED"])

# Create a dictionary with column names as keys and corresponding series as values
data_dict = {
    "Name": name_series,
    "Country of Origin": country_of_origin_series,
    "Processor Type": processor_type_series,
    "Operating System": operating_system_series,
    "Display Type": display_type_series
}

# Create a DataFrame using the data dictionary
df = pd.DataFrame(data_dict)

# Adding a column of prices
price_list = [25.234687, 20.984959, 17.94587, 15.76347624, 120000.576]
df["Price"] = price_list

# Round off each of the Price in the DataFrame to the nearest 2 decimal places
df["Price"] = df["Price"].round(2)

# Print the columns of Name, Processor Type, and Price rounded off
print(df[["Name", "Processor Type", "Price"]])


import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'x': [3.14159], 'n': [2]})

# Round the elements in the DataFrame to n decimal places
df['Result'] = df['x'].round(df['n'])

# Print the DataFrame
print(df)

# Example 6: sqrt(x)
# Returns the square root of x.

import pandas as pd
import math

# Create a DataFrame
df = pd.DataFrame({'x': [16]})

# Calculate the square root of the elements in the DataFrame
df['Result'] = df['x'].apply(math.sqrt)

# Print the DataFrame
print(df)


# Example 7: choice(seq)
# Returns a random element from a non-empty sequence

import pandas as pd
import random

# Create a DataFrame
df = pd.DataFrame({'iterable': [1, 3, 5, 7, 9]})

# Choose a random number from the DataFrame
random_num = random.choice(df['iterable'])

# Print the random number
print(random_num)


# Example 8: shuffle(lst)
# Shuffles the elements in a list in-place

import pandas as pd
import random

# Create a DataFrame
df = pd.DataFrame({'lst': [1, 2, 3, 4, 5]})

# Shuffle the elements in the DataFrame
df['lst'] = df['lst'].sample(frac=1).reset_index(drop=True)

# Print the shuffled DataFrame
print(df)


# Example 9: abs(x)
# Returns the absolute value of x

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'x': [-5, 2.34, -34.34]})

# Calculate the absolute value of the elements in the DataFrame
df['Result'] = df['x'].abs()

# Print the DataFrame
print(df)


# Example 10: fabs(x)
# Returns the absolute value of x as a float

import pandas as pd
import math

# Create a DataFrame
df = pd.DataFrame({'x': [-3.5, 2.8, -1.2, 4.6]})

# Calculate the absolute value of the elements in the DataFrame
df['Result'] = df['x'].apply(math.fabs)

# Print the DataFrame
print(df)


# Example 11: floor(x)
# Returns the largest integer less than or equal to x

import pandas as pd
import math

# Create a DataFrame
df = pd.DataFrame({'x': [5.8, 3.2, -2.7, 4.9]})

# Calculate the floor value of the elements in the DataFrame
df['Result'] = df['x'].apply(math.floor)

# Print the DataFrame
print(df)


# Example 12: log(x)
# Returns the natural logarithm of x

import pandas as pd
import math

# Create a DataFrame
df = pd.DataFrame({'x': [10, 100, 1000]})

# Calculate the natural logarithm of the elements in the DataFrame
df['Result'] = df['x'].apply(math.log)

# Print the DataFrame
print(df)


# Example 13: modf(x)
# Returns the fractional and integer parts of x as a tuple

import pandas as pd
import math

# Create a DataFrame
df = pd.DataFrame({'x': [4.5, -2.3, 6.8, -9.1]})

# Calculate the fractional and integer parts of the elements in the DataFrame
df[['Fractional', 'Integer']] = df['x'].apply(lambda x: pd.Series(math.modf(x)))

# Print the DataFrame
print(df)


# Example 14: Arithmetic Operators:

import pandas as pd

# Create a dictionary with the data
data = {
    "Name": ["John", "Alex"],
    "Age": [18, 15],
    "Points": [120, 150]
}

# Create a DataFrame using the data dictionary
df = pd.DataFrame(data)

# Increase the age of each person by 5
df["Age"] = df["Age"] + 5

# Increase the points of each person by 1000
df["Points"] = df["Points"] + 1000

# Print the updated DataFrame
print(df)


# Example 15: Using an Arithmetic Operator:

import pandas as pd

# Create a dictionary with the data
data = {
    "Name": ["John", "Alex"],
    "Age": [18, 15],
    "Points": [120, 150]
}

# Create a DataFrame using the data dictionary
df = pd.DataFrame(data)

# Increase the age of each person by 5
df["Age"] = df["Age"] + 5

# Increase the points of each person by 1000
df["Points"] = df["Points"] + 1000

# Print the updated DataFrame
print(df)


# 10. Comparison Operators
# Compare values in DataFrame columns and generate boolean masks.
# Syntax: df['condition_column'] = df['column'] > threshold_value

import pandas as pd

# Create two DataFrames with string values
df1 = pd.DataFrame({'Name': ['Alice', ' Felix', 'Charlie'],
                    'Age': [25, 30, 35]})

df2 = pd.DataFrame({'Name': ['Alice', 'Ryan', 'Charlie'],
                    'Age': [30, 30, 40]})

# Compare the 'Name' column of df1 and df2 for equality
name_result = df1['Name'] == df2['Name']

age_result = df1['Age'] == df2['Age']

# Add 'name_result' and 'age_result' columns to df1
df1['name_result'] = name_result
df1['age_result'] = age_result

# Print the modified df1 DataFrame
print(df1)

# 11. Aggregation
# Perform statistical operations on DataFrame columns, such as mean, sum, min, max.
# Syntax: df.mean() or df['column'].sum()

import pandas as pd

student_data = [
    ["John", 89, 76, 90, 87, 90],
    ["Victor", 96, 92, 78, 86, 90],
    ["Grace", 90, 96, 90, 87, 75],
    ["Alvin", 80, 78, 76, 60, 96]
]

columns = ["Name", "English", "Math", "Chemistry", "Programming", "Physics"]

df = pd.DataFrame(student_data, columns=columns)

print(df)

# Calculate Sum marks for each student (name)
df['Sum Marks'] = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].sum(axis=1)

# Calculate the mean for each student (name)
df['Mean Marks'] = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].mean(axis=1)

# Calculate the total marks for each subject
subject_totals = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].sum()
df.loc['Total'] = pd.Series(subject_totals, index=columns)

# Calculate the mean marks for each subject
subject_means = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].mean()
df.loc['Mean'] = pd.Series(subject_means, index=columns)

print("\nUpdated DataFrame:")
print(df)

class_sum = df.loc['Total', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']].sum()

print("\nTotal Marks for Each Subject:")
print(df.loc['Total', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']])

print("\nMean Marks for Each Subject:")
print(df.loc['Mean', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']])

print("\nSum of Marks for the Whole Class:", class_sum)



# 12. Filtering
# Filter rows based on specific criteria or conditions.
# Syntax: df[df['condition']] or df.query('condition')

import pandas as pd

student_data = [
    ["John", 89, 76, 90, 87, 90],
    ["Victor", 96, 92, 78, 86, 90],
    ["Grace", 90, 96, 90, 87, 75],
    ["Alvin", 80, 78, 76, 60, 96]
]

columns = ["Name", "English", "Math", "Chemistry", "Programming", "Physics"]

df = pd.DataFrame(student_data, columns=columns)

print(df)

# Calculate Sum marks for each student (name)
df['Sum Marks'] = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].sum(axis=1)

# Calculate the mean for each student (name)
df['Mean Marks'] = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].mean(axis=1)

# Calculate the total marks for each subject
subject_totals = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].sum()
df.loc['Total'] = pd.Series(subject_totals, index=columns)

# Calculate the mean marks for each subject
subject_means = df[['English', 'Math', 'Chemistry', 'Programming', 'Physics']].mean()
df.loc['Mean'] = pd.Series(subject_means, index=columns)

print("\nUpdated DataFrame:")
print(df)

class_sum = df.loc['Total', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']].sum()

print("\nTotal Marks for Each Subject:")
print(df.loc['Total', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']])

print("\nMean Marks for Each Subject:")
print(df.loc['Mean', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']])

print("\nSum of Marks for the Whole Class:", class_sum)

# Filter and display students with mean greater than 87
filtered_students = df[df['Mean Marks'] > 87]
print("\nStudents with Mean Marks > 87:")
print(filtered_students)

# Filter and display subjects with mean greater than 130
filtered_subjects = df.loc['Mean', ['English', 'Math', 'Chemistry', 'Programming', 'Physics']] > 130
print("\nSubjects with Mean Marks > 130:")
print(filtered_subjects)

# 13. Missing Data Handling
# Handle missing or NaN (Not a Number) values in a DataFrame, such as dropping or replacing them.
# Syntax: df.dropna() or df.fillna(value)

import pandas as pd

# Sample data with missing values
data = {
    'Name': ['John', 'Alex', 'Emily', 'James'],
    'Age': [25, 30, None, 28],
    'Score': [80, 90, 85, None]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values with prior values (forward fill)
df_filled = df.fillna(method='ffill')

print("\nDataFrame with Missing Values Filled (Forward Fill):")
print(df_filled)


# 14. Joining
# Combine multiple DataFrames based on common columns or indices.
# Syntax: pd.merge(df1, df2, on='common_column') or df1.join(df2, on='index')

import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Name': ['Alice', 'Bob', 'Charlie']})

# Create the second DataFrame
df2 = pd.DataFrame({'ID': [2, 3, 4],
                    'Age': [25, 30, 35]})

# Perform an inner join based on the 'ID' column
df_merged = pd.merge(df1, df2, on='ID', how='inner')

# Print the merged DataFrame
print(df_merged)


# 15. Sorting
# Sort DataFrame rows or columns based on specific criteria.
# Syntax: df.sort_values(by='column_label') or df.sort_index()

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35],
                   'Score': [90, 85, 95]})

# Sort the DataFrame by the 'Age' column in ascending order
df_sorted_age = df.sort_values('Age')

# Sort the DataFrame by the 'Score' column in descending order
df_sorted_score = df.sort_values('Score', ascending=False)

# Print the sorted DataFrames
print("Sorted by Age:")
print(df_sorted_age)
print("\nSorted by Score:")
print(df_sorted_score)



# These operations provide powerful tools for manipulating, analyzing, and transforming data within a DataFrame,
# facilitating data exploration and decision-making processes.
