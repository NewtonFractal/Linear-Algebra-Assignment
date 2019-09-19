import numpy as np
from scipy.optimize import fmin

Argument = np.array([0, 0, 0])
y = np.array([1,-1,1,-1])

def optimize(parameters):
    x1,x2,x3 = parameters[0],parameters[1],parameters[2]
    x = [x1,x2,x3]
    A = np.array([[1,1,2],
                 [1,2,1],
                 [2,1,1],
                 [2,2,1]])
    objective = np.abs((A@x)-y)
    norm = np.linalg.norm(objective)
    return norm

optimization = fmin(optimize,Argument,xtol=0.001)

print(optimization)
