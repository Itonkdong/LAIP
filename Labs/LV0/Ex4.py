import numpy as np


class GaussMethod:
    def __init__(self, array):
        self.full_matrix = np.array(array)

    def swap(self, row_1, row_2):
        self.full_matrix[row_1,], self.full_matrix[row_2,] = self.full_matrix[row_2,], np.array(self.full_matrix[row_1,])

    def scale(self, row, factor):
        self.full_matrix[row,] *= factor

    def scale_and_add(self, scale_row, factor, add_row):
        self.full_matrix[add_row,] += (-5) * self.full_matrix[scale_row,]

    def __str__(self):
        return self.full_matrix.__str__()


if __name__ == '__main__':
    matrix_G = GaussMethod([[0, 1, 4, 0], [1, 2, -1, 0], [5, 8, 0, 0]])
    print(matrix_G)

    # Smena na dve redici
    matrix_G.swap(0, 1)
    print(matrix_G)

    # Mnozenje na redica so nekoj broj i dodavanje na druga
    matrix_G.scale_and_add(0, -5, 2)
    print(matrix_G)
