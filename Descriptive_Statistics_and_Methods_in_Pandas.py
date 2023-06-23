# Descriptive Statistics Notes

# Statistics refers to the mathematical techniques and methodologies used to analyze and interpret data
# It encompasses the collection, organization, and analysis of data to derive meaningful insights and make informed decisions 

# Data Set refers to a structured collection of data organized into rows and columns. 
# It represents a tabular or spreadsheet-like format where each row typically represents a specific observation or record, while columns represent different variables or attributes associated with those observations

# Descriptive Statistics is a branch of statistics that focuses on summarizing and describing the main characteristics and properties of a dataset. 

# 1. count
# Count is a descriptive statistic that calculates the number of non-null values in each column of a DataFrame.
# It helps to identify missing or incomplete data in the dataset.
# Example: 
import pandas as pd

data_count = pd.DataFrame({'A': [1, 2, 3, None, 5],
                           'B': [6, None, 8, 9, 10],
                           'C': [11, 12, 13, 14, None]})
count = data_count.count()


print("\nCount:")
print(count)


# 2. mean
# Mean is a measure of central tendency that calculates the average value of numerical data in a DataFrame column.
# It is obtained by summing all the values and dividing by the total number of observations.
# Example:


# 3. median
# Median is a measure of central tendency that calculates the middle value in a sorted list of numerical data.
# It represents the central value and is less affected by outliers compared to the mean.
# Example:

# 4. min and max
# Min and Max are descriptive statistics that return the minimum and maximum values, respectively, in a DataFrame column.
# They help identify the range of values present in the data.

# Example:

import random
import pandas as pd

# Initialize an empty dictionary
student_data = {}

# List of student names
students = ["John", "Emily", "Michael", "Sarah", "David", "Emma"]

# List of subject names
subjects = ["Mathematics for Data Science", "Statistics and Probability", "Programming in Python", 
            "Data Analysis and Visualization", "Machine Learning", "Big Data Analytics"]

# Iterate over each student
for student in students:
    # Initialize an empty dictionary for each student
    student_marks = {}
    
    # Iterate over each subject
    for subject in subjects:
        # Generate a random mark between 45 and 100
        marks = random.randint(45, 100)
        
        # Store subject marks in the student's dictionary
        student_marks[subject] = marks
    
    # Store student's data in the main dictionary
    student_data[student] = student_marks

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(student_data, orient='index')

print(df)
# Calculate descriptive statistics for each student
for student in students:
    print(f"\nDescriptive statistics for {student}:")
    print(f"Mean:\n{df.loc[student].mean()}")
    print(f"Median:\n{df.loc[student].median()}")
    print(f"Min:\n{df.loc[student].min()}")
    print(f"Max:\n{df.loc[student].max()}")
   
   
   
# 5. quantile(q)
# Quantile is a descriptive statistic that calculates the specified percentile (q) of numerical data in a DataFrame column.
# It provides insights into the data distribution and can be used to identify outliers.

import pandas as pd

# Create a DataFrame
data_quantile = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Calculate the 25th percentile (quantile) of the data
quantile_25 = data_quantile.quantile(q=0.25)


# 6. var
# Variance is a descriptive statistic that calculates the variability or spread of numerical data in a DataFrame column.
# It measures the average squared deviation from the mean and indicates how much the data points differ from the mean.

import pandas as pd

# Create a DataFrame
data_var = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Calculate the variance of the data
variance = data_var.var()

# Print the result
print("\nVariance:")
print(variance)


# 7. std
# Standard deviation is a descriptive statistic that calculates the square root of the variance.
# It indicates the average amount of variation or dispersion from the mean and provides a measure of data volatility.

import pandas as pd

# Create a DataFrame 
data_std = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Calculate the standard deviation of the data
std_deviation = data_std.std()

# Print the result
print("\nStandard Deviation:")
print(std_deviation)

# 8. corr
# Correlation is a descriptive statistic that measures the strength and direction of the linear relationship between pairs of numerical columns in a DataFrame.
# It ranges from -1 to 1, where -1 indicates a strong negative correlation, 0 indicates no correlation, and 1 indicates a strong positive correlation.


# Create a DataFrame
data_corr = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                          'B': [6, 7, 8, 9, 10]})

# Calculate the correlation between columns 'A' and 'B'
correlation = data_corr.corr()

# Print the result
print("\nCorrelation:")
print(correlation)


# 9. COV
# Covariance is a descriptive statistic that measures the degree to which two numerical columns in a DataFrame vary together.
# It provides insights into the direction of the relationship between variables and whether they move in the same or opposite directions.

import pandas as pd

# Create a DataFrame 
data_cov = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                         'B': [6, 7, 8, 9, 10]})

# Calculate the covariance between columns 'A' and 'B'
covariance = data_cov.cov()

# Print the result
print("\nCovariance:")
print(covariance)


# 10. Skew
# Skewness is a descriptive statistic that measures the asymmetry of the probability distribution of a numerical column in a DataFrame.
# It indicates whether the data distribution is skewed to the left (negative skewness) or to the right (positive skewness).

import pandas as pd

# Create a DataFrame 
data_skew = pd.DataFrame({'A': [1, 2, 3, 4, 10]})

# Calculate the skewness of the data
skewness = data_skew.skew()

# Print the result
print("\nSkewness:")
print(skewness)

# 11. kurtosis
# Kurtosis is a descriptive statistic that measures the "tailedness" of the probability distribution of a numerical column in a DataFrame.
# It quantifies the shape of the distribution and indicates whether it is more peaked or flat compared to a normal distribution.

import pandas as pd

# Create a DataFrame 
data_kurtosis = pd.DataFrame({'A': [1, 2, 3, 4, 10]})

# Calculate the kurtosis of the data
kurtosis = data_kurtosis.kurtosis()

# Print the result
print("\nKurtosis:")
print(kurtosis)
# These descriptive statistical measures provide valuable insights into the characteristics, distribution, and relationships within the data.
# They are fundamental tools for data exploration, analysis, and making data-driven decisions.
