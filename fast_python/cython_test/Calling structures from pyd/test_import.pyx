from test_struct cimport Test

cpdef void f(Test):
    print(Test.a)
    
f(Test)