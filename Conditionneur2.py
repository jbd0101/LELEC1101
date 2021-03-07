import matplotlib.pyplot as plt
import numpy as np
from random import randint as rd
from scipy import signal
from scipy.signal import hilbert

t = np.linspace(0, 4, 10000, endpoint=True)

son = 14*np.sin(2*np.pi*15*t)
square = 0.5*(signal.square(2*np.pi*t)+1)
noise1 =   2*np.sin(2*np.pi*4*t)
noise2 =   1*np.sin(2*np.pi*10*t+100)
noise3 =   1*np.sin(2*np.pi*13*t+3)
noise4 =   1*np.cos(2*np.pi*13*t+20)
Vin  = 4+son*square + (noise1 +noise2 + noise3 + noise4)
sansOffset = son*square + (noise1 +noise2 + noise3 + noise4)
post_passeBas = son*square + 0.3*(noise1 +noise2 + noise3 + noise4)



post_comp = 15*square

plt.figure(1)


plt.plot(t, Vin)
plt.xlabel("t [s]") ; plt.ylabel("V [V]") ; plt.ylim(-25,25)
plt.show()
plt.plot(t, sansOffset)
plt.xlabel("t [s]") ; plt.ylabel("V [V]") ; plt.ylim(-25,25)
plt.show()
plt.plot(t, post_passeBas)
plt.xlabel("t [s]") ; plt.ylabel("V [V]") ; plt.ylim(-25,25)
plt.show()
plt.plot(t, abs(hilbert(post_passeBas)))
plt.xlabel("t [s]") ; plt.ylabel("V [V]") ; plt.ylim(-1,20)
plt.show()
plt.plot(t, post_comp)
plt.xlabel("t [s]") ; plt.ylabel("V [V]") ; plt.ylim(-1,20)
plt.show()