from FunctionsUnit import *
import numpy as np

__author__ = "NemoNology (Банковский А.С.)"

###########################################################################
#                                   Task 1 (1)
#
# Даны два действительных числа a и b. Получить их сумму, разность и произведение.
#
# https://ivtipm.github.io/Programming/Glava01/index01.htm#z1
#
###########################################################################

def task1(a: float, b: float):
    """Return a + b, a - b, a * b as 3-elements Tuple"""

    return (a + b, a - b, a * b)




###########################################################################
#                                   Task 2 (44)
#
# Если сумма трех попарно различных действительных чисел x, y, z меньше единицы, 
# то наименьшее из этих трех чисел заменить полусуммой двух других; в противном 
# случае заменить меньшее из x и y полусуммой двух оставшихся значений.
#
# https://ivtipm.github.io/Programming/Glava02/index02.htm#z44
#
###########################################################################


def task2(x : float, y : float, z : float):
    """Если сумма трех попарно различных действительных чисел x, y, z меньше единицы,
    то наименьшее из этих трех чисел заменить полусуммой двух других; в противном
    случае заменить меньшее из x и y полусуммой двух оставшихся значений.
    """

    # print(f"""Inputted values: 
    # x = {x:.3f}
    # y = {y:.3f}
    # z = {z:.3f}
    # """)

    if (x + y + z < 1):
        
        if (min(x, y, z) == 1):

            x = (y + z) / 2

        if (min(x, y, z) == 2):

            y = (x + z) / 2

        if (min(x, y, z) == 3):

            z = (y + x) / 2

    else:

        if x <= y:

            x = (y + z) / 2

        else:

            y = (x + z) / 2

    # print(f"""Calculated values: 
    # x = {x:.3f}
    # y = {y:.3f}
    # z = {z:.3f}
    # """)

    return (x, y, z)



###########################################################################
#                                   Task 3 (66)
#
# Даны целые числа k, m, действительные числа x, y, z. При k < m, k = m, 
# k > m заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.
#
# https://ivtipm.github.io/Programming/Glava03/index03.htm#z66
#
###########################################################################


def task3(k: int, m :int, x : float, y : float, z : float):
    """Даны целые числа k, m, действительные числа x, y, z. При k < m2, k = m2, 
    k > m2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.
    """

    # print(f"""Inputted values: 
    # k = {k}
    # m = {m}

    # x = {x:.3f}
    # y = {y:.3f}
    # z = {z:.3f}
    # """)

    if k < m:

        k = int(x)
        y -= 0.5
        z -= 0.5

    elif k == m:

        k = int(y)
        x -= 0.5
        z -= 0.5

    else:

        k = int(z)
        y -= 0.5
        x -= 0.5


    # print(f"""Calculated values: 
    # k = {k}
    # m = {m}

    # x = {x:.3f}
    # y = {y:.3f}
    # z = {z:.3f}
    # """)

    return (k, m, x, y, z)

###########################################################################
#                                   Task 4 (114 б)
#
# Вычислить: 
# б) алгебраическая сумма (in range(i = 1, 50)) i^-3
#
# https://ivtipm.github.io/Programming/Glava04/index04.htm#z114
#
###########################################################################

def task4(f = lambda x: x**-3, tuple_len3 = (1, 15, 1)):
    """return sum of function f(x), where x = n..m with step h

    Args:
        f (function, optional): labda expression - function f(x). Defaults to lambda x : x^-3.
        tuple_len3 (tuple, optional): tuple. Defaults to tuple: (1, 15, 1).
    """

    if (len(tuple_len3) != 3):

        raise Exception("Invalid argument: tuple_len3 length is not 3")

    m, n, h = tuple_len3
    
    return func_sum(f, range(m, n, h))




###########################################################################
#                                   Task 5 (136 н)
#
# Даны натуральное число n, действительные числа a1, ..., an. 
# Вычислить: (√(|x|) - x)^2
# (Пример см. по ссылке)
#
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
#
###########################################################################

def task5(numbers : list = [rnd.uniform(-2, 2) for i in range(0, 10)], f = lambda x: (abs(x) ** (1 / 2) - x) ** 2):
    """Print sum of function f(x), where x = numbers[0]..numbers[len(numbers)]

    Args:
        numbers (list, optional): Inputting list of numbers,\n
        that will be input at function f(x) and sum. Defaults to list(10) filled with random.uniform(-2, 2).\n
        f (function, optional): Inputting function. Defaults to lambda x: (√(|x|) - x)^2.
    """

    print_list(numbers)

    sum = 0

    for i in range(0, len(numbers)):

        sum += f(numbers[i])

    print(f"Calculated sum: {sum:.4f}")

###########################################################################
#                                   Task 6 (178 a)
#
# Даны натуральные числа n, a1...an. Определить количество членов ak последовательности a1,...,an:
# являющихся нечетными числами;
#
# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
#
###########################################################################

def task6(numbers : list = [rnd.randint(-50, 50) for i in range(0, 10)], f = lambda x: x % 2 == 0):
    """Print list elements amount that were True (Match) at the output of the predicate f(x),
        where x = numbers[0]..numbers[len(numbers)]

    Args:
        numbers (list, optional): Inputting list of numbers,\n
        that will be input at function f(x) and checked. Defaults to list(10) filled with random.randint(-50, 50).\n
        f (function-predicate, optional): Inputting function-predicate. Defaults to lambda x: x % 2 == 0.
    """

    print_list(numbers)

    matchCount = 0

    for i in range(0, len(numbers)):

        if f(numbers[i]):

            matchCount += 1

    print(f"Match elements amount: {matchCount}")

###########################################################################
#                                   Task 7 (320)
#
# Вычилить: Σ(1, N) (k^3) * Σ(1, M) ((k - l)^2)
# (Пример см. по ссылке)
#
# https://ivtipm.github.io/Programming/Glava10/index10.htm#z320
#
###########################################################################

def task7(f1 = lambda x, y: x ** 3 * y,
          f2 = lambda x, y: (x - y)**2, 
          N : int = 10, M : int = 20):
    """Print sum of Σ(1..N):
            ( f1(x,  y = Σ(1..M): 
                ( f2(x, y) )
                ))

    Args:
        f1 (function, optional): first function by depth. Defaults to lambda x, y: x^3 * y.
        f2 (function, optional): second function by depth. Defaults to lambda x, y: (x - y)^2.
        N (int, optional): first function calculation count. Defaults to 10.
        M (int, optional): second function calculation count. Defaults to 20.
    """

    print("Task: Σ(1, N) (k^3) * Σ(1, M) ((k - l)^2)")

    res = 0

    for k in range(1, N):

        for l in range(1, M):

            buffer += f2(k, l)

        res += f1(k, buffer)

        buffer = 0

    print(f"Calculated sum: {res}")


###########################################################################
#                                   Task 8 (673)
#
# Даны действительная матрица размера n x (n + 1) действительные числа a1, ..., an+1, b1, ..., bn+1
# натуральные числа p, q (p ≤ n, q ≤ n+1). Образовать матрицу размера (n + 1) x (n + 2) вставкой после строки
# с номером р данной матрицы новой строки с элементами a1, ..., an+1 и последующей вставкой
# после столбца с номером q нового столбца с элементами b1, ..., bn+1.
#
# https://ivtipm.github.io/Programming/Glava20/index20.htm#z673
#
###########################################################################

def task8():

    n = -1

    while (n < 0):

        n = int(input("Input number n:"))

    # B = np.random.uniform(-2, 2, n + 1)
    # A = np.random.uniform(-2, 2, n + 1)

    A = np.zeros(n + 1) 
    B = np.zeros(n + 1) 

    p = -1

    while (p > n or p < 0):

        p = int(input("Input number p ( p <= n and p >= 0 ):"))

    q = -1

    while (q > n + 1 or q < 0 ):

        q = int(input("Input number q ( q <= n + 1 and q >= 0 ):"))


    matrix = np.random.uniform(-2, 2, (n, n + 1))

    print("Start matrix:")
    print_matrix(matrix)

    matrix = np.insert(matrix, p + 1, A, 0).reshape(n + 1, n + 1)
    matrix = np.insert(matrix, q + 1, B, 1).reshape(n + 1, n + 2)

    # print("Adding vectors:\nA:")
    # print_matrix(A)
    # print("B:")
    # print_matrix(B, False)

    print("Final matrix:")
    print_matrix(matrix)
