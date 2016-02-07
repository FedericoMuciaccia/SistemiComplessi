# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## importazione del dataframe dai dati di Mozilla
# 
# TODO mettere il logo di Mozilla Stumbler e MLS (Mozilla Location Service)
# 
# TODO trascrivere la documentazione dettagliata dei label delle colonne dal sito di Mozilla

# <codecell>


# dato che ci serve matplotlib useremo python 2

# import numpy
# %pylab

import pandas

dataframe = pandas.read_csv("../data/cell_towers_diff-2016012100.csv")

# coordinate = dataframe[['lon', 'lat']]

# <codecell>

from matplotlib import pyplot

%matplotlib inline

dataframe.plot(kind="scatter", x="lon", y="lat")

# pyplot.show()

# <markdowncell>

# ## golocalizzazione

# <codecell>

import math

def euclideanDistace(x,y):
    return sqrt(x**2 + y**2)

# <codecell>

# import geopy # TODO AttributeError: 'module' object has no attribute 'distance'
from geopy import distance, geocoders

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
    # i dati si danno in (latitudine, longitudine), ma vanno intesi come (y, x)
    # ovvero vanno visualizzati come x=longitudine, y=latitudine
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

# <codecell>

name = "Sapienza, Roma"

print(geodesicDistance(geolocate(name)))
print(isInRome(geolocate(name)))

# <codecell>

copertura = dataframe[["range"]]

dataframe.plot(kind="scatter", x="lon", y="lat", s=copertura/1000) # TODO

# pyplot.show()

# <markdowncell>

# ## selezione dei dati
# 
# il filtraggio viene inizialmente fatto per mobile country code (Italy)
# ```python
# mcc = 222
# ```
# e successivamente vengono scartati i valori ritenuti inaffidabili, ovvero con soltanto una rilevazione
# ```python
# samples > 1
# ```

# <codecell>

isInItaly = dataframe.mcc == 222

isReliable = dataframe.samples > 1

# Crit3 = isInRome((dataframe.lat, dataframe.lon))

# AllCriteria = isInItaly & isReliable & Crit3

# dataframe[AllCriteria]

italia = dataframe[isInItaly & isReliable]

# TODO riordinare gli indici levando i buchi

# <codecell>

italia.plot(kind="scatter", x="lon", y="lat", label="Italy")

# pyplot.show()

# <markdowncell>

# Iuri ha fatto la selezione su Roma e ha creato un nuovo file csv  
# TODO integrare il suo codice
# 
# ```python
# # isInRome((dataframe.lat, dataframe.lon))
# 
# italyDataframe["lat"].apply(sum)
# 
# dataframe["distanze"] = arrayDistanzeCalcolate
# 
# .apply()
# .applymap()
# .resample()
# .transform()
# .groupby
# 
# code_groups[['data']].transform(sum)
# ```

# <codecell>

roma = pandas.read_csv("../data/roma_towers.csv")
roma.plot(kind="scatter", x="lon", y="lat", label="Roma PRELIMINARE")

# pyplot.show()

# TODO mettere il grafico quadrato e con le scale uguali
# e con le coordinate del colosseo al centro

# TODO mettere output del comando in SVG
# TODO mettere interattività, magari utilizzando Bokeh o mpld3

# vedere
# http://stackoverflow.com/questions/24525111/how-can-i-get-the-output-of-a-matplotlib-plot-as-an-svg
# https://nickcharlton.net/posts/outputting-matplotlib-plots.html

# <markdowncell>

# ## TODO Capocci
# 
# <ul>
# <li><input type="checkbox">dati MLS</li>
# <li><input type="checkbox" checked>filtro Roma</li>
# <li><input type="checkbox">grafo</li>
# <li><input type="checkbox">distribuzione del grado P(k)</li>
# <li><input type="checkbox">dati disaggregati per compagnia, canale radio, ecc</li>
# <li><input type="checkbox">soglia percolativa</li>
# </ul>

# <markdowncell>

# ## creazione del grafo con NetworkX
# 
# TODO si può anche fare un grafo pesato sull'intensità del segnale  
# 
# TODO:
# 
# * mettere sfondo allo scatterplot con mappa terrestre
# (farlo con le API di Google Maps o con quelle di OpenStreetMaps)
# 
# * provare API grafi per fare grafo delle antenne
# * aggiungere colonna database per distanze e coperture antenne
# 

# <codecell>

import networkx

G = networkx.Graph()
G.add_node("Fede")
G.add_node("Iuri")
G.add_edge(1,2)
G.add_edge('a','b')
G.add_edge('a','c')
G.add_edge('c','d')
G.add_edge('c','e')
G.add_edge('c','f')
G.add_edge('a','d')

# <codecell>

print(G.nodes())
print(G.edges())
position=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,position,node_size=300)
networkx.draw_networkx_edges(G,position,width=5)
networkx.draw_networkx_labels(G,position,font_size=15,font_family='sans-serif')
# pyplot.axis("off")

position

# <codecell>

H=networkx.path_graph(10)
networkx.draw_networkx_nodes(G,position,node_size=300)

# <codecell>

networkx.draw_random(G)

# <codecell>

dataframePiccolo = italia[0:10]
dataframePiccolo["cell"]

# <codecell>

dataframePiccolo = italia[0:10]

grafoPiccolo = networkx.Graph()
grafoPiccolo.add_nodes_from(dataframePiccolo["cell"])
# grafoPiccolo.add_nodes_from(dataframePiccolo.iterrows())
# grafoPiccolo.add_nodes_from(dataframePiccolo.itertuples())
networkx.draw(grafoPiccolo)

# <codecell>

import numpy
matriceDiAdiacenza = numpy.zeros((10,10))
# le matrici hanno indici che partono da zero

# <codecell>

matriceDiAdiacenza

# <codecell>


