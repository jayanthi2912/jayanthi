import matplotlib.pyplot as plt
import numpy as np
fs=1000
f1=100
f2=150
n=200
y=np.arange(n)
a=np.cos(2*np.pi*f1/fs*y)
plt.subplot(311)
plt.plot(y,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

b=np.cos(2*np.pi*f2/fs*y)
plt.subplot(312)
plt.plot(y,b)
z=a+b
plt.subplot(313)
plt.plot(y,z)
plt.title('addition of two waves')
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()


