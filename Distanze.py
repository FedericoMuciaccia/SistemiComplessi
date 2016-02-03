
import geopy
from geopy import distance #TODO BUGGONE
import math
import itertools

colosseo = (41.890173, 12.492331)
raccordo = [(41.914456, 12.615807),(41.990672, 12.502714),(41.793883, 12.511297),(41.812566, 12.396628),(41.956277, 12.384611)]
raggi = []

def geodesicDistance(A, B=colosseo):
    return geopy.distance.vincenty(A, B).meters

raggi = map(geodesicDistance, raccordo)

raggiomedio = 0
for i in raggi:
	raggiomedio += i
raggiomedio /= len(distanza)
raggiomedio = 11000
#print distanza
#print media

import pandas
dataframe = pandas.read_csv("copiaprova.csv")
#dataframe


distanza = []
#dataframe['lon'] == "Noise - Street/Sidewalk"
coordinate = dataframe[dataframe.lat > 0][dataframe.lon > 0][['lon', 'lat']].values
#inroma = pandas.DataFrame([[41.947416, 12.371001],
#                            [41.899392, 12.397436],
#                            [41.870510, 12.287917],
#                            [41.899648, 12.515196]], 
#                            columns=('lon', 'lat'))


distanza = map(geodesicDistance, coordinate)


def isInRome(point):
    return geodesicDistance(point) <= raggiomedio
#latitudini = dataframe[dataframe.lat > 0][['lat']].values
#longitudini = dataframe[dataframe.lat > 0][['lat']].values 

#coordinate = (latitudini, longitudini)
a = isInRome((41.899903, 12.503008))
print geodesicDistance((41.899903, 12.503008))
print raggiomedio
print a
filter(isInRome, coordinate)
#isInRome(colosseo)