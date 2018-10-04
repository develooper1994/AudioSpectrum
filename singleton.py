import pyaudio
import numpy as np
from scipy import signal
p = pyaudio.PyAudio()
volume=0.5
duration=10
f=400
wave=input("what is wave form?: ")
volume = int(input("how much volume(db)?: "))     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = int(input("how much time(second)?: "))   # in seconds, may be float
f = int(input("what is sound frequency(hz)?: "))        # sine frequency, Hz, may be float
# generate samples, note conversion to float32 array
if wave=='sin':
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
elif wave=='cos':
	samples = (np.cos(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
elif wave=='sin2':
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)**2).astype(np.float32)
elif wave=="squ":
	samples = (signal.square(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
elif wave=="saw":
	samples = (signal.sawtooth(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
# play. May repeat with different volume values (if done interactively)
stream.write(volume*samples)
stream.stop_stream()
stream.close()
p.terminate()