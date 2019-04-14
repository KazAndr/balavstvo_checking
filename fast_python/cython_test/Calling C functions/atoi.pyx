from libc.stdlib cimport atoi
#from __future__ import print_function

cdef char *s = '5'

cpdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "byte string value is NULL"
    return atoi(s)  # note: atoi() has no error detection!

print(parse_charptr_to_py_int(s))