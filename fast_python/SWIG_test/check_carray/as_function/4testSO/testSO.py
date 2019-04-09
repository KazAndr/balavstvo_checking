import example

a  = example.new_doubleArray(10)

for i in range(10):
    example.doubleArray_setitem(a, i, 2*i)

num = int(input('How mach?'))

for i in range(num): print(example.doubleArray_getitem(a,i))
