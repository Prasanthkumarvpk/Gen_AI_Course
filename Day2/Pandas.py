# PANDAS COMPLETE NOTES WITH EXAMPLES - INTERVIEWS AND PRACTICE
# =============================================================
#
# What is Pandas?
# ---------------
# Pandas is an open-source Python library used for:
# - Data Analysis
# - Data Cleaning
# - Data Manipulation
# - Data Transformation
#
# Pandas is built on top of NumPy.
#
# Why Pandas?
# -----------
# 1. Easy handling of tabular data
# 2. Fast data processing
# 3. Supports CSV, Excel, JSON files
# 4. Handles missing values
# 5. Powerful grouping and aggregation

import pandas as pd
import numpy as np

# =================================================
# SERIES
# =================================================

# Definition:
# A Series is a one-dimensional labeled array.

print("=" * 50)
print("SERIES EXAMPLES")
print("=" * 50)

# Basic Series
s = pd.Series([10, 20, 30, 40])
print("Basic Series:")
print(s)
# 0    10
# 1    20
# 2    30
# 3    40

# Series with Custom Index
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("\nSeries with Custom Index:")
print(s)
# a    10
# b    20
# c    30

# Access by index
print("\nAccess by index 'b':", s["b"])  # 20

# Series with name
s = pd.Series([100, 200, 300], index=["Jan", "Feb", "Mar"], name="Monthly Sales")
print("\nNamed Series:")
print(s)

# Series from dictionary
sales_dict = {"Mon": 500, "Tue": 700, "Wed": 600}
s = pd.Series(sales_dict)
print("\nSeries from Dictionary:")
print(s)

# =================================================
# DATAFRAME
# =================================================

print("\n" + "=" * 50)
print("DATAFRAME EXAMPLES")
print("=" * 50)

# Definition:
# A DataFrame is a two-dimensional table with rows and columns.

data = {
    "Name":       ["John", "Sam", "Priya", "Ravi", "Alice"],
    "Age":        [25, 30, 28, 35, 22],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary":     [50000, 45000, 60000, 70000, 40000],
    "Gender":     ["M", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
#     Name  Age Department  Salary Gender
# 0   John   25         IT   50000      M
# 1    Sam   30         HR   45000      M
# 2  Priya   28         IT   60000      F
# 3   Ravi   35    Finance   70000      M
# 4  Alice   22         HR   40000      F

# =================================================
# READING FILES
# =================================================

print("\n" + "=" * 50)
print("READING FILES EXAMPLES")
print("=" * 50)

# Read CSV
# df = pd.read_csv("data.csv")
# df = pd.read_csv("data.csv", sep=",")         # custom separator
# df = pd.read_csv("data.csv", header=0)        # first row as header
# df = pd.read_csv("data.csv", nrows=100)       # read only 100 rows
# df = pd.read_csv("data.csv", usecols=["Name","Age"])  # specific columns

# Read Excel
# df = pd.read_excel("data.xlsx")
# df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Read JSON
# df = pd.read_json("data.json")

print("File reading syntax shown in comments above")
print("Example: df = pd.read_csv('employees.csv')")

# =================================================
# VIEWING DATA
# =================================================

print("\n" + "=" * 50)
print("VIEWING DATA EXAMPLES")
print("=" * 50)

print("df.head() - First 5 rows:")
print(df.head())

print("\ndf.head(3) - First 3 rows:")
print(df.head(3))

print("\ndf.tail(2) - Last 2 rows:")
print(df.tail(2))

print("\ndf.sample(2) - Random 2 rows:")
print(df.sample(2))

print("\ndf.shape - Rows and Columns count:")
print(df.shape)   # (5, 5)

print("\ndf.columns - Column names:")
print(df.columns)

print("\ndf.index - Index values:")
print(df.index)

# =================================================
# DATA INFORMATION
# =================================================

print("\n" + "=" * 50)
print("DATA INFORMATION EXAMPLES")
print("=" * 50)

print("df.info():")
df.info()

print("\ndf.describe() - Statistics:")
print(df.describe())
#        Age        Salary
# count  5.0      5.000000
# mean  28.0  53000.000000
# std    4.9  11726.039399
# min   22.0  40000.000000
# max   35.0  70000.000000

# =================================================
# ROWS AND COLUMNS
# =================================================

print("\n" + "=" * 50)
print("ROWS AND COLUMNS EXAMPLES")
print("=" * 50)

# Single column
print("Single Column - df['Name']:")
print(df["Name"])

# Multiple columns
print("\nMultiple Columns - df[['Name', 'Salary']]:")
print(df[["Name", "Salary"]])

# iloc - integer location (position based)
print("\ndf.iloc[0] - First row by position:")
print(df.iloc[0])

print("\ndf.iloc[1:3] - Rows 1 and 2:")
print(df.iloc[1:3])

print("\ndf.iloc[0, 1] - Row 0, Column 1:")
print(df.iloc[0, 1])   # 25

# loc - label based
print("\ndf.loc[0] - Row with index 0:")
print(df.loc[0])

print("\ndf.loc[0:2, 'Name':'Age'] - Rows 0-2, Columns Name to Age:")
print(df.loc[0:2, "Name":"Age"])

# =================================================
# INDEXING
# =================================================

print("\n" + "=" * 50)
print("INDEXING EXAMPLES")
print("=" * 50)

# Set index
df_indexed = df.set_index("Name")
print("Set Name as Index:")
print(df_indexed)

# Access by name after set_index
print("\nAccess Priya's data:")
print(df_indexed.loc["Priya"])

# Reset index
df_reset = df_indexed.reset_index()
print("\nReset Index:")
print(df_reset.head(2))

# =================================================
# FILTERING
# =================================================

print("\n" + "=" * 50)
print("FILTERING EXAMPLES")
print("=" * 50)

# Single condition
print("Age > 25:")
print(df[df["Age"] > 25])

# AND condition
print("\nAge > 25 AND Salary > 45000:")
print(df[(df["Age"] > 25) & (df["Salary"] > 45000)])

# OR condition
print("\nAge < 25 OR Salary > 60000:")
print(df[(df["Age"] < 25) | (df["Salary"] > 60000)])

# Filter by specific value
print("\nDepartment == IT:")
print(df[df["Department"] == "IT"])

# isin filter
print("\nDepartment in IT or HR:")
print(df[df["Department"].isin(["IT", "HR"])])

# between filter
print("\nAge between 25 and 30:")
print(df[df["Age"].between(25, 30)])

# =================================================
# SORTING
# =================================================

print("\n" + "=" * 50)
print("SORTING EXAMPLES")
print("=" * 50)

print("Sort by Age (Ascending):")
print(df.sort_values("Age"))

print("\nSort by Salary (Descending):")
print(df.sort_values("Salary", ascending=False))

print("\nSort by Department then Salary:")
print(df.sort_values(["Department", "Salary"], ascending=[True, False]))

# =================================================
# MISSING VALUES
# =================================================

print("\n" + "=" * 50)
print("MISSING VALUES EXAMPLES")
print("=" * 50)

# Create DataFrame with missing values
data_missing = {
    "Name":   ["John", "Sam", "Priya", "Ravi", "Alice"],
    "Age":    [25, None, 28, 35, None],
    "Salary": [50000, 45000, None, 70000, 40000]
}
df_missing = pd.DataFrame(data_missing)
print("DataFrame with Missing Values:")
print(df_missing)

print("\ndf.isnull() - Which values are null:")
print(df_missing.isnull())

print("\ndf.isnull().sum() - Count of nulls per column:")
print(df_missing.isnull().sum())
# Age      2
# Salary   1

print("\ndf.dropna() - Remove rows with any null:")
print(df_missing.dropna())

print("\ndf.fillna(0) - Fill nulls with 0:")
print(df_missing.fillna(0))

print("\nFill Age nulls with mean:")
df_missing["Age"] = df_missing["Age"].fillna(df_missing["Age"].mean())
print(df_missing)

# =================================================
# RENAME COLUMNS
# =================================================

print("\n" + "=" * 50)
print("RENAME COLUMNS EXAMPLES")
print("=" * 50)

df_renamed = df.rename(columns={"Age": "UserAge", "Salary": "CTC"})
print("Renamed Columns:")
print(df_renamed.head(3))

# Rename all columns
df_renamed2 = df.copy()
df_renamed2.columns = ["EmpName", "EmpAge", "Dept", "CTC", "Sex"]
print("\nAll Columns Renamed:")
print(df_renamed2.head(3))

# =================================================
# DROP COLUMNS
# =================================================

print("\n" + "=" * 50)
print("DROP COLUMNS EXAMPLES")
print("=" * 50)

print("Drop single column 'Gender':")
print(df.drop("Gender", axis=1).head(3))

print("\nDrop multiple columns:")
print(df.drop(["Gender", "Department"], axis=1).head(3))

# Drop rows
print("\nDrop row at index 0:")
print(df.drop(0, axis=0).head(3))

# =================================================
# DROP DUPLICATES
# =================================================

print("\n" + "=" * 50)
print("DROP DUPLICATES EXAMPLES")
print("=" * 50)

data_dup = {
    "Name":   ["John", "Sam", "John", "Priya", "Sam"],
    "Age":    [25, 30, 25, 28, 30],
    "Salary": [50000, 45000, 50000, 60000, 45000]
}
df_dup = pd.DataFrame(data_dup)
print("DataFrame with Duplicates:")
print(df_dup)

print("\nAfter drop_duplicates():")
print(df_dup.drop_duplicates())

print("\nDrop duplicates based on Name only:")
print(df_dup.drop_duplicates(subset=["Name"]))

print("\nCount duplicates:")
print(df_dup.duplicated().sum())   # 2

# =================================================
# ADD NEW COLUMN
# =================================================

print("\n" + "=" * 50)
print("ADD NEW COLUMN EXAMPLES")
print("=" * 50)

df_new = df.copy()

# Add Bonus column
df_new["Bonus"] = df_new["Salary"] * 0.10
print("After adding Bonus column:")
print(df_new)

# Add constant column
df_new["Company"] = "TechCorp"
print("\nAfter adding Company column:")
print(df_new.head(3))

# Add column based on condition
df_new["Level"] = df_new["Salary"].apply(
    lambda x: "Senior" if x >= 60000 else "Junior"
)
print("\nAfter adding Level column:")
print(df_new[["Name", "Salary", "Level"]])

# =================================================
# UPDATE COLUMN
# =================================================

print("\n" + "=" * 50)
print("UPDATE COLUMN EXAMPLES")
print("=" * 50)

df_update = df.copy()

# Increment Age by 1
df_update["Age"] = df_update["Age"] + 1
print("After Age + 1:")
print(df_update[["Name", "Age"]])

# Update specific row value
df_update.loc[0, "Salary"] = 55000
print("\nAfter updating John's Salary to 55000:")
print(df_update[["Name", "Salary"]])

# Update based on condition
df_update.loc[df_update["Department"] == "IT", "Salary"] += 5000
print("\nAfter IT department salary hike of 5000:")
print(df_update[["Name", "Department", "Salary"]])

# =================================================
# STRING OPERATIONS
# =================================================

print("\n" + "=" * 50)
print("STRING OPERATIONS EXAMPLES")
print("=" * 50)

print("Uppercase:")
print(df["Name"].str.upper())

print("\nLowercase:")
print(df["Name"].str.lower())

print("\nLength of each name:")
print(df["Name"].str.len())

print("\nStartswith 'J':")
print(df[df["Name"].str.startswith("J")])

print("\nContains 'a' (case insensitive):")
print(df[df["Name"].str.contains("a", case=False)])

print("\nReplace in string:")
print(df["Department"].str.replace("IT", "Information Technology"))

print("\nStrip whitespace:")
names_with_spaces = pd.Series(["  John ", " Sam  ", "Priya "])
print(names_with_spaces.str.strip())

# =================================================
# GROUPBY
# =================================================

print("\n" + "=" * 50)
print("GROUPBY EXAMPLES")
print("=" * 50)

print("Average Salary by Department:")
print(df.groupby("Department")["Salary"].mean())
# Department
# Finance    70000.0
# HR         42500.0
# IT         55000.0

print("\nCount employees by Department:")
print(df.groupby("Department")["Name"].count())

print("\nMax Salary by Department:")
print(df.groupby("Department")["Salary"].max())

print("\nMultiple aggregations:")
print(df.groupby("Department")["Salary"].agg(["min", "max", "mean", "sum"]))

print("\nGroupBy multiple columns:")
print(df.groupby(["Department", "Gender"])["Salary"].mean())

# =================================================
# AGGREGATION
# =================================================

print("\n" + "=" * 50)
print("AGGREGATION EXAMPLES")
print("=" * 50)

print("Total Salary Sum:", df["Salary"].sum())         # 265000
print("Average Salary:", df["Salary"].mean())           # 53000.0
print("Max Salary:", df["Salary"].max())                # 70000
print("Min Salary:", df["Salary"].min())                # 40000
print("Salary Count:", df["Salary"].count())            # 5
print("Salary Std Dev:", df["Salary"].std())            # standard deviation
print("Salary Median:", df["Salary"].median())          # 50000
print("Salary Variance:", df["Salary"].var())           # variance

# =================================================
# MERGING DATAFRAMES
# =================================================

print("\n" + "=" * 50)
print("MERGING DATAFRAMES EXAMPLES")
print("=" * 50)

df1 = pd.DataFrame({
    "id":   [1, 2, 3, 4],
    "Name": ["John", "Sam", "Priya", "Ravi"]
})

df2 = pd.DataFrame({
    "id":         [1, 2, 3, 5],
    "Department": ["IT", "HR", "IT", "Finance"]
})

print("df1:")
print(df1)
print("\ndf2:")
print(df2)

# Inner Join - common ids only
print("\nInner Join (common ids 1,2,3):")
print(pd.merge(df1, df2, on="id", how="inner"))

# Left Join - all from df1
print("\nLeft Join (all from df1):")
print(pd.merge(df1, df2, on="id", how="left"))

# Right Join - all from df2
print("\nRight Join (all from df2):")
print(pd.merge(df1, df2, on="id", how="right"))

# Outer Join - all from both
print("\nOuter Join (all from both):")
print(pd.merge(df1, df2, on="id", how="outer"))

# =================================================
# CONCATENATION
# =================================================

print("\n" + "=" * 50)
print("CONCATENATION EXAMPLES")
print("=" * 50)

df_a = pd.DataFrame({
    "Name":   ["John", "Sam"],
    "Salary": [50000, 45000]
})

df_b = pd.DataFrame({
    "Name":   ["Priya", "Ravi"],
    "Salary": [60000, 70000]
})

print("Vertical Concat (stack rows):")
print(pd.concat([df_a, df_b], ignore_index=True))

df_c = pd.DataFrame({
    "Department": ["IT", "HR"],
    "Age":        [25, 30]
})

print("\nHorizontal Concat (add columns):")
print(pd.concat([df_a, df_c], axis=1))

# =================================================
# PIVOT TABLE
# =================================================

print("\n" + "=" * 50)
print("PIVOT TABLE EXAMPLES")
print("=" * 50)

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)
print("Pivot - Average Salary by Department:")
print(pivot)

pivot2 = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean",
    fill_value=0
)
print("\nPivot - Salary by Department and Gender:")
print(pivot2)

# =================================================
# VALUE COUNTS
# =================================================

print("\n" + "=" * 50)
print("VALUE COUNTS EXAMPLES")
print("=" * 50)

print("Department value counts:")
print(df["Department"].value_counts())
# IT         2
# HR         2
# Finance    1

print("\nGender value counts:")
print(df["Gender"].value_counts())

print("\nValue counts with percentage:")
print(df["Department"].value_counts(normalize=True) * 100)

# =================================================
# UNIQUE VALUES
# =================================================

print("\n" + "=" * 50)
print("UNIQUE VALUES EXAMPLES")
print("=" * 50)

print("Unique Departments:")
print(df["Department"].unique())
# ['IT' 'HR' 'Finance']

print("\nNumber of unique Departments:")
print(df["Department"].nunique())   # 3

print("\nAll column unique counts:")
print(df.nunique())

# =================================================
# APPLY FUNCTION
# =================================================

print("\n" + "=" * 50)
print("APPLY FUNCTION EXAMPLES")
print("=" * 50)

df_apply = df.copy()

# Apply lambda - 10% salary hike
df_apply["Salary"] = df_apply["Salary"].apply(lambda x: x * 1.1)
print("After 10% Salary hike:")
print(df_apply[["Name", "Salary"]])

# Apply custom function
def grade(salary):
    if salary >= 60000:
        return "A"
    elif salary >= 45000:
        return "B"
    else:
        return "C"

df_apply["Grade"] = df_apply["Salary"].apply(grade)
print("\nAfter adding Grade column:")
print(df_apply[["Name", "Salary", "Grade"]])

# Apply on entire row (axis=1)
df_apply["Summary"] = df_apply.apply(
    lambda row: f"{row['Name']} works in {row['Department']}",
    axis=1
)
print("\nAfter adding Summary column:")
print(df_apply[["Name", "Department", "Summary"]])

# =================================================
# MAP FUNCTION
# =================================================

print("\n" + "=" * 50)
print("MAP FUNCTION EXAMPLES")
print("=" * 50)

df_map = df.copy()

# Map Gender codes to full words
df_map["Gender"] = df_map["Gender"].map({"M": "Male", "F": "Female"})
print("After mapping Gender:")
print(df_map[["Name", "Gender"]])

# Map Department to codes
dept_codes = {"IT": "D01", "HR": "D02", "Finance": "D03"}
df_map["DeptCode"] = df_map["Department"].map(dept_codes)
print("\nAfter mapping Department codes:")
print(df_map[["Name", "Department", "DeptCode"]])

# =================================================
# DATE TIME
# =================================================

print("\n" + "=" * 50)
print("DATE TIME EXAMPLES")
print("=" * 50)

data_dates = {
    "Name":      ["John", "Sam", "Priya", "Ravi"],
    "JoinDate":  ["2020-01-15", "2019-06-20", "2021-03-10", "2018-11-05"],
    "Salary":    [50000, 45000, 60000, 70000]
}
df_dates = pd.DataFrame(data_dates)

# Convert to datetime
df_dates["JoinDate"] = pd.to_datetime(df_dates["JoinDate"])
print("After converting to datetime:")
print(df_dates.dtypes)

# Extract year, month, day
df_dates["Year"]  = df_dates["JoinDate"].dt.year
df_dates["Month"] = df_dates["JoinDate"].dt.month
df_dates["Day"]   = df_dates["JoinDate"].dt.day

print("\nExtracted Date Parts:")
print(df_dates[["Name", "JoinDate", "Year", "Month", "Day"]])

# Calculate experience in days
df_dates["Experience_Days"] = (pd.Timestamp.now() - df_dates["JoinDate"]).dt.days
print("\nExperience in Days:")
print(df_dates[["Name", "JoinDate", "Experience_Days"]])

# Filter by date
print("\nJoined after 2020:")
print(df_dates[df_dates["JoinDate"] > "2020-01-01"][["Name", "JoinDate"]])

# =================================================
# EXPORT FILES
# =================================================

print("\n" + "=" * 50)
print("EXPORT FILES EXAMPLES")
print("=" * 50)

# Export to CSV
df.to_csv("output.csv", index=False)
print("Exported to output.csv")

# Export to Excel
# df.to_excel("output.xlsx", index=False)
# print("Exported to output.xlsx")

# Export to JSON
df.to_json("output.json", orient="records")
print("Exported to output.json")

print("\nExport options:")
print("df.to_csv('file.csv', index=False)      # No row numbers")
print("df.to_excel('file.xlsx', index=False)   # Excel file")
print("df.to_json('file.json')                 # JSON file")

# =================================================
# NUMPY VS PANDAS
# =================================================

print("\n" + "=" * 50)
print("NUMPY VS PANDAS COMPARISON")
print("=" * 50)

print("""
NumPy:
------
- Works with Arrays (1D, 2D, 3D)
- Faster Numerical Computation
- Mathematical Operations
- No column labels
- Best for: Images, Signals, Matrix math

Example:
  arr = np.array([1, 2, 3, 4, 5])
  arr.mean()   # 3.0
  arr * 2      # [2, 4, 6, 8, 10]

Pandas:
-------
- Works with Tables (rows + columns)
- Data Analysis and Cleaning
- Handles missing values
- Named columns and indexes
- Built on NumPy
- Best for: CSV data, Excel, SQL tables

Example:
  df = pd.DataFrame({'Name': ['John'], 'Age': [25]})
  df['Age'].mean()
  df[df['Age'] > 20]

When to use what?
-----------------
Numbers/Math/ML  → NumPy
Tables/CSV/Excel → Pandas
""")

print("=" * 50)
print("ALL PANDAS EXAMPLES COMPLETED!")
print("=" * 50)