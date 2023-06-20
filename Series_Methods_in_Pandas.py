# Series Methods in Pandas

# Series methods in Pandas refer to the set of functions or operations that can be performed on a Pandas Series object

# 1. Head Method
# Returns the first n rows of the Series.
# Useful for quickly inspecting the beginning of the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
head_result = series.head(3)  # Returns the first 3 rows of the Series
print(head_result)

# 2. Tail Method
# Returns the last n rows of the Series.
# Useful for quickly inspecting the end of the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
tail_result = series.tail(2)  # Returns the last 2 rows of the Series
print(tail_result)

# 3. Describe Method
# Generates descriptive statistics of the Series.
# Provides count, mean, standard deviation, minimum, maximum, and quartile values.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
describe_result = series.describe()  # Returns descriptive statistics of the Series
print(describe_result)

# 4. Info Method
# Provides a concise summary of the Series.
# Includes data type, number of non-null values, and memory usage.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
info_result = series.info()  # Prints concise summary of the Series
print(info_result)

# 5. Mean Method
# Computes the arithmetic mean of the values in the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
mean_result = series.mean()  # Computes the mean of the Series
print(mean_result)

# 6. Sum Method
# Calculates the sum of all values in the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
sum_result = series.sum()  # Calculates the sum of the Series
print(sum_result)

# 7. Unique Method
# Returns an array of unique values in the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5, 1, 2, 3])
unique_result = series.unique()  # Returns unique values in the Series
print(unique_result)

# 8. Value_counts Method
# Counts the occurrences of each unique value in the Series.
# Example:'
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5, 1, 2, 3])
value_counts_result = series.value_counts()  # Returns frequency of values in the Series
print(value_counts_result)

# 9. Sort_values Method
# Sorts the Series in ascending or descending order based on its values.
# Example:
import pandas as pd
series = pd.Series([3, 1, 4, 2, 5])
sort_values_result = series.sort_values()  # Sorts the Series in ascending order
print(sort_values_result)
print("Alternatively: ")
sort_values_result = series.sort_values(ascending=False)  # Sorts the Series in descending order
print(sort_values_result)

# 10. Apply Method
# Applies a function to each element of the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
apply_result = series.apply(lambda x: x * 2)  # Applies lambda function to each element
print(apply_result)

# Alternatively:

# Apply Method
# The apply method is used to apply a function to each element of the Series and return a new Series.

import pandas as pd

# Define a list
original_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a Pandas Series from the list
original_series = pd.Series(original_list)

# Define a function that adds 5 to a value
def add_5(x):
    return x + 5

# Apply the add_5 function to each element of the original series
new_series = original_series.apply(add_5)

# Print the original series
print("Original Series:")
print(original_series)

# Print the new series with each element incremented by 5
print("New Series (after applying add_5 function):")
print(new_series)


# 11. Fillna Method
# Fills missing or NaN (null) values in the Series with a specified value or method.
# Example:
import pandas as pd
series = pd.Series([1, 2, None, 4, 5])
fillna_result = series.fillna(0)  # Fills missing values with 0
print(fillna_result)

# 12. Drop Method
# Removes specified labels from the Series.
# Example:
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
drop_result = series.drop([2, 4])  # Drops elements at index 2 and 4
print(list(drop_result))

# 13. Concat Method
# Concatenates multiple Series objects along a particular axis.
# Example:
import pandas as pd
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
concat_result = pd.concat([series1, series2])  # Concatenates series1 and series2
print(concat_result)
print(list(concat_result))
