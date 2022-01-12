from libc.math cimport atan


cpdef double cyt_integrate(double a, double b, double n_iter):
    cdef double h
    cdef int i
    cpdef double result
    result = 0
    h = 1 / n_iter
    while a <= b - h:
        result += (atan(a) + atan(a + h)) / 2 * h
        a += h
    return result