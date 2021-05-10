from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
R1 = 3.3e6
C1 = 100e-9
R2 = 200e3
C2 = 100e-9
R4 = 2.2e6
R3 = 4e3
BPM1= 6.283 #6OBPM
BPM2 = 21 #200BPM

f = np.linspace(0.1,50,10000)
w= 2*np.pi*f
G = (1+R4/R3)*(w*1j*C1*R1)/((w*1j*C2*R2+1)*(w*1j*R1*C1+1))
GB1 = (1+R4/R3)*(BPM1*1j*C1*R1)/((BPM1*1j*C2*R2+1)*(BPM1*1j*R1*C1+1))
GB2 = (1+R4/R3)*(BPM2*1j*C1*R1)/((BPM2*1j*C2*R2+1)*(BPM2*1j*R1*C1+1))
plt.figure(1)
plt.ylim([42,57])
plt.semilogx(w,20*np.log10(abs(G)))
a = plt.stem([BPM1],[20*np.log10(abs(GB1))],linefmt="C1--",markerfmt="C1o")
b = plt.stem([BPM2],[20*np.log10(abs(GB2))],linefmt="C1--",markerfmt="C1o")
plt.legend([a,b],["60BPM","200BPM"], loc='upper right')

plt.grid(which="both")
plt.xlabel("w [rad/s]")
plt.ylabel("Gain [dB]")
plt.show()
