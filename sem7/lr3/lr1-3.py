import c_integrate 
import timeit

stp = """
import math 
import concurrent.futures as ftres
from functools import partial
from main import integrate, integrate_async, c_integrate 
"""

print(timeit.timeit("integrate(math.atan, 0, math.pi / 2, n_iter=10**6)", setup=stp, number=100))
print(timeit.timeit("c_integrate.cyt_integrate(0, math.pi / 2, 10**6)", setup=stp, number=100))