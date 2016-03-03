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

#esempio di creazione grafo
grafo = Graph(directed=False)
v1 = grafo.add_vertex()
v2 = grafo.add_vertex()
vlist = grafo.add_vertex(10)
e = grafo.add_edge(v1, v2)
f = grafo.add_edge(grafo.vertex(10), grafo.vertex(8))
%matplotlib inline
graph_draw(grafo, vertex_text=grafo.vertex_index, vertex_font_size=18,
           output_size=(800, 800), output="two-nodes.png")

# <codecell>

adiacenzaRoma = numpy.genfromtxt("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_Roma.csv",delimiter=',',dtype='int')
adiacenzaTim = numpy.genfromtxt("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_Tim.csv",delimiter=',',dtype='int')
adiacenzaVoda = numpy.genfromtxt("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_Vodafone.csv",delimiter=',',dtype='int')
adiacenzaWind = numpy.genfromtxt("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_Wind.csv",delimiter=',',dtype='int')
adiacenzaTre = numpy.genfromtxt("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_Tre.csv",delimiter=',',dtype='int')

# <codecell>

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,
           output_size=(800, 800), output="two-nodes.png")

# <codecell>

g = Graph(directed=False)
%time conversione(g, adiacenzaTre)
pos = graph_tool.draw.sfdp_layout(g)
graph_draw(g, pos=pos, output_size=(2000, 2000), vertex_color=[1,1,1,0],
           vertex_size=2, edge_pen_width=0.8,
           vcmap=matplotlib.cm.gist_heat_r, output="provaTre.png")

# <markdowncell>

# ## Grafi semplici con networkx

# <codecell>

pyplot.figure(figsize=(9,9))
simpleWatts = networkx.watts_strogatz_graph(1500, 4, 0.1)
#simpleWatts = networkx.watts_strogatz_graph(100, 10, 1)
networkx.draw_circular(simpleWatts, node_size=80,
                       with_labels = False,
                       #node_color=simpleWatts.degree().values(),
                       cmap=pyplot.cm.Reds_r)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/totalrandomwatts', format='eps', dpi=1000)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/random-smallworld', format='eps', dpi=1000)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/smallworld', format='eps', dpi=1000)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/ringnet', format='eps', dpi=1000)
pyplot.show()

# <codecell>

#    if(modello == 'Erdos-Renyi'):
%matplotlib inline
pyplot.figure(figsize=(16,9))
simpleErdos = networkx.erdos_renyi_graph(80, 0.04)
networkx.draw_random(simpleErdos, node_size=80,
                     with_labels = False,
                     node_color=simpleErdos.degree().values(),
                     cmap=pyplot.cm.Reds_r)
#pyplot.show()



pyplot.figure(figsize=(16,9))
simpleBara = networkx.barabasi_albert_graph(100, 1)
networkx.draw_random(simpleBara, node_size=80,
                     with_labels = False,
                     node_color=simpleBara.degree().values(),
                     cmap=pyplot.cm.Reds_r)
pyplot.show()

# <markdowncell>

# NB: Quando si hanno pochi nodi, una connessione tra soli primi vicini e poca probabilità di avere un rewire, il grafo può essere tracciato come un cerchio con le corde, quando però si aumentano nodi, connessioni tra vicini, e sopratutto probabilità di rewire, la rete è assolutamente indistinguibile sia nel grafo, sia come distribuzione del grado, a una rete random di Erdos-Renyi.

# <markdowncell>

# ## Conversioni modelli reti da networkx a graph-tool

# <codecell>

#    if(modello == 'Erdos-Renyi'):
grafoErdos = networkx.erdos_renyi_graph(3000, 0.01687)
gradoErdos = grafoErdos.degree().values()
#adiacenzaErdos = networkx.to_numpy_matrix(grafoErdos)
#adiacenzaErdos
#gToolGrafoErdos = graph_tool.Graph(directed = False)
#%time conversione(gToolGrafoErdos, adiacenzaErdos)

#    if(modello == 'Watts-Strogatz'):
#grafoWatts = networkx.watts_strogatz_graph(3000, 50, 0.48)
#gradoWatts = grafoWatts.degree().values()
#adiacenzaWatts = networkx.to_numpy_matrix(grafoWatts)
#adiacenzaWatts
#gToolGrafoWatts = graph_tool.Graph(directed = False)
#%time conversione(gToolGrafoWatts, adiacenzaWatts)


#    if(modello == 'Barabasi-Abert'):
#grafoBarabasi = networkx.barabasi_albert_graph(3000, 1)
#gradoBarabasi = grafoBarabasi.degree().values()
#adiacenzaBarabasi = networkx.to_numpy_matrix(grafoBarabasi)
#adiacenzaBarabasi
#gToolGrafoBarabasi = graph_tool.Graph(directed = False)
#%time conversione(gToolGrafoBarabasi, adiacenzaBarabasi)

# <codecell>

%matplotlib inline
pyplot.figure(figsize=(16,9)) 
grafico = degreeDistributionLog(gradoErdos, 'Erdos-Renyi', '#699534')
grafico = degreeDistributionLog(gradoWatts, 'Watts-Strogatz', '#3D5A92')
grafico = degreeDistributionLog(gradoBarabasi, 'Barabasi-Albert', '#FD6266')
pyplot.ylim(0.9,2500)
pyplot.xlim(1,100)
pyplot.legend()
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/ComparGradeModel_Final', format='eps', dpi=1000)

# <codecell>

#grafo watts
%matplotlib inline
#pos = graph_tool.draw.radial_tree_layout(gToolGrafoWatts, gToolGrafoWatts.vertex(0))
#gToolGrafoWatts = graph_tool.generation.circular_graph(80, 2)
#pos = graph_tool.draw.sfdp_layout(gToolGrafoWatts, cooling_step=0.95)
pos = graph_tool.draw.arf_layout(gToolGrafoWatts)
#pos = graph_tool.draw.sfdp_layout(gToolGrafoWatts)
graph_draw(gToolGrafoWatts, pos = pos, output_size=(1000, 1000),
           vertex_color=[1,1,1,0], vertex_size=5, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="zoomring.eps")

# <codecell>


#grafo erdos
pos = graph_tool.draw.arf_layout(gToolGrafoErdos)
#pos = graph_tool.draw.radial_tree_layout(gToolGrafoErdos, gToolGrafoErdos.vertex(0))
graph_draw(gToolGrafoErdos, pos = pos, output_size=(1000, 1000), 
           vertex_color=[1,1,1,0], vertex_size=4, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="Erdosmodel.eps")



#grafo barabasi
pos = graph_tool.draw.sfdp_layout(gToolGrafoBarabasi)
#pos = graph_tool.draw.radial_tree_layout(gToolGrafoBarabasi, gToolGrafoBarabasi.vertex(0))
graph_draw(gToolGrafoBarabasi, pos = pos, output_size=(1000, 1000), 
           vertex_color=[1,1,1,0], vertex_size=4, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="Barabasimodel.eps")

# <markdowncell>

# ## Generazione modelli reti direttamente con graph tool

# <markdowncell>

# ### Barabasi Albert con *initial attractiveness*

# <codecell>

#g = graph_tool.generation.price_network(10000, m=1, gamma = 1, directed=False)
initial = 10
%time g = graph_tool.generation.price_network(1000, m=2, c=initial, gamma = 1, directed=False)
pos = graph_tool.draw.sfdp_layout(g)
graph_draw(g, pos = pos, output_size=(1000, 1000), 
           vertex_color=[1,1,1,0], vertex_size=5, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output=("c = {0}.png".format(initial)))

# <codecell>

%matplotlib inline
# We will need some things from several places
from __future__ import division, absolute_import, print_function
import sys
if sys.version_info < (3,):
    range = xrange
import os
from pylab import *  # for plotting
from numpy.random import *  # for random sampling
seed(42)

# We need to import the graph_tool module itself
from graph_tool.all import *

in_hist = vertex_hist(g, "out")

y = in_hist[0]

err = sqrt(in_hist[0])
err[err >= y] = y[err >= y] - 1e-2

figure(figsize=(8,5))
errorbar(in_hist[1][:-1], in_hist[0], fmt="o", yerr=err,
        label="in")
gca().set_yscale("log")
gca().set_xscale("log")
gca().set_ylim(1, 1000)
gca().set_xlim(2, 60)
subplots_adjust(left=0.2, bottom=0.2)
xlabel("$k$")
ylabel("$P(k)$")
tight_layout()
#savefig("price-deg-dist.pdf")
savefig(("grado c = {0}.png").format(initial))
gradoBarabasi = gradiFinal = pandas.DataFrame(in_hist[0], columns=['grado'])
gradoBarabasi.to_csv(("c = {0}.csv".format(initial)))

# <markdowncell>

# ##Documentazione graph-tool
# 
# * [Quick Start](https://graph-tool.skewed.de/static/doc/quickstart.html)
# * [Graph generators](https://graph-tool.skewed.de/static/doc/generation.html#graph_tool.generation.price_network)
# * [Topologia (diametro etc)](https://graph-tool.skewed.de/static/doc/topology.html)
# * [Statistica (gradi etc)](https://graph-tool.skewed.de/static/doc/stats.html)
# * [Draw e layouts](https://graph-tool.skewed.de/static/doc/draw.html#graph_tool.draw.arf_layout)
# * [Animazioni](http://graph-tool.skewed.de/static/doc/demos/animation.html)

# <markdowncell>

# ## Attacco e failure con modelli

# <codecell>

def modelAttack(modello, steps):
    if(modello == 'Erdos-Renyi'):
        grafoFinal = networkx.erdos_renyi_graph(1500, 0.05)
        gradoFinal = grafoFinal.degree().values()
        #print grado
        grafico = degreeDistributionLog(gradoFinal, 'Erdos-Renyi', '#4d4d4d')
    if(modello == 'Barabasi-Abert'):
        grafoFinal = networkx.barabasi_albert_graph(1500, 40)
        gradoFinal = grafoFinal.degree().values()
        #print grado 
        grafico = degreeDistributionLog(gradoFinal, 'Barabasi', '#ff3300')
    if(modello == 'Watts-Strogatz'):
        grafoFinal = networkx.watts_strogatz_graph(1500, 37, 1)
        gradoFinal = grafoFinal.degree().values()
        #print grado  
        grafico = degreeDistributionLog(gradoFinal, 'Watts', '#47d147')
    
    graphSize = networkx.number_of_nodes(grafoFinal)
    passo = networkx.number_of_nodes(grafoFinal)/float(steps)

    i = 0
    ascisse.append(i)
    aziendaFinal.append(modello)
    diametro.append(2)
    relSizeGC.append(1)

    
    while (networkx.number_of_nodes(grafoFinal) > passo):
        gradiFinal = pandas.DataFrame(grafoFinal.degree().items(), columns=['index', 'grado'])
        gradiFinal.sort(["grado"], ascending=[False], inplace=True)
        sortedIDnode = gradiFinal['index'].values

        for identificativo in sortedIDnode:
            if (networkx.number_of_nodes(grafoFinal) > len(sortedIDnode) - passo):
                grafoFinal.remove_node(identificativo)

        giantCluster = max(networkx.connected_component_subgraphs(grafoFinal), key = len)
        
        i += 100/steps
        ascisse.append(i)
        aziendaFinal.append(modello)

        graphSize = networkx.number_of_nodes(grafoFinal)
        diametro.append(networkx.diameter(giantCluster, e=None))
        relSizeGC.append(networkx.number_of_nodes(giantCluster)/float(graphSize))
        
def modelFailure(modello, steps):
    if(modello == 'Erdos-Renyi'):
        grafoFinal = networkx.erdos_renyi_graph(1500, 0.05)
        gradoFinal = grafoFinal.degree().values()
        #print grado
        grafico = degreeDistributionLog(gradoFinal, 'Erdos-Renyi', '#4d4d4d')
    if(modello == 'Barabasi-Abert'):
        grafoFinal = networkx.barabasi_albert_graph(1500, 40)
        gradoFinal = grafoFinal.degree().values()
        #print grado 
        grafico = degreeDistributionLog(gradoFinal, 'Barabasi', '#ff3300')
    if(modello == 'Watts-Strogatz'):
        grafoFinal = networkx.watts_strogatz_graph(1500, 37, 1)
        gradoFinal = grafoFinal.degree().values()
        #print grado  
        grafico = degreeDistributionLog(gradoFinal, 'Watts', '#47d147')
    

    graphSize = networkx.number_of_nodes(grafoFinal)
    passo = networkx.number_of_nodes(grafoFinal)/float(steps)

    i = 0
    ascisse.append(i)
    aziendaFinal.append(modello)
    diametro.append(2)
    relSizeGC.append(1)

    while (networkx.number_of_nodes(grafoFinal) > passo):
        gradiFinal = pandas.DataFrame(grafoFinal.degree().items(), columns=['index', 'grado'])
        randomante = gradiFinal['index'].values
        randomante = numpy.random.permutation(randomante)

        for identificativo in randomante:
            if (networkx.number_of_nodes(grafoFinal) > len(randomante) - passo):
                grafoFinal.remove_node(identificativo)

        giantCluster = max(networkx.connected_component_subgraphs(grafoFinal), key = len)

        i += 100/steps
        ascisse.append(i)
        aziendaFinal.append(modello)
        
        graphSize = networkx.number_of_nodes(grafoFinal)
        diametro.append(networkx.diameter(giantCluster, e=None))
        relSizeGC.append(networkx.number_of_nodes(giantCluster)/float(graphSize))

# <codecell>

#calcolo attacco con modelli

diametro = []
relSizeGC = []
aziendaFinal = []
ascisse = []

pyplot.figure(figsize=(16,9))       
modelAttack('Erdos-Renyi', 100)
modelAttack('Watts-Strogatz', 100)
modelAttack('Barabasi-Abert', 100)
pyplot.legend()

datiFinal = pandas.DataFrame()

datiFinal['percent'] = ascisse
datiFinal['Modello'] = aziendaFinal
datiFinal['diam'] = diametro
datiFinal['GC'] = relSizeGC
datiFinal.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/ModelAttackForSeaborn.csv")
datiFinal.head()

# <codecell>

#calcolo failure con modelli
diametro = []
relSizeGC = []
aziendaFinal = []
ascisse = []

pyplot.figure(figsize=(16,9))       
modelFailure('Watts-Strogatz', 100)
modelFailure('Erdos-Renyi', 100)
modelFailure('Barabasi-Abert', 100)
pyplot.legend()

datiFinal = pandas.DataFrame()

datiFinal['percent'] = ascisse
datiFinal['Modello'] = aziendaFinal
datiFinal['diam'] = diametro
datiFinal['GC'] = relSizeGC
datiFinal.to_csv("/home/protoss/Documenti/SistemiComplessi/data/Iuri/ModelFailureForSeaborn.csv")
datiFinal.head()

# <markdowncell>

# ## Faccio i grafici

# <codecell>

#Attack
import seaborn

datiFinal = pandas.read_csv('/home/protoss/Documenti/SistemiComplessi/data/Iuri/AttackDataForSeaborn.csv')

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#PLOTS
seaborn.lmplot('percent', 'diam',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           hue='Modello',
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attacco con i modelli di rete: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0, 1)
pyplot.ylim(0,max(diametro)+2)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/AttackD_Model', format='eps', dpi=1000)

seaborn.lmplot('percent', 'GC',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           hue='Modello',
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attacco con i modelli di rete: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/AttackGC_Model', format='eps', dpi=1000)

# <codecell>

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")


seaborn.lmplot('percent', 'diam',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           hue='Modello',
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure con i modelli di rete: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
#pyplot.ylim(0, 1)
pyplot.ylim(0,max(diametro)+2)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/FailureD_Model', format='eps', dpi=1000)

seaborn.lmplot('percent', 'GC',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           hue='Modello',
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure con i modelli di rete: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/iuri/FailureGC_Model', format='eps', dpi=1000)

