import scipy.constants as c
import numpy as np
from numpy import vstack,array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))
# SciPy basiert immer auf numpy
# arbeitet immer mit den arrays von Numpy
# Ist in viele einzelene subpackages

list = [1, 2, 3, 4]
arr = np.array(list)  # erstellt aus der Liste ein numpy array
print(arr)

zeros = np.zeros((3, 3))  # Erstellt ein Array mit 3 Zeilen mit jeweils 3 Nullen
ones = np.ones((3, 3))  # Erstellt ein Array mit 3 Zeilen mit jeweils 3 Einsern
arange = np.arange(7)  # Erstellt ein Array mit insgesamt 7 Elementen beginnend bei 0

dataType = np.arange(2, 12, dtype=float)
# Erstellt ein Array das bei 2 beginnt und 12 Elemente vom Typen float enthält

linspace = np.linspace(1., 4., 6)
# Erstellt ein Array mit 6 Elementen die gleichmäßig um start(1.) und endpunkt(4.) angeordnet sind
print(linspace)

matrix = np.matrix("1 2; 3 4")
print(matrix)

