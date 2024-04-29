import numpy as np 
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# From 'a' remove all of 'b'
print(np.setdiff1d(a,b))
