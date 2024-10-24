import numpy as np

arr = np.random.randint(1,10,(3,3))

print(arr)
print(np.mean(arr.diagonal()))
arr = np.fliplr(arr)
print(np.mean(arr.diagonal()))











