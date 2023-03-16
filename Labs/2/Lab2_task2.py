import numpy as np


def step1(m: np.ndarray, k: int):
    """1st step of the Jorgan-Gaussian jargon-check for a [k] [k] == 0.

    Args:
        m (np.ndarray): Calculating 2D Matrix.
    """

    n = len(m)

    for j in range(k, n):

        if (m[k][k] == 0):

            for i in range(k + 1, n):

                if m[i][k] != 0:

                    buffer = m[k]
                    m[k] = m[i]
                    m[i] = buffer
                    break

                break

        break

    return m


def step2(mat: np.ndarray, k: int):
    """Jorgan-Gauss 2nd step method - calculation a[i][j],
    for i != k & j > k & "Zeroing" elements under a[k][k].


    Args:
        mat (np.ndarray): Calculating 2D Matrix.
    """

    n = len(mat)
    m = len(mat[0])

    for i in range(0, n):

        for j in range(k + 1, m):

            if i != k:

                mat[i][j] = (mat[i][j] * mat[k][k] - mat[i][k] * mat[k][j]) / mat[k][k]

    return mat


def step3(m: np.ndarray, k: int):
    """3rd step of the Jorgan-Gauss method - 
    "Zeroing" elements in column k

    Args:
        m (np.ndarray): Calculating 2D Matrix.
    """

    n = len(m)

    for i in range(0, n):

        if i != k:

            m[i][k] = 0

    return m


def step4(mat: np.ndarray, k: int):
    """4th step of the Jorgan-Gauss method - 
    Calculating a[k][j]

    Args:
        mat (np.ndarray): Calculating 2D Matrix.
    """

    m = len(mat[0])

    for j in range(m - 1, k - 1, -1):

        mat[k][j] /= mat[k][k]

    return mat


def task2(matrix2D: np.ndarray):
    """Calculating 2D matrix by Jardan-Gauss
    Matrix must be N x N + 1 size,
        where last columb is B and anothers columns is A

    Args:
        matrix2D (np.ndarray): Calculating 2D Matrix.
    """

    n = len(matrix2D)
    m = len(matrix2D[0])

    if m != n + 1:

        raise Exception("Invalid data: Matrix is not correct")

    for k in range(0, n):

        matrix2D = step1(matrix2D, k)
        matrix2D = step2(matrix2D, k)
        matrix2D = step3(matrix2D, k)
        matrix2D = step4(matrix2D, k)

    return matrix2D[:, m - 1]
