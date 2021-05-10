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
n = 8  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1

def readFile(filename, offset=0):
    X, U, Y = [], [], []
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            X.append(float(row[0])*5e-3)
            U.append(float(row[1]))
            Y.append(float(row[2]))
    return X, U, Y


#####################################################
# Les paramètres
#####################################################


#####################################################
# Main
#####################################################

X, U, Y = readFile("mesures/NewFile1.csv")
U =  lfilter(b,a,U)
Y =  lfilter(b,a,Y)
# plt.title('Signaux bloc conditionneur')
plt.xlabel('Temps [s]')
plt.ylabel('Tension [V]')
plt.plot(X, U,linewidth=1,label="Signal en sortie du bloc")
plt.plot(X, Y,linewidth=1,label='Signal du bloc 1 après filtrage')
plt.grid()
plt.legend(loc='upper right')
plt.show()
