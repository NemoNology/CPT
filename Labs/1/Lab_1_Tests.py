from Lab_1 import *
import unittest as ut
import numpy as np

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

        self.assertEqual(task4(lambda x: x, (1, 10, 1)), 45)
        self.assertEqual(task4(lambda x: x, (1, 10, 10)), 1)
        self.assertAlmostEqual(task4(lambda x: x**-1, (1, 10, 1)), 2.828968253968254)

    def test_task5(self):

        self.assertEqual(task5(range(1, 10), lambda x: x), 45)
        self.assertEqual(task5(range(1, 10), lambda x: x * 0), 0)
        self.assertAlmostEqual(task5(range(1, 10), lambda x: x**-1), 2.828968253968254)
        self.assertEqual(task5([x**2 for x in range(1, 5)], lambda x: x), 30)

    def test_task6(self):

        self.assertEqual(task6(range(1, 11)), 5)
        self.assertEqual(task6(range(1, 11), lambda x: x % 2 != 0), 5)
        self.assertEqual(task6(range(1, 11), lambda x: x != 0), 10)
        self.assertEqual(task6(range(1, 11), lambda x: x == 0), 0)

    def test_task7(self):

        self.assertAlmostEqual(task7(lambda x, y: x, lambda x, y: y, 2, 2), 1)
        self.assertAlmostEqual(task7(lambda x, y: x, lambda x, y: y, 0, 0), 0)

    def test_task8(self):

        # Raises tests
        with self.assertRaises(Exception):
            task8(-3, 4, 4)
            task8(4, 5, 4)
            task8(4, 2, 7)

        # First test
        m = task8(0, -1, 0)
        o = np.array([[0, 0]])

        self.assertEqual(m.all(), o.all())

        # Second test
        m = task8(4, 2, 2, True)
        o = np.array([[1, 1, 0, 1, 1, 1], 
                      [1, 1, 0, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0],
                      [1, 1, 0, 1, 1, 1],
                      [1, 1, 0, 1, 1, 1]])
        
        self.assertEqual(m.all(), o.all())
        
        # Third test
        m = task8(4, -1, -1, True)
        o = np.array([[0, 0, 0, 0, 0, 0], 
                      [0, 1, 1, 1, 1, 1],
                      [0, 1, 1, 1, 1, 1],
                      [0, 1, 1, 1, 1, 1],
                      [0, 1, 1, 1, 1, 1]])
        
        self.assertEqual(m.all(), o.all())

        # Fourth test
        m = task8(4, 3, 4, True)
        o = np.array([[1, 1, 1, 1, 0, 1], 
                      [1, 1, 1, 1, 0, 1],
                      [1, 1, 1, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 0, 1]])
        
        # Fifth test
        m = task8(5, 0, 5, True)
        o = np.array([[1, 1, 1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0], 
                      [1, 1, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 0]])
        
        self.assertEqual(m.all(), o.all())

ut.main()