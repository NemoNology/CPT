from Lab_1 import *
import unittest as ut

__author__ = "NemoNology (Банковский А.С.)"


class Lab1UnitTest(ut.TestCase):

    def test_task1(self):

        # First test
        o = task1(1, 1)
        t = [2, 0, 1]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

        # Second test
        o = task1(7.77, 58.23)
        t = [66, -50.46, 452.4471]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

    def test_task2(self):

        # First test
        o = task2(0, 0, 0)
        t = [0, 0, 0]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

        # Second test
        o = task2(1.3, 2.2, 3.1)
        t = [2.65, 2.2, 3.1]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

        # Third test
        o = task2(0.3, 0.2, 0.4)
        t = [0.3, 0.35, 0.4]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

    def test_task3(self):

        # First test
        o = task3(0, 0, 0, 0, 0)
        t = [0, 0, -0.5, 0, -0.5]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

        # Second test
        o = task3(1, 15, 94.8, -91.47, 62.7)
        t = [94, 15, 94.8, -91.97, 62.2]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

        # Third test
        o = task3(99, 31, 94.8, -91.47, 62.7)
        t = [62, 31, 94.3, -91.97, 62.7]

        for i in range(0, len(o)):

            self.assertAlmostEqual(o[i], t[i])

    def test_task4(self):

        self.assertEquals(task4(lambda x: x, (1, 10, 1)), 45)
        self.assertEquals(task4(lambda x: x, (1, 10, 10)), 1)
        self.assertAlmostEqual(task4(lambda x: x**-1, (1, 10, 1)), 2.828968253968254)


ut.main()