# Matplotlib = Engine

# Seaborn = Luxury Car built on that Engine

# Matplotlib = More code

# Seaborn = Less code + Better visuals

# Lesson 1: Count Plot
# Why Count Plot?

# Suppose we have:

# Male
# Female
# Male
# Male
# Female
# Male

# Question:

# How many males?
# How many females?

# Count Plot answers this instantly.

import seaborn as sns
import matplotlib.pyplot as plt

gender = [
    "male",
    "female",
    "male",
    "male",
    "female",
    "male"
]

sns.countplot(x=gender)

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

department = [
    "IT",
    "HR",
    "IT",
    "Finance",
    "IT",
    "HR",
    "Finance",
    "IT"
]

sns.countplot(x=department)

plt.title("Department Count")

plt.show()

# Lesson 2: Heatmap ⭐⭐⭐⭐⭐

# This is the most important Seaborn plot in Machine Learning.

# Every ML Engineer uses heatmaps.

# Problem

# Suppose we have:

# Experience	Salary	Age
# 1	30	22
# 2	40	24
# 3	50	26
# 4	60	28

# Question:

# Which columns are related?

# Heatmap answers this.

# Correlation

# A correlation value can be:

# +1  → Strong Positive Relationship

#  0  → No Relationship

# -1  → Strong Negative Relationship

# Example:

# Experience ↑
# Salary ↑

# Correlation:

# 0.95

# Strong Positive Relationship.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Experience" : [1,2,3,4],
    "Salary" : [30,40,50,60],
    "Age" : [22,24,26,28]
}

df = pd.DataFrame(data)

sns.heatmap(df.corr(), annot=True)

plt.show()

# Seaborn Lesson 3: Pairplot ⭐⭐⭐⭐⭐

# This is one of the coolest features in Seaborn.

# Problem

# Suppose your dataset contains:

# Age	Salary	Experience
# 22	30000	1
# 24	40000	2
# 26	50000	3
# 28	65000	4

# You want to see relationships between all columns.

# Without pairplot:

# Age vs Salary
# Age vs Experience
# Salary vs Experience

# Need multiple scatter plots.

# Pairplot Solution :

import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Age" : [22,24,26,28],
    "Salary" : [30000,40000,50000,65000],
    "Experience" : [1,2,3,4]
}

df = pd.DataFrame(data)

sns.pairplot(df)

plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Age": [
        22,22,22,22,22,
        23,23,23,
        24,24,
        25,
        26,
        27,
        28
    ],

    "Salary": [
        30000,31000,32000,33000,34000,
        35000,36000,37000,
        40000,42000,
        45000,
        50000,
        55000,
        65000
    ],

    "Experience": [
        1,1,1,1,1,
        2,2,2,
        3,3,
        4,
        5,
        6,
        7
    ]
}

df = pd.DataFrame(data)

sns.pairplot(df)
# plt.hist(df["Age"], orientation="horizontal")
# sns.scatterplot(data=df, x="Age", y="Salary")

plt.show()

# What Pairplot Does

# Automatically creates:

# Age vs Salary

# Age vs Experience

# Salary vs Experience

# +
# Histograms on diagonal

# One command gives complete EDA.

# Why ML Engineers Love Pairplot

# Before training a model:

# Check relationships
# Check distributions
# Find patterns
# Spot outliers

# All in one visualization.

# Pairplot vs Heatmap
# Heatmap

# Shows:

# Correlation numbers

# Example:

# Salary ↔ Experience = 0.95
# Pairplot

# Shows:

# Actual scatter plots

# You can visually inspect patterns.

import seaborn as sns
import matplotlib.pyplot as plt

marks = [45,50,55,60,65,70,75,80,85,90]

sns.histplot(marks)

plt.show()

# Add KDE Curve :

sns.histplot(marks, kde=True)

plt.show()

# What is KDE?

# KDE = Kernel Density Estimate

# Think of it as a smooth curve showing where most data is concentrated.

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Salary":[25000,30000,35000,40000,45000,
              50000,55000,60000,65000]
}

df = pd.DataFrame(data)

sns.histplot(df["Salary"], kde=True)

plt.show()

# Seaborn Plots You Now Know :-
# ============================

# Plot	        Purpose
# Countplot	    Count categories
# Heatmap	    Correlation
# Pairplot	    Relationships + Distributions
# Histplot	    Distribution

# Quick Comparison
# Plot	        Example
# Countplot	    Male/Female count
# Heatmap	    Study Hours vs Marks correlation
# Pairplot	    All column relationships
# Histplot	    Salary distribution


# Countplot → Count Categories

# Histplot → Distribution

# KDE → Smooth Distribution Curve

# Heatmap → Correlation Numbers

# Pairplot → All Relationships + Distributions