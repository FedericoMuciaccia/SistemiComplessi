
# coding: utf-8

# ## Attack

# In[ ]:


import numpy, networkx, pandas

# gestori = ["Tim", "Vodafone", "Wind", "Tre"]

# diametro = []
# relSizeGC = []
# aziendaFinal = []
# ascisse = []

def attack(gestore, steps):
    adiacenza = numpy.genfromtxt(
        ("~/dati Iuri/AdiacenzaEuclidea_{0}.csv".format(gestore)),
        delimiter=',',
        dtype='int')
        # adiacenza.nbytes sarebbe 8 volte minore
        # se si mettesse 'bool' invece che 'int'
        # ma purtroppo networkx non genera correttamente
        # il grafo da una matrice di booleani
    grafo = networkx.Graph(adiacenza)

    graphSize = networkx.number_of_nodes(grafo)
    # binning
    passo = graphSize/steps # arrotonda all'intero
    
#    i = 0
#    ascisse.append(i)
#    aziendaFinal.append(compagnia)
#    diametro.append(2)
#    relSizeGC.append(1)

    
    while (graphSize > passo):
        gradi = pandas.DataFrame(grafo.degree().items(), columns=['index', 'grado'])
        gradi.sort(["grado"], ascending=[False], inplace=True)
        gradi = gradi.reset_index(drop=True)
        sortedIDnode = gradiFinal['index'].values

        for identificativo in sortedIDnode:
            if (graphSize > len(sortedIDnode) - passo):
                grafoFinal.remove_node(identificativo)
                # ricomputare graphSize

        sottografi = networkx.connected_component_subgraphs(grafoFinal)
        giantCluster = sottografi[0]
        
        i += 1
        ascisse.append(i)
        aziendaFinal.append(compagnia)

        
        diametro.append(networkx.diameter(giantCluster, e=None))
        relSizeGC.append(networkx.number_of_nodes(giantCluster)/float(graphSize))

    
get_ipython().magic(u'matplotlib inline')

for provider in gestori:
    get_ipython().magic(u'time attacco(provider,100)')


datiFinal = pandas.DataFrame()

datiFinal['percent'] = ascisse
datiFinal['Compagnia'] = aziendaFinal
datiFinal['diam'] = diametro
datiFinal['GC'] = relSizeGC

datiFinal.head()

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")


seaborn.lmplot('percent', 'diam',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           hue='Compagnia',
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attacco: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,max(diametro)+2)

seaborn.lmplot('percent', 'GC',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           hue='Compagnia',
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attacco: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)

#networkx.draw_random(grafoTre)

# <codecell>

























