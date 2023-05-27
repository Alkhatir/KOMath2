"""
Authors: Oleh Karavskyi (k12139895) / Artur Garipov (k12146699)
Topic: Matrix operations
"""

import random
import sys
import copy


class Matrix(object):

    def __init__(self, in_matrix):

        self.in_matrix = in_matrix
        self.rows = len(in_matrix)
        self.cols = len(in_matrix[0])


    def __getitem__(self, in_matrix):
        return self.in_matrix

    def __repr__(self):
        return f"Matrix: {self.in_matrix}, dimensions={self.rows}x{self.cols})"


    """" Different input options """

    @classmethod
    def RandomInput (cls, rows, columns, low=0, high=10):
        """ Make a random matrix with elements in range (low-high) """

        r_matrix = [[random.randint(low, high) for _ in range(columns)] for _ in range(rows)]
        print(r_matrix)

        return Matrix(r_matrix)

    @classmethod
    def ZeroInput(cls, rows, columns):
        """ Make a zero-matrix """

        z_matrix = [[0] * columns for r in range(rows)]
        print(z_matrix)

        return Matrix(z_matrix)

    @classmethod
    def StringRowbyRowInput (cls):
        """ Read a matrix from standard input """

        print (f"Enter matrix as int row by row as e.g.: '10 8 3'. Type 'q' to quit")
        s_matrix = []
        while True:
            line = sys.stdin.readline().strip()
            if line == 'q': break

            row = [int(x) for x in line.split()]
            s_matrix.append(row)

        return Matrix(s_matrix)

    """" Main functions """

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Cannot add matrices of different dimensions.")

        m_output = []
        for i in range(self.rows):
            m_output.append([])
            for j in range(self.cols):
                m_output[i].append(self.in_matrix[i][j] + other.in_matrix[i][j])

        return Matrix(m_output)


    def __subtract__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Cannot add matrices of different dimensions.")

        m_output = []
        for i in range(self.rows):
            m_output.append([])
            for j in range(self.cols):
                m_output[i].append(self.in_matrix[i][j] - other.in_matrix[i][j])

        return Matrix(m_output)


    def __multiply__(self, other):
        m_output = []

        if isinstance(other, (int, float)):
            m_output = [[other * cell for cell in row] for row in self.in_matrix]

            return Matrix(m_output)

        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Incompatible dimensions for matrix multiplication.")

            for i in range(self.rows):
                m_row = []
                for j in range(other.cols):
                    cell = 0
                    for k in range(self.cols):
                        cell += self.in_matrix[i][k] * other.in_matrix[k][j]
                    m_row.append(cell)
                m_output.append(m_row)

            return Matrix(m_output)


    def _determinant_v1_(self):
        if self.rows != self.cols:
            raise ValueError("Determinant can be calculated only for square matrix")
        if self.rows == 2:
            det_output = self.in_matrix[0][0] * self.in_matrix[1][1] - self.in_matrix[1][0] * self.in_matrix[0][1]
            return det_output

        else:

            def det_recursive(rec_matrix):

                rec_output = 0
                idx = list(range(len(rec_matrix)))

                if len(rec_matrix) == 2 and len(rec_matrix[0]) == 2:
                    rec_output = rec_matrix[0][0] * rec_matrix[1][1] - rec_matrix[1][0] * rec_matrix[0][1]
                    return rec_output

                for col in idx:
                    new_matrix = rec_matrix
                    new_matrix = new_matrix[1:]

                    for i in range(len(new_matrix)):
                        new_matrix[i] = new_matrix[i][0:col] + new_matrix[i][col + 1:]

                    sign = (-1) ** (col % 2)
                    SubFun = det_recursive(new_matrix)
                    rec_output += sign * rec_matrix[0][col] * SubFun

                return rec_output

            return det_recursive(self.in_matrix)


    def _determinant_v2_(self):
        if self.rows != self.cols:
            raise ValueError("Determinant can be calculated only for square matrix")
        if self.rows == 2:
            det_output = self.in_matrix[0][0] * self.in_matrix[1][1] - self.in_matrix[1][0] * self.in_matrix[0][1]
            return det_output

        else:
            new_matrix = copy.deepcopy(Matrix(self.in_matrix))
            new_matrix = new_matrix[1:]

            for diag in range(len(new_matrix)):
                for i in range(diag + 1, len(new_matrix)):
                    ScalarMatrix = new_matrix[i][diag] / new_matrix[diag][diag]

                    for j in range(len(new_matrix)):
                        new_matrix[i][j] = new_matrix[i][j] - ScalarMatrix * new_matrix[diag][j]

            det_output = 1.0
            for i in range(len(new_matrix)):
                det_output *= new_matrix[i][i]

            return det_output



""""Test examples"""

# MA = Matrix([[2,3,5], [5,5,8]])
# MB = Matrix([[5,9,7], [9,6,1]])
# MD = Matrix([[5,5,8], [1,6,3], [2,3,5]])
# MH = Matrix([[3,5], [5,2]])
#
#
# MC = MA._add_(MB)
# MF = MA._subtract_(MB)
# ME = MA._multiply_(MD)
# MEr = MD._multiply_(MA)
# MG = MA._multiply_(3)
# print(f"MC: {MC},\n MF: {MF},\n ME: {ME},\n MG: {MG}")
#
#
# ML = MH._determinant_v1_()
# ML = MD._determinant_v2_()
# ML = MD._determinant_v1_()
#
# MR = Matrix.RandomInput(3,5)
# MEr = MR._determinant_v1_()
# MEr = MR._determinant_v2_()
#
# MZ = Matrix.ZeroInput(3,3)
#
# MS = Matrix.StringRowbyRowInput()
# 8 5 4
# 10 5 2
# 1 5 3
# q