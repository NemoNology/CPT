from FunctionsUnit import *
from Lab2_task2 import *
import numpy as np
import seaborn as sb
# import pandas as pd
import matplotlib.pyplot as pl


def task1(N: int = 3, M: int = 7, isRandIntMatrix: bool = False):
    """Return a random N x M 2D matrix (ndarray)

    Args:
        N (int, optional): Rows amount. Defaults to 3.
        M (int, optional): Columns amount. Defaults to 7.
    """

    # uniform - floar matrix; randint - integer

    if isRandIntMatrix:

        return np.random.randint(-10, 10, (N, M))

    else:

        
        return np.random.uniform(-2, 2, (N, M))


def task2_test():

    # СЛАУ - [a00 * x0, ... a0n * xn, b0] 
    # СЛАУ - [....   . . ... . .. ..... ] 
    # СЛАУ - [am0 * x0, ... amn * xn, bm] 
    # Last Column - B
    m = np.array([
        [0.42, -0.72, 0.02, -0.28, 0.2, 0.66],
        [-0.67, 0.17, -0.86, 0.88, -0.88, 0.53],
        [0.14, -0.11, 0.86, -0.61, 0.61, 0.32],
        [0.83, -0.97, -0.29, -0.66, 0.7, -0.88],
        [0.91, -0.04, -0.41, -0.24, 0.09, 0.66]
    ])

    m1 = np.array(m)

    answer = np.array([-3.2017, 0.089519, -1.334208, -18.306746, -15.150182])

    print("Mine:"); printMatrix(task2(m))
    print("NumPy:"); printMatrix(np.linalg.solve(m[:, :-1], m[:, -1:]).reshape(1, 5))
    print("Answers:"); printMatrix(answer)


def task3(matrix2D: np.ndarray):

    # annot: if True - show matrix values; False - otherside
    # cmap - using color palette  
    sb.heatmap(matrix2D, annot=True, cmap='binary')
    pl.show()


def task4(matrix2D: np.ndarray):

    # ndarray.ravel() - convert matrix to vector
    sb.histplot(matrix2D.ravel())
    pl.show()


def task5(function=lambda x: (np.sin(x) - np.tan(x) * np.log(x)) * np.cbrt(x**-1) + np.sqrt(x) * x):

    # np.arange is usual range, but with float type possibility 
    Xs = np.arange(1, 100, 0.1)
    Ys = function(Xs)
    Ys_noise = Ys + np.random.uniform(-30, 30, (len(Xs)))

    # xlabel - name of horisontal Axis; ylabel - vertical
    # label - name of plot
    # pl.legend() - Enable legends
    pl.xlabel('X')
    pl.ylabel('Y')
    pl.plot(Ys, label='(sin(x) - tan(x * log(x)) * (x^-1)^(1/3) + sqrt(x) * x')
    pl.plot(Ys_noise, label='(sin(x) - tan(x * log(x)) * (x^-1)^(1/3) + sqrt(x) * x - with Noise', alpha=0.4)
    pl.subplot()
    pl.legend()
    pl.grid(True)
    pl.show()



task5()