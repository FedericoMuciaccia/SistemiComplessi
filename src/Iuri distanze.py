# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import geopy
from geopy import distance #TODO BUGGONE
import math
import itertools
import pandas
import numpy

# <codecell>

colosseo = (41.890173, 12.492331)
raccordo = [(41.914456, 12.615807),(41.990672, 12.502714),(41.793883, 12.511297),(41.812566, 12.396628),(41.956277, 12.384611)]
raggi = []

def geodesicDistance(A, B=colosseo):
    return geopy.distance.vincenty(A, B).meters

raggioTerra = 6371000
def euclidDistance(A, B=colosseo):
    x1 = raggioTerra*math.sin(math.pi-A[0])*math.cos(A[1])
    y1 = raggioTerra*math.sin(math.pi-A[0])*math.sin(A[1])
    z1 = raggioTerra*math.cos(math.pi-A[0])
    x2 = raggioTerra*math.sin(math.pi-B[0])*math.cos(B[1])
    y2 = raggioTerra*math.sin(math.pi-B[0])*math.sin(B[1])
    z2 = raggioTerra*math.cos(math.pi-B[0])
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

raggi = map(geodesicDistance, raccordo)
print raggi

raggi1= []
raggi1 = map(euclidDistance, raccordo)
print raggi1

raggiomedio = 0
for i in raggi:
	raggiomedio += i
raggiomedio /= len(raggi)
#raggiomedio = 11000
print raggiomedio
#print media

# <codecell>

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

# <codecell>

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
romacellid.to_csv("../data/roma_towers.csv")

#distanza = map(geodesicDistance, cell)
#def isInRome(point):
#    return geodesicDistance(point) <= raggiomedio
#filter(isInRome, cell)

# <markdowncell>

# ##TODO:  
# * Prendere array coordinate                                                           ✔
# * fare array distanze                                                                  ✔
# * mettere colonna distanze in dataframe  ✔
# * selezionare righe con variabile compresa entro raggiomedio                           ✔  
# * fare un nuovo dataframe  ✔
# * escludere tutti i nodi con 1 sample solo ✔
# * fare P(k)
# 
# ✔✔ggwpbb

# <markdowncell>

# Domande su iterazione su panda dataframe e efficienza, un tizio dice che la funzione iterrows è molto poco efficiente e sarebbe molto meglio usare un numpy array. Forse esistono funzioni più efficienti.
# http://stackoverflow.com/questions/10729210/iterating-row-by-row-through-a-pandas-dataframe
# http://stackoverflow.com/questions/7837722/what-is-the-most-efficient-way-to-loop-through-dataframes-with-pandas

# <codecell>


#dataframe = pandas.read_csv("../Siscomp_datas/cell_towers.csv")
dataframe = pandas.read_csv("../data/romaprova.csv")
#dataframe

#celle = dataframe[['cell', 'lat', 'lon', 'range']].values
#print celle
coordinate = dataframe[['lat', 'lon']].values
raggio = dataframe['range'].values

#print coordinate
#print raggio

def geodesicDistance(A, B):
    return geopy.distance.vincenty(A, B).meters
    #return geopy.distance.great_circle(A, B).meters
    
def euclidDistance(A, B):
    return math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)

def matricesuperiore(datiCoordinate, datiRaggi):
    a = numpy.zeros((datiRaggi.size,datiRaggi.size))
    for i in xrange(datiRaggi.size):
        for j in xrange(datiRaggi.size-i-1):
            if euclidDistance(datiCoordinate[i], datiCoordinate[j+i+1]) <= datiRaggi[i] + datiRaggi[j+i+1]:
#            if geodesicDistance(datiCoordinate[i], datiCoordinate[j+i+1]) <= datiRaggi[i] + datiRaggi[j+i+1]:
                a[i,j+i+1] = 1
                a[j+i+1,i] = 1
    return a
                
def matricetutta(datiCoordinate, datiRaggi):
    a = numpy.zeros((datiRaggi.size,datiRaggi.size))
    for i in xrange(datiRaggi.size):
        for j in xrange(datiRaggi.size):
            if geodesicDistance(datiCoordinate[i], datiCoordinate[j]) <= datiRaggi[i] + datiRaggi[j]:
                a[i,j] = 1
            if (i == j):
                a[i,j] = 0
    return a

%time adiacenzasopra = matricesuperiore(coordinate, raggio)

%time adiacenzatutta = matricetutta(coordinate, raggio)




#print adiacenzasopra
#print adiacenzatutta
            
#ridotto = dataframe[['cell', 'lat', 'lon', 'range']]        
#b = numpy.zeros((50,50))

#for i in ridotto.iterrows():
#    for j in ridotto.iterrows():
#        if linkVettori(i, j):
#            a[ridotto["index"],ridotto["index"]] = 1

            
            

# <markdowncell>

# Il primo tentativo è stato di fare la matrice di adiacenza a forza bruta. Con un campione di soli 50 nodi ci metteva pochi microsecondi, quindi abbiamo provato a fare la matrice di adiacenza delle 7000 antenne entro il raccordo anulare, notando che la compilazione durava tanto, facendo le dovute proporzioni abbiamo preventivato 2,5 ore di tempo di calcolo. La prima cosa che abbiamo sistemato è stato ovviamente fare un ciclo che calcolasse soltanto la metà superiore della matrice, dimezzando il tempo di calcolo. 
# 
# La prima cosa che abbiamo pensato di fare è stato di diagonalizzare a blocchi la matrice, o fare un ciclo di bassissimo livello che mettesse 0 a tutti gli elementi relativi alle antenne con $\Delta$Latitudine e/o $\Delta$Longitudine maggiori del range massimo del campione di dati. Il problema avuto è che il range delle antenne è tendenzialmente grande, con alcune che arrivano a 10km (con raggioRoma 11km)(e anche tanti samples), quindi non c'era modo di ridurre i calcoli. 
# 
# L'unica altra idea che abbiamo avuto è stata di non fare il calcolo complicato con la distanza sul geoide con il metodo vincenty. Primo passo è stato usare il metodo con great circles, l'altro è stato di considerare la porzione di Roma presa come un cerchio piano, calcolando quindi la distanza euclidea tra coordinate geografiche e convertendola in metri. E ci mette MOLTO meno tempo $\sim$10 volte in meno. Con un preventivo quindi di 10 minuti di tempo di calcolo invece di 1 ora e mezza.
# 
# TODO vedere parallelaizazione

# <markdowncell>

# con vincenti 
# $\sim$45 ms
# 
# con great circols
# $\sim$25 ms
# 
# con euclid
# $\sim$5 ms

# <codecell>


