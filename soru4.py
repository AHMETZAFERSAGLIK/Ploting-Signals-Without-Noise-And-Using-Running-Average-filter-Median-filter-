from matplotlib import pyplot as plt
import numpy as np

n=np.arange(-3,6)
x=[4,0,0,1,0,0,0,0,-1]
z=[0,-1,0,1,0,0,-7,0,0]
plt.xlabel("n")
plt.ylabel("x[n]")
#plt.plot(n,x)
#plt.plot(n,z)
y=np.convolve(x,z)
nson=np.arange(2*n[0],2*n[8]+1)
plt.plot(nson,y)
plt.show()
