import matplotlib.pyplot as plt
import numpy as np

fs=8000
f=1000
x=np.arange(-200,200,0.1)
p1=90
y=np.sinc((2*np.pi*f*x/fs)+p1)
plt.subplot(3,1,1)
plt.plot(x,y)
p2=90
y1=np.sinc((2*np.pi*f*x/fs)+p2)
plt.subplot(3,1,2)
plt.plot(x,y1)
y3=y1+y
plt.subplot(3,1,3)
plt.plot(x,y3)

plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()
