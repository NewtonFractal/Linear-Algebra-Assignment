from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def equation_solver(x_1,x_2):
    x_3_pos = (2*x_1-5*x_2+((27*(x_1**2)+2)**(1/2)))/2
    x_3_neg = (2*x_1-5*x_2-((27*(x_1**2)+2)**(1/2)))/2
    return [x_3_pos,x_3_neg]

x = np.linspace(-1, 1, 300)
y = np.linspace(-1, 1, 300)

X, Y = np.meshgrid(x, y)
Z = equation_solver(X,Y)[0]


fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green')

plt.show()

Z = equation_solver(X,Y)[1]

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green')

plt.show()

