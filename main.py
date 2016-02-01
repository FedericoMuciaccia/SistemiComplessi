
# dato che ci serve matplotlib useremo python 2

# import numpy
# %pylab

import pandas

dataframe = pandas.read_csv("cell_towers_diff-2016012100.csv")

# coordinate = dataframe[['lon', 'lat']]

#####################################

from matplotlib import pyplot

%matplotlib inline

dataframe.plot(kind="scatter", x="lon", y="lat")

# pyplot.show()

######################################

import math

def euclideanDistace(x,y):
    return sqrt(x**2 + y**2)

######################################

import geopy

# distanze in km
# geopy.distance.vincenty(A, B) # su sferoide oblato
# geopy.distance.great_circle(A, B) # sulla sfera

# punti di prova
# A = (41.49008, -71.312796)
# B = (41.499498, -81.695391)

def geolocate(place): # string
    """
    return coordinates for addresses and toponyms
    """
    geolocator = geopy.geocoders.Nominatim()
    location = geolocator.geocode(place)
    return (location.latitude, location.longitude) # coordinate
    
def geodesicDistance(A, B = geolocate("Colosseo")):
    """
    return the Vincenty's geodesic distance in meters
    default place = Colosseum
    """
    # colosseo = (41.890183, 12.492369)
    return geopy.distance.vincenty(A, B).meters

def isInRome(place):
    """
    return True if the place is less than 10 km away from Colosseum
    """
    raggioRaccordoAnulare = 10000 # in metri
    return geodesicDistance(place) <= raggioRaccordoAnulare

######################################

name = "Sapienza, Roma"

print(geodesicDistance(geolocate(name)))
print(isInRome(geolocate(name)))

######################################

copertura = dataframe[["range"]]

dataframe.plot(kind="scatter", x="lon", y="lat", s=copertura/1000) # TODO

######################################



