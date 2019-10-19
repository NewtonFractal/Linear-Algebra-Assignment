import numpy as np
import matplotlib.pyplot as plot

x_values = []
epsilon_values = []


A = np.array([[1, 3, 2],
              [-3, 4, 3],
              [2, 3, 1]])

def recursive():
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        vector = np.array([a_n, b_n, c_n])
        normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
        limit = vector / normed
        q_n = np.matmul(np.matmul(limit, A),limit)
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(1, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        vector = np.array([a_n, b_n, c_n])
        normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
        limit = vector / normed
        q_n_2 = np.matmul(np.matmul(limit, A),limit)
        x_values.append(x)
        epsilon_values.append(abs(4-q_n_2))
        if abs(4-q_n_2) < 10**(-8):
            print(x)
            break
    for x in range(x+1, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        vector = np.array([a_n, b_n, c_n])
        normed = ((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)
        limit = vector / normed
        q_n_2 = np.matmul(np.matmul(limit, A),limit)
        x_values.append(x)
        epsilon_values.append(abs(4 - q_n_2))
        if abs(4 - q_n_2) < 10**(-16):
            print(x)
            return None

recursive()

plot.xlabel('Iterates')
plot.ylabel('Epsilon')
plot.semilogy(x_values, epsilon_values)
plot.show()

