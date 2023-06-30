# String Methods in Python Pandas

# 1. str.lower(): Converts all characters in a string column to lowercase

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Email': ['john@example.com', 'jane@example.com', 'adam@example.com'],
        'Phone': ['123-456-7890', '555-123-4567', '999-888-7777']}
df = pd.DataFrame(data)

# Convert 'Name' column to lowercase
df['Name'] = df['Name'].str.lower()

print(df)


# 2. str.upper(): Converts all characters in a string column to uppercase

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Email': ['john@example.com', 'jane@example.com', 'adam@example.com'],
        'Phone': ['123-456-7890', '555-123-4567', '999-888-7777']}
df = pd.DataFrame(data)

# Convert 'Name' column to uppercase
df['Name'] = df['Name'].str.upper()

print(df)

# 3. str.len(): Computes the length of each string in a string column.

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Email': ['john@example.com', 'jane@example.com', 'adam@example.com'],
        'Phone': ['123-456-7890', '555-123-4567', '999-888-7777']}
df = pd.DataFrame(data)

# Compute the length of each email in the 'Email' column
df['Email_Length'] = df['Email'].str.len()

print(df)

# 4. str.strip(): Removes leading and trailing whitespace from each string in a string column

import pandas as pd

# Create a DataFrame with string data
data = {'Name': [' John Doe ', ' Jane Smith ', ' Adam Johnson '],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print(df)

# Strip whitespace from 'Name' column
df['Name'] = df['Name'].str.strip()

print(df)

# 5. rstrip(): Removes trailing whitespace characters from the right end of a string

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe   ', 'Jane Smith   ', 'Adam Johnson   '],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Strip whitespace from the right side of 'Name' column
df['Name'] = df['Name'].str.rstrip()

print(df)

# 6. lstrip(): Removes leading whitespace characters from the left end of a string

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['   John Doe', '   Jane Smith', '   Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Strip whitespace from the left side of 'Name' column
df['Name'] = df['Name'].str.lstrip()

print(df)


# 7. title(): Converts the first character of each word in a string to uppercase and the remaining characters to lowercase, creating a title-cased string

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['john doe', 'jane smith', 'adam johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Convert 'Name' column to title case
df['Name'] = df['Name'].str.title()

print(df)

# 8. capitalize(): Converts the first character of a string to uppercase and the remaining characters to lowercase
import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['john doe', 'jane smith', 'adam johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Capitalize 'Name' column
df['Name'] = df['Name'].str.capitalize()

print(df)

# 9. swapcase(): Swaps the case of each character in a string, converting lowercase characters to uppercase and vice versa.

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Swap the case of 'Name' column
df['Name'] = df['Name'].str.swapcase()

print(df)

# 10. join(): Concatenates the elements of a string sequence using a specified separator

import pandas as pd

# Create a DataFrame with string data
data = {'Name': [['John', 'Doe'], ['Jane', 'Smith'], ['Adam', 'Johnson']],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Join the elements in the 'Name' column with a space delimiter
df['Full Name'] = df['Name'].str.join(' ')

print(df)

# 11. replace(): Replaces occurrences of a substring in a string with another specified string

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Replace 'Doe' with 'Smith' in 'Name' column
df['Name'] = df['Name'].str.replace('Doe', 'Smith')

print(df)

# 12. contains(): Checks if a substring exists in a string and returns a boolean value

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Check if 'Name' column contains 'Doe'
df['Contains Doe'] = df['Name'].str.contains('Doe')

print(df)

# 13. startswith(): Checks if a string starts with a specified substring and returns a boolean value.

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Check if 'Name' column starts with 'John'
df['Starts with John'] = df['Name'].str.startswith('John')

print(df)

# 14. endswith(): Checks if a string ends with a specified substring and returns a boolean value

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Check if 'Name' column ends with 'Johnson'
df['Ends with Johnson'] = df['Name'].str.endswith('Johnson')

print(df)

# 15. count(): Counts the occurrences of a substring in a string and returns the count as an integer

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Count the occurrences of 'n' in 'Name' column
df['Count of n'] = df['Name'].str.count('n')

print(df)

# 16. str.extract(): Extracts substrings from each string based on a specified regular expression pattern

import pandas as pd

# Create a DataFrame with string data
data = {'Name': ['John Doe', 'Jane Smith', 'Adam Johnson'],
        'Email': ['john@example.com', 'jane@example.com', 'adam@example.com'],
        'Phone': ['123-456-7890', '555-123-4567', '999-888-7777']}
df = pd.DataFrame(data)

# Extract the domain from the 'Email' column using regular expression pattern
df['Domain'] = df['Email'].str.extract(r'@(.+)')

print(df)

# 17. str.cat(): Concatenates strings in a string column with a specified separator

import pandas as pd

# Create a DataFrame
data = {
    'First Name': ['John', 'Emily', 'Michael'],
    'Last Name': ['Doe', 'Smith', 'Johnson'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

# Concatenate 'First Name' and 'Last Name' with a space separator
df['Full Name'] = df['First Name'].str.cat(df['Last Name'], sep=' ')

print(df)


