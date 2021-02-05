import matplotlib.pyplot as plt
import numpy as np
from random import randint as rd
from scipy import signal

t = np.linspace(0, 4, 1000, endpoint=True)

son = 0.25*np.sin(2*np.pi*15*t)
square = 0.5*(signal.square(2*np.pi*t)+1)

plt.figure(1)
plt.plot(t,son)
plt.figure(3)
plt.plot(t,square)
plt.figure(2)

plt.plot(t, son*square)
plt.show()
