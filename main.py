import numpy as np


def col_contains_trues(np_matrix, col_number, lead_element):
    for row in np_matrix[lead_element:]:
        if (row[col_number]) == 1:
            return True

    return False


def xor(np_matrix, lead_element, i):
    for j, (lead_col, col) in enumerate(zip(np_matrix[lead_element], np_matrix[i])):
        np_matrix[i][j] = (lead_col + col) % 2


def binary_echelon(mtx: [[int]]) -> [[int]]:
    np_matrix = np.array(mtx)
    rows, cols = np.shape(np_matrix)
    print(rows, cols)

    lead_element = 0

    for j in range(0, cols):
        if not col_contains_trues(np_matrix, j, lead_element):
            print("Skipped", np_matrix)
            continue

        flag = False
        for i in range(lead_element, rows):
            if np_matrix[i][j] == 1:
                # if lead_element == i:
                #     flag = True
                #     continue
                if not flag:
                    np_matrix[[i, lead_element]] = np_matrix[[lead_element, i]]
                    flag = True
                    print("Swapped matrix", i, j, lead_element, np_matrix)
                elif flag:
                    xor(np_matrix, lead_element, i)
                    print("Xor", np_matrix)
        lead_element += 1

    return np_matrix


def mian():
    matrix = [[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, ],
              [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, ],
              [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, ],
              [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, ],
              [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, ], ]

    mtx_result = binary_echelon(matrix)

    for row in mtx_result:
        print(' '.join(("{0:d}".format(int(x)) for x in row)))


if __name__ == '__main__':
    mian()
