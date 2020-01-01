# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:47:32 2019

@author: flori
"""

##########################################################################

from scipy.stats import norm, binom

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from pandas import Series, DataFrame

# moegliche Werte von X
werte = np.array([0,10,11])
# X simulieren
sim = Series(np.random.choice(werte, size=1000, replace=True))
# Mehrere Grafiken neben- und untereinander
plt.subplot(4,2,1)
# Histogramm erstellen
sim.hist(bins=[0,1,10,11,12], edgecolor="black")
plt.title("Original")
plt.subplot(4,2,2)
# Normalplot erstellen
st.probplot(sim,plot=plt)
plt.title("Normal Q-Q Plot")


######################################


n = 5
# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))
#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,3)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 5 Beobachtungen")
plt.subplot(4,2,4)
st.probplot(sim_mean,plot=plt)
plt.title("Normal Q-Q Plot")
