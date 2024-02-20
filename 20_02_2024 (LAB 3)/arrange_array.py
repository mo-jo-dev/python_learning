import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Sum of arr1:", np.sum(arr1))
print("Mean of arr2:", np.mean(arr2))

arr3 = np.arange(10)  
print("Original array:", arr3)
arr3_reshaped = arr3.reshape(2, 5) 
print("Reshaped array:")
print(arr3_reshaped)