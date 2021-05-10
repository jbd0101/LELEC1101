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
n1 = 2  # the larger n is, the smoother curve will be
b1 = [1.0 / n1] * n1
a1 = 1
X, U, Y = readFile("mesures/NewFile2.csv")
U =  lfilter(b1,a1,U)
#Y =  lfilter(b,a,Y)
# plt.title('Signaux [AC] en sortie du transimpédance et après conditionneur 1')
plt.rcParams.update({'font.size': 30})
plt.xlabel('Temps [s]')
plt.ylabel('Tension [V]')
plt.plot(X, U,linewidth=3,label="Signal [AC] en sortie du bloc transducteur")
#plt.plot(X, Y,linewidth=1,label='Signal en sorite du conditionneur 1 ')
#plt.legend(loc='upper right')
plt.grid()
plt.show()
