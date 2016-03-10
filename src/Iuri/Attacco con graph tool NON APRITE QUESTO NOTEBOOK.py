# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from graph_tool.all import *
import networkx
import matplotlib
from matplotlib import pyplot
import numpy
import pandas
import math
#import seaborn

#Costruzione grafo con graph-tool da matrice di adiacenza
def conversione(grafo, adiacenza):
    grafo.add_vertex(len(adiacenza))
    num_vertices = adiacenza.shape[0]
    for i in range(num_vertices - 1):
        for j in range(i + 1, num_vertices):
            if adiacenza[i,j] != 0:
                e = grafo.add_edge(i, j)
                
def costruzione(gestore):
    grafo = graph_tool.Graph(directed = False)
    adiacenza = numpy.genfromtxt("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_{0}.csv".format(gestore),delimiter=',',dtype='int')
    conversione(grafo, adiacenza)
    grafo.save("GTool{0}.xml".format(gestore))
    #graph_tool.draw.graph_draw(grafoTre)
gestore = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]

# <codecell>

def averageLength(grafo):
    istoLength = graph_tool.stats.distance_histogram(grafo)
    istoLength[1] = numpy.delete(istoLength[1], len(istoLength[1])-1)
    return numpy.average(istoLength[1], weights=istoLength[0])

def diameter(grafo):
    istoLength = graph_tool.stats.distance_histogram(grafo)
    return len(istoLength[0])-1

def clustering(grafo):
    cluster = graph_tool.clustering.local_clustering(grafo)
    array = numpy.array(cluster.a)
    return numpy.average(array)

def averageGrado(grafo):
    kmedio = graph_tool.stats.vertex_average(grafo, "total")
    return kmedio[0]

def criterion(grafo):
    kmedio = graph_tool.stats.vertex_average(grafo, "total")
    kmedioQuadro = numpy.power(kmedio, 2)
    criterion = (kmedioQuadro[0]+kmedioQuadro[1])/(kmedio[0])
    return criterion

def topologia(grafo):
    d = diameter(grafo)
    l = averageLength(grafo)
    C = clustering(grafo)
    k = averageGrado(grafo)
    c = criterion(grafo)
    return (d, l), C, (k, c)

# <codecell>

for compagnia in gestore:
    %time costruzione(compagnia)

# <codecell>

for compagnia in gestore:
    print compagnia
    grafo = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(gestore))
    topo = %time topologia(grafo)
    print topo, "\n"

# <codecell>

#PERCENT ATTACK!!
def attackPercent(compagnia, steps):
    grafoFinal = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(compagnia))

    graphSize = grafoFinal.num_vertices()
    passo = graphSize/float(steps)

    i = 0
    ascisse.append(i)
    aziendaFinal.append(compagnia)

    diametro.append(diameter(grafoFinal))
    cammino.append(averageLength(grafoFinal))
    cluster.append(clustering(grafoFinal))
    gradomedio.append(averageGrado(grafoFinal))
    criterio.append(criterion(grafoFinal))
    relSizeGC.append(1)
    
    
    # PROBLEMA: BISOGNA FARE IN MODO CHE NON CRASHI
    while (grafoFinal.num_vertices() > passo):
        istogradi = graph_tool.stats.vertex_hist(grafoFinal, "total")
        gradiFinal = pandas.DataFrame(istogradi[0], columns=['grado'])
        gradiFinal = pandas.DataFrame.reset_index(gradiFinal)
        gradiFinal.sort(["grado"], ascending=[False], inplace=True)
        sortedIDnode = gradiFinal['index'].values

        for identificativo in sortedIDnode:
            if (grafoFinal.num_vertices() > len(sortedIDnode) - passo):
                grafoFinal.remove_vertex(identificativo)

        giantCluster = graph_tool.topology.label_largest_component(grafoFinal)
        giantCluster = graph_tool.GraphView(grafoFinal, vfilt=giantCluster)

        i += 100/steps
        ascisse.append(i)
        aziendaFinal.append(compagnia)

        graphSize = grafoFinal.num_vertices()
        diametro.append(diameter(grafoFinal))
        cammino.append(averageLength(grafoFinal))
        cluster.append(clustering(grafoFinal))
        gradomedio.append(averageGrado(grafoFinal))
        criterio.append(criterion(grafoFinal))
        relSizeGC.append((giantCluster.num_vertices())/(float(graphSize)))

# <codecell>

#gestore = ["Tim", "Vodafone", "Wind", "Tre"]
gestore = "Tre"
diametro = []
cammino = []
cluster = []
gradomedio = []
criterio = []
relSizeGC = []

aziendaFinal = []
ascisse = []

#for compagnia in gestore:
#    %time attackPercent(compagnia, 10)

attackPercent(gestore, 10)

datiFinal = pandas.DataFrame()
datiFinal['percent'] = ascisse

datiFinal['provider'] = aziendaFinal
datiFinal['diameter'] = diametro
datiFinal['average path length'] = cammino
datiFinal['clustering'] = cluster
datiFinal['average degree'] = gradomedio
datiFinal['soglia percolativa'] = criterio

datiFinal['GCsize'] = relSizeGC
datiFinal.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/AttackDataForSeaborn.csv")
datiFinal.head()

