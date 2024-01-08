import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy.interpolate import CubicSpline

print("hello")

#adding x and y footage and channel numbers
Data=open('/Users/Irving/Documents/x_Joint 004220 - Dent 000187.csv')
x_data=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Documents/y_mesh_Joint 004220 - Dent 000187.csv')
y_data=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Documents/Mesh_Deflections_Joint 004220 - Dent 000187.csv')
z_data=np.genfromtxt(Data,delimiter=",",dtype=float)

#Startup coordinates for visual x - footage and z - deflections and y will be the channel numbers
xx,yy=np.meshgrid(x_data,y_data)
print(x_data[0])
x_new=np.arange(x_data[0],x_data[len(x_data)-1],0.5)
#calculate cubicv spline
#x_new=np.arange(x_data)

#for iterator in range(len(z_data)):
#CALCULATE SPOLINE FOR DATA SET
for iterator in range(len(z_data)):
    cubic_iterator=CubicSpline(x_data,z_data[0],bc_type='natural')(x_new)
    cubic_spline=np.stack(cubic_iterator)

plt.plot(x_new,cubic,'o', label=f'Test Profile')

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.plot_surface(xx,yy,z_data,cmap="plasma", linewidth=0, antialiased=False, alpha=0.5)
plt.show()