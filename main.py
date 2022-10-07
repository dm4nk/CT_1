import numpy as np

from logic import rref, print_mtrx
from model import LinearCode


def mian():
    S = [[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, ],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, ],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, ],
         [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, ],
         [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, ], ]

    S_ref, lead_elements = LinearCode.ref(S)
    G, lead_elements = LinearCode.rref_from_echelon_mtrx(S_ref, lead_elements)
    print_mtrx(G)
    X = LinearCode.sub(G, lead_elements)
    rows, cols = LinearCode.get_shape(X)
    # print_mtrx(X)
    H = LinearCode.append_e(X, lead_elements)
    # print_mtrx(H)

    code_words = LinearCode.get_all_code_words(rows, G)
    code_words = np.array([list(word) for word in code_words])

    LinearCode.check_code_words(code_words, H)

    d, t = LinearCode.distance(G, rows, cols)
    print(f"Distance: d={d}, t={t}")

    e1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0])  # found
    e2 = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # not found
    v = code_words[0]
    v_p_e = (v + e2) % 2
    code_words[0] = v_p_e

    LinearCode.check_code_words(code_words, H)


if __name__ == '__main__':
    mian()
