import numpy as np
import matplotlib.pyplot as plot

normed_values = []
x_values = []

A = np.array([[1, 3, 2],
              [-3, 4, 3],
              [2, 3, 1]])

def recursive():
    a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = 8, 41, 3, 24, 12, 37
    for x in range(0, 500):
        a_n_1, a_n, b_n_1, b_n, c_n_1, c_n = a_n, a_n_1 + 3 * b_n_1 + 2 * c_n_1, b_n, -3 * a_n_1 + 4 * b_n_1 + 3 * c_n_1, c_n, 2 * a_n_1 + 3 * b_n_1 + c_n_1
        normed_values.append(((a_n ** 2) + (b_n ** 2) + (c_n ** 2)) ** (1 / 2)), x_values.append(x)

recursive()

plot.xlabel('Iterates')
plot.ylabel('Normed Value')
plot.semilogy(x_values, normed_values)
plot.show()
