import matplotlib.pyplot as plt
import numpy as np
from random import randint as rd

offset = 0.5

F = 1
bruit = lambda x: (rd(-100,100) /900.0)*np.sin(400*x) + offset
main = lambda x: np.sin(2*np.pi*F*x)

table = np.linspace(0,2,1000)
plt.figure(1)
plt.plot(main(table)+bruit(table))
plt.figure(2)
plt.plot(main(table))
plt.show()
