import numpy as np
import time
import cupy as cp
import logging

### Numpy and CPU
def crazyrun(i=700, verbose= False):
    ''' run some example calculation to compare the speed of gpu and CPU
            i is the dimension of the 3d tensor to calcuate eg tensor.shape = (i,i,i)
            verbosity is the amount of logging to show, 
            ::verbose: Bool    either true or false
            ::i: int     Default 700
            '''
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    answer={}
    answer['numpy']={}
    answer['cupy']={}
    s = time.time()
    x_cpu = np.ones((i,i,i))
    e = time.time()
    logging.debug('numpy generation is {}'.format(e - s))
    answer['numpy']['generation']=e-s
    ### CuPy and GPU
    s = time.time()
    x_gpu = cp.ones((i,i,i))
    e = time.time()
    logging.debug('cupy generation is {}'.format(e - s))
    answer['cupy']['generation']=e-s
    ### Numpy and CPU
    s = time.time()
    x_cpu *= 5
    e = time.time()
    logging.debug('numpy calculation is {}'.format(e - s))
    answer['numpy']['calculation']=e-s
    ### CuPy and GPU
    s = time.time()
    x_gpu *= 5
    e = time.time()
    logging.debug('cupy calculation is {}'.format(e - s))
    answer['cupy']['calculation']=e-s
    ### Numpy and CPU
    s = time.time()
    x_cpu *= 5
    x_cpu *= x_cpu
    x_cpu += x_cpu
    e = time.time()
    logging.debug('numpy calculation is {}'.format(e - s))
    answer['numpy']['calculation2']=e-s
    ### CuPy and GPU
    s = time.time()
    x_gpu *= 5
    x_gpu *= x_gpu
    x_gpu += x_gpu
    e = time.time()
    logging.debug('cupy calculation is {}'.format(e - s))
    answer['cupy']['calculation2']=e-s
    return answer

if __name__=='__main__':
    for i in range(500):
        crazyrun()