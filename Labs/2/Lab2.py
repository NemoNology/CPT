from FunctionsUnit import *
# from Lab2 import *
import numpy as np

def task1(N : int = 3, M : int = 7):
    """Return a random N x M 2D matrix (ndarray)

    Args:
        N (int, optional): Rows amount. Defaults to 3.
        M (int, optional): Columns amount. Defaults to 7.
    """

    return np.random.uniform(-2, 2, (N, M))



    
