import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy.interpolate import CubicSpline, splrep, BSpline,splev

#Strain in dents may be estimated using data from ILI tools or from direct measurement of dent deformation contours. This project consists of testing relationship between the penalized sum of squares smoothing objective of the fitted spline versus calculated dent strain.
t=0.281 # WALL THICKNESS
#Channel width: (in)	1.1497

#adding x and y footage and channel numbers
Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/x_coordinates_Joint 216730 - Dent 000080.csv')
x_data=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/y_coordinates_Joint 216730 - Dent 000080.csv')
y_data=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/Joint 216730 - Dent 000080.csv')
z_data=np.genfromtxt(Data,delimiter=",",dtype=float)

#AXIAL DENT PROFILE and SPLINE CALCULATION
Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/x_coordinates_dent_80.csv')
x_data_dentprofile=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/x_coordinates_dent_80_inches.csv')
x_data_dentprofile_inches=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/y_coordinates_dent_80.csv')
y_data_dentprofile=np.genfromtxt(Data,delimiter=",",dtype=float)

dent_profile_splinecoefficients=splrep(x_data_dentprofile_inches,y_data_dentprofile,k=3,s=0.1)
dent_profile_spline=BSpline(*dent_profile_splinecoefficients,extrapolate=True)(x_data_dentprofile_inches)

#CIRCUMFERENTIAL DENT PROFILE
Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/x_circumferential_coordinates_dent_80.csv')
x_data_dentprofile_circum=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/y_circumferential_coordinates_dent_80.csv')
y_data_dentprofile_circum=np.genfromtxt(Data,delimiter=",",dtype=float)

x_circum=np.arange(x_data_dentprofile_circum[0],x_data_dentprofile_circum[len(x_data_dentprofile_circum)-1],0.1)

dent_profile_spline_circum_coeff=splrep(x_data_dentprofile_circum,y_data_dentprofile_circum,k=3,s=0.1)
dent_profile_spline_circum=BSpline(*dent_profile_spline_circum_coeff,extrapolate=True)(x_circum)




#SPLINE DERIVATIVES
dent_profile_spline_deriv=splev(x_data_dentprofile_inches,dent_profile_splinecoefficients,der=1)
dent_profile_spline_deriv2=splev(x_data_dentprofile_inches,dent_profile_splinecoefficients,der=2)

dent_profile_spline_circum_deriv=splev(x_circum,dent_profile_spline_circum_coeff,der=1)
dent_profile_spline_circum_deriv2=splev(x_circum,dent_profile_spline_circum_coeff,der=2)


#CREATING ARRAY OF RADIUS, STRAIN VALUES
radius=np.array(range(len(x_data_dentprofile_inches)),dtype=float) # MAKE ARRAY TYPE FLOAT
strain_long=np.array(range(len(x_data_dentprofile_inches)),dtype=float) # MAKE ARRAY

radius_circum=np.array(range(len(x_circum)),dtype=float) # MAKE ARRAY TYPE FLOAT FOR RADIUS - CIRCUMFERENTIAL
strain_circum=np.array(range(len(x_circum)),dtype=float) # MAKE ARRAY TYPE FLOAT FOR RADIUS - CIRCUMFERENTIAL
for derivator in range(len(dent_profile_spline_deriv)):

    radius[derivator]=(1+(dent_profile_spline_deriv[derivator])**2)**(3/2)/abs(dent_profile_spline_deriv2[derivator])
    strain_long[derivator] = t / (2 * (radius[derivator]))*100
    # if dent_profile_spline_deriv[derivator-1]>0:
    #     if dent_profile_spline_deriv[derivator]<0:
    #         print("x -distance", x_data_dentprofile_inches[derivator])
    #         print("int", derivator)
    #         print("radius", radius[derivator])
    #         print("strain", strain_long[derivator])
    #         print("---------------")
# count=1000
# start=0.03
# end=0.1
# s_values=np.arange(start,end,end/count)
# strain_long_test_variable=np.array([])
# radius_test_plot=np.array([])
# s_values_plot=np.array([])
# for smooth in range(len(s_values)):
#
#     dent_profile_splinecoefficients = splrep(x_data_dentprofile_inches, y_data_dentprofile, k=3, s=s_values[smooth])
#     dent_profile_spline = BSpline(*dent_profile_splinecoefficients, extrapolate=True)(x_data_dentprofile_inches)
#     dent_profile_spline_deriv = splev(x_data_dentprofile_inches, dent_profile_splinecoefficients, der=1)
#     dent_profile_spline_deriv2 = splev(x_data_dentprofile_inches, dent_profile_splinecoefficients, der=2)
#
#     radius_test=(1+(dent_profile_spline_deriv[731])**2)**(3/2)/abs(dent_profile_spline_deriv2[731])
#     strain_long_test= t / (2 * (radius_test))*100
#     s_values_plot=np.append(s_values_plot,[s_values[smooth]])
#     strain_long_test_variable=np.append(strain_long_test_variable,[strain_long_test])
#     radius_test_plot=np.append(radius_test_plot,[radius_test])

for derivator_circum in range(len(radius_circum)):
    radius_circum[derivator_circum]=(1+(dent_profile_spline_circum_deriv[derivator_circum])**2)**(3/2)/abs(dent_profile_spline_circum_deriv2[derivator_circum])
    strain_circum[derivator_circum]=(t/2)*((1/15)-(1/(radius_circum[derivator_circum])))*100

    # if dent_profile_spline_circum_deriv[derivator_circum-1]>0:
    #     if dent_profile_spline_circum_deriv[derivator_circum]<0:
    #         print("x -distance_circ", x_circum[derivator_circum])
    #         print("int_circ",derivator_circum)
    #         print("radius_circ",radius_circum[derivator_circum])
    #         print("strain_circ",strain_circum[derivator_circum])
    #         print("---------------")



#CIRCUMFERENTIAL DENT PROFILE AND SPLINE CALCULATION

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/x_circumferential_coordinates_dent_80.csv')
x_data_dentprofile_circum=np.genfromtxt(Data,delimiter=",",dtype=float)
Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/y_circumferential_coordinates_dent_80.csv')
y_data_dentprofile_circum=np.genfromtxt(Data,delimiter=",",dtype=float)


dent_profile_splinecoefficients_circum=splrep(x_data_dentprofile_circum,y_data_dentprofile_circum,k=3,s=1)
dent_profile_spline_circumferential=BSpline(*dent_profile_splinecoefficients_circum,extrapolate=True)(x_data_dentprofile_circum)

#Startup coordinates for visual x - footage and z - deflections and y will be the channel numbers
xx,yy=np.meshgrid(x_data,y_data)

x_new=np.arange(x_data[0],x_data[len(x_data)-1],0.01)

#calculate cubicv spline
#x_new=np.arange(x_data)

#for iterator in range(len(z_data)):

#CALCULATE SPLINE FOR DATA SET
for iterator in range(len(z_data)):
    spline_coefficients=splrep(x_data,z_data[iterator],k=3,s=0.1)
    spline=BSpline(*spline_coefficients,extrapolate=True)(x_new)
    if(iterator==0):
        cubic_final=spline
    else:
        cubic_final=np.vstack((cubic_final,spline))

#mesh new coordinates for calculated spline and new x values
x_spline,y_spline=np.meshgrid(x_new,y_data)

fig,(axis1,axis2) =plt.subplots(2,1)

axis1.set_ylabel('Inflection [inches]')
axis1.set_xlabel('Distance [ft]')
axis1.set_title('Axial Profile')
axis2.set_title('Circumferential Profile')
#ax = plt.axes(projection ='3d')
#ax.plot_surface(x_spline,y_spline,cubic_final,cmap="plasma", linewidth=0, antialiased=False, alpha=0.5)
x_data_dentprofile_feet=x_data_dentprofile_inches/12
axis1.plot(x_data_dentprofile_feet,y_data_dentprofile,".",color='green')
axis1.plot(x_data_dentprofile_feet,dent_profile_spline,color="black")




axis2.set_ylabel('Inflection [inches]')
axis2.set_xlabel('Channel')
axis2.plot(x_data_dentprofile_circum,y_data_dentprofile_circum,".",color="Green")
axis2.plot(x_circum,dent_profile_spline_circum,'-',color="black")


# axis3.plot(x_data_dentprofile_inches,strain_long)
# axis4.plot(x_circum,strain_circum)
# axis5.plot(s_values_plot,strain_long_test_variable)
# axis6.plot(s_values_plot,radius_test_plot)
plt.show()
