import numpy as np # Import the package to deal with number and math
import matplotlib.pyplot as plt# Import package helping us draw the graph
import math

def H(p1):
    return -(p1*np.log(p1)+(1-p1)*np.log(1-p1))
#--------------set the data set of x and y------------------
xlist = np.linspace(0.01,0.99,num=100)#create linear space of sample of x-axis,np.linspace(start,end,number of sample)
ylist = H(xlist)
#-------------plot the figure-------------------------------
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
#------------Add extra stuff-------------------------------
plt.title("n=2")
plt.xlabel("Probability")
plt.ylabel("Entopy")
plt.grid(True)#Show the net lines
plt.savefig("entropy_plot.png")