import numpy as np
from scipy.io import wavfile

fs = 44.1e3
t = np.arange(0, 1.0, 1.0/fs)

f1 = 440
f2 = 600

x = 0.5*np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

fname = 'output.wav'
wavfile.write( fname, fs, x )


fs, data = wavfile.read( fname )

print(fs, data[:10])