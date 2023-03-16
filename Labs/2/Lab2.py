from FunctionsUnit import *
from Lab2_task2 import *
import numpy as np


def task1(N: int = 3, M: int = 7):
    """Return a random N x M 2D matrix (ndarray)

    Args:
        N (int, optional): Rows amount. Defaults to 3.
        M (int, optional): Columns amount. Defaults to 7.
    """

    return np.random.uniform(-2, 2, (N, M))


def task2_test():

    m = np.array([
        [0.42, -0.72, 0.02, -0.28, 0.2, 0.66],
        [-0.67, 0.17, -0.86, 0.88, -0.88, 0.53],
        [0.14, -0.11, 0.86, -0.61, 0.61, 0.32],
        [0.83, -0.97, -0.29, -0.66, 0.7, -0.88],
        [0.91, -0.04, -0.41, -0.24, 0.09, 0.66]
    ])

    answer = np.array([-3.2017, 0.089519, -1.334208, -18.306746, -15.150182])

    printMatrix(task2(m))
    printMatrix(answer)


task2_test()