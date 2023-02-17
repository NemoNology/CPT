import randint from random
import uniform from random

def min(x, y, z):
    """Функция возвращающая номер минимального элемента из 3-ёх"""

    if x <= y and x <= z:

        return 1

    elif y <= x and y <= z:

        return 2

    else:

        return 3


def printList(lst: list, nextLineCounter = 5):

    counter = 0

    for x in lst:

        print(f"{x.3f}\t")

        counter += 1

        if counter == nextLineCounter:

            print()

def randomIntList(elementsAmount, minValue, maxvalue):
    """Функция возвращающая случайный список из int элементов
    elementsAmount - длина массива/кол-во элементов в нём
    minValue - минимальное значение для элемента в списке
    maxvalue - максимальное значение для элемента в списке
    """
    
    return list(randint(minValue, maxValue) for i in range(elementsAmount))


def randomFloatList(elementsAmount, minValue, maxvalue):
    """Функция возвращающая случайный список из int элементов
    elementsAmount - длина массива/кол-во элементов в нём
    minValue - минимальное значение для элемента в списке
    maxvalue - максимальное значение для элемента в списке
    """
    
    return list(uniform(minValue, maxValue) for i in range(elementsAmount))