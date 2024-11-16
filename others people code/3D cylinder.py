#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin, cos, pi

fig = plt.figure(figsize = (4,4))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2,2) 
ax.set_ylim(-2,2) 
ax.set_zlim(0,2) 
theta = np.linspace(-1*pi,1*pi, 700)
Z = np.linspace(0,1,700)
Z,theta = np.meshgrid(Z, theta)
R = 1
X = (R*np.cos(theta))
Y = (R*np.sin(theta))
ax.plot_surface(X,Y,Z,linewidth = 0,facecolor = 'r', shade = True, alpha = 0.6)
plt.show()