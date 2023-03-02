from FunctionsUnit import *
import numpy as np

###########################################################################
#                                   Task 1 (1)
#
# Даны два действительных числа a и b. Получить их сумму, разность и произведение.
#
# https://ivtipm.github.io/Programming/Glava01/index01.htm#z1
#
###########################################################################

def Task1():

    a = float(input("Input first number - a: "))
    b = float(input("Input second number - b: "))

    print(
    f"""Their:
    Sum: {a + b}
    Substraction (a - b): {a - b}
    Multiplication: {a * b}
    """)


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


def Task2():

    x = float(input("Input first number - x: "))
    y = float(input("Input second number - y: "))
    z = float(input("Input third number - z: "))

    print(f"""Inputted values: 
    x = {x:.3f}
    y = {y:.3f}
    z = {z:.3f}
    """)

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

    print(f"""Calculated values: 
    x = {x:.3f}
    y = {y:.3f}
    z = {z:.3f}
    """)



###########################################################################
#                                   Task 3 (66)
#
# Даны целые числа k, m, действительные числа x, y, z. При k < m2, k = m2, 
# k > m2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.
#
# https://ivtipm.github.io/Programming/Glava03/index03.htm#z66
#
###########################################################################


def Task3():


    k = int(input("Input number k: "))
    m = int(input("Input number m: "))

    x = float(input("Input number x: "))
    y = float(input("Input number y: "))
    z = float(input("Input number z: "))

    print(f"""Inputted values: 
    k = {k}
    m = {m}

    x = {x:.3f}
    y = {y:.3f}
    z = {z:.3f}
    """)

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


    print(f"""Calculated values: 
    k = {k}
    m = {m}

    x = {x:.3f}
    y = {y:.3f}
    z = {z:.3f}
    """)

###########################################################################
#                                   Task 4 (114 б)
#
# Вычислить: 
# б) алгебраическая сумма (in range(i = 1, 50)) 1 / i^3
#
# https://ivtipm.github.io/Programming/Glava04/index04.htm#z114
#
###########################################################################

def Task4(f : function = lambda x: 1 / x**3):
    """print sum of function f(x), where x = n..m with step h

    Args:
        f (lambda, optional): labda expression - function f(x). Defaults to lambda x : 1/x**3
    """

    print("Task: sum of function f(x), where x = n..m with step h: ")

    m = int(input("input m:"))
    n = int(input("input n:"))
    h = int(input("input h:"))

    sum = 0

    for x in range(m, n, h):

        sum += f(x)

    print(f"Calculated sum: {sum:.4f}")


###########################################################################
#                                   Task 5 (136 н)
#
# Даны натуральное число n, действительные числа a1,..., an. Вычислить:
# (Пример см. по ссылке)
#
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
#
###########################################################################

# TODO: use map

def Task5():

    n = int(input("Input number n: "))

    numbers = randomFloatList(n, -2, 2)

    print("Matrix:\n")
    print_matrix(numbers)

    for i in range(0, n):

        sum += ((abs(numbers[i]))**(1/2) - numbers[i])**2

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

def Task6():

    n = int(input("Input number n: "))

    numbers = randomIntList(n, -50, 50)
    evenAmount = 0

    print("Matrix:\n")
    print_matrix(numbers)

    for i in range(0, n):

        if numbers[i] % 2 == 0:

            evenAmount += 1

    print(f"Even numbers amount: {evenAmount}")

###########################################################################
#                                   Task 7 (320)
#
# Вычилить:
# (Пример см. по ссылке)
#
# https://ivtipm.github.io/Programming/Glava10/index10.htm#z320
#
###########################################################################

# TODO: use map

def Task7():

    print("Task: Σ(1, N) (k^3) * Σ(1, M) ((k - l)^2)")

    n = int(input("Input N: "))
    m = int(input("Input M: "))

    res = 0

    for k in range(1, n):

        for l in range(1, m):

            res += (k - l)**2

        k = k**3 * res

        res = 0

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

def Task8():

    n = -1

    while (n < 0):

        n = int(input("Input number n:"))

    A = randomFloatList(n, -2, 2)
    B = randomFloatList(n, -2, 2)

    p = -1

    while (p > n or p < 0):

        p = int(input("Input number p ( p <= n and p >= 0 ):"))

    q = -1

    # while (q > n + 1 or q < 0 ):

        # q = int(input("Input number q ( q <= n + 1 and q >= 0 ):"))


    matrix = np.random.uniform(-2, 2, (n, n + 1))

    print("Start matrix:")
    print_matrix(matrix)

    matrix = np.vstack((matrix, A), )
    
    # insert(matrix, p, A)
    # matrix = np.insert(matrix, q, B, axis=1)

    print("Adding vectors:\nA:\n")
    print_matrix(A, 99)
    print("B:\n")
    print_matrix(B, 1)

    print("Final matrix:")
    print_matrix(matrix)



Task8()