Yewon Kang,202303141,computer engineering,sophomore of Hufs


import numpy as np
import matplotlib.pyplot as plt

u=[5,9,6]
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.set_xlim(-1,10)
ax.set_ylim(-10,10)
ax.set_xlim(0,10)
start=[0,0,0]
ax.quiver(start[0],start[1],start[2],u[0],u[1],u[2],color='r')
