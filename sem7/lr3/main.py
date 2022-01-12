import math
import concurrent.futures as ftres
from functools import partial
import c_integrate 


def f(x):
    return math.sin(x) + math.cos(x)


# def integrate(func, a, b, *, n_iter=1000):
#     h = (b - a) / n_iter
#     i = a + h
#     r1 = b - h
#     r2 = b - 2 * h
#     odd = 0
#     even = 0
#     while i <= r1:
#         odd += func(i)
#         i += 2 * h
#     i = a + 2 * h
#     while i <= r2:
#         even += func(i)
#         i += 2 * h
#     res = h / 3 * (func(a) + func(b) + 4 * odd + 2 * even)
#     return res

def integrate(fn, a, b, n_iter=10**6):
    result = 0
    h = 1 / n_iter
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return result


def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):
    executor = ftres.ThreadPoolExecutor(n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in ftres.as_completed(fs))
