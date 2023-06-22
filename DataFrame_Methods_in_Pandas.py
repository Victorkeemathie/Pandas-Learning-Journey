# DataFrame Methods

# 1. Head: Returns the first n rows of the DataFrame, where n is the specified number (default is 5).
# It allows quick inspection of the DataFrame's data.
# Example:

import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Emma', 'Alex', 'Olivia', 'Michael'], 'Age': [25, 30, 28, 32, 27]})
head_data = df.head(3)
print("\nHead:")
print(head_data)



# 2. Tail: Returns the last n rows of the DataFrame, where n is the specified number (default is 5).
# It is useful to check the end of the DataFrame.
# Example:

import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Emma', 'Alex', 'Olivia', 'Michael'], 'Age': [25, 30, 28, 32, 27]})
tail_data = df.tail(2)
print("\nTail:")
print(tail_data)


# 3. Describe: Generates descriptive statistics of the DataFrame, including count, mean, std, min, 25%, 50%, 75%, and max.
# It provides insights into the distribution of numerical data.
# Example:

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6]})
describe_data = df.describe()
print("\nDescribe:")
print(describe_data)

# 4. Info: Prints a concise summary of the DataFrame, including the index dtype, column names, non-null values, and data types.
# It helps in understanding the DataFrame's structure and identifying missing values.
# Example:
# 4. Info
import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Emma', 'Alex', 'Olivia', 'Michael'], 'Age': [25, 30, 28, 32, 27]})
info_data = df.info()
print("\nInfo:")
print(info_data)


# 5. Groupby: Groups the DataFrame by specified columns and allows performing aggregation operations on the grouped data.
# It enables data exploration and analysis based on different groups.
# Example:

import pandas as pd

df = pd.DataFrame({'Category': ['Fruit', 'Fruit', 'Vegetable', 'Vegetable'],
                   'Item': ['Apple', 'Banana', 'Carrot', 'Broccoli'],
                   'Price': [1.2, 0.8, 0.5, 0.9]})
grouped_data = df.groupby('Category').sum()
print("\nGroupby:")
print(grouped_data)

# 6. Sort_values: Sorts the DataFrame based on one or more columns, either in ascending or descending order.
# It helps in organizing the data in a desired order for analysis or presentation.
# Example:

import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Emma', 'Alex', 'Olivia', 'Michael'],
                   'Age': [25, 30, 28, 32, 27]})
sorted_data = df.sort_values(by='Age', ascending=False)
print("\nSort_values:")
print(sorted_data)

# 7. Dropna: Removes rows or columns with missing values (NaN).
# It is used to clean the data by eliminating missing data points.
# Example:

import pandas as pd

df = pd.DataFrame({'A': [1, 2, None, 4, 5], 'B': ['Apple', 'Banana', None, 'Mango', 'Grapes']})
dropped_data = df.dropna()
print("\nDropna:")
print(dropped_data)

# 8. Fillna: Fills the missing values (NaN) in the DataFrame with a specified value or using interpolation methods.
# It helps in handling missing data by providing substitute values.
# Example:

import pandas as pd

df = pd.DataFrame({'A': [1, 2, None, 4, 5], 'B': ['Apple', 'Banana', None, 'Mango', 'Grapes']})
filled_data = df.fillna('Unknown')
print("\nFillna:")
print(filled_data)

# 9. Pivot_table: Creates a spreadsheet-style pivot table based on the DataFrame, allowing summarization and analysis of data from multiple dimensions.
# It provides a compact representation of data in a tabular format.
# Example:

import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Emma', 'John', 'Emma', 'John'],
                   'Subject': ['Math', 'Math', 'Science', 'Science', 'Math'],
                   'Score': [80, 85, 90, 92, 88]})
pivot_data = df.pivot_table(values='Score', index='Name', columns='Subject', aggfunc='mean')
print("\nPivot_table:")
print(pivot_data)

# 10. Merge: Combines multiple DataFrames into a single DataFrame based on common columns.
# It allows joining data from different sources based on specified keys, enabling data integration.
# Example:

import pandas as pd

left_df = pd.DataFrame({'Name': ['John', 'Emma', 'Alex'],
                        'Age': [25, 30, 28],
                        'City': ['New York', 'London', 'Paris']})
right_df = pd.DataFrame({'Name': ['Emma', 'Alex', 'Michael'],
                         'Salary': [5000, 6000, 7000],
                         'City': ['London', 'Paris', 'Sydney']})
merged_data = pd.merge(left_df, right_df, on='Name')
print("\nMerge:")
print(merged_data)



# 11. Apply: Applies a function along either axis of the DataFrame.
# It allows custom operations to be performed on the DataFrame's data, providing flexibility in data transformation and manipulation.
# Example:

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
squared_data = df['A'].apply(lambda x: x ** 2)
print("\nApply:")
print(squared_data)

