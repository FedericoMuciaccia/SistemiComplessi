
# coding: utf-8

# # Percolation

# In[6]:


import numpy, networkx, pandas

# import graph_tool
# from graph_tool.all import *

# from matplotlib import pyplot

# %matplotlib inline


# In[2]:


# simple parallelization

# import multiprocessing
# cpus = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cpus)
# pool.map(...)


# ## Random failure

# In[11]:


def randomFailure(graph, steps=101):
    initialGraph = graph
    initialGraphSize = networkx.number_of_nodes(initialGraph)
    numbersOfNodesToRemove = numpy.linspace(0, initialGraphSize, num=steps, dtype='int')
    initialNodes = initialGraph.nodes()
    randomizedNodes = numpy.random.permutation(initialNodes)
    
    def analyzeSingleGraph(index):
        # TODO vedere se si possono agevolmente parallelizzare le list comprehension
        # che sono molto più scorrevoli da usare ripetto a map() 
        newGraph = initialGraph.copy()
        newGraph.remove_nodes_from(randomizedNodes[0:index])
        newGraphSize = networkx.number_of_nodes(newGraph)
        grado = newGraph.degree().items()
        subgraphs = sorted(networkx.connected_component_subgraphs(newGraph), key = len, reverse=True)
        try:
            giantCluster = subgraphs[0]
            giantClusterSize = networkx.number_of_nodes(giantCluster)
            relativeGiantClusterSize = numpy.true_divide(giantClusterSize, newGraphSize)
#            diameter = networkx.diameter(giantCluster, e=None)
            diameter = 0
        except:
            giantCluster = networkx.empty_graph()
            giantClusterSize = 0
            relativeGiantClusterSize = 0
            diameter = 0
        return relativeGiantClusterSize, diameter
    
    # TODO parallelizzare questa mappa
    failureResults = map(analyzeSingleGraph, numbersOfNodesToRemove)
    failureDataframe = pandas.DataFrame(failureResults, columns=['relativeGiantClusterSize', 'diameter'])
    ascisse = numpy.linspace(0,100, num=steps, dtype='int')
    failureDataframe['percentuale'] = ascisse
    
    return failureDataframe


# ## Intentional attack

# In[12]:


def intentionalAttack(graph, steps=101):
    initialGraph = graph
    initialGraphSize = networkx.number_of_nodes(initialGraph)
    numbersOfNodesToRemove = numpy.linspace(0, initialGraphSize, num=steps, dtype='int')
    initialNodes = initialGraph.nodes()
    
    initialDegrees = initialGraph.degree()
    degreeDataframe = pandas.DataFrame(initialDegrees.items(), columns=['index', 'degree']) # TODO index -> ID
    degreeDataframe.sort(["degree"], ascending=[False], inplace=True) # TODO vedere se si può fare a meno di una colonna
    # degreeDataframe = degreeDataframe.reset_index(drop=True)
    sortedNodes = degreeDataframe['index'].values # TODO degreeDataframe.index
    
    def analyzeSingleGraph(index):
        # TODO vedere se si possono agevolmente parallelizzare le list comprehension
        # che sono molto più scorrevoli da usare ripetto a map() 
        newGraph = initialGraph.copy()
        newGraph.remove_nodes_from(sortedNodes[0:index]) # TODO vedere ordinamento più veloce
        newGraphSize = networkx.number_of_nodes(newGraph)
        grado = newGraph.degree().items()
        # subgraphs = sorted(networkx.connected_component_subgraphs(newGraph), key = len, reverse=True)
        subgraphs = networkx.connected_component_subgraphs(newGraph)
        try:
            giantCluster = max(subgraphs, key = len)
            # giantCluster = subgraphs[0]
            giantClusterSize = networkx.number_of_nodes(giantCluster)
            relativeGiantClusterSize = numpy.true_divide(giantClusterSize, newGraphSize)
#            diameter = networkx.diameter(giantCluster, e=None)
            diameter = 0
        except:
            giantCluster = networkx.empty_graph()
            giantClusterSize = 0
            relativeGiantClusterSize = 0
            diameter = 0
        return relativeGiantClusterSize, diameter
    
    # TODO parallelizzare questa mappa
    attackResults = map(analyzeSingleGraph, numbersOfNodesToRemove)
    attackDataframe = pandas.DataFrame(attackResults, columns=['relativeGiantClusterSize', 'diameter'])
    ascisse = numpy.linspace(0,100, num=steps, dtype='int')
    attackDataframe['percentuale'] = ascisse
    
    return attackDataframe


# In[17]:


#gestori = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]
#colori = ['#004184','#ff3300','#ff8000','#018ECC', '#4d4d4d']

#gestori = ["Tim", "Vodafone", "Wind", "Tre"]
#colori = ['#004184','#ff3300','#ff8000','#018ECC']

gestori = ["Roma"]
colori = ['#004184']


# In[ ]:


# data reading, calculations, data writing

# TODO parallelizzare
for provider in gestori:
    
    # read data
    adjacencyMatrix = numpy.genfromtxt(("../data/graphs/adiacenzaEuclidea_{0}.csv".format(provider)),
                                 delimiter=',',
                                 dtype='int')
    providerGraph = networkx.Graph(adjacencyMatrix)
    
    # calculate results
#    print provider, "random failure:"
#    %time failureResults = randomFailure(providerGraph, steps=101) # default: steps=101
    print provider, "intentional attack:"
    get_ipython().magic(u'time attackResults = intentionalAttack(providerGraph, steps=11)')
    
    # write on file
#    failureResults.to_csv('../data/percolation/randomFailure_{0}.csv'.format(provider), index=False)
    attackResults.to_csv('../data/percolation/intentionalAttack_{0}.csv'.format(provider), index=False)


# In[ ]:




# In[ ]:



