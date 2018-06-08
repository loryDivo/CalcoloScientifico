import scipy.fftpack as sp
from PIL import Image
import numpy as np
import math
import time
import csv
from scipy.misc import imread
from scipy.misc import imsave
import scipy.misc

# function that computes DCT2 with built-in library
# param z: bidimensional numeric array
# return type: bidimensional numeric array
def python_dct(z):
    new_z2 = sp.dct(sp.dct(z.T, norm="ortho").T, norm="ortho")
    return new_z2

# fucntion that implements DCT on an array of value
# param z: unidimensional numeric array
# return type: unidimensional numeric array
def my_dct(z):
    N = z.size
    c = np.zeros(N)
    for k in range(N):
        sum_dct = 0
        for i, z_i in enumerate(z):
            sum_dct += z_i * math.cos(k * math.pi * (2 * i + 1) / (2 * N))
        c[k] = get_alpha(k, N) * sum_dct
    return c

def get_alpha(k, N):
    if k == 0:
        return math.sqrt(1 / N)
    else:
        return math.sqrt(2 / N)

# function that computes DCT2 applying function my_dct twice: first on the rows,
# then on the columns.
# param z: bidimensional numeric array
# return type: bidimensional numeric array
def my_dct_bidimensional(z):
    z_shape = z.shape
    c_temp = np.apply_along_axis(my_dct, axis=0, arr=z)
    c = np.apply_along_axis(my_dct, axis=1, arr=c_temp)
    return c.astype('float64')

# function that tests my_dct implementation on the example given by the
# specification on both the dimensions.
def my_dct_test():
    z = np.array([[231,32,233,161,24,71,140,245],
    [247,40,248,245,124,204,36,107],
    [234,202,245,167,9,217,239,173],
    [193,190,100,167,43,180,8,70],
    [11,24,210,177,81,243,8,112],
    [97,195,203,47,125,114,165,181],
    [193,70,174,167,41,30,127,245],
    [87,149,57,192,65,129,178,228]])

    c = my_dct_bidimensional(z)
    print("my dct")
    print(c)

    m = np.array([[1.11e+03,4.40e+01,7.59e+01,-1.38e+02,3.50e+00,1.22e+02,1.95e+02,-1.01e+02],
    [7.71e+01,1.14e+02,-2.18e+01,4.13e+01,8.77e+00,9.90e+01,1.38e+02,1.09e+01],
    [4.48e+01,-6.27e+01,1.11e+02,-7.63e+01,1.24e+02,9.55e+01,-3.98e+01,5.85e+01],
    [-6.99e+01,-4.02e+01,-2.34e+01,-7.67e+01,2.66e+01,-3.68e+01,6.61e+01,1.25e+02],
    [-1.09e+02,-4.33e+01,-5.55e+01,8.17e+00,3.02e+01,-2.86e+01,2.44e+00,-9.41e+01],
    [-5.38e+00,5.66e+01,1.73e+02,-3.54e+01,3.23e+01,3.34e+01,-5.81e+01,1.90e+01],
    [7.88e+01,-6.45e+01,1.18e+02,-1.50e+01,-1.37e+02,-3.06e+01,-1.05e+02,3.98e+01],
    [1.97e+01,-7.81e+01,9.72e-01,-7.23e+01,-2.15e+01,8.13e+01,6.37e+01,5.90e+00]])

    print("Check matrices:")
    print(np.array_equal(c, m))
    c2 = my_dct(np.array([231, 32, 233, 161, 24, 71, 140, 245]))
    print("First line")

    print(c2)

# function that launch the comparison, prints the resuts to the console and
# writes them to a file called "compare_dct.csv" in the current directory
def compare_dct():
    z1 = np.array(np.random.randint(0, 255, size=(100, 100)), dtype=float)
    z2 = np.array(np.random.randint(0, 255, size=(200, 200)), dtype=float)
    z3 = np.array(np.random.randint(0, 255, size=(300, 300)), dtype=float)
    z4 = np.array(np.random.randint(0, 255, size=(400, 400)), dtype=float)
    z5 = np.array(np.random.randint(0, 255, size=(500, 500)), dtype=float)
    z6 = np.array(np.random.randint(0, 255, size=(600, 600)), dtype=float)


    to_print = [['size', 'pyDctTime', 'myDctTime']]

    to_print.append([z1.shape[0]] + dct(z1))
    to_print.append([z2.shape[0]] + dct(z2))
    to_print.append([z3.shape[0]] + dct(z3))
    to_print.append([z4.shape[0]] + dct(z4))
    to_print.append([z5.shape[0]] + dct(z5))
    to_print.append([z6.shape[0]] + dct(z6))

    with open("compare_dct.csv", "wt", encoding="utf8", newline="") as out_file:
        writer = csv.writer(out_file, delimiter=",")
        for row in to_print:
            print(row)
            writer.writerow(row)

# function that measures the performance of the user-defined DCT implementation
# compared to the built-in function.
# param: bidimensional numeric array
# return type: array of two values. The first value is the execution time (in
# seconds) of the built-in funcion, the second one is the execution time of the
# user-defined function (in seconds)
def dct(z):
    start_time = time.time()
    time.sleep(1)
    python_dct(z)
    elapsed_time = time.time() - start_time - 1
    start_time2 = time.time()
    my_dct_bidimensional(z)
    elapsed_time2 = time.time() - start_time2

    return [elapsed_time, elapsed_time2]

# uncomment the method below to run the test in the specification
# status: running
my_dct_test()

# running comparison
#compare_dct()
