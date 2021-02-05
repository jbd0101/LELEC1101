import matplotlib.pyplot as plt
import numpy as np
from random import randint as rd


F = 1.5e3
main = lambda x: np.sin(2*np.pi*F*x)

table = np.linspace(0,2,1000)
plt.plot(main(table))
plt.show()
