import geopy
from geopy import distance #TODO BUGGONE
import math
import itertools
import pandas
import numpy

colosseo = (41.890173, 12.492331)
raccordo = [(41.914456, 12.615807),(41.990672, 12.502714),(41.793883, 12.511297),(41.812566, 12.396628),(41.956277, 12.384611)]
raggi = []

def geodesicDistance(A, B=colosseo):
    return geopy.distance.vincenty(A, B).meters

raggi = map(geodesicDistance, raccordo)
print raggi
raggiomedio = 0
for i in raggi:
	raggiomedio += i
raggiomedio /= len(raggi)
#raggiomedio = 11000
print raggiomedio
#print media

dataframe = pandas.read_csv("../Siscomp_datas/cell_towers.csv")
#dataframe = pandas.read_csv("./romaprova.csv")
#dataframe
criterioMCC = dataframe.mcc == 222
criterioMinsamples = dataframe.samples > 1
italydoitcleaner = dataframe[criterioMCC & criterioMinsamples]
italydoitcleaner
#del italydoitcleaner['index']
italydoitcleaner = italydoitcleaner.reset_index()
#print italydoitcleaner

#inroma = pandas.DataFrame([[41.947416, 12.371001],
#                            [41.899392, 12.397436],
#                            [41.870510, 12.287917],
#                            [41.899648, 12.515196]], 
#                            columns=('lon', 'lat'))

#istruzione che fa selezione alcune righe con criteri su alcune colonne, 
#ne seleziona alcune e restituisce un array nompy di valori desiderati
coordinate = dataframe[criterioMCC & criterioMinsamples][['lat', 'lon']].values
#print coordinate

distanza = []
distanza = map(geodesicDistance, coordinate)
print len(distanza)

#da approfondire
#italydoitcleaner['distanze'] = italydoitcleaner[['lat', 'lon']].map(lambda x: geodesicDistance())
italydoitcleaner['distanze'] = distanza
italydoitcleaner
criterioRaccordo = italydoitcleaner.distanze < raggiomedio
romacellid = italydoitcleaner[criterioRaccordo]
romacellid = romacellid.reset_index()
romacellid.to_csv("roma_towers.csv")

#distanza = map(geodesicDistance, cell)
#def isInRome(point):
#    return geodesicDistance(point) <= raggiomedio
#filter(isInRome, cell)



#dataframe = pandas.read_csv("../Siscomp_datas/cell_towers.csv")
dataframe = pandas.read_csv("roma_towers.csv")
#dataframe

#celle = dataframe[['cell', 'lat', 'lon', 'range']].values
#print celle
coordinate = dataframe[['lat', 'lon']].values
raggio = dataframe['range'].values

#print coordinate
#print raggio

def geodesicDistance(A, B):
    return geopy.distance.vincenty(A, B).meters

def sommaRange(A, B):
    return A+B

def sonoLinkati(A, rangeA, B, rangeB):
    return geodesicDistance(A, B) <= sommaRange(rangeA, rangeB)

def linkVettori(rigA, rigB):
    return sonoLinkati((rigA['lat'], rigA['lon']), rigA['range'], (rigB['lat'], rigB['lon']), rigB['range'])

dimensioni = raggio.size
a = numpy.zeros((dimensioni,dimensioni))
print a

for i in xrange(raggio.size):
    for j in xrange(raggio.size):
        if geodesicDistance(coordinate[i], coordinate[j]) <= raggio[i] + raggio[j]:
            a[i,j] = 1

print a
#for i in celle:
#    for j in celle:
#        if linkVettori(i, j):
#            a[i,j] = 1

            
#ridotto = dataframe[['cell', 'lat', 'lon', 'range']]        
#b = numpy.zeros((50,50))

#for i in ridotto.iterrows():
#    for j in ridotto.iterrows():
#        if linkVettori(i, j):
#            a[ridotto["index"],ridotto["index"]] = 1

            
            
