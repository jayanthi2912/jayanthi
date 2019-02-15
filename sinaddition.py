import matplotlib.pyplot as plt
import numpy as np

fs=8000
f=1000
x=np.arange(1,50,0.2)
y=np.sin(2*np.pi*f*x/fs)
plt.subplot(3,1,1)
plt.plot(x,y)

y1=np.sin(2*np.pi*f*x/fs)
plt.subplot(3,1,2)
plt.plot(x,y1)
y3=y1+y
plt.subplot(3,1,3)
plt.plot(x,y3)

plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()
