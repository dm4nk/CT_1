import numpy as np

from logic import rref


class LinearCode:
    def __init__(self, matrix: [[int]]):
        self.__matrix, self.__lead_elements = rref(matrix)
        self.__rows, self.__cols = np.shape(self.__matrix)

        for row in self.__matrix:
            print(' '.join(("{0:d}".format(int(x)) for x in row)))

        print(self.__lead_elements[:, 1])

        self.__matr_2 = np.delete(self.__matrix, self.__lead_elements[:, 1], 1)

        for row in self.__matr_2:
            print(' '.join(("{0:d}".format(int(x)) for x in row)))
