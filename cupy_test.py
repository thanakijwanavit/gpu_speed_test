import cupy as cp
import numpy as np
import timeit
size_array = 1000000
number = 1000000

def add_arrays():
    x = cp.arange(0,size_array,1)
    y = cp.random.randn( size_array , 1 ,dtype= cp.float32)
    z= x/y
    #print(z)
aa = '''
def add_arrays():
    x = cp.arange(0,size_array,1)
    y = cp.random.randn( size_array , 1 ,dtype= cp.float32)
    z= x/y
    '''

def add_arrays_numpy():
    x = np.arange(0,size_array,1)
    y = np.random.randn( size_array , 1 )
    z= x/y
    #print(z)
aan ='''
def add_arrays_numpy():
    x = np.arange(0,size_array,1)
    y = np.random.randn( size_array , 1 )
    z= x/y
    '''
add_arrays()
add_arrays_numpy()

cp_time = timeit.timeit(setup = '''
import cupy as cp
import numpy as np
import timeit
size_array = {}
        '''.format(size_array),
        stmt = aa,
        number = number
        )

np_time = timeit.timeit(setup = '''
import cupy as cp
import numpy as np
import timeit
size_array = {}
        '''.format(size_array),
        stmt = aan,
        number = number
        )



print('time taken for cupy is {}'.format(cp_time))
print('time taken for numpy is {}'.format(np_time))
