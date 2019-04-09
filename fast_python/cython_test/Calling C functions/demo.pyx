from libc.math cimport sin

cdef double f_1(double x):
    return sin(x * x)

cpdef double f_2(double x):
    return sin(x * x)
