# A Program to craete arrays and pefrom indexing, slicing and reshaping

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print("Original Array:", array1)

# Indexing
print("Element at index 2:", array1[2])

# Slicing
print("Sliced Array (index 1 to 3):", array1[1:4])

# Reshaping
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D Array:\n", array2)