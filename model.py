import numpy as np

from logic import ref, rref_from_echelon_matrix


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

    @staticmethod
    def int_to_bin_word_array(i: int, k: int):
        bin_str = format(i, 'b')
        n = k - len(bin_str)
        if n > 0:
            bin_str = ''.zfill(n) + bin_str
        return [int(digit_char) for digit_char in bin_str]

    # 1.4.2
    @staticmethod
    def get_all_code_words(k, n, mtrx):
        if k != mtrx.shape[0]:
            print("ERROR")
            exit(-1)
        code_words1 = LinearCode.get_code_words_from_g_and_k(k, mtrx)
        code_words2 = [np.array(row, dtype=int) for row in LinearCode.get_code_words_from_k(mtrx)]

        # print(code_words1)
        # print(code_words2)
        # print((np.array(code_words1) == np.array(code_words2)).all())

        return np.unique(code_words1, axis=0)

    @staticmethod
    def get_code_words_from_k(mtrx):
        k = mtrx.shape[0]
        n = mtrx.shape[1]
        words_by_sum = np.array([])

        idx = []
        for i in range(k):
            idx.append(i)
        sub_idx = LinearCode.sub_sets(idx)

        for sub in sub_idx:
            w = np.zeros(11)
            if sub:
                for i in sub:
                    w += mtrx[i]
            w %= 2
            words_by_sum = np.append(words_by_sum, w)

        words_by_sum = np.resize(words_by_sum, (2 ** k, n))
        words_by_sum = words_by_sum.astype(int)
        words_by_sum = np.unique(words_by_sum, axis=0)
        return words_by_sum

    # 1.4.2
    @staticmethod
    def get_code_words_from_g_and_k(k, mtrx):
        max_i = 2 ** k
        words = []
        for i in range(max_i):
            words.append(LinearCode.int_to_bin_word_array(i, k))
        words = np.array(words, dtype=int)
        code_words = []
        for word in words:
            res = word @ mtrx % 2
            code_words.append(res)
        return code_words

    @staticmethod
    def subsets_recur(current, x):
        if x:
            return LinearCode.subsets_recur(current, x[1:]) + LinearCode.subsets_recur(current + [x[0]], x[1:])
        return [current]

    # 1.4.1
    @staticmethod
    def sub_sets(arr):
        return LinearCode.subsets_recur([], sorted(arr))

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

    # 1.4
    @staticmethod
    def distance(mtrx, rows, cols):
        for i in range(0, rows - 1):
            for j in range(i + 1, rows):
                temp = sum((mtrx[i] + mtrx[j]) % 2)
                if temp < cols:
                    cols = temp
        return cols, cols - 1
