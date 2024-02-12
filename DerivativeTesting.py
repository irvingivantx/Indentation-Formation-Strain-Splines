import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, splrep, BSpline,splev

x = [1,3,5,8]
t = [2,3,9,10]

splinecoefficients=splrep(x,t,k=3,s=0)
x_interpolated=np.arange(1,8,0.1)
spline=BSpline(*splinecoefficients)(x_interpolated)

derviative1=splev(x_interpolated,splinecoefficients,der=1)
derviative2=splev(x_interpolated,splinecoefficients,der=2)
fig,(axis1,axis2)=plt.subplots(2,1)
radius=np.array(range(len(x_interpolated)),dtype=float)
for derivator in range(len(x_interpolated)):
    radius[derivator]=(1+(derviative1[derivator])**2)**(3/2)/(abs(derviative2[derivator]))
    if derviative1[derivator-1]>0:
        if(derviative1[derivator]<0):
            print(derivator)
            print(radius[derivator])
            print(2*3.14*radius[derivator])


axis1.plot(x_interpolated,spline)
axis1.plot(x_interpolated,derviative1)
axis1.plot(x_interpolated,derviative2)
axis2.plot(x_interpolated,radius)
axis1.plot(x,t,'*')
plt.show()