import unittest
import numpy as nm
import Simple_operations

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_inv(self):
        matrix = []
        matrix.append(1)
        matrix.append(2)
        matrix.append(3)
        matrix.append(4)
        m1 = nm.array(matrix, dtype=float).reshape(2, 2)
        matrix2 = []
        matrix2.append(-2)
        matrix2.append(1)
        matrix2.append(1.5)
        matrix2.append(-0.5)
        m2 = nm.array(matrix2, dtype=float).reshape(2, 2)
        self.assertEqual(Simple_operations.do_inv(m1).all(), m2.all())


    def test_det(self):
        matrix = []
        matrix.append(1)
        matrix.append(2)
        matrix.append(3)
        matrix.append(4)
        m = nm.array(matrix, dtype=int).reshape(2, 2)
        self.assertAlmostEqual(Simple_operations.do_det(m) , -2)

    def test_transpose(self):
        a = []
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        m1 = nm.array(a, dtype=int).reshape(2, 2)
        b = []
        b.append(1)
        b.append(3)
        b.append(2)
        b.append(4)
        m2 = nm.array(b, dtype=int).reshape(2, 2)
        self.assertEqual(Simple_operations.do_transpose(m1).reshape(1, 4).all(), m2.all())


    def test_sum(self):
        first = []
        for i in range (9):
            first.append(i)
        second = []
        for i in range(9):
            second.append(1)
        m1 = nm.array(first, dtype=float).reshape(3, 3)
        m2 = nm.array(second, dtype=float).reshape(3, 3)
        result = []
        for i in range(9):
            result.append(i + 1)
        r = nm.array(result, dtype=float).reshape(3, 3)
        self.assertAlmostEqual(Simple_operations.do_sum(m1, m2).all(), r.all())


if __name__ == '__main__':
    unittest.main()
