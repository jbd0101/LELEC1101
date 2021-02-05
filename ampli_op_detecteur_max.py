
from scipy import signal

import matplotlib.pyplot as plot

import numpy as np



t = np.linspace(0, 2, 1000, endpoint=True)

plot.plot(t, (signal.square(2 * np.pi * 1 * t,)+1)*0.5)
plot.title('Ampli op, activé au maxima de la fréquence cardiaque (~1hz)')

plot.show()
