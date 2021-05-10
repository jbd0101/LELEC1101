# LEPL1502 - Projet 2
#
# Ce programme sert à récupérer des données du Picoscope afin de les
# plot sur un graphe
#
# Vincent Bauffe, 2020

import csv
import matplotlib
import matplotlib.pyplot as plt

from scipy.signal import lfilter
# n = 8  # the larger n is, the smoother curve will be
# b = [1.0 / n] * n
# a = 1

def readFile(filename, offset=0):
    X, U, Y = [], [], []
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        for row in reader:
            X.append(float(row[0]))
            Y.append(float(row[1]))
            U.append(float(row[2])*50+50*6)
    return X, U, Y


#####################################################
# Les paramètres
#####################################################


#####################################################
# Main
#####################################################
n1 = 2  # the larger n is, the smoother curve will be
b1 = [1.0 / n1] * n1
a1 = 1
X, U, Y = readFile("simu/transd.txt")
# U =  lfilter(b1,a1,U)
# Y =  lfilter(b,a,Y)
# plt.title('Sortie du bloc transimpédance [AC]')
plt.xlabel('Temps [s]')
plt.ylabel('Tension [V]')
plt.plot(X, U,linewidth=1,label="Signal [AC] en sortie du transimpédance (x50)")
plt.plot(X, Y,linewidth=1,label='Signal en sortie du conditionneur 1 ')
plt.xlim([0,4])
plt.legend(loc='upper right')
plt.grid()
plt.show()
