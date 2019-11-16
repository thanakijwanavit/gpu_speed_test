import numpy as np
import time
import cupy as cp
### Numpy and CPU
i=700
def crazyrun():
    s = time.time()
    x_cpu = np.ones((i,i,i))
    e = time.time()
    print('numpy generation is {}'.format(e - s))
    ### CuPy and GPU
    s = time.time()
    x_gpu = cp.ones((i,i,i))
    e = time.time()
    print('cupy generation is {}'.format(e - s))
    ### Numpy and CPU
    s = time.time()
    x_cpu *= 5
    e = time.time()
    print('numpy calculation is {}'.format(e - s))
    ### CuPy and GPU
    s = time.time()
    x_gpu *= 5
    e = time.time()
    print('cupy calculation is {}'.format(e - s))
    ### Numpy and CPU
    s = time.time()
    x_cpu *= 5
    x_cpu *= x_cpu
    x_cpu += x_cpu
    e = time.time()
    print('numpy calculation is {}'.format(e - s))
    ### CuPy and GPU
    s = time.time()
    x_gpu *= 5
    x_gpu *= x_gpu
    x_gpu += x_gpu
    e = time.time()
    print('cupy calculation is {}'.format(e - s))

for i in range(500):
    crazyrun()