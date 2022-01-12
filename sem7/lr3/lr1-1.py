import timeit

stp = """
import math 
from main import integrate
"""

res = timeit.timeit("integrate(math.atan, 0, math.pi / 2, n_iter=10**6)", setup=stp, number=100)
print(res)