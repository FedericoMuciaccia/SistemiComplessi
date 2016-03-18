# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Attacco e failure con Graph-tool

# <markdowncell>

# ###Importo librerie e definisco funzioni fondamentali

# <codecell>

from graph_tool.all import *
import matplotlib
from matplotlib import pyplot
import numpy
import pandas
import math
#import seaborn


gestore = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]
colori = ['#004184','#ff3300','#ff8000','#018ECC', '#4d4d4d']

# <codecell>

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

# <codecell>

#funzioni topologiche
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

# <markdowncell>

# ### Cicli input/output gafi

# <codecell>

#Eseguire soltanto la prima volta per costruire e salvare le reti
for compagnia in gestore:
    %time costruzione(compagnia)

# <markdowncell>

# ## Analisi preliminare delle reti

# <codecell>

def topologia(compagnia):
    azienda = []
    diametro = []
    cammino = []
    cluster = []
    relSizeGC = []
    gradomedio = []
    criterio = []
    fcritica = []

    grafo = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(compagnia))
    
    def gradonodo(identificativo):
        vertice = grafo.vertex(identificativo)
        return vertice.out_degree()

    def kmedio(listadeg):
        return numpy.mean(listadeg)
    
    def kquadromedio(listadeg):
        listadegQuadri = numpy.power(listadeg, 2)
        return numpy.mean(listadegQuadri)
    
    def freqCriterion(criterion):
        return 1-(1/(criterion-1))
    
    graphSize = grafo.num_vertices()
    giantCluster = graph_tool.topology.label_largest_component(grafo)
    giantCluster = graph_tool.GraphView(grafo, vfilt=giantCluster)
    
    azienda.append(compagnia)
    diametro.append(diameter(grafo))
    cammino.append(averageLength(grafo))
    cluster.append(clustering(grafo))
    relSizeGC.append((giantCluster.num_vertices())/(float(graphSize)))

    indice = numpy.arange(grafo.num_vertices())
    listaGradi = map(gradonodo, indice)
        
    gradomedio.append(kmedio(listaGradi))
    criterion = kquadromedio(listaGradi)/kmedio(listaGradi)
    criterio.append(criterion)
    fcritica.append(freqCriterion(criterion))

# <codecell>

# caricamento rete e studio topologico iniziale
for compagnia in gestore:
    %time topologia(compagnia)

datiInitial = pandas.DataFrame()
datiInitial['Rete'] = azienda
datiInitial['GC %'] = relSizeGC
datiInitial['D'] = diametro
datiInitial['<l>'] = cammino
datiInitial['C'] = cluster
datiInitial['<k>'] = gradomedio
datiInitial['<k^2>/<k>'] = criterio
datiInitial['f'] = fcritica

datiInitial.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/DatiIniziali.csv")

# <codecell>

datiInitial

# <markdowncell>

# # Simulazione attacco, andamento grandezze topologiche in funzione dei nodi rimossi

# <codecell>

#PERCENT ATTACK!!
def attackPercent(compagnia, steps):
    grafoFinal = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(compagnia))

    def gradonodo(identificativo):
        vertice = grafoFinal.vertex(identificativo)
        return vertice.out_degree()

    def kmedio(listadeg):
        return numpy.mean(listadeg)
    
    def kquadromedio(listadeg):
        listadegQuadri = numpy.power(listadeg, 2)
        return numpy.mean(listadegQuadri)
    
    graphSize = grafoFinal.num_vertices()
    passo = graphSize/steps

    i = 0
    ascisse.append(i)
    aziendaFinal.append(compagnia)

    diametro.append(diameter(grafoFinal))
    cammino.append(averageLength(grafoFinal))
    cluster.append(clustering(grafoFinal))
    
    indice = numpy.arange(graphSize)
    listaGradi = map(gradonodo, indice)

    gradomedio.append(kmedio(listaGradi))
    criterion = kquadromedio(listaGradi)/kmedio(listaGradi)
    criterio.append(criterion)
    relSizeGC.append(1)
    
    while (grafoFinal.num_vertices() > passo):    
        gradiFinal = pandas.DataFrame(listaGradi, columns=['grado'])
        gradiFinal = pandas.DataFrame.reset_index(gradiFinal)
        gradiFinal.sort(["grado"], ascending=[False], inplace=True)
        sortedIDnode = gradiFinal['index'].values

        daRimuovere = numpy.take(sortedIDnode, range(passo))
        grafoFinal.remove_vertex(daRimuovere)

        giantCluster = graph_tool.topology.label_largest_component(grafoFinal)
        giantCluster = graph_tool.GraphView(grafoFinal, vfilt=giantCluster)
        grafoFinal = Graph(grafoFinal, prune = True)
        
        graphSize = graphSize-passo
        i += 100/steps
        ascisse.append(i)
        aziendaFinal.append(compagnia)
        
        
        diametro.append(diameter(grafoFinal))
        cammino.append(averageLength(grafoFinal))
        cluster.append(clustering(grafoFinal))
        relSizeGC.append((giantCluster.num_vertices())/(float(graphSize)))
        
        indice = numpy.arange(grafoFinal.num_vertices())
        listaGradi = map(gradonodo, indice)
        
        gradomedio.append(kmedio(listaGradi))
        criterion = kquadromedio(listaGradi)/kmedio(listaGradi)
        criterio.append(criterion)

#PERCENT FAILURE!!
def failurePercent(compagnia, steps):
    grafoFinal = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(compagnia))

    def gradonodo(identificativo):
        vertice = grafoFinal.vertex(identificativo)
        return vertice.out_degree()

    def kmedio(listadeg):
        return numpy.mean(listadeg)
    
    def kquadromedio(listadeg):
        listadegQuadri = numpy.power(listadeg, 2)
        return numpy.mean(listadegQuadri)
    
    graphSize = grafoFinal.num_vertices()
    passo = graphSize/steps

    i = 0
    ascisse.append(i)
    aziendaFinal.append(compagnia)

    diametro.append(diameter(grafoFinal))
    cammino.append(averageLength(grafoFinal))
    cluster.append(clustering(grafoFinal))
    
    indice = numpy.arange(graphSize)
    listaGradi = map(gradonodo, indice)

    gradomedio.append(kmedio(listaGradi))
    criterion = kquadromedio(listaGradi)/kmedio(listaGradi)
    criterio.append(criterion)
    relSizeGC.append(1)
    
    while (grafoFinal.num_vertices() > passo): 
        gradiFinal = pandas.DataFrame(listaGradi, columns=['grado'])
        gradiFinal = pandas.DataFrame.reset_index(gradiFinal)
        randomante = gradiFinal['index'].values
        randomante = numpy.random.permutation(randomante)

        daRimuovere = numpy.take(randomante, range(passo))
        grafoFinal.remove_vertex(daRimuovere)

        giantCluster = graph_tool.topology.label_largest_component(grafoFinal)
        giantCluster = graph_tool.GraphView(grafoFinal, vfilt=giantCluster)
        grafoFinal = Graph(grafoFinal, prune = True)
        
        graphSize = graphSize-passo
        i += 100/steps
        ascisse.append(i)
        aziendaFinal.append(compagnia)
        
        
        diametro.append(diameter(grafoFinal))
        cammino.append(averageLength(grafoFinal))
        cluster.append(clustering(grafoFinal))
        relSizeGC.append((giantCluster.num_vertices())/(float(graphSize)))
        
        indice = numpy.arange(grafoFinal.num_vertices())
        listaGradi = map(gradonodo, indice)
        
        gradomedio.append(kmedio(listaGradi))
        criterion = kquadromedio(listaGradi)/kmedio(listaGradi)
        criterio.append(criterion)

# <codecell>

gestore = ["Tim", "Vodafone", "Wind", "Tre"]
#gestore = ["Roma"]
#compagnia = "Tre"

indice = []
diametro = []
cammino = []
cluster = []
gradomedio = []
criterio = []
relSizeGC = []

aziendaFinal = []
ascisse = []

for compagnia in gestore:
    %time attackPercent(compagnia, 100)

#attackPercent(compagnia, 100)

datiFinal = pandas.DataFrame()
datiFinal['percent'] = ascisse

datiFinal['Provider'] = aziendaFinal
datiFinal['diameter'] = diametro
datiFinal['average path length'] = cammino
datiFinal['clustering'] = cluster
datiFinal['average degree'] = gradomedio
datiFinal['soglia percolativa'] = criterio

datiFinal['GCsize'] = relSizeGC
#datiFinal.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolAttackDataForSeaborn.csv")
datiFinal.head()

# <codecell>

gestore = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]
#gestore = ["Tim", "Vodafone", "Wind", "Tre"]
#gestore = "Roma"
diametro = []
cammino = []
cluster = []
gradomedio = []
criterio = []
relSizeGC = []

aziendaFinal = []
ascisse = []

for compagnia in gestore:
    %time failurePercent(compagnia, 100)

#attackPercent(gestore, 50)

datiFinal = pandas.DataFrame()
datiFinal['percent'] = ascisse

datiFinal['Provider'] = aziendaFinal
datiFinal['diameter'] = diametro
datiFinal['average path length'] = cammino
datiFinal['clustering'] = cluster
datiFinal['average degree'] = gradomedio
datiFinal['soglia percolativa'] = criterio

datiFinal['GCsize'] = relSizeGC
datiFinal.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolFailureDataForSeaborn.csv")
datiFinal.head()

