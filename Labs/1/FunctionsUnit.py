import random as rnd
import numpy as np

def min(x, y, z):
    """Функция возвращающая номер минимального элемента из 3-ёх"""

    if x <= y and x <= z:

        return 1

    elif y <= x and y <= z:

        return 2

    else:

        return 3

def print_list(lst: list, nextLineCounter = 5):
    """Print list in normal view

    Args:
        lst (list): Printing list
        nextLineCounter (int, optional): List elements in one line amount. Defaults to 5.
    """

    counter = 1

    for x in lst:

        print(f"{x:5.3f}\t", end='')

        if (counter % nextLineCounter == 0):

            print()

        counter += 1

def print_matrix(matrix: np.array, is_horisontal : bool = True):
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

def randomIntList(elementsAmount : int, minValue : int, maxValue : int):
    """Функция возвращающая случайный список из int элементов\n
    elementsAmount - длина массива/кол-во элементов в нём\n
    minValue - минимальное значение для элемента в списке\n
    maxValue - максимальное значение для элемента в списке
    """
    
    return list(rnd.randint(minValue, maxValue) for i in range(elementsAmount))

def randomFloatList(elementsAmount : float, minValue : float, maxValue : float):
    """Функция возвращающая случайный список из int элементов\n
    elementsAmount - длина массива/кол-во элементов в нём\n
    minValue - минимальное значение для элемента в списке\n
    maxValue - максимальное значение для элемента в списке
    """
    
    return list(rnd.uniform(minValue, maxValue) for i in range(elementsAmount))

def func_sum(func, values : list):
    """ Returns sum of function f(x), where x = list[0]..list[-1]

    Args:
        f (function): function/labda expression - function f(x).
        values (list): list of summing values.
    """

    sum = 0

    for x in values:

        sum += func(x)

    return sum
