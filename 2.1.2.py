import numpy as np

A = np.array([[1, 3, 2],
              [-3, 4, 3],
              [2, 3, 1]])


def recursive():
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 40):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
    vector = [a_n, b_n, c_n]
    limit = vector / np.linalg.norm(vector)
    q_n = np.matmul(np.matmul(vector, A), vector)
    print(q_n)


recursive()


def recursive_2():
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
    vector = np.array([a_n, b_n, c_n])
    normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
    limit = vector / normed
    print(limit)
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        vector = np.array([a_n, b_n, c_n])
        normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
        limit_2 = vector / normed
        epsilon = 10 ** (-8)
        diff = np.linalg.norm(limit - limit_2)
        if diff < epsilon:
            print(x)
            print(diff)
            break


recursive_2()

def recursive_3():
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
    vector = np.array([a_n, b_n, c_n])
    normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
    limit = vector / normed
    print(limit)
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        vector = np.array([a_n, b_n, c_n])
        normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
        limit_2 = vector / normed
        epsilon = 10 ** (-16)
        diff = np.linalg.norm(limit - limit_2)
        if diff < epsilon:
            print(diff)
            print(x)
            break

recursive_3()
