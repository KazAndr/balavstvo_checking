#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import cython

n = int(input())

%load_ext cython


%%cython

def fib_cython(int k):
    cdef int i,
    cdef long int c, d
    c, d = 1, 1
    for i in range(k):
        c, d = c + d, c
    return c

print(fib_cython(n))
