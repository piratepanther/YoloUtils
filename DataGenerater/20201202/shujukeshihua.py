import numpy as np
import cv2
import random
import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits import mplot3d
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
#创建一个三维坐标轴
ax = plt.axes(projection='3d')

# img=np.zeros((20,20,1), np.uint8)


# in_path = 'J:/HRImage/20201214imageprocess/done/1.jpg'
in_path = 'J:/HRImage/20201214imageprocess/todo/tiechan/3-000001.jpg'

img = cv2.imread(in_path,0)

x = np.linspace(0, img.shape[1]-1, img.shape[1])
y = np.linspace(0, img.shape[0]-1, img.shape[0])

X, Y = np.meshgrid(x, y)
Z=img
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, edgecolor='none')


# ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('rainbow'))


ax.contourf(X, Y, Z, zdir='z',offset=-0.8, cmap='rainbow')
plt.contourf(X, Y, Z, 80, alpah = 0.75, cmap='rainbow')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# ax.set_title('surface')
plt.colorbar()
plt.show()
