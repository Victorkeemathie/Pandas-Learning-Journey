# Pandas - Operations on Series

# Indexing
# - Access elements of a Series using labels or positions.
# - Label-based indexing: `series[label]` or `.loc[label]`.
# - Position-based indexing: `.iloc[position]`.
# - Boolean indexing: Apply a boolean mask to filter elements.
# Example 1 : Using .loc[] method:
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])

# Accessing a specific item
specific_item = series.loc['B']
print("Label-based indexing - Example 1:")
print("Specific item using .loc['B']:", specific_item)

# Accessing multiple items
multiple_items = series.loc[['A', 'C', 'E']]
print("\nLabel-based indexing - Example 1:")
print("Multiple items using .loc[['A', 'C', 'E']]:")
print(multiple_items)

# Accessing a range of items
range_of_items = series.loc['B':'D']
print("\nLabel-based indexing - Example 1:")
print("Range of items using .loc['B':'D']:")
print(range_of_items)

# Example 2:  Using the .iloc[] method:

import pandas as pd

# Create a Series
series = pd.Series(['Red', 'Green', 'Blue', 'Yellow', 'Orange'], index=[3, 0, 2, 4, 1])

# Accessing a specific item
specific_item = series.iloc[2]
print("Position-based indexing - Example 2:")
print("Specific item using .iloc[2]:", specific_item)

# Accessing multiple items
multiple_items = series.iloc[[1, 3, 4]]
print("\nPosition-based indexing - Example 2:")
print("Multiple items using .iloc[[1, 3, 4]]:")
print(multiple_items)

# Accessing a range of items
range_of_items = series.iloc[0:3]
print("\nPosition-based indexing - Example 2:")
print("Range of items using .iloc[0:3]:")
print(range_of_items)

# Example 3: Using Boolean Indexing:

import pandas as pd

# Create a dictionary of countries and their populations
data = {'USA': 331449281, 'UK': 67886004, 'France': 65480710, 'Germany': 83149300, 'Japan': 126476461}

# Convert the dictionary into a Series
series = pd.Series(data)

# Boolean indexing to get the countries with population greater than 80 million
countries_greater_than_80m = series[series > 80000000]
print("Countries with population greater than 80 million:")
print(countries_greater_than_80m)

# Boolean indexing to get the countries with population less than 70 million
countries_less_than_70m = series[series < 70000000]
print("Countries with population less than 70 million:")
print(countries_less_than_70m)

# Boolean indexing to get the countries with population between 65 million and 85 million
countries_between_65m_and_85m = series[(series >= 65000000) & (series <= 85000000)]
print("Countries with population between 65 million and 85 million:")
print(countries_between_65m_and_85m)

# Boolean indexing to get the countries with population equal to 126476461
countries_with_population_126m = series[series == 126476461]
print("Countries with population equal to 126,476,461:")
print(countries_with_population_126m)

# Slicing
# - Slice a Series using labels or positions.
# - Label-based slicing: `series[start_label:end_label]` or `.loc[start_label:end_label]`.
# - Position-based slicing: `.iloc[start_position:end_position]`.

# Example 1: Using the [start_label:end_label]

import pandas as pd

# Set of capital cities in Africa
capital_cities = {'Cairo', 'Lagos', 'Nairobi', 'Accra', 'Addis Ababa', 'Dakar', 'Rabat'}

# Convert the set to a list
capital_cities_list = list(capital_cities)

# Create a Series
series = pd.Series(capital_cities_list)

# Slice the Series using labels
slice_labels = series[2:5]

print(slice_labels)

# Example 2: Using the .iloc Method:

import pandas as pd

# Dictionary of special dishes in Japan with prices in Japanese Yen
special_dishes = {
    'Sushi': 5000,
    'Takoyaki': 1500,
    'Kaiseki': 10000,
    'Okonomiyaki': 2000,
    'Hitsumabushi': 3500,
    'Hakata Ramen': 1800,
    'Genghis Khan': 4000,
    'Soki Soba': 2500
}

# Convert prices from Japanese Yen to Kenyan Shillings
special_dishes = {dish: price * 1.5 for (dish, price) in special_dishes.items()}

# Create a Series from the dictionary
series = pd.Series(special_dishes)

# Slice the Series using positions
slice_positions = series.iloc[1:4]

print(slice_positions)

# Example 3: Using the .loc[start_label:end_label] method: 

import pandas as pd

# Tuple of popular tourist attractions in Australia
tourist_attractions = (
    'Sydney Opera House',
    'Great Barrier Reef',
    'Uluru-Kata Tjuta National Park',
    'Bondi Beach',
    'Great Ocean Road',
    'Kangaroo Island',
    'Blue Mountains National Park',
    'Daintree Rainforest',
    'Purnululu National Park'
)

# Create a Series from the tuple
series = pd.Series(tourist_attractions)

# Set the index labels using range of length of series
series.index = range(len(series))  # Assigning index labels as [0, 1, 2, ..., n-1]

# Slice the Series using labels
slice_labels = series.loc[3:]  # Slicing from index 1 to 5 (inclusive)

print(slice_labels)




# Arithmetic Operations
# - Perform arithmetic operations on Series.
# - Common operations: addition `+`, subtraction `-`, multiplication `*`, division `/`.
# - Series can also be combined with scalar values or other Series.

# The following are some of the examples of the Pandas Series Arithmetic Functions and Operations we will do:

# Example 1: pow(x, y)
# Returns x raised to the power of y.

import pandas as pd

# Create a Series
series = pd.Series([2, 3])

# Perform power operation on the Series
result = series.pow(3)

# Print the result
print(result)


# Example 2: exp(x)
# Returns the exponential value of x (e^x).

import pandas as pd
import math

# Create a Series
series = pd.Series([2])

# Calculate the exponential value of the elements in the Series
result = series.apply(math.exp)

# Print the result
print(result)


# Example 3: max(iterable)
# Returns the maximum value from an iterable.

import pandas as pd

# Create a Series
series = pd.Series([5, 8, 2, 1, 9])

# Find the maximum value in the Series
max_num = series.max()

# Print the maximum value
print(max_num)


# Example 4: min(iterable)
# Returns the minimum value from an iterable.

import pandas as pd

# Create a Series
series = pd.Series([5, 8, 2, 1, 9])

# Find the minimum value in the Series
min_num = series.min()

# Print the minimum value
print(min_num)


# Example 5: round(x, n)
# Rounds the number x to n decimal places.

import pandas as pd

# Create a Series
series = pd.Series([3.14159])

# Round the elements in the Series to 2 decimal places
result = series.round(2)

# Print the result
print(result)



# Example 6: sqrt(x)
# Returns the square root of x.

import pandas as pd
import math

# Create a Series
series = pd.Series([16])

# Calculate the square root of the elements in the Series
result = series.apply(math.sqrt)

# Print the result
print(result)


# Example 7: choice(seq)
# Returns a random element from a non-empty sequence.

import pandas as pd
import random

# Create a Series
series = pd.Series(['red', 'blue', 'green'])

# Choose a random color from the Series
chosen_color = random.choice(series)

# Print the chosen color
print(chosen_color)


# Example 8: randrange(start, stop[, step])
# Returns a randomly selected element from the range(start, stop, step).

import pandas as pd
import random

# Create a Series
series = pd.Series([1, 3, 5, 7, 9])

# Choose a random odd number between 1 and 10 (exclusive)
num = random.randrange(series.min(), series.max(), 2)

# Print the random number
print(num)


# Example 9: random()
# Returns a random floating-point number between 0 and 1.

import pandas as pd
import random

# Generate a random number between 0 and 1
num = random.random()

# Print the random number
print(num)


# Example 10: shuffle(lst)
# Shuffles the elements in a list in-place.

import pandas as pd
import random

# Create a Series
series = pd.Series([1, 2, 3, 4, 5])

# Shuffle the elements in the Series
series = series.sample(frac=1).reset_index(drop=True)

# Print the shuffled Series
print(series)


# Example 11: abs(x)
# Returns the absolute value of x.

import pandas as pd

# Create a Series
series = pd.Series([-5, 2.34, -34.34])

# Calculate the absolute value of the elements in the Series
result = series.abs()

# Print the result
print(result)


# Example 12: ceil(x)
# Returns the smallest integer greater than or equal to x.

import pandas as pd
import math

# Create a Series
series = pd.Series([3.2, 5.8, -2.7, 4.9])

# Calculate the ceil value of the elements in the Series
result = series.apply(math.ceil)

# Print the result
print(result)


# Example 13: fabs(x)
# Returns the absolute value of x as a float.

import pandas as pd
import math

# Create a Series
series = pd.Series([-3.5, 2.8, -1.2, 4.6])

# Calculate the absolute value of the elements in the Series
result = series.apply(math.fabs)

# Print the result
print(result)


# Example 14: floor(x)
# Returns the largest integer less than or equal to x.

import pandas as pd
import math

# Create a Series
series = pd.Series([5.8, 3.2, -2.7, 4.9])

# Calculate the floor value of the elements in the Series
result = series.apply(math.floor)

# Print the result
print(result)

# Example 15: log(x)
# Returns the natural logarithm of x.

import pandas as pd
import math

# Create a Series
series = pd.Series([10, 100, 1000])

# Calculate the natural logarithm of the elements in the Series
result = series.apply(math.log)

# Print the result
print(result)


# Example 16: log10(x)
# Returns the base-10 logarithm of x.

import pandas as pd
import math

# Create a Series
series = pd.Series([10, 100, 1000])

# Calculate the base-10 logarithm of the elements in the Series
result = series.apply(math.log10)

# Print the result
print(result)

# Example 17: modf(x)
# Returns the fractional and integer parts of x as a tuple.

import pandas as pd
import math

# Create a Series
series = pd.Series([4.5, -2.3, 6.8, -9.1])

# Calculate the fractional and integer parts of the elements in the Series
result = series.apply(math.modf)

# Print the result
print(result)

# Example 18: uniform(x, y)
# Returns a random floating-point number between x and y.

import pandas as pd
import random

# Create a Series
series = pd.Series([1, 2, 3, 4, 5])

# Generate a random floating-point number between 1 and 5 for each element in the Series
result = series.apply(lambda x: random.uniform(x, x + 1))

# Print the result
print(result)





# Comparison Operations
# - Compare elements of Series and create boolean Series.
# - Common operations: equality `==`, inequality `!=`, greater than `>`, less than `<`, etc.

# Example 1: Using the == Operator:
import pandas as pd

# Create two Series
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([1, 2, 6, 4, 5])

# Compare the two Series for equality
result = series1 == series2

# Print the result
print(result)

# Example 2: Using the != Operator:

import pandas as pd

# Create two tuples
tuple_1 = ('apple', 'passion', 'mango', 'banana', 'orange', 'strawberry')
tuple_2 = ('banana', 'passion', 'mango', 'kiwi', 'grape', 'watermelon')

# Create Series from the tuples
series1 = pd.Series(tuple_1)
series2 = pd.Series(tuple_2)

# Compare the two Series for inequality
result = series1 != series2

# Print the result
print(result)


# Example 3: Using the >= symbol:
import pandas as pd

# Create two dictionaries with column-wise data
dict1 = {
    'Lake District': 20,
    'Peak District': 15,
    'Snowdonia': 18,
    'Yorkshire Dales': 12
}

dict2 = {
    'Peak District': 16,
    'Brecon Beacons': 14,
    'Lake District': 22,
    'Cairngorms': 20
}

# Convert the dictionaries into Pandas Series
series1 = pd.Series(dict1)
series2 = pd.Series(dict2)

# Convert the entry fees from Euros to KSH using dictionary comprehension
series1_ksh = pd.Series({park: value * 150 for park, value in dict1.items()})
series2_ksh = pd.Series({park: value * 150 for park, value in dict2.items()})

# Align the Series based on their indexes
series1_ksh, series2_ksh = series1_ksh.align(series2_ksh, fill_value=0)

# Compare the entry fees of the two Series for greater than or equal to
result = series1_ksh >= series2_ksh

# Print the result
for park, value in result.items():
    print(f"{park}: {value}")


# Aggregation
# - Perform aggregation operations on a Series.
# - Common operations: sum `sum()`, mean `mean()`, median `median()`, maximum `max()`, minimum `min()`, etc.

# Example 1:
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40, 50])

# Compute the sum of the series
sum_result = series.sum()

# Print the sum result
print("Sum:", sum_result)

# Example 2:
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40, 50])

# Compute the mean (average) of the series
mean_result = series.mean()

# Print the mean result
print("Mean:", mean_result)

# Example 3:
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40, 50])

# Compute the median of the series
median_result = series.median()

# Print the median result
print("Median:", median_result)
        

# Filtering
# - Filter elements of a Series based on certain conditions.
# - Create a boolean mask using comparison operations.
# - Apply the boolean mask to the Series using boolean indexing.

# Example:

import pandas as pd

# Dictionary of the highest mountains in Africa and their heights in meters
mountains_africa = {
    'Mount Kilimanjaro': 5895,
    'Mount Kenya': 5199,
    'Ras Dashen': 4620,
    'Mount Stanley': 5109,
    'Mount Meru': 4562,
    'Mount Karisimbi': 4507,
    'Mount Speke': 4890,
    'Mount Elgon': 4321
}

# Extract the values from the dictionary
heights = list(mountains_africa.values())

# Print the list of heights
print(heights)

# Create a Pandas Series from the list
series1 = pd.Series(heights)

# Check which heights are greater than 5000
top = series1 > 5000

# Create a new list with the heights greater than 5000
top_heights = series1[top]

# Print the list of heights greater than 5000
print(top_heights)

