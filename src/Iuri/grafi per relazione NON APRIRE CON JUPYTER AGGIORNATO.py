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
    distribuzioneRange = pyplot.hist(gradi, bins=max(gradi)-min(gradi), histtype='step', label=azienda, color=colore, linewidth=1.1)
    pyplot.title('Degree distribution')
    pyplot.xlabel("Degree")
    pyplot.ylabel("Frequency")

    pyplot.gca().set_xscale("log")
    pyplot.gca().set_yscale("log")
#    pyplot.ylim(1,100)

#Costruzione grafo da matrice di adiacenza
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

# ## Conversioni modelli reti da networkx a graph-tool

# <codecell>

#    if(modello == 'Erdos-Renyi'):
grafoErdos = networkx.erdos_renyi_graph(1000, 0.004)
gradoErdos = grafoErdos.degree().values()
adiacenzaErdos = networkx.to_numpy_matrix(grafoErdos)
#adiacenzaErdos
gToolGrafoErdos = graph_tool.Graph(directed = False)
%time conversione(gToolGrafoErdos, adiacenzaErdos)

pos = graph_tool.draw.arf_layout(gToolGrafoErdos)
#pos = graph_tool.draw.radial_tree_layout(gToolGrafoErdos, gToolGrafoErdos.vertex(0))
graph_draw(gToolGrafoErdos, pos = pos, output_size=(1000, 1000), 
           vertex_color=[1,1,1,0], vertex_size=4, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="Erdosmodel.png")

# <codecell>

#    if(modello == 'Watts-Strogatz'):
grafoWatts = networkx.watts_strogatz_graph(1000, 4, 0.6)
gradoWatts = grafoWatts.degree().values()
adiacenzaWatts = networkx.to_numpy_matrix(grafoWatts)
#adiacenzaWatts
print "check"
gToolGrafoWatts = graph_tool.Graph(directed = False)
print "check"
%time conversione(gToolGrafoWatts, adiacenzaWatts)

#pos = graph_tool.draw.radial_tree_layout(gToolGrafoWatts, gToolGrafoWatts.vertex(0))
pos = graph_tool.draw.arf_layout(gToolGrafoWatts)
#pos = graph_tool.draw.sfdp_layout(gToolGrafoWatts)
graph_draw(gToolGrafoWatts, pos = pos, output_size=(1000, 1000),
           vertex_color=[1,1,1,0], vertex_size=4, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="Wattsmodel.png")

# <codecell>

#    if(modello == 'Barabasi-Abert'):
grafoBarabasi = networkx.barabasi_albert_graph(2000, 1)
gradoBarabasi = grafoBarabasi.degree().values()
adiacenzaBarabasi = networkx.to_numpy_matrix(grafoBarabasi)
#adiacenzaBarabasi
gToolGrafoBarabasi = graph_tool.Graph(directed = False)
%time conversione(gToolGrafoBarabasi, adiacenzaBarabasi)

pos = graph_tool.draw.sfdp_layout(gToolGrafoBarabasi)
#pos = graph_tool.draw.radial_tree_layout(gToolGrafoBarabasi, gToolGrafoBarabasi.vertex(0))
graph_draw(gToolGrafoBarabasi, pos = pos, output_size=(1000, 1000), 
           vertex_color=[1,1,1,0], vertex_size=4, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="Barabasimodel.png")

# <codecell>

%matplotlib inline
pyplot.figure(figsize=(16,9)) 
grafico = degreeDistributionLog(gradoErdos, 'Erdos-Renyi', '#4d4d4d')
grafico = degreeDistributionLog(gradoWatts, 'Watts', '#47d147')
grafico = degreeDistributionLog(gradoBarabasi, 'Barabasi', '#ff3300')
pyplot.legend()

# <markdowncell>

# ## Generazione modelli reti direttamente con graph tool

# <markdowncell>

# ### Barabasi Albert con *initial attractiveness*

# <codecell>

g = graph_tool.generation.price_network(2000, m=1, c= 1, gamma = 1, directed=False)

pos = graph_tool.draw.sfdp_layout(g)
graph_draw(g, pos = pos, output_size=(1000, 1000), 
           vertex_color=[1,1,1,0], vertex_size=4, edge_pen_width=1.2,
           vcmap=matplotlib.cm.gist_heat_r, output="InitialAttr.png")

#pos=graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
#graph_draw(g, pos=pos, output_size=(1000, 1000),
#              vertex_fill_color=g.vertex_index, vertex_size=2,
#              edge_pen_width=1.0, output="initialAttractiv.png")

#todo mettere gradi minimi sempre più grandi e provare initial attrattivness
#fare in un box a parte per lavorare solo con distr grado

# <codecell>

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
gca().set_ylim(1, 1e4)
#gca().set_xlim(10, 1e3)
subplots_adjust(left=0.2, bottom=0.2)
xlabel("$k$")
ylabel("$P(k)$")
tight_layout()
savefig("price-deg-dist.pdf")
savefig("price-deg-dist.png")

# <markdowncell>

# ##Documentazione graph-tool
# 
# * [Quick Start](https://graph-tool.skewed.de/static/doc/quickstart.html)
# * [Graph generators](https://graph-tool.skewed.de/static/doc/generation.html#graph_tool.generation.price_network)
# * [Topologia (diametro etc)](https://graph-tool.skewed.de/static/doc/topology.html)
# * [Statistica (gradi etc)](https://graph-tool.skewed.de/static/doc/stats.html)
# * [Draw e layouts](https://graph-tool.skewed.de/static/doc/draw.html#graph_tool.draw.arf_layout)
# * [Animazioni](http://graph-tool.skewed.de/static/doc/demos/animation.html)

# <codecell>


