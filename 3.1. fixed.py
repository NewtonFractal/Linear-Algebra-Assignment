from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

x = np.linspace(-1, 1, 300)
y = np.linspace(-1, 1, 300)

X, Y = np.meshgrid(x, y)
Z = (2*Y-5*X+((27*(X**2)+2)**(1/2)))/2


fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green')

plt.show()
