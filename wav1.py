import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('rgut.wav')
print(fs)
print(data)
#t=np.arange(0,len(data)/fs,1.0/fs)
plt.plot(data)
plt.show()
wav.write('rgut.wav',2*fs,data)


