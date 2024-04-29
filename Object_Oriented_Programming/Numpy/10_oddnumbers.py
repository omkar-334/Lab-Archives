import numpy as numpy
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)