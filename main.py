from logic import rref
from model import LinearCode


def mian():
    matrix = [[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, ],
              [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, ],
              [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, ],
              [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, ],
              [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, ], ]

    mtx_result = rref(matrix)[0]

    ln = LinearCode(matrix)


if __name__ == '__main__':
    mian()
