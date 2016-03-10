# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Attacco e failure con seaborn

# <markdowncell>

# ###Importo librerie e definisco funzioni fondamentali

# <codecell>

from graph_tool.all import *
import networkx
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

# <codecell>

def gradonodo(identificativo):
        vertice = grafo.vertex(identificativo)
        return vertice.out_degree()
indice = numpy.arange(grafo.num_vertices())
listagradi = map(gradonodo, indice)

# <codecell>

def kquadromedio(listadeg):
    sommatoriaquadra = 0.0
    for grado in listadeg:
        sommatoriaquadra = sommatoriaquadra + grado**2    
    return sommatoriaquadra/len(listadeg)

criterion = kquadromedio(listadeg)/averageGrado(grafo)
%time kquadromedio(listagradi)

# <markdowncell>

# ### Cicli input/output gafi

# <codecell>

#NON ESEGUIRE, reti già costruite
for compagnia in gestore:
    %time costruzione(compagnia)

# <codecell>

# caricamento rete e studio topologico iniziale
for compagnia in gestore:
    print compagnia
    grafo = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(gestore))
    topo = %time topologia(grafo)
    print topo, "\n"

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
        criterion = kquadromedio(listaGradi)/averageGrado(grafoFinal)
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
        criterion = kquadromedio(listaGradi)/averageGrado(grafoFinal)
        criterio.append(criterion)

# <codecell>

#gestore = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]
gestore = ["Tim", "Vodafone", "Wind", "Tre"]
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
datiFinal.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolAttackDataForSeaborn.csv")
datiFinal.head()

# <codecell>

#gestore = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]
gestore = ["Tim", "Vodafone", "Wind", "Tre"]
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

# <codecell>

#Attack
import seaborn
%matplotlib inline
datiFinal = pandas.read_csv('/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolAttackDataForSeaborn.csv')

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#diametro
seaborn.lmplot('percent', 'diameter', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0, 80)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolAttackD_Final', format='eps', dpi=1000)

#giant cluster
seaborn.lmplot('percent', 'GCsize', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolAttackGC_Final', format='eps', dpi=1000)

#average length
seaborn.lmplot('percent', 'average path length', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: average path length')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,14)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolAttackl_Final', format='eps', dpi=1000)

#clustering
seaborn.lmplot('percent', 'clustering', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: coefficiente clustering')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolAttackC_Final', format='eps', dpi=1000)

#gradomedio
seaborn.lmplot('percent', 'average degree', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: average degree')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,100)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolAttackk_Final', format='eps', dpi=1000)

#CRITERION
seaborn.lmplot('percent', 'soglia percolativa', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: criterion')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,10)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolAttackc_Final', format='eps', dpi=1000)

# <codecell>

#Failure
import seaborn
%matplotlib inline
datiFinal = pandas.read_csv('/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolFailureDataForSeaborn.csv')

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#diametro
seaborn.lmplot('percent', 'diameter', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0, 20)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolFailureD_Final', format='eps', dpi=1000)

#giant cluster
seaborn.lmplot('percent', 'GCsize', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolFailureGC_Final', format='eps', dpi=1000)

#average length
seaborn.lmplot('percent', 'average path length', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: average path length')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,4)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolFailurel_Final', format='eps', dpi=1000)

#clustering
seaborn.lmplot('percent', 'clustering', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: coefficiente clustering')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolFailureC_Final', format='eps', dpi=1000)

#gradomedio
seaborn.lmplot('percent', 'average degree', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: average degree')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,100)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolFailurek_Final', format='eps', dpi=1000)

#CRITERION
seaborn.lmplot('percent', 'soglia percolativa', data=datiFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: criterion')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,10)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/gToolFailurec_Final', format='eps', dpi=1000)

# <codecell>


