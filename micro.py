import matplotlib.pyplot as plt
import numpy as np
from random import randint as rd
from scipy import signal

t = np.linspace(0, 4, 1000, endpoint=True)

son = 14*np.sin(2*np.pi*15*t)
square = 0.5*(signal.square(2*np.pi*t)+1)
noise1 =   2*np.sin(2*np.pi*4*t)
noise2 =   1*np.sin(2*np.pi*10*t+100)
noise3 =   1*np.sin(2*np.pi*13*t+3)
noise4 =   1*np.cos(2*np.pi*13*t+20)
output = son*square + noise1 +noise2 + noise3 + noise4
plt.figure(1)


plt.plot(t, output+4)
plt.figure(2)
plt.plot(t, output)
plt.show()
