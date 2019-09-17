import numpy as np
from scipy.optimize import fmin

x = 0
y = 0
parameters = [x,y]
goal = 100

def optimize(array):
    x = array[0]
    y = array[1]
    correct = x**2+5*x + 2*y**2+3*y
    objective = np.abs(correct-goal)
    return objective


optimize([0,0])

optimization = fmin(optimize,parameters,xtol=0.001)

print(optimization)
