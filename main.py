# file principale di prova

print("Sistemi Complessi!")

# dato che ci serve matplotlib useremo python 2

import numpy
import pandas
from matplotlib import pyplot as plt

dataframe = pandas.read_csv("cell_towers_diff-2016012100.csv")

coordinate = dataframe[['lon', 'lat']]

# %matplotlib inline

plt.figure(); df.plot(); plt.legend(loc='best')

