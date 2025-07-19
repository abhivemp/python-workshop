# ----------------------------
# Lesson 1: Intro to Data Science & ML Lifecycle
# ----------------------------

# 1. Data Collection
# 2. Data Cleaning
# 3. Data Exploration/Visualization
# 4. Feature Engineering
# 5. Modeling (Machine Learning)
# 6. Evaluation
# 7. Deployment

# TODO:
# - List out examples for each stage
# - Discuss why cleaning and exploration are crucial before modeling

'''
element = [1, 2, 3]
element[2]
#      0  1  2
x = [ [1, 2, 3], # 0
      [4, 5, 6], # 1
      [7, 8, 9]  # 2

    ]
#         0          1          2
#      0  1  2    0  1  2    0  1  2
x = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 

x[1][2]
'''

# ----------------------------
# Lesson 2: Working with NumPy Arrays
# ----------------------------

import numpy as np

# TODO: Create a 1D array
a = np.array([1, 2, 3])

# TODO: Create a 2D array
b = np.array([[1, 2], [3, 4], [5,6]])
regular_b = [[1, 2], [3, 4]]

print(a)
# print(regular_b)
print(b)


# TODO: Print shape, ndim
print("A's shape: ", a.shape)
print("B's shape: ", b.shape)

# TODO: Perform math operations: +, *, **
print("a + 10:", a + 10)
print("a * 2: ", a * 2)
print("a ** 2: ", a ** 2)

# TODO: Use mean, median, std
print("Mean a: ", np.mean(a))
print("Median a: ", np.median(a))
print("Standard Deviation a: ", np.std(a))

print("Mean b: ", np.mean(b))
print("Median b: ", np.median(b))
print("Standard Deviation b:", np.std(b))

# ----------------------------
# Lesson 3: Introduction to Pandas DataFrames
# ----------------------------

import pandas as pd

data = {
    "Name": ["Tony", "Steve", "Bruce", "Clint"],
    "Age": [40, 122, 45, None],
    "City": ["LA", "NYC", "DFW", None]
}
# TODO: Create a DataFrame with Name, Age, and City columns
df = pd.DataFrame(data)

# TODO: Print head, info, describe
# print("DataFrame: \n", df)
print("Head info:\n", df.head())
print("Info: \n")
df.info()

print("\n Describe: \n", df.describe())
# TODO: Access specific columns using both methods
print("Names in the dataframe:\n", df['Name'])
print("Access using the dot notation: \n", df.Age)


# ----------------------------
# Lesson 4: Data Cleaning & Manipulation
# ----------------------------

# TODO: Check for missing values
print("Missing values per columns: \n", df.isnull().sum())

# TODO: Rename "City" to "Location"
df.rename(columns={'City': 'Location'}, inplace=True)

print(df)
# TODO: Add new column "Senior" if Age > 100

df["Senior"] = df["Age"] > 100
print(df)

# TODO: Filter rows where Senior is True
print("Filtered Seniors: \n ", df[df["Senior"] == True])

# TODO: Sort rows by Age descending
print("Sorted by Age descending: \n", df.sort_values("Age", ascending=False))
