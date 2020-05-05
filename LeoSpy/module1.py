#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt


#fig = plt.figure()
#ax1 = fig.add_subplot(111, projection= '3d')

#x=[1,2,3,4,5,6,7,8,9,10]
#y=[3,2,4,2,7,6,5,10,6,7]
#z=[6,2,5,4,5,2,3,9,7,8]  


#ax1.plot_wireframe(x,y,z)


#x=[1,2,3,4,5,6,7,8,9,10]
#y=[3,2,4,2,7,6,5,10,6,7]
#z=[6,2,5,4,5,2,3,9,7,8] 





#ax1.set_xlabel('X axis')
#ax1.set_ylabel('Y axis')
#ax1.set_zlabel('Z axis')

#plt.show()



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()

