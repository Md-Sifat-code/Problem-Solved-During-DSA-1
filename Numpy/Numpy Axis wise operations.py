import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

print(np.sum(arr))
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))