
# coding: utf-8

# ## Random Failure (parallelization)

# In[41]:


import numpy, networkx, pandas, matplotlib, seaborn

from matplotlib import pyplot

get_ipython().magic(u'matplotlib inline')


# In[139]:


import multiprocessing

cpus = multiprocessing.cpu_count()

pool = multiprocessing.Pool(processes=cpus)

# pool.map(...)

import functools


# In[140]:


#Failure

gestore = ["Tim", "Vodafone", "Wind", "Tre"]
#
gestore = ["Tre"]


def randomFailure(compagnia, steps=20):
    
    
    ascisse = numpy.linspace(0,100, num=steps, dtype='int')
    
    adiacenza = numpy.genfromtxt(("/home/federico/dati Iuri/AdiacenzaEuclidea_{0}.csv".format(compagnia)),                                 delimiter=',',                                 dtype='int')
    initialGraph = networkx.Graph(adiacenza)
    
    initialGraphSize = networkx.number_of_nodes(initialGraph)
    
    #passo = initialGraphSize/steps
    passi = numpy.linspace(0,initialGraphSize, num=steps, dtype='int')
    
    initialNodes = initialGraph.nodes()
    
    randomizedNodes = numpy.random.permutation(initialNodes)
    
    #initialDegrees = initialGraph.degree() #.items()
    
    #randomDegrees = numpy.random.permutation(initialDegrees)
    
    def createSmallerGraph(index):
        graph = initialGraph.copy()
        graph.remove_nodes_from(randomizedNodes[0:index])
        return graph
    
    # vedere se si possono agevolmente parallelizzare le list comprehension, che sono molto più scorrevoli da usare
    grafi = map(createSmallerGraph, passi)
    
    
    def computeDegree(graph):
        return graph.degree().items()
    
    gradi = map(computeDegree, grafi)
    
    
    # TODO controllare che il primo grafo abbia relativeSize = 1
    
    
    # TODO fare tutta l'analisi di un singolo sottografo in un'unica funzione
    # e poi fare una mappa parallela sulle varie sngole analisi
    
    
    
    def takeGiantCluster(graph):
        subgraphs = networkx.connected_component_subgraphs(graph)
        try:
            return subgraphs[0]
        except:
            return networkx.Graph()
    
    giantClusters = map(takeGiantCluster, grafi)
    
    giantClusterSizes = map(networkx.number_of_nodes, giantClusters)
    
    graphSizes = map(networkx.number_of_nodes, grafi)
    
    relativeGiantClusterSizes = numpy.true_divide(giantClusterSizes, graphSizes)
    
#    def computeDiameter(graph):
#        return networkx.diameter(graph, e=None)
    computeDiameter = functool.partial(networkx.diameter, e=None)
    
    #diameters = map(computeDiameter, giantClusters)
    
    diameters = []
    
    return relativeGiantClusterSizes, diameters










for provider in gestore:
    get_ipython().magic(u'time relativeGiantClusterSize, diameter = randomFailure(provider)')
    print "attacco"
    
    
pass









datiFinal = pandas.DataFrame()

datiFinal['percent'] = ascisse
# datiFinal['Compagnia'] = gestore # TODO
# datiFinal['diam'] = diameter
datiFinal['GC'] = relativeGiantClusterSize

datiFinal.head()

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")


#seaborn.lmplot('percent', 'diam',
#           data=datiFinal,
#           fit_reg=False,
#           size = 7,
#           aspect = 1.7778,
#           # hue='Compagnia', # TODO
#           scatter_kws={"marker": "D", "s": 100})
#pyplot.title('Random failure: diametro')
#pyplot.xlabel("%")
#pyplot.ylabel("Valore")
#pyplot.xlim(0, 100)
#pyplot.ylim(0,max(diametro)+2)

seaborn.lmplot('percent', 'GC',
           data=datiFinal,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           # hue='Compagnia', # TODO
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)



# In[ ]:




# In[122]:

adiacenza = numpy.genfromtxt("/home/federico/dati Iuri/AdiacenzaEuclidea_Tre.csv",                                 delimiter=',',                                 dtype='int')
initialGraph = networkx.Graph(adiacenza)


# In[123]:

c = initialGraph.nodes()
print len(c)
c.pop()
print len(c)


# In[124]:

initialGraph.remove_nodes_from(c)


# In[129]:

networkx.connected_component_subgraphs(initialGraph)[0].nodes()


# In[130]:

initialGraph.remove_node(1314)


# In[131]:

initialGraph


# In[132]:

initialGraph.nodes()


# In[135]:

try: networkx.connected_component_subgraphs(initialGraph)[0].nodes()


# In[137]:

networkx.number_of_nodes(initialGraph)


# In[ ]:



