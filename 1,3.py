import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import fmin
norm_list_y = []
norm_list_x = []
for x in range(1,1000,5):
    x= x/100
    norm_list_x.append(x)
for a in range(1,1000,5):
    a = a/100
    Argument = np.array([0, 0, 0])
    y_transpose = np.array([[1],
                           [a],
                           [1],
                           [a]])

    def optimize(parameters):
        x1, x2, x3 = parameters[0], parameters[1], parameters[2]
        x = [x1, x2, x3]
        A = np.array([[1, 1, 2],
                      [1, 2, 1],
                      [2, 1, 1],
                      [2, 2, 1]])
        objective = np.abs((A @ x) - y_transpose)
        norm = np.linalg.norm(objective)
        return norm


    optimization = fmin(optimize, Argument, xtol=0.001)
    print(optimization)
    norm_list_y.append(np.linalg.norm(optimization))

print(norm_list_y)
plt.plot(norm_list_x,norm_list_y)
plt.ylabel('norm')
plt.xlabel('parameter value')
plt.show()
