import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy.interpolate import splrep

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



print(len(z_data[0]))
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.plot_surface(xx,yy,z_data)
plt.show()