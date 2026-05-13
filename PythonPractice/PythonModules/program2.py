# Implement matrix mulitiplcation using Numpy and verifiy results 

import numpy as np

# Matrix A
a = np.array([[1, 2], [3, 4]])
# Matrix B
b = np.array([[5, 6], [7, 8]])

# Matrix Muliplication

result = np.dot(a,b)

print("Result of Matrix Multiplication:\n", result)
