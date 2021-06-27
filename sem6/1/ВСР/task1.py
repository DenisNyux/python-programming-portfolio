import numpy as np
import time
import random


start_time = time.time()
n = random.randint(0, 101)
arr1 = np.random.sample((n, n))
arr2 = np.random.sample((n, n))
result = np.dot(arr1, arr2, out=None)
total_time = time.time() - start_time
print("%s - seconds" % total_time)
print("%d - size" % n)

# print(result)
# print(time.time() - start_time)
