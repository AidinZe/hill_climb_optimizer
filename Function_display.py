#Aidin_ze
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import math 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from matplotlib import pylab
from numpy import arange,array,ones
from scipy import stats
import matplotlib.ticker as mtick
import sys
import os
import numpy as np
import math
# the function that I'm going to plot
def z_func(x1,x2):
    return x1**2+x2**2 #your function

x1 = np.arange(5.0,-5.0,-0.1)
x2 = np.arange(-5.0,5.0,0.1)
X1,X2 = meshgrid(x1, x2) # grid of point
Z = z_func(X1, X2) # evaluation of the function on the grid


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X1, X2, Z, rstride=1, cstride=1, cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.view_init(elev=25, azim=-120)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
