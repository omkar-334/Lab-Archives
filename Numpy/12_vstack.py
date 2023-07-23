import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

# Answers
# Method 1:
x=np.concatenate([a, b], axis=0)

# Method 2:
y=np.vstack([a, b])

# Method 3:
z=np.r_[a, b]
print(x,y,z)