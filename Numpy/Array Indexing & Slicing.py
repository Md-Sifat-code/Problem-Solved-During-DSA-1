import numpy as np
arr = np.array([1,2,3,4,5,6])
#array indexing
print(arr[0])
print(arr[1])
print(arr[-1])

# Array slicing
print(arr[1:4])
print(arr[:4])
print(arr[::2])

arr2d = np.array([[1,2,3,4,5],
                  [2,3,4,56,6],
                  [3,4,5,7,1]])
print("This is for 2d array")
print(arr2d[0,3])
print(arr2d[1,1])
print(arr2d[2,3])

print(arr2d[:,2])
print(arr2d[1,:])