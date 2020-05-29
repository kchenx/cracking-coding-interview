# Zero Matrix
# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0

from typing import List
import unittest


def zeroify(mat: List[List[int]]):
    """Set rows and cols with zeros to all zeros"""
    m = len(mat)
    n = len(mat[0])

    # determine if need to zero first row/col
    zerofirstrow = any(mat[0][j] == 0 for j in range(n))
    zerofirstcol = any(mat[i][0] == 0 for i in range(m))

    # if need to zero row/col, store zero in first col/row of matrix
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    # zero rows/cols depending on first col/row
    for i in range(m):
        if mat[i][0] == 0:
            mat[i] = [0] * n
    for j in range(n):
        if mat[0][j] == 0:
            for i in range(m):
                mat[i][j] = 0

    # zero first row/col if necessary
    if zerofirstrow:
        mat[0] = [0] * n
    if zerofirstcol:
        for i in range(m):
            mat[i][0] = 0


class TestZeroMatrix(unittest.TestCase):
    def test_zeroify(self):
        m1 = [[1, 2], [3, 4]]
        zeroify(m1)
        self.assertEqual(m1, [[1, 2], [3, 4]])
        m2 = [[1, 2], [3, 0]]
        zeroify(m2)
        self.assertEqual(m2, [[1, 0], [0, 0]])
        m3 = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
        zeroify(m3)
        self.assertEqual(m3, [[0, 0, 0], [4, 5, 0], [7, 8, 0]])
        m4 = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
        zeroify(m4)
        self.assertEqual(m4, [[0, 2, 3], [0, 0, 0], [0, 8, 9]])
        m5 = [[1, 2, 0, 4], [5, 0, 7, 8], [9, 10, 11, 12]]
        zeroify(m5)
        self.assertEqual(m5, [[0, 0, 0, 0], [0, 0, 0, 0], [9, 0, 0, 12]])


if __name__ == "__main__":
    unittest.main()
