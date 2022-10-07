import numpy as np

from logic import rref, ref, rref_from_echelon_matrix


class LinearCode:

    # 1.3.1
    @staticmethod
    def ref(mtrx):
        return ref(mtrx)

    # 1.3.2
    @staticmethod
    def get_shape(mtrx):
        return np.shape(mtrx)

    # 1.3.3 step 1, 2
    @staticmethod
    def rref_from_echelon_mtrx(echelon_matrix, lead_elements):
        return rref_from_echelon_matrix(echelon_matrix, lead_elements)

    # 1.3.3 step 3
    @staticmethod
    def sub(mtrx, lead_elements):
        return np.delete(mtrx, lead_elements[:, 1], 1)

    # 1.3.3, step 4
    @staticmethod
    def append_e(mtrx, lead_elements):
        lead = lead_elements[:, 1]
        E = np.eye(len(mtrx[0]))

        n = len(E) + len(mtrx)
        H = []
        E_counter = 0
        X_counter = 0
        for i in range(n):
            if i in lead:
                H.append(mtrx[X_counter])
                X_counter += 1
            else:
                H.append(E[E_counter])
                E_counter += 1

        return np.array(H, dtype=int)

    # 1.4.2
    @staticmethod
    def get_all_code_words(k, mtrx):
        if k != mtrx.shape[0]:
            print("ERROR")
            exit(-1)

        def int_to_bin_word_array(i: int, k: int):
            bin_str = format(i, 'b')
            n = k - len(bin_str)
            if n > 0:
                bin_str = ''.zfill(n) + bin_str
            return [int(digit_char) for digit_char in bin_str]

        max_i = 2 ** k

        words = []
        for i in range(max_i):
            words.append(int_to_bin_word_array(i, k))
        words = np.array(words, dtype=int)

        code_words = []
        for word in words:
            res = word @ mtrx % 2
            code_words.append(res)

        return np.unique(code_words, axis=0)

    @staticmethod
    def check_code_words(code_words, mtrx):
        print("Checking code words")
        for word in code_words:
            res = word @ mtrx % 2
            if sum(res) > 0:
                print(f"Illegal code word = {word}, res = {res}")
                return False
        print("Code words are correct")
        return True

    #1.4
    @staticmethod
    def distance(mtrx, rows, cols):
        for i in range(0, rows - 1):
            for j in range(i + 1, rows):
                temp = sum((mtrx[i] + mtrx[j]) % 2)
                if temp < cols:
                    cols = temp
        return cols, cols - 1
