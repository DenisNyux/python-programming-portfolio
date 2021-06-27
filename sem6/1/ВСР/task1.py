import numpy as np
import time

start_time = time.time()
arr1 = np.random.sample((16, 16))
arr2 = np.random.sample((16, 16))
result = np.dot(arr1, arr2, out=None)
print(time.time() - start_time)
# print(result)
# print(time.time() - start_time)
