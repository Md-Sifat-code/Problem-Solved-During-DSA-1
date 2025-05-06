import numpy as np

# Array shape
arr = np.array([[1,2,4],[2,5,6]])
print(arr.shape)

# Array reshaping
arr1 = np.array([1,2,3,4,5,6,5,4,3])
reshaped = arr1.reshape(3,3)
print(reshaped)

# Flatten an array
arr2d = np.array([[1,2,3,4],
                  [4,5,6,7]])
flatterned = arr2d.flatten()
print(flatterned)
# Using the -1 we can auto reshape
arr2 = np.array([1,2,3,4,5,6,7,8,9])
reshaped1 = arr.reshape((2,-1))

# We can normally make an range array using np.arrange(12)
arr3 = np.array(12)
print(arr3)