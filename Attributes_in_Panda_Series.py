# Attributes in Pandas Series:

# 1: index: Returns the index labels associated with the Pandas Series
# Example:
import pandas as pd

# Creating a Pandas Series
series = pd.Series([1, 2, 3, 4, 5])

# Accessing the attributes

# index attribute
index_labels = series.index
print("Index labels:", index_labels)  # Output: Index labels: RangeIndex(start=0, stop=5, step=1)


# 2: size: Returns the number of elements in the Pandas Series
# Example:
series = pd.Series([1, 2, 3, 4, 5])

# size attribute
series_size = series.size
print("Size:", series_size)  # Output: Size: 5


# 3: dtype: Returns the data type of the values in the Pandas Series
# Example:
series = pd.Series([1, 2, 3, 4, 5])

# dtype attribute
series_dtype = series.dtype
print("Data type:", series_dtype)  # Output: Data type: int64


# 4: name: Returns the name of the Pandas Series
# Example:
series = pd.Series([1, 2, 3, 4, 5], name='MySeries')

# name attribute
series_name = series.name
print("Series name:", series_name)  # Output: Series name: MySeries


# 5: is_unique: Returns a boolean indicating whether the values in the Pandas Series are unique
# i.e if there are any repititions
# Example:
series = pd.Series([1, 2, 3, 4, 5])

# is_unique attribute
series_is_unique = series.is_unique
print("Is unique:", series_is_unique)  # Output: Is unique: True


# 6: is_monotonic_increasing: Returns a boolean indicating whether the values in the Pandas Series are monotonically increasing
# i.e Ascending Order = True, Descending Order = False
# Example:
series = pd.Series([1, 2, 3, 4, 5])

# is_monotonic_increasing attribute
series_is_monotonic_increasing = series.is_monotonic_increasing
print("Is monotonic increasing:", series_is_monotonic_increasing)  # Output: Is monotonic increasing: True


# 7: is_monotonic_decreasing: Returns a boolean indicating whether the values in the Pandas Series are monotonically decreasing
# Example:
series = pd.Series([5, 4, 3, 2, 1])

# is_monotonic_decreasing attribute
series_is_monotonic_decreasing = series.is_monotonic_decreasing
print("Is monotonic decreasing:", series_is_monotonic_decreasing)  # Output: Is monotonic decreasing: True
