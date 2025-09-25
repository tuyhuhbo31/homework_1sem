import numpy as np


arr = np.array([1,2,3])
print(arr)
arr2 = np.array([2,3,4])
print(arr*arr2)
print(arr@arr2)

matrix = np.stack([arr,arr,arr2])
matrix2 = np.stack([arr,arr2,arr2])
print(matrix, '\n', matrix2)
print(matrix*matrix2)

arr1 = np.ones(5)
arr2 = np.ones((2,2))
print(arr1)
print(arr2)
arr3 = np.array([0,1])*0.5
print(arr2+arr3)

