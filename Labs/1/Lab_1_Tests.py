from Lab_1 import *
import unittest as ut

__author__ = "NemoNology (Банковский А.С.)"


class Lab1UnitTest(ut.TestCase):

    def test_task1(self):

        self.assertEquals(task1(1, 1), (2, 0, 1))
        self.assertEquals(task1(7.77, 58.23), (66, -50.459999999999994, 452.4471))

    def test_task2(self):

        self.assertEquals(task2(0, 0, 0), (0, 0, 0))
        self.assertEquals(task2(1.3, 2.2, 3.1), (2.6500000000000004, 2.2, 3.1))
        self.assertEquals(task2(0.3, 0.2, 0.4), (0.3, 0.35, 0.4))

    def test_task3(self):

        self.assertEquals(task3(0, 0, 0, 0, 0), (0, 0, -0.5, 0, -0.5))
        self.assertEquals(task3(1, 15, 94.8, -91.47, 62.7), (94, 15, 94.8, -91.97, 62.2))
        self.assertEquals(task3(99, 31, 94.8, -91.47, 62.7), (62, 31, 94.3, -91.97, 62.7))

    def test_task4(self):

        self.assertEquals(task4(lambda x: x, (1, 10, 1)), 45)
        self.assertEquals(task4(lambda x: x, (1, 11, 1)), 45)


ut.main()