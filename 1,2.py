import numpy as np
from scipy.optimize import fmin

parameters = np.array([0, 0, 0])
goal = np.array([1,-1,1,-1])

def optimize(array):
    x1,x2,x3 = array[0],array[1],array[2]
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
