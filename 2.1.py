import numpy as np

A = np.array([[1, 3,  2],
              [-3, 4, 3],
              [2, 3,  1]])

def recursive():
    a_n_1,a_n, b_n_1,b_n, c_n_1,c_n = 8, 41, 3, 24, 12, 37
    for x in range(0,40):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
    vector = [a_n,b_n,c_n]
    limit = vector/np.linalg.norm(vector)
    print(limit)
    Step_1 = np.matmul(vector,A)
    q_n  = np.matmul(Step_1,vector)
    print(q_n)
    a_n_1,a_n, b_n_1,b_n, c_n_1,c_n = 8, 41, 3, 24, 12, 37
    for x in range(0,40):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        vector = [a_n, b_n, c_n]
        if np.linalg.norm(vector - limit) < 10**(-8):
            print(x)

recursive()