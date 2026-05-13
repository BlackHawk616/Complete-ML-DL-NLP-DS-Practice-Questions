# Compute Mean, Median and standard deviation & variance using numpy

import numpy as np

# Sample Data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Data: ", data)
print("mean: ", np.mean(data))
print("Median: ", np.median(data))
print("Standard Deviation: ", np.std(data))
print("Variance: ", np.var(data))