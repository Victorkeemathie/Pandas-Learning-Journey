# I/O Tools in Pandas Python:

# 1. Reading & Writing CSV:
# Pandas provides functions to read and write CSV (Comma-Separated Values) files.
# The pd.read_csv() function is used to read CSV files into a DataFrame.
# The df.to_csv() function is used to write a DataFrame to a CSV file
# Example:

import pandas as pd

# Read CSV file from the specified location
df = pd.read_csv('G:/Pandas/sample_data.csv')

# Display the DataFrame
print(df)

# Example 2:

import pandas as pd

# Create a DataFrame
data = {'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Write DataFrame to CSV file at the specified location
df.to_csv('G:/Pandas/output.csv', index=False)


# 2. Reading & Writing Excel:
# Pandas supports reading and writing Excel files.
# The pd.read_excel() function is used to read Excel files into a DataFrame.
# The df.to_excel() function is used to write a DataFrame to an Excel file
# Example:

import pandas as pd

# Read Excel file from the specified location and sheet name
df = pd.read_excel('G:/Pandas/sample_data.xlsx', sheet_name='Sheet1')

# Display the DataFrame
print(df)

# Example 4:

import pandas as pd

# Create a DataFrame
data = {'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Write DataFrame to Excel file at the specified location with sheet name
df.to_excel('G:/Pandas/output.xlsx', sheet_name='Sheet1', index=False)


# Example:

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Alice', 'Bob'],
        'Age': [25, 28, 30, 35],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Create an Excel writer object
writer = pd.ExcelWriter('G:/Pandas/output.xlsx', engine='openpyxl')

# Write the DataFrame to the Excel file
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Save the Excel file
writer._save()

# Reading & Writing JSON:
# Pandas allows reading and writing data in JSON (JavaScript Object Notation) format.
# The pd.read_json() function is used to read JSON data into a DataFrame.
# The df.to_json() function is used to write a DataFrame to a JSON file
# Example:

import pandas as pd

# Read JSON file from the specified location
df = pd.read_json('G:/Pandas/sample_data.json')

# Display the DataFrame
print(df)


# Example 6:

import pandas as pd

# Create a DataFrame
data = {'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Write DataFrame to JSON file at the specified location
df.to_json('G:/Pandas/output.json', orient='records')

# Read: usecols, set_index
