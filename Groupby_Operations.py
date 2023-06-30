# Groupby Operations in Python Pandas

# 1. groupby
# In Python Pandas, the groupby method is used to group data based on one or more columns in a DataFrame
# It creates a GroupBy object that allows performing various operations on grouped data

import pandas as pd

data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Grouping the DataFrame by 'Category'
grouped = df.groupby('Category')

print(grouped.groups)

import pandas as pd

# Create a dictionary with the data
data = {
    'Name': ['Jane', 'Janet', 'Ali', 'John'],
    'Class': ['North', 'South', 'North', 'South'],
    'Marks': [400, 390, 370, 430],
    'Grade': ['A', 'B', 'B', 'A']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Grouping the DataFrame by 'Class' and 'Grade'
grouped = df.groupby(['Class', 'Grade'])

# Calculating the mean of 'Marks' for each group
df_grouped = grouped['Marks'].mean()

# Printing the result
print(df_grouped)


# Aggregation on groupby in Pandas involves applying a summary function, such as mean, sum, count, etc., to groups of data.
# It calculates a single value for each group, resulting in a reduced dataset.


import pandas as pd

# Create a dictionary with the data
data = {'Category': ['A', 'A', 'B', 'B', 'B', 'A', 'C', 'A', 'C', 'C', 'C'],
        'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 70]}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Grouping the DataFrame by 'Category' and aggregating the sum, mean, min, and max of 'Value'
grouped = df.groupby('Category')

# Aggregating the data using predefined functions
aggregated_data = grouped.agg({
    'Value': ['sum', 'mean', 'min', 'max']
})

# Printing the aggregated results
print(aggregated_data)


# Transformation on groupby in Pandas involves applying a function to each group separately and returning a modified version of the original data.
# It retains the original shape of the DataFrame but may contain modified values based on the transformation function

import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B', 'B'],
        'Value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Transforming the 'Value' column by scaling it within each group
transformed = df.groupby('Category')['Value'].transform(lambda x: x**2)

print(transformed)

# Ex 2:

import pandas as pd

# Create a DataFrame with 'Group' and 'Value' columns
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B'],
    'Value': [10, 15, 20, 25, 30]
})

# Calculate the mean value for each group using transform
mean_values = df.groupby('Group')['Value'].transform('mean')

# Print the calculated mean values
print(mean_values)

# Filter the DataFrame based on the condition where 'Value' is less than mean_values
df_filtered = df[df['Value'] < mean_values]

# Print the filtered DataFrame
print(df_filtered)


# Filteration in Pandas involves selecting subsets of data based on specific conditions.
# It allows filtering rows or columns based on criteria such as values, conditions, or logical expressions


import pandas as pd

# Create a DataFrame with 'Group' and 'Value' columns
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B'],
    'Value': [10, 15, 20, 25, 30]
})

# Define a custom filter function
def filter_condition(group):
    # Calculate the mean value for the 'Value' column of the group
    mean_value = group['Value'].mean()
    
    # Print the mean value
    print(mean_value)
    
    # Return True if the mean value is greater than 10, False otherwise
    return mean_value > 10

# Apply the filter function to each group in the DataFrame and keep only the groups satisfying the condition
filtered_df = df.groupby('Group').filter(filter_condition)

# Print the filtered DataFrame
print(filtered_df)
