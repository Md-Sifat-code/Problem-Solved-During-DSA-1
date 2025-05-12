import numpy as np

arr2d = np.array([[1,2,3],
                  [4,5,6]])
col = np.array([[10],
                [20]])

result = arr2d + col

print(result)

b = np.array([100,200,300])
print(arr2d + b)

c = np.array([[10],[20]])
print(arr2d + c)