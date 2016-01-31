
# dato che ci serve matplotlib useremo python 2

import numpy
import pandas
from matplotlib import pyplot

# %pylab

dataframe = pandas.read_csv("cell_towers_diff-2016012100.csv")

coordinate = dataframe[['lon', 'lat']]

# %matplotlib inline

coordinate.plot(kind="scatter", x="lon", y="lat")

pyplot.show()




