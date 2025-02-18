import numpy as np

if __name__ == '__main__':
    # 1
    A = np.array([[1], [3], [4], [7]])
    B = np.array([[5], [2], [1], [2]])
    print(2 * A * B)
    # 2
    M = np.array([[1, 10, 4], [3, 4, 0]])
    N = np.array([[0, 2, 2], [7, 1, 5]])
    T = np.array([[1 / 2, 1, 0], [0, 1, 1 / 4]])
    print((M - N) * T)
    # 3
    n = int(input())
    array = []
    element = 0
    j = 0
    i = 0
    full_end = 2 ** (2 * n - 2)
    while True:
        row_end = 2 ** (n - 1 + i)
        if row_end > full_end:
            break
        tmp_array = []
        j = 0
        while True:
            element = 2 ** (i + j)
            if element > row_end:
                break
            tmp_array.append(element)
            j += 1
        array.append(tmp_array)
        i += 1
    Hn = np.array(array)
    In = np.eye(n)

    print((1/(n+1)) * Hn * In)
