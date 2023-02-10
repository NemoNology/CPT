
###########################################################################
#                                   Task 1 (1)
#
# Даны два действительных числа a и b. Получить их сумму, разность и произведение.
#
# https://ivtipm.github.io/Programming/Glava01/index01.htm#z1
#
###########################################################################

# a = float(input("Input first number - a: "))
# b = float(input("Input second number - b: "))

# print(
# f"""Theirs:
# Sum: {a + b}
# Substraction (a - b): {a - b}
# Multiplication: {a * b}
# """)

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

# def min(x, y, z):

#     if x <= y and x <= z:

#         return 0

#     elif y <= x and y <= z:

#         return 1

#     else:

#         return 2


# numbers = []

# numbers.append(float(input("Input first number - x: ")))
# numbers.append(float(input("Input second number - y: ")))
# numbers.append(float(input("Input third number - z: ")))


# if (numbers.sum < 1):
    
#     numbers[min(numbers)] = (numbers.sum - numbers[min(numbers)]) / 2

# else:

#     if numbers[0] <= numbers[1]:

#         numbers[0] = (numbers[1] + numbers[2]) / 2

#     else:

#         numbers[1] = (numbers[0] + numbers[2]) / 2



###########################################################################
#                                   Task 3 (66)
#
# Даны целые числа k, m, действительные числа x, y, z. При k < m2, k = m2, 
# k > m2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.
#
# https://ivtipm.github.io/Programming/Glava03/index03.htm#z66
#
###########################################################################


# k = int(input("Input number k: "))
# m = int(input("Input number m: "))

# x = float(input("Input number x: "))
# y = float(input("Input number y: "))
# z = float(input("Input number z: "))

# if k < m:

#     k = int(x)
#     y -= 0.5
#     z -= 0.5

# elif k == m:

#     k = int(y)
#     x -= 0.5
#     z -= 0.5

# else:

#     k = int(z)
#     y -= 0.5
#     x -= 0.5

###########################################################################
#                                   Task 4 (114 б)
#
# Вычислить: 
# б) алгебраическая сумма (in range(i = 1, 50)) 1 / i^3
#
# https://ivtipm.github.io/Programming/Glava04/index04.htm#z114
#
###########################################################################

# sum = 0

# for i in range(1, 50):

#     sum += 1 / i**3



###########################################################################
#                                   Task 5 (136 н)
#
# Даны натуральное число n, действительные числа a1,..., an. Вычислить:
# (Пример см. по ссылке)
#
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
#
###########################################################################

# n = int(input("Input number n: "))

# numbers = [0] * n
# sum = 03

# for i in range(0, n):

#     numbers[i] = float(input(f"Input number a{i}: "))

# for i in range(0, n):

#     sum += ((abs(numbers[i]))**(1/2) - numbers[i])**2

# sum

###########################################################################
#                                   Task 6 (178 a)
#
# Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:
# являющихся нечетными числами;
#
# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
#
###########################################################################


# n = int(input("Input number n: "))

# numbers = []
# oddAmount = 0

# for i in range(0, n):

#     if numbers[i] % 2 == 0:

#         oddAmount += 1


###########################################################################
#                                   Task 7 (320)
#
# Вычилить:
# (Пример см. по ссылке)
#
# https://ivtipm.github.io/Programming/Glava10/index10.htm#z320
#
###########################################################################

# k = 0
# l = 0
# res = 0

# for i in range(1, 10):

#     k = k**3

#     for j in range(1, 15):

#         res += (k - l)**2


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

# import numpy as np

# n = -1

# while (n < 0):

#     n = int(input("Input number n:"))

# A = []
# B = []

# for i in range(1, n + 1):

#     A[i] = float(input(f"Input number a{i}:"))
#     B[i] = float(input(f"Input number b{i}:"))

# p = -1

# while (p < 0 and p > n):

#     p = int(input("Input number p ( p <= n! ):"))

# q = -1

# while (q < 0 and q > n + 1):

#     q = int(input("Input number q ( q <= n + 1! ):"))


# startMatrix = np.ar