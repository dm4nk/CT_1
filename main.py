import numpy as np

from logic import print_mtrx
from model import LinearCode


def mian():
    S = [[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, ],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, ],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, ],
         [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, ],
         [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, ], ]

    S_ref, lead_elements = LinearCode.ref(S)
    # print_mtrx(S_ref)
    G, lead_elements = LinearCode.rref_from_echelon_mtrx(S_ref, lead_elements)
    # print_mtrx(G)
    X = LinearCode.sub(G, lead_elements)
    rows, cols = LinearCode.get_shape(X)
    # print_mtrx(X)
    H = LinearCode.append_e(X, lead_elements)
    print_mtrx(H)

    code_words = LinearCode.get_all_code_words(rows, cols, G)
    code_words = np.array([list(word) for word in code_words])

    LinearCode.check_code_words(code_words, H)

    d, t = LinearCode.distance(G, rows, cols)
    print(f"Distance: d={d}, t={t}")

    # e1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0])
    # v = code_words[0]
    # v_p_e = (v + e1) % 2
    # code_words[0] = v_p_e
    #
    # LinearCode.check_code_words(code_words, H)

    # e1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    # v = code_words[8]
    # v_p_e = (v + e1) % 2
    # code_words[8] = v_p_e
    #
    # LinearCode.check_code_words(code_words, H)

    # found error
    for j in range(1, 2 ** 10):
        e2 = LinearCode.int_to_bin_word_array(j, 11)
        if sum(e2) > 2:
            continue
        for i in range(0, len(code_words)):
            v = code_words[i]
            v_p_e = (v + e2) % 2
            code_words[i] = v_p_e
            if LinearCode.check_code_words(code_words, H):
                print("FOUND: ", e2)
            code_words[i] = v




if __name__ == '__main__':
    mian()
