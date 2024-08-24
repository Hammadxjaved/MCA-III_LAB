import numpy as np 

def odd_rows_even_columns(arr):
    return arr[::2, 1::2]

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Odd rows and even columns:\n", odd_rows_even_columns(array))
