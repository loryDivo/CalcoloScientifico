import numpy as np
import scipy.io
import scipy.sparse
import scipy.sparse.linalg
import sys
import time
def matrix_solver(directory_sparse_matrix):
    #matrix load
    a = scipy.io.mmread(directory_sparse_matrix)
    #fill zero matrix
    xe = np.ones(a.shape[0])
    print(a.shape[0])
    #product column-row matrix
    b = a.dot(xe)
    print("Press enter to start matrix resolution.")
    sys.stdin.readline()
    start_time = time.time()
    #solve matrix
    x = scipy.sparse.linalg.spsolve(a, b, use_umfpack=True)
    elapsed_time = time.time() - start_time
    print("Press enter to continue.")    
    sys.stdin.readline()
    #calculate error
    error = np.linalg.norm(xe - x) / np.linalg.norm(xe)

    print("time: ", elapsed_time)
    print("error: ", error)


matrix_solver('/Users/lorenzodivito/Desktop/Universita/MetodiCalcoloScientifico/FirstProject/MatrixPositive/mtx/ex15.mtx')
