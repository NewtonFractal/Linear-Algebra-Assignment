import numpy as np
from scipy.optimize import fmin
x1 = 0
x2 = 0
x3 = 0

parameters = np.array([x1, x2, x3])
goal = np.array([1,-1,1,-1])

def optimize(array):
    x1 = array[0]
    x2 = array[1]
    x3 = array[2]
    x = [x1,x2,x3]
    guess = np.array([[1,1,2],
                 [1,2,1],
                 [2,1,1],
                 [2,2,1]])
    objective = np.abs((guess@x)-goal)
    norm = np.linalg.norm(objective)
    return norm



optimization = fmin(optimize,parameters,xtol=0.001)

print(optimization)
