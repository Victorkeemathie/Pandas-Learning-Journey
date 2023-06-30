# Window Functions in Python Pandas
# In Python Pandas, window functions are powerful tools for analyzing data over a specified window or interval
# They operate on a series of data points within the window and apply a specific calculation or transformation

# 1. Rolling Window:
# The rolling window function calculates a metric or statistic over a sliding window of a fixed size.
# It allows you to perform operations such as calculating moving averages, cumulative sums, or other aggregated functions on a rolling basis

import pandas as pd

# Create a DataFrame with a time series data
data = {'Date': pd.date_range(start='2022-01-01', periods=10),
        'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]}
df = pd.DataFrame(data)

# Calculate the rolling average using a window of size 3
df["rolling_avg"] = df['Value'].rolling(window=3).mean()

print(df)

# Rolling Fucntions Examples:

# E1:

import pandas as pd

data = {'Value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Custom function to calculate the sum of squares
def sum_of_squares(x):
    return sum(x**2)

# Apply the custom function to a rolling window of size 2
df['rolling_result'] = df['Value'].rolling(window=2).apply(sum_of_squares)

print(df)

# E2:

import pandas as pd

data = {'Value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Aggregate using predefined functions sum and mean in a rolling window of size 2
rolling_result = df['Value'].rolling(window=2).agg(['sum', 'mean'])

print(rolling_result)

# E3:

import pandas as pd

data = {'Value': [1, 5, 2, 7, 3]}
df = pd.DataFrame(data)

# Compute the maximum value in a rolling window of size 2
rolling_result = df['Value'].rolling(window=2).max()

print(rolling_result)


# E4:

import pandas as pd

data = {'Value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Compute the mean value in a rolling window of size 2
rolling_result = df['Value'].rolling(window=2).mean()

print(rolling_result)


# 2. Expanding Window:
# The expanding window function calculates a metric or statistic that continually expands the window size as it iterates through the data
# It includes all previous data points up to the current point and provides cumulative insights over time, such as cumulative sums or growth rates

import pandas as pd

# Create a DataFrame with sales data
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# Calculate the cumulative sales using an expanding window
cumulative_sales = df['Sales'].expanding().sum()

print(cumulative_sales)


# 3. Exponentially Weighted Window:
# The exponentially weighted window assigns weights to data points based on their proximity to the current point
# It gives more weight to recent data and less weight to older data, allowing for dynamic adjustments in the window
# It is commonly used in time series analysis, smoothing noisy data, and detecting trends
# The parameter "alpha" represents the smoothing factor or decay factor
# It determines the weight given to each data point in the calculation of the moving average
# A smaller alpha value gives more weight to recent data points, while a larger alpha value considers a broader range of historical data

import pandas as pd

# Create a DataFrame with temperature readings
data = {'Date': pd.date_range(start='2022-01-01', periods=5),
        'Temperature': [25.5, 26.0, 27.2, 26.8, 25.9]}
df = pd.DataFrame(data)

# Calculate the exponentially weighted moving average with smoothing factor 0.5
ewma = df['Temperature'].ewm(alpha=0.5).mean()

print(ewma)


# 4. Weighted Window
# The weighted window function assigns custom weights to each data point within the window
# It enables you to define the weights based on specific criteria or domain knowledge, giving more flexibility in analyzing the data
# It is useful when you want to emphasize or de-emphasize certain data points based on their importance or relevance

import pandas as pd

# Create a DataFrame with a time series data
data = {'Date': pd.date_range(start='2022-01-01', periods=10),
        'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]}
df = pd.DataFrame(data)

# Define the weights for the weighted moving average
weights = [0.1, 0.2, 0.3, 0.2, 0.1]  # Example weights summing up to 1

# Calculate the weighted moving average using a custom function
weighted_avg = df['Value'].rolling(window=len(weights)).apply(lambda x: (x * weights).sum())

print(weighted_avg)

# Ex2:

import pandas as pd

# Create a DataFrame with student scores and weights
data = {'Student': ['John', 'Jane', 'Adam', 'Emma'],
        'Score': [80, 90, 85, 95],
        'Weight': [0.2, 0.3, 0.1, 0.4]}
df = pd.DataFrame(data)

# Calculate the weighted average of scores
weighted_avg = (df['Score'] * df['Weight']).sum()

print(weighted_avg)




