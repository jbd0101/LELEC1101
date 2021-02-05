import matplotlib.pyplot as plt
import numpy as np
from random import randint as rd
from scipy import signal

t = np.linspace(0, 4, 1000, endpoint=True)
F1 = 1
activateur = lambda t: (signal.square(2 * np.pi * F1 * t,)+1)*0.5
F2 = 1.5e3
son = lambda x: np.sin(2*np.pi*F2*x)
envoye = lambda x: np.sin(2*np.pi*F2*x)*((signal.square(2 * np.pi * F1 * t,)+1)*0.5)
plt.figure(1)
plt.plot(son(t))
plt.plot(activateur(t))
plt.figure(2)

plt.plot(son(t)*activateur(t))
plt.show()
