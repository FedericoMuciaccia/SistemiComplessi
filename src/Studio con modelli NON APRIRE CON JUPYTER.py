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

# <markdowncell>

# ### Definisco alcune funzioni utili

# <codecell>


def degreeDistributionLog(gradi, azienda, colore):
    distribuzioneRange = pyplot.hist(gradi, bins=max(gradi)-min(gradi), histtype='step', label=azienda, 
                                     color=colore, alpha= 0.7, linewidth=3)
    pyplot.title('Comparazione distribuzioni del grado')
    pyplot.xlabel("Grado")
    pyplot.ylabel("Frequenza")

    pyplot.gca().set_xscale("log")
    pyplot.gca().set_yscale("log")
#    pyplot.ylim(1,100)

#Costruzione grafo con graph-tool da matrice di adiacenza
def conversione(grafo, adiacenza):
    grafo.add_vertex(len(adiacenza))
    num_vertices = adiacenza.shape[0]
    for i in range(num_vertices - 1):
        for j in range(i + 1, num_vertices):
            if adiacenza[i,j] != 0:
                e = grafo.add_edge(i, j)

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

def topologia(grafo, tipo):
    
    def gradonodo(identificativo):
        vertice = grafo.vertex(identificativo)
        return vertice.out_degree()

    def kmedio(listadeg):
        return numpy.mean(listadeg)
    
    def kquadromedio(listadeg):
        listadegQuadri = numpy.power(listadeg, 2)
        return numpy.mean(listadegQuadri)
    
    def freqCritica(criterion):
        return 1-(1/float(criterion-1))
    
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
    criterion = kquadromedio(listaGradi)/float(kmedio(listaGradi))
    criterio.append(criterion)
    fcritica.append(freqCritica(criterion))

# <markdowncell>

# ### Traccio i grafi delle reti in esame con graph-tool

# <codecell>


gestore = ["Tim", "Vodafone", "Wind", "Tre"]
for compagnia in gestore:
    grafoFinal = load_graph("/home/protoss/Documenti/Siscomp_datas/data/GTool{0}.xml".format(compagnia))

    pos = graph_tool.draw.sfdp_layout(grafoFinal)
    graph_draw(grafoFinal, pos=pos, output_size=(2000, 2000), vertex_color=[1,1,1,0],
               vertex_size=3, edge_pen_width=0.8,
               vcmap=matplotlib.cm.gist_heat_r, 
               output="prova{0}.png".format(compagnia)
               )

# <markdowncell>

# ## Grafi semplici con networkx

# <codecell>

# modello Watts-Strogatz
simpleWatts = networkx.watts_strogatz_graph(100, 4, 0.0)
# modello Erdos-Renyi
simpleErdos = networkx.erdos_renyi_graph(100, 0.04)
# modello Barabasi-Albert
simpleBara = networkx.barabasi_albert_graph(100, 1)


#%matplotlib inline
#pyplot.figure(figsize=(9,9))
#networkx.draw_random(simpleErdos, node_size=80,
#                     with_labels = False,
#                     #node_color=simpleErdos.degree().values(),
#                     cmap=pyplot.cm.Reds_r)
#pyplot.savefig('random.svg', format='svg', dpi=1000)
#pyplot.show()

# <markdowncell>

# ## Conversioni modelli reti da networkx a graph-tool

# <codecell>

# modello Erdos-Renyi
grafoErdos = networkx.erdos_renyi_graph(1000, 0.02)
adiacenzaErdos = networkx.to_numpy_matrix(grafoErdos)

gToolGrafoErdos = graph_tool.Graph(directed = False)
%time conversione(gToolGrafoErdos, adiacenzaErdos)
#gToolGrafoErdos.save("GToolErdos.xml")

# modello Watts-Strogatz
grafoWatts = networkx.watts_strogatz_graph(1000, 30, 0)
adiacenzaWatts = networkx.to_numpy_matrix(grafoWatts)

gToolGrafoWatts = graph_tool.Graph(directed = False)
%time conversione(gToolGrafoWatts, adiacenzaWatts)
#gToolGrafoWatts.save("GToolWatts.xml")

# modello Barabasi-Abert
grafoBarabasi = networkx.barabasi_albert_graph(1000, 2)
adiacenzaBarabasi = networkx.to_numpy_matrix(grafoBarabasi)

gToolGrafoBarabasi = graph_tool.Graph(directed = False)
%time conversione(gToolGrafoBarabasi, adiacenzaBarabasi)

# <codecell>

#analisi con graph-tool
azienda = []
diametro = []
cammino = []
cluster = []
relSizeGC = []
gradomedio = []
criterio = []
fcritica = []

topologia(gToolGrafoErdos, "Random")
datiInitial = pandas.DataFrame()
datiInitial['Rete'] = azienda
datiInitial['GC %'] = relSizeGC
datiInitial['D'] = diametro
datiInitial['<l>'] = cammino
datiInitial['C'] = cluster
datiInitial['<k>'] = gradomedio
datiInitial['<k^2>/<k>'] = criterio
datiInitial['f'] = fcritica
datiInitial

# <codecell>

#lista gradi con networkx
gradoErdos = grafoErdos.degree().values()

#lista gradi con Graph-tool
def gradonodo(identificativo):
        vertice = gToolGrafoErdos.vertex(identificativo)
        return vertice.out_degree()
    
indice = numpy.arange(gToolGrafoErdos.num_vertices())
listaGradi = map(gradonodo, indice)

# <codecell>

%matplotlib inline
pyplot.figure(figsize=(12,9)) 
grafico = degreeDistributionLog(gradoErdos, 'Con Networkx', '#699534')
grafico = degreeDistributionLog(listaGradi, 'Con Graph-tool', '#3D5A92')
#pyplot.ylim(0.9,1100)
#pyplot.xlim(1,25)
pyplot.legend()
#pyplot.savefig('compareSameN.svg', format='svg', dpi=1000)

# <markdowncell>

# ### Traccio i grafi convertiti in graph-tool, con la grafica di graph-tool

# <codecell>

#alcuni layout
#pos = graph_tool.draw.radial_tree_layout(gToolGrafoWatts, gToolGrafoWatts.vertex(0))
#pos = graph_tool.draw.sfdp_layout(gToolGrafoWatts, cooling_step=0.95)
#pos = graph_tool.draw.arf_layout(gToolGrafoWatts)

#questa riga genera il reticolo circolare da cui parte Watts-Strogatz
#gToolGrafoWatts = graph_tool.generation.circular_graph(70, 2)
nomeGrafo = gToolGrafoBarabasi

pos = graph_tool.draw.sfdp_layout(nomeGrafo)
graph_draw(nomeGrafo, pos = pos, output_size=(1000, 1000),
           vertex_color=[1,1,1,0], vertex_size=5, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, 
           output="grafo.svg"
           )

# <markdowncell>

# ## Generazione modelli reti direttamente con graph tool

# <markdowncell>

# ### Barabasi Albert con *initial attractiveness*

# <codecell>

initial = 0
g = graph_tool.generation.price_network(10000, m=10, gamma = 1,
                                        c=initial,
                                        #seed_graph = gToolGrafoErdos,
                                        directed=False)
#pos = graph_tool.draw.sfdp_layout(g)
#graph_draw(g, pos = pos, output_size=(1000, 1000), 
#           vertex_color=[1,1,1,0], vertex_size=3, edge_pen_width=1,
#           vcmap=matplotlib.cm.gist_heat_r, 
#           output=("barabalbert1.svg"))

# <codecell>

#analisi

azienda = []
diametro = []
cammino = []
cluster = []
relSizeGC = []
gradomedio = []
criterio = []
fcritica = []

topologia(g, "Barabalbero")
datiInitial = pandas.DataFrame()
datiInitial['Rete'] = azienda
datiInitial['GC %'] = relSizeGC
datiInitial['D'] = diametro
datiInitial['<l>'] = cammino
datiInitial['C'] = cluster
datiInitial['<k>'] = gradomedio
datiInitial['<k^2>/<k>'] = criterio
datiInitial['f'] = fcritica
datiInitial

# <codecell>


def gradonodo(identificativo):
        vertice = g.vertex(identificativo)
        return vertice.out_degree()
    
indice = numpy.arange(g.num_vertices())
listaGradi = map(gradonodo, indice)
numpy.sum(listaGradi)

# <markdowncell>

# ##Documentazione graph-tool
# 
# * [Quick Start](https://graph-tool.skewed.de/static/doc/quickstart.html)
# * [Graph generators](https://graph-tool.skewed.de/static/doc/generation.html#graph_tool.generation.price_network)
# * [Topologia (diametro etc)](https://graph-tool.skewed.de/static/doc/topology.html)
# * [Statistica (gradi etc)](https://graph-tool.skewed.de/static/doc/stats.html)
# * [Draw e layouts](https://graph-tool.skewed.de/static/doc/draw.html#graph_tool.draw.arf_layout)
# * [Animazioni](http://graph-tool.skewed.de/static/doc/demos/animation.html)

