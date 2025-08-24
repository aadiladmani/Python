#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10
import numpy as np
a = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix with values from 2 to 10:\n", a)

# Write a NumPy program to reverse an array (the first element becomes the last).
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
print("Reversed array:", arr[::-1])

# Write a NumPy program to find common values between two arrays.
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
print("Common values:", np.intersect1d(arr1, arr2))

# Write a NumPy program to repeat array elements.
arr = np.array([1, 2, 3])
print("Repeat each element 3 times:", np.repeat(arr, 3))
print("Tile the array 2 times:", np.tile(arr, 2))

# Write a NumPy program to find the memory size of a NumPy array.
arr = np.array([1, 2, 3, 4, 5])
print("Size of each element in bytes:", arr.itemsize)
print("Total memory size in bytes:", arr.nbytes)

# Write a NumPy program to create an array of ones and zeros.
print("Array of ones:\n", np.ones((3, 3), dtype=int))
print("Array of zeros:\n", np.zeros((3, 3), dtype=int))

# Write a NumPy program to find the 4th element of a specified array.
arr = np.array([10, 20, 30, 40, 50])
print("4th element:", arr[3])  # index starts from 0
