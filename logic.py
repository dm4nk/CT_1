import numpy as np


def print_mtrx(echelon_matrix: np.ndarray):
    for row in echelon_matrix:
        print(' '.join(("{0:d}".format(int(x)) for x in row)))


def col_contains_trues(np_matrix, col_number, lead_element):
    for row in np_matrix[lead_element:]:
        if (row[col_number]) == 1:
            return True

    return False


def xor(np_matrix, lead_element, i):
    for j, (lead_col, col) in enumerate(zip(np_matrix[lead_element], np_matrix[i])):
        np_matrix[i][j] = (lead_col + col) % 2


# 1.1
def ref(mtx: [[int]]) -> ([[int]], np.ndarray):
    np_matrix = np.array(mtx)
    rows, cols = np.shape(np_matrix)
    lead_elements = []
    lead_element_row = 0

    for j in range(0, cols):
        if not col_contains_trues(np_matrix, j, lead_element_row):
            continue

        flag = False
        for i in range(lead_element_row, rows):
            if np_matrix[i][j] == 1:
                if lead_element_row == i:
                    flag = True
                    continue
                if not flag:
                    np_matrix[[i, lead_element_row]] = np_matrix[[lead_element_row, i]]
                    flag = True
                elif flag:
                    xor(np_matrix, lead_element_row, i)
        lead_elements.append([lead_element_row, j])
        lead_element_row += 1

    return np_matrix, np.array(lead_elements)


def rref_from_echelon_matrix(echelon_matrix: np.ndarray, lead_elements: np.ndarray) -> ([[int]], np.ndarray):
    rows, cols = np.shape(echelon_matrix)

    lead_element = 0

    for j in range(0, cols):
        if not col_contains_trues(echelon_matrix, j, lead_element):
            continue

        for i in range(0, lead_element):
            if echelon_matrix[i][j] == 1:
                if lead_element == i:
                    continue
                xor(echelon_matrix, lead_element, i)
        lead_element += 1

    return echelon_matrix[~np.all(echelon_matrix == 0, axis=1)], lead_elements


# 1.2
def rref(mtx: [[int]]) -> ([[int]], np.ndarray):
    echelon_matrix, lead_elements = ref(mtx)
    return rref_from_echelon_matrix(echelon_matrix, lead_elements)
