
# coding: utf-8

# # Percolation

# In[24]:


import numpy, networkx, pandas, matplotlib, seaborn

from matplotlib import pyplot

get_ipython().magic(u'matplotlib inline')


# In[25]:


# simple parallelization

# import multiprocessing
# cpus = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cpus)
# pool.map(...)


# ## Random failure

# In[26]:


def randomFailure(graph, steps=100):
    initialGraph = graph
    initialGraphSize = networkx.number_of_nodes(initialGraph)
    numbersOfNodesToRemove = numpy.linspace(0, initialGraphSize, num=steps, dtype='int')
    initialNodes = initialGraph.nodes()
    randomizedNodes = numpy.random.permutation(initialNodes)
    
    #initialDegrees = initialGraph.degree() #.items()
    
    #randomDegrees = numpy.random.permutation(initialDegrees)
    
    
    
    
    # TODO vedere se si possono agevolmente parallelizzare le list comprehension, che sono molto più scorrevoli da usare
    
    
    # TODO fare tutta l'analisi di un singolo sottografo in un'unica funzione
    # e poi fare una mappa parallela sulle varie sngole analisi
    
    
    def analyzeSingleGraph(index):
        newGraph = initialGraph.copy()
        newGraph.remove_nodes_from(randomizedNodes[0:index])
        newGraphSize = networkx.number_of_nodes(newGraph)
        grado = newGraph.degree().items()
        subgraphs = networkx.connected_component_subgraphs(newGraph)
        try:
            giantCluster = subgraphs[0]
        except:
            giantCluster = networkx.Graph()
        giantClusterSize = networkx.number_of_nodes(giantCluster)
        relativeGiantClusterSize = numpy.true_divide(giantClusterSize, newGraphSize)
        try:
            diameter = networkx.diameter(giantCluster, e=None)
        except:
            diameter = 0
        # diameter = 1
        return relativeGiantClusterSize, diameter

    failureResults = map(analyzeSingleGraph, numbersOfNodesToRemove)
    failureDataframe = pandas.DataFrame(failureResults, columns=['relativeGiantClusterSize', 'diameter'])
    ascisse = numpy.linspace(0,100, num=steps, dtype='int')
    failureDataframe['percentuale'] = ascisse
    
    return failureDataframe


# In[27]:


gestore = ["Tim", "Vodafone", "Wind", "Tre"]
#
gestore = ["Tre"]

    

# TODO parallelizzare
for provider in gestore:
    adiacenza = numpy.genfromtxt(("/home/federico/dati Iuri/AdiacenzaEuclidea_{0}.csv".format(provider)),                                 delimiter=',',                                 dtype='int')
    providerGraph = networkx.Graph(adiacenza)
    get_ipython().magic(u'time failureResults = randomFailure(providerGraph, steps=100)')
    print "random failure"


# TODO fare diametro relativo e scatterplot di correlazione tra diametro relativo e relativeGiantClusterSize


seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")


seaborn.lmplot('percentuale', 'diameter',
           data=failureResults,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           # hue='Compagnia', # TODO
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure')
pyplot.xlabel("Percentuale")
pyplot.ylabel("Diametro")
pyplot.xlim(0, 101)
pyplot.ylim(0, 10)
pyplot.savefig('../img/randomFailure_diameter_Fede.eps', format='eps', dpi=1000)

seaborn.lmplot('percentuale', 'relativeGiantClusterSize',
           data=failureResults,
           fit_reg=False,
           size = 7,
           aspect = 1.7778,
           # hue='Compagnia', # TODO
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure')
pyplot.xlabel("Percentuale")
pyplot.ylabel("Dimensione relativa del giant cluster")
pyplot.xlim(0, 101)
pyplot.ylim(0, 1,1)
pyplot.savefig('../img/randomFailure_relativeGiantClusterSize_Fede.eps', format='eps', dpi=1000)


# In[18]:

failureResults.diameter


# In[19]:

failureResults.relativeGiantClusterSize


# In[122]:

adiacenza = numpy.genfromtxt("/home/federico/dati Iuri/AdiacenzaEuclidea_Tre.csv",                                 delimiter=',',                                 dtype='int')
initialGraph = networkx.Graph(adiacenza)


# ## Intentional attack

# In[1]:

def intentionalAttack():
    pass


# In[ ]:




# In[ ]:



