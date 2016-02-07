
import pandas

dataframe = pandas.read_csv("../data/cell_towers.csv")

# from matplotlib import pyplot

isInItaly = dataframe.mcc == 222

isReliable = dataframe.samples > 1

italyDataframe = dataframe[isInItaly & isReliable]

# italyDataframe.plot(kind="scatter", x="lon", y="lat", label="Italy")

# pyplot.show()

italyDataframe


































