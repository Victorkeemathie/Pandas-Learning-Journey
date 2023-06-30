# Visualization in Pandas Python
# Pandas provides various tools for data visualization, allowing users to explore and analyze their data visually

# 1. Line plot
# A line plot, also known as a line chart, is used to display the relationship between two continuous variables over a continuous interval or time
#  It is useful for visualizing trends, patterns, and changes in data
# Example:

import pandas as pd
import matplotlib.pyplot as plt

# Prior data
data = {'x' : range(1,6),
        'y': [10, 15, 7, 12, 9]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a line plot
df.plot(x='x', y='y', kind= 'line')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# Display the plot
plt.show()


# 2. Bar plot
# A bar plot, or bar chart, is used to represent categorical data using rectangular bars.
# It displays the distribution or comparison of values across different categories
# Bar plots are effective for visualizing frequencies, counts, or aggregated values of discrete variables
# Example:

import pandas as pd
import matplotlib.pyplot as plt

# Prior data
data = {'Categories': ['A', 'B', 'C', 'D'],
        'Values': [15, 10, 12, 8]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
df.plot(x='Categories', y='Values', kind='bar')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')

# Display the plot
plt.show()


# 3. Scatter plot:
# A scatter plot is used to visualize the relationship between two continuous variables.
# Each data point is represented as a point on the graph, and the position of the point corresponds to the values of the variables
# Scatter plots are helpful in identifying patterns, correlations, or clusters in the data
# Example:

import pandas as pd
import matplotlib.pyplot as plt

# Prior data
data = {'x': [1, 2, 3, 4, 5],
        'y': [10, 15, 7, 12, 9]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
df.plot(x='x', y='y', kind='scatter')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()


# 4. Box plot:
# A box plot, also known as a box-and-whisker plot, is used to display the distribution of a continuous variable.
# It provides a visual summary of the minimum, first quartile, median, third quartile, and maximum values
# Box plots are useful for comparing distributions and identifying outliers
# Example:

import pandas as pd
import matplotlib.pyplot as plt

# Prior data
data = {'Values': [30, 25, 27, 32, 28, 35, 20]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot
df.plot(kind='box')

# Add labels and title
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Box Plot')

# Display the plot
plt.show()

# 5. Area plot:
# An area plot, or area chart, is used to represent the cumulative totals or proportions of different categories over a continuous interval
# It visualizes the contribution of each category to the whole
# It visualizes the contribution of each category to the whole
# Example:

import pandas as pd
import matplotlib.pyplot as plt

# Prior data
data = {'x': [1, 2, 3, 4, 5],
        'y': [10, 15, 7, 12, 9]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create an area plot
df.plot(x='x', y='y', kind='area', color = 'green')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot')

# Display the plot
plt.show()

# 6. Density plot:
# A density plot, or kernel density plot, is used to estimate the probability density function of a continuous variable.
# It provides a smooth curve that represents the distribution of the data. 
# Density plots are useful for visualizing the shape, skewness, and multimodality of the data distribution
# Example:

import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with random data
data = pd.DataFrame({'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# Create a density plot using Pandas
data.plot(kind='density')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Plot')

# Display the plot
plt.show()




