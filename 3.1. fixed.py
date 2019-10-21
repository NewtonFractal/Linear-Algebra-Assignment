from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def equation_solver(x_3):
    x_1 = x_3[0]
    x_2 = x_3[1]
    zeroes = np.zeros(2)
    zeroes[0] = (2*x_1-5*x_2+((27*(x_1**2)+2)**(1/2)))/2
    zeroes[1] = (2*x_1-5*x_2-((27*(x_1**2)+2)**(1/2)))/2
    return zeroes

x = np.linspace(-1, 1, 300)
y = np.linspace(-1, 1, 300)

X, Y = np.meshgrid(x, y)
Z = fsolve(equation_solver,[1.0,1.0])

Z = np.linalg.norm(Z)

print(Z)

print(Z.shape)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green')

plt.show()
