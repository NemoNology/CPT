import numpy as np


def printMatrix(matrix: np.ndarray, is_horisontal: bool = True):
    """Print matrix (Max 2D) in normal veiw

    Args:
        matrix (np.array): printing matrix
        is_horisontal (bool, optional): True - print horisontal vector (1D matrix); False - vertical 
    """

    if (matrix.ndim > 2 or matrix.ndim == 0):
        return

    if (matrix.ndim == 2):

        n, m = np.shape(matrix)

        for i in range(0, n):

            for j in range(0, m):

                print(f"{matrix[i, j]:10.3f}", end="")

            print("")

    else:

        n = len(matrix)

        ending = "" if is_horisontal else "\n"

        for i in range(0, n):

            print(f"{matrix[i]:10.3f}", end=ending)

        print("")
