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

x_new=np.arange(x_data[0],x_data[len(x_data)-1],0.01)

#calculate cubicv spline
#x_new=np.arange(x_data)

#for iterator in range(len(z_data)):

#CALCULATE SPLINE FOR DATA SET
for iterator in range(len(z_data)):
    cubic_iterator=CubicSpline(x_data,z_data[iterator],bc_type='natural')(x_new)
    if(iterator==0):
        cubic_final=cubic_iterator
    else:
        cubic_final=np.vstack((cubic_final,cubic_iterator))

#mesh new coordinates for calculated spline and new x values
x_spline,y_spline=np.meshgrid(x_new,y_data)
print(cubic_final)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")

ax.plot_surface(x_spline,y_spline,cubic_final,cmap="plasma", linewidth=0, antialiased=False, alpha=0.5)
plt.show()