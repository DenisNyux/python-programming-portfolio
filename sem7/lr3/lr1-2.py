import timeit

stp = """
import math 
import concurrent.futures as ftres
from functools import partial
from main import integrate, integrate_async
"""

print(timeit.timeit("integrate(math.atan, 0, math.pi / 2, n_iter=10**6)", setup=stp, number=100))
print(timeit.timeit("integrate_async(math.atan, 0, math.pi / 2, n_jobs = 2, n_iter=10**6)", setup=stp, number=100))
print(timeit.timeit("integrate_async(math.atan, 0, math.pi / 2,  n_jobs = 4, n_iter=10**6)", setup=stp, number=100))
print(timeit.timeit("integrate_async(math.atan, 0, math.pi / 2,  n_jobs = 8, n_iter=10**6)", setup=stp, number=100))