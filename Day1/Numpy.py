import numpy as np

# 0-D Array (Scalar)
import numpy as np
arr = np.array(42)
print(arr.ndim)

# 1-D Arrays
arr = np.array([1,2,3,4,5])
print(arr)
print(np.__version__)

# 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

# 3-D arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr1 = np.array(["apple", "banana", "cherry"])  
print(arr1.dtype)

arr2 = np.array([1, 2, 3])

copy = arr2.copy()

arr2[0] = 100
view = arr2.view()

print(copy)
print(view)

arr3 = np.array([1, 2, 3])

x = arr3.view()

arr3[0] = 100

print(arr3)
print(x)

arr.ndim     # dimensions
# 10                    → 0D
# [10,20,30]            → 1D
# [[10,20],[30,40]]     → 2D
# [[[1],[2]],[[3],[4]]] → 3D

# [1]               -> 1D
# [[1]]             -> 2D
# [[[1]]]           -> 3D
# [[[[1]]]]         -> 4D
# [[[[[1]]]]]       -> 5D

arr.shape    # size in each dimension (No.of Rows * No.of Columns)
# Example : Think like a box in loop (boxes inside box)
arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr5 = np.array([1,2,3,4,5,6])
print(arr5.shape) # (6,)
print(arr4.shape) # (2, 4)

arr = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print(arr.shape) # (2, 2, 2)

arr.reshape()
# reshape() anedi array data ni marchakunda, dani structure (shape) ni marchadaniki use chestham.
# Same Data + Different Arrangement = reshape()

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr) # Ippudu idi 1D array. Output : [1 2 3 4 5 6]

new_arr = arr.reshape(2,3)
print(new_arr) # Ippudu idi 2D array. Output : [[1 2 3] [4 5 6]]
arr.reshape(2,3)   # 2×3 = 6
arr.reshape(3,2)   # 3×2 = 6
arr.reshape(1,6)   # 1×6 = 6
arr.reshape(6,1)   # 6×1 = 6
arr.reshape(2,1,3) # 2×1×3 = 6
new_arr = arr.reshape(3,3) # ValueError: cannot reshape array of size 6 into shape (3,3) 
# Note : 3 Rows × 3 Columns = 9 Elements

# shape = (layers, rows, columns)
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

# reshape with copy 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = arr.reshape(2, 4)
print(new_arr.base) # output : [1 2 3 4 5 6 7 8]

# Reshape using Copy and Modification 

import numpy as np
arr = np.array([1, 2, 3, 4])
new_arr = arr.reshape(2, 2)
new_arr[0, 0] = 100
print(arr) # Output : [100   2   3   4]
print(new_arr.base is arr) # True

arr.size     # total elements
arr.dtype    # data type

# Mathematical Operations :

arr = np.array([1,2,3,4])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

# Matrix Operations :

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.dot(a,b))

# Random Numbers :

np.random.rand(3)

np.random.randint(1,100,5)

# Broadcasting :

arr = np.array([1,2,3])

print(arr + 5)

# Indexing and Slicing :

arr = np.array([10,20,30,40,50])

print(arr[0])
print(arr[-1])

print(arr[1:4])

# Iteraring : It means going through elements one by one.

# 1D : 
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

# Iterate on each scalar element of the 2-D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y) 

# 3D :
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x) 

# nditer() --> It will return elements inside nested array without using nested for loop

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)  # Output : 1 2 3 4 5 6 7 8

# op_dtypes : op_dtypes anedi np.nditer() lo use chestaru.

# Idi iteration chesetappudu temporary ga data type convert cheyyadaniki use avuthundi.

import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, op_dtypes=['S']):
    print(x, x.dtype)

# Endukante NumPy original array ni modify cheyyakunda conversion cheyyali.

# Kabatti flags=['buffered'] use chestham.

import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(
    arr,
    flags=['buffered'],
    op_dtypes=['S']
):
    print(x)


# Iterating With Different Step Size - skipping the elements based on condition(step)

import numpy as np

arr = np.array([1,2,3,4,5,6])

for x in np.nditer(arr[::2]):
    print(x)

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

# Enumerated Iteration Using ndenumerate() : Returns "Element + index position"

import numpy as np

arr = np.array([10, 20, 30])               # (0,) 10
for index, value in np.ndenumerate(arr):   # (1,) 20
    print(index, value)                    # (2,) 30

# Joining NumPy Arrays

# 1) concatenate() : It will not create a axis (list) until or unless explicit adding axis into it

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr) # Output : [1 2 3 4 5 6]

# Join two 2-D arrays along rows (axis=1): Axis is nothing but creating an extra list like nested array

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr) # Output : [ [1 2 3] [4 5 6]]

# Joining Arrays Using Stack Functions : it will create a new axis 

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

# Stacking Along Rows : hstack()

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

# hstack()	Side-by-side	    Columns increase
# vstack()	Top-to-bottom	    Rows increase
# dstack()	Depth-wise	        3rd dimension increase
# stack()	New axis create	    ndim + 1

# Splitting NumPy Arrays : Splitting ante oka pedda array ni chinna arrays ga divide cheyyadam.

# Simple ga:

# Original Array : [1 2 3 4 5 6]

# split : [1 2]  [3 4]  [5 6]

# array_split() : 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 2)

print(newarr) # Output : [array([1, 2, 3]), array([4, 5, 6])]

# chunks = np.array_split(arr, range(N, len(arr), N))

N = 3

newarr = np.array_split(arr, range(3, len(arr), 3))

print(newarr)  # Output : [array([1, 2, 3]), array([4, 5, 6]), array([7])]

import numpy as np

arr6 = np.array(
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    ) 

new_arr = np.array_split(arr6, range(5, len(arr6), 10)) # 5 elements * 10 steps(array's)
print(new_arr)

# Splitting 2D Arrays :

arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

newarr = np.array_split(arr, 2)

print(newarr) # Output : [ array([[1,2], [3,4]]), array([[5,6], [7,8]])]

# hsplit(), vsplit(), dsplit() ni batti confuse avutaru. Internal ga NumPy axis basis meeda split chestundi.

# Axis Concept :

arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

print(arr.shape) #(2,4)  Axios = 0 : Rows Indication and Axios = 1 : Columns Indication 

# hsplit()           [
#                       [1 2 | 3 4]    # Split at Columns
#                       [5 6 | 7 8]
#                    ]
#       ↓
# Left | Right      [
#                       [1 2 3 4]
#                       ----------------   Split at rows
#                       [5 6 7 8]
#                   ]


# vsplit()
#       ↓
# Top
# ---
# Bottom

result = np.hsplit(arr, 2)

print(result)  # [array([[1, 2], [5, 6]]), array([[3, 4], [7, 8]])]  

result = np.vsplit(arr, 2)

print(result)  # [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]


# dsplit() : 3D Array -- Axis = 2 --> This should have a minimum 3D Array

import numpy as np

arr = np.array([
    [
        [1,2,3,4],  # here no.of columns === 4 ([1,5],[2,6],[3,7],[4,8])
        [5,6,7,8]
    ]
])

print(arr.shape) # Output : (1, 2, 4)  Axis 0 = 1 Layer  --> [Outer Array]
#                                      Axis 1 = 2 Rows   --> [Row inside Outer Array] 
#                                      Axis 2 = 4 Columns (Depth Split Axis) --> Extra Layer is coated over Outside Array === [[]]


# NumPy Searching Arrays : Searching ante array lo oka specific value ekkada undo (index position) kanukovadam.

# NumPy lo mostly np.where() use chestham.

# 1) Search a Value : 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4])

x = np.where(arr == 4)

# Index : 0 1 2 3 4 5    Index 3 lo 4 undi
# Array : 1 2 3 4 5 4    Index 5 lo 4 undi
#             ↑   ↑

print(x) # Output : (array([3,5]))

# 2) Search Even Numbers :

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])   # 2 → index 1
                                    # 4 → index 3
                                    # 6 → index 5
                                    # 8 → index 7
x = np.where(arr % 2 == 0)

print(x)  # Output : (array([1, 3, 5, 7]))

# 3) Search Odd Numbers :

x = np.where(arr % 2 == 1)

print(x)

# 4) searchsorted() : Extracting Matched Index

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x) # Output : 1 --> Index 

# Extracting Nearest Matched Index -> 7 to 8 --> 7.5 == Nearest to 8

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7.5)

print(x) # Output : 2 

# 5) Search Multiple Values :

arr = np.array([1,3,5,7])

x = np.searchsorted(arr, [2,4,6])

print(x)  # Output : [1 2 3]

# NumPy Sorting Arrays : Sorting means putting elements in an ordered sequence, like numeric or alphabetical, ascending or descending.

# Sort the array:

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr)) # Output : [0 1 2 3]

# Sort the array alphabetically:

import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))  # Output : ['apple' 'banana' 'cherry']

# Sort a boolean array:

import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr)) # Output : [False  True  True]

# Sorting a 2-D Array : If you use the sort() method on a 2-D array, both arrays will be sorted

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr)) # Output : [[2 3 4] [0 1 5]]

# NumPy Filter Array : Getting some elements out of an existing array and creating a new array out of them is called filtering.

# Create a filter array that will return only values higher than 42: 
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # Output : [False, False, True, True]
print(newarr) # [43 44]

# Create a filter array that will return only even elements from the original array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

for element in arr :
    if element % 2 == 0 :
      filter_arr.append(True)
    else :
       filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)  # Output : [False, True, False, True, False, True, False]
print(newarr)      # [2 4 6]

# Creating Filter Directly From Array :

import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Generate Random Number :

from numpy import random

x = random.randint(100) # 0 to 100

print(x)

# Generate Random Float :

from numpy import random

x = random.rand()  # 0 to 1

print(x)

# The randint() method takes a size parameter where you can specify the shape of an array :

# Generate a 1-D array containing 5 random integers from 0 to 100 :

from numpy import random

x=random.randint(100, size=(5)) # 0 to 100 ==> 1 row

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100 :

from numpy import random

x = random.randint(100, size=(3, 5))  # 0 to 100 ==> rows : 3 and columns : 5

print(x) 

# The rand() method also allows you to specify the shape of the array :

from numpy import random

x = random.rand(5) # Output : [0.3363088 0.0426240 0.8741073 0.0854266 0.4870117]

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers: 

from numpy import random

x = random.rand(3, 5) # Output : [[0.03379952 0.78263517 0.9834899  0.47851523 0.02948659] 
#                                 [0.36284007 0.10740884 0.58485016 0.20708396 0.00969559] 
#                                 [0.88232193 0.86068608 0.75548749 0.61233486 0.06325663]]

print(x)

# Generate Random Number From Array :

# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.

from numpy import random

x = random.choice([3, 5, 7, 9]) # Output : 5

print(x)

# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5)) # Output : [[9 3 5 5 7] 
#                                                        [7 5 3 3 9] 
#                                                        [7 5 9 9 7]]

print(x)

# Random Distribution :

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) # Output : [5 7 3 5 7 9 5 ... Upto 100 nums]

print(x)

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) # Output : [[5 7 7 5 7]
#                                                                                [7 5 3 5 7]
#                                                                                [7 3 7 7 5]]

print(x)

# Shuffling Arrays :

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

# Generating Permutation of Arrays :

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

# Install Seaborn : pip install seaborn

# If you use Jupyter, install Seaborn using this command: !pip install seaborn

# Displots : Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

# Import Matplotlib : import matplotlib.pyplot as plt

# Import Seaborn : import seaborn as sns

# Plotting a Displot :

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a Displot Without the Histogram : (Bar-Chart)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()

# Visualization of Normal Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()

# Binomial Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show()

# Difference Between Normal and Binomial Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()

# Visualization of Poisson Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))

plt.show()

# Difference Between Normal and Poisson Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}

sns.displot(data, kind="kde")

plt.show()

# Difference Between Binomial and Poisson Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}

sns.displot(data, kind="kde")

plt.show()

# Visualization of Uniform Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=1000), kind="kde")

plt.show()

# Visualization of Logistic Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=1000), kind="kde")

plt.show()

# Difference Between Logistic and Normal Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}

sns.displot(data, kind="kde")

plt.show()

# Multinomial Distribution : 

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

# Visualization of Exponential Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.exponential(size=1000), kind="kde")

plt.show()

# Visualization of Chi Square Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=1, size=1000), kind="kde")

plt.show()

# Rayleigh Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()

# Pareto Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()

# Zipf Distribution :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()







