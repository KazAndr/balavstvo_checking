import numpy as np
import time

import matmul1

M1 = 1000
N1M2  = 5000
N2 = 1000

a = np.empty((M1, N1M2), dtype=np.float64)
b = np.empty((N1M2, N2), dtype=np.float64)
c = np.empty((M1, N2), dtype=np.float64)

a[:] = np.random.rand(M1,N1M2)
b[:] = np.random.rand(N1M2,N2)


#Fortran call
start = time.time()
c = matmul1.matmul1(a, b, M1, N1M2, N2)
stop = time.time()

print('Fortran took ', (stop - start)*1000, ' milli-seconds')

#Numpy
start = time.time()
c = np.dot(a, b)
stop = time.time()

print('Numpy took ', (stop - start)*1000, ' milli-seconds')
