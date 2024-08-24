import numpy as np

def sort_by_second_row(arr):
    return arr[:, arr[1, :].argsort()]

def sort_by_second_column(arr):
    return arr[arr[:, 1].argsort()]

array = np.array([[12, 15, 10], [7, 8, 9], [1, 2, 3]])

print("Sorted by second row:\n", sort_by_second_row(array))
print("Sorted by second column:\n", sort_by_second_column(array))
