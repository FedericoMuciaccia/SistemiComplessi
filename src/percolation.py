
# coding: utf-8

# # Percolation

# In[2]:


import numpy, networkx, pandas

# import graph_tool
# from graph_tool.all import *

# from matplotlib import pyplot

# %matplotlib inline


# In[3]:


# simple parallelization

# import multiprocessing
# cpus = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cpus)
# pool.map(...)


# ## Random failure

# In[4]:


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
        # subgraphs = sorted(networkx.connected_component_subgraphs(newGraph), key = len, reverse=True)
        subgraphs = networkx.connected_component_subgraphs(newGraph)
        try:
            # giantCluster = subgraphs[0]
            giantCluster = max(subgraphs, key = networkx.number_of_nodes)
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

# In[5]:


def intentionalAttack(graph, steps=101):
    initialGraph = graph
    initialGraphSize = networkx.number_of_nodes(initialGraph)
    numbersOfNodesToRemove = numpy.linspace(0, initialGraphSize, num=steps, dtype='int')
    initialNodes = initialGraph.nodes()
    
    initialDegrees = initialGraph.degree()
    degreeDataframe = pandas.DataFrame(initialDegrees.items(), columns=['ID', 'degree'])
    degreeDataframe.sort(["degree"], ascending=[False], inplace=True) # TODO vedere se si può fare a meno di una colonna
    # degreeDataframe = degreeDataframe.reset_index(drop=True)
    sortedNodes = degreeDataframe['ID'].values # TODO degreeDataframe.ID
    
    def analyzeSingleGraph(number):
        # TODO vedere se si possono agevolmente parallelizzare le list comprehension
        # che sono molto più scorrevoli da usare ripetto a map() 
        newGraph = initialGraph.copy()
        newGraph.remove_nodes_from(sortedNodes[0:number]) # TODO vedere ordinamento più veloce
        newGraphSize = networkx.number_of_nodes(newGraph)
        grado = newGraph.degree().items()
        # subgraphs = sorted(networkx.connected_component_subgraphs(newGraph), key = len, reverse=True)
        subgraphs = networkx.connected_component_subgraphs(newGraph)
        try:
            # giantCluster = subgraphs[0]
            giantCluster = max(subgraphs, key = networkx.number_of_nodes)
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


# In[7]:


#gestori = ["Tim", "Vodafone", "Wind", "Tre", "Roma"]
#colori = ['#004184','#ff3300','#ff8000','#018ECC', '#4d4d4d']

#gestori = ["Tim", "Vodafone", "Wind", "Tre"]
#colori = ['#004184','#ff3300','#ff8000','#018ECC']

gestori = ["Roma"]
colori = ['#004184']


# In[9]:


# data reading, calculations, data writing

# TODO parallelizzare
for provider in gestori:
    
    # read data
    adjacencyMatrix = numpy.genfromtxt(("/home/protoss/Documenti/Siscomp_datas/data/AdiacenzaEuclidea_{0}.csv".format(provider)),
                                 delimiter=',',
                                 dtype='int')
    providerGraph = networkx.Graph(adjacencyMatrix)
    
    # calculate results
    print provider, "random failure:"
    get_ipython().magic(u'time failureResults = randomFailure(providerGraph, steps=10) # default: steps=101')
#    print provider, "intentional attack:"
#    %time attackResults = intentionalAttack(providerGraph, steps=101)
    
    # write on file
    failureResults.to_csv('../data/percolation/ComparazioneRandom{0}.csv'.format(provider), index=False)
#    attackResults.to_csv('../data/percolation/intentionalAttack_{0}.csv'.format(provider), index=False)


# In[ ]:




# In[ ]:



