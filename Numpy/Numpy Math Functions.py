import numpy as np 

arr = np.array([0, np.pi/2, np.pi])
print(arr)

print(np.sin(arr))
print(np.cos(arr))
print(np.exp(arr))
print(np.log(arr+1))
print(np.sqrt(arr+1))

# [0.         1.57079633 3.14159265]
# [0.0000000e+00 1.0000000e+00 1.2246468e-16]
# [ 1.000000e+00  6.123234e-17 -1.000000e+00]
# [ 1.          4.81047738 23.14069263]
# [0.         0.94421571 1.42108041]
# [1.         1.6033703  2.03509033]
