# Customization Options in Python Pandas
# In Python Pandas, there are several customization options available to tailor the display and behavior of DataFrames and Series


# Customizing Display Options
# These options can be set globally using pd.set_option()

# Changing the font size and color:

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Adam', 'Emma', 'Michael'],
        'Age': [25, 30, 35, 28, 32],
        'Country': ['USA', 'Canada', 'UK', 'Australia', 'Germany'],
        'Score': [80, 90, 85, 95, 87],
        'Grade': ['A', 'A', 'B', 'A', 'B']}
df = pd.DataFrame(data)

# Example: Changing the font size
styled_df = df.style.set_properties(subset=df.columns, **{'font-size': '12pt'})

# Example: Changing the font color
styled_df = styled_df.set_properties(subset=df.columns, **{'color': 'blue'})

# Display the styled DataFrame
styled_df


# Adjusting the column width or row height

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Adam'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Example: Adjusting column width or row height
styled_df = df.style.set_table_styles([{'selector': 'th', 'props': [('max-width', '50px')]}])

# Display the styled DataFrame
styled_df


# Setting decimal precision:

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Adam'],
        'Age': [25.12345, 30.6789, 35.0]}
df = pd.DataFrame(data)

# Example: Setting decimal precision
styled_df = df.style.format({'Age': '{:.2f}'})

# Display the styled DataFrame
styled_df

# Adding or removing gridlines

import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Adam'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Example: Adding or removing gridlines
styled_df = df.style.set_properties(**{'border': '1px solid black'})

# Display the styled DataFrame
styled_df


# 2: Customizing Data Types
# Pandas allows users to customize the data types of columns in DataFrames, enabling efficient storage and manipulation of data

import pandas as pd

# Create a DataFrame with mixed data types
data = {'Name': ['John', 'Jane', 'Adam'],
        'Age': [25, 30, 35],
        'Salary': ['1000', '2000', '3000']}
df = pd.DataFrame(data)

# Convert the 'Salary' column to integer data type
df['Salary'] = df['Salary'].astype(int)

print(df.dtypes)

# 3. Customizing Data Cleaning and Manipulation
# Pandas offers a wide range of methods and functions to customize data cleaning and manipulation operations
# Explore these methods on https://github.com/Victorkeemathie/Pandas-Learning-Journey/


