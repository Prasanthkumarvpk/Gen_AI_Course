import numpy as np

# 1-D Arrays
arr = np.array([1,2,3,4,5])

print(arr)
print(np.__version__)

# 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

3# -D arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
