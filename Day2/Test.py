# import matplotlib.pyplot as plt

# days = [1,2,3,4,5]

# visitors = [100,120,140,170,200]

# plt.xlabel("Days")
# plt.ylabel("Visitors")
# plt.title("Visitors per day")

# plt.plot(days, visitors, linestyle='--', marker='o', linewidth=3, color='r')
# for i in range(len(days)) :
#     plt.text(days[i], visitors[i], visitors[i])

# plt.show()

# import matplotlib.pyplot as plt

# months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# sales = [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]

# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Sales per Month")

# plt.plot(months, sales, marker='o', linestyle='--', linewidth=2, color='g')
# plt.show()

# import matplotlib.pyplot as plt

# fruits = ["Apple", "Mango", "Orange", "Banana"]
# sales = [50, 80, 40, 70]

# plt.bar(fruits, sales)

# plt.title("Fruit Sales")

# plt.xlabel("Fruits")

# plt.ylabel("Sales")

# plt.show()


# import matplotlib.pyplot as plt

# students = ["A", "B", "C", "D", "E"]

# marks = [75, 90, 60, 85, 95]

# plt.bar(students, marks)

# plt.title("Student Marks")

# plt.xlabel("Students")

# plt.ylabel("Marks")

# plt.show()

# candidates = ["React", "Python", "ML", "AI"]

# selected = [25, 40, 15, 10]

# plt.bar(candidates, selected)

# plt.title("Selected Candidates by Skill")

# plt.xlabel("Skill")

# plt.ylabel("Candidates")

# plt.show()

# import matplotlib.pyplot as plt

# months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# sales = [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]

# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Sales per Month")

# plt.barh(months, sales, color='g')

# for i in range(len(months)) :
#     plt.text(i, sales[i], sales[i])

# plt.show()

# import matplotlib.pyplot as plt

# months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# sales = [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]

# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Sales per Month")

# plt.scatter(months, sales, color='g')

# plt.show()

# import matplotlib.pyplot as plt

# experience = [1,2,3,4,5,6]

# salary = [25000,35000,45000,55000,70000,85000]

# plt.scatter(experience, salary)

# plt.title("Experience vs Salary")

# plt.xlabel("Experience")

# plt.ylabel("Salary")

# plt.show()

# import matplotlib.pyplot as plt

# marks = [45,50,55,60,65,70,75,80,85,90]

# plt.hist(marks)

# plt.show()

# import matplotlib.pyplot as plt

# marks = [45,50,55,60,65,70,75,80,85,90]

# plt.hist(marks, bins=5)

# plt.title("Student Marks Distribution")

# plt.xlabel("Marks")

# plt.ylabel("Number of Students")

# plt.show()

# import matplotlib.pyplot as plt

# marks = [40,42,45,48,50,52,55,58,60,62,
#          65,68,70,72,75,78,80,85,88,90]

# plt.hist(marks, bins=5)

# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.title("Marks Distribution")

# plt.show()

# import matplotlib.pyplot as plt

# marks = [
# 20,22,24,25,26,
# 27,28,29,
# 30,31,32,
# 75,78,80,82,85,
# 88,90,92
# ]

# plt.hist(marks,bins=5)

# plt.xlabel("Marks")
# plt.ylabel("Students")
# plt.title("Histogram Example")

# plt.show()

import matplotlib.pyplot as plt

salaries = [
    25000,
    28000,
    30000,
    32000,
    35000,
    40000,
    500000
]

plt.boxplot(salaries)

plt.title("Salary Distribution")

plt.show()

# Four Plots You Must Remember : 

# Plot	            Purpose
# =====             ========

# Line Plot	        Trends
# Bar Plot	        Compare Categories
# Scatter Plot	    Relationships
# Histogram	        Distribution
# Box Plot	        Outliers

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

