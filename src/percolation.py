
# coding: utf-8

# # Percolation

# In[102]:


import numpy, networkx, pandas, matplotlib, seaborn

# import graph_tool
# from graph_tool.all import *

from matplotlib import pyplot

get_ipython().magic(u'matplotlib inline')


# In[103]:


# simple parallelization

# import multiprocessing
# cpus = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cpus)
# pool.map(...)


# ## Random failure

# In[104]:


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
        subgraphs = networkx.connected_component_subgraphs(newGraph)
        try:
            giantCluster = subgraphs[0]
            giantClusterSize = networkx.number_of_nodes(giantCluster)
            relativeGiantClusterSize = numpy.true_divide(giantClusterSize, newGraphSize)
            diameter = networkx.diameter(giantCluster, e=None)
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


# In[109]:


# calculating

gestore = ["Tim", "Vodafone", "Wind", "Tre"]
#
gestore = ["Tre"]

    

# TODO parallelizzare
for provider in gestore:
    adiacenza = numpy.genfromtxt(("/home/federico/dati Iuri/AdiacenzaEuclidea_{0}.csv".format(provider)),                                 delimiter=',',                                 dtype='int')
    providerGraph = networkx.Graph(adiacenza)
    print "random failure:"
    get_ipython().magic(u'time failureResults = randomFailure(providerGraph, steps=101) # 101')


# TODO fare diametro relativo e scatterplot di correlazione tra diametro relativo e relativeGiantClusterSize


# In[118]:


# plotting

failureResults.plot(kind = 'scatter',
                   x = 'percentuale',
                   y = 'diameter',
                   s = 90,
                   title = 'Random failure',
                   xlim = (0, 101),
                   ylim = (0, max(failureResults.diameter)+1),
                   figsize = (16,12),
                   grid = False,
                   alpha = 0.8,
                   label = 'Tre',
                   antialiased = True)

pyplot.xlabel("Percentuale")
pyplot.ylabel("Diametro")
pyplot.savefig('../img/randomFailure_diameter.eps', format='eps', dpi=600)

failureResults.plot(kind = 'scatter',
                   x = 'percentuale',
                   y = 'relativeGiantClusterSize',
                   s = 90,
                   title = 'Random failure',
                   xlim = (0, 101),
                   ylim = (0, 1.02),
                   figsize = (16,12),
                   grid = False,
                   alpha = 0.8,
                   label = 'Tre',
                   antialiased = True)

pyplot.xlabel("Percentuale")
pyplot.ylabel("Dimensione relativa del giant cluster")
pyplot.savefig('../img/randomFailure_relativeGiantClusterSize.eps', format='eps', dpi=600)


#seaborn.set_context("notebook", font_scale=1.1)
#seaborn.set_style("ticks")
#
#seaborn.lmplot('percentuale', 'diameter',
#           data=failureResults,
#           fit_reg=False,
#           size = 7,
#           aspect = 1.7778,
#           # hue='Compagnia', # TODO
#           scatter_kws={"marker": "D", "s": 100})
#pyplot.title('Random failure')
#pyplot.xlabel("Percentuale")
#pyplot.ylabel("Diametro")
#pyplot.xlim(0, 101)
#pyplot.ylim(0, max(failureResults.diameter)+1)
#pyplot.savefig('../img/randomFailure_diameter.eps', format='eps', dpi=600)
#
#seaborn.lmplot('percentuale', 'relativeGiantClusterSize',
#           data=failureResults,
#           fit_reg=False,
#           size = 7,
#           aspect = 1.7778,
#           # hue='Compagnia', # TODO
#           scatter_kws={"marker": "D", "s": 100})
#pyplot.title('Random failure')
#pyplot.xlabel("Percentuale")
#pyplot.ylabel("Dimensione relativa del giant cluster")
#pyplot.xlim(0, 101)
#pyplot.ylim(0, 1.02)
#pyplot.savefig('../img/randomFailure_relativeGiantClusterSize.eps', format='eps', dpi=600)


# ## Intentional attack

# In[112]:


def intentionalAttack(graph, steps=101):
    initialGraph = graph
    initialGraphSize = networkx.number_of_nodes(initialGraph)
    numbersOfNodesToRemove = numpy.linspace(0, initialGraphSize, num=steps, dtype='int')
    initialNodes = initialGraph.nodes()
    
    
    initialDegrees = initialGraph.degree()
    degreeDataframe = pandas.DataFrame(initialDegrees.items(), columns=['index', 'degree'])
    degreeDataframe.sort(["degree"], ascending=[False], inplace=True) # TODO
    degreeDataframe = degreeDataframe.reset_index(drop=True) # TODO
    
    sortedNodes = degreeDataframe['index'].values # TODO degreeDataframe.index
    
    # TODO vedere se ritornare pure i degree ordinati da mettere come sfondo al grafico di matplotlib
    
    def analyzeSingleGraph(index):
        # TODO vedere se si possono agevolmente parallelizzare le list comprehension
        # che sono molto più scorrevoli da usare ripetto a map() 
        newGraph = initialGraph.copy()
        newGraph.remove_nodes_from(sortedNodes[0:index]) # TODO vedere ordinamento più veloce
        newGraphSize = networkx.number_of_nodes(newGraph)
        grado = newGraph.degree().items()
        subgraphs = networkx.connected_component_subgraphs(newGraph)
        try:
            giantCluster = subgraphs[0]
            giantClusterSize = networkx.number_of_nodes(giantCluster)
            relativeGiantClusterSize = numpy.true_divide(giantClusterSize, newGraphSize)
            diameter = networkx.diameter(giantCluster, e=None)
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


# In[113]:


# calculating

gestore = ["Tim", "Vodafone", "Wind", "Tre"]
#
gestore = ["Tre"]


# TODO parallelizzare
for provider in gestore:
    adiacenza = numpy.genfromtxt(("/home/federico/dati Iuri/AdiacenzaEuclidea_{0}.csv".format(provider)),                                 delimiter=',',                                 dtype='int')
    providerGraph = networkx.Graph(adiacenza)
    print "intentional attack:"
    get_ipython().magic(u'time attackResults = intentionalAttack(providerGraph, steps=101)')
# TODO fare diametro relativo e scatterplot di correlazione tra diametro relativo e relativeGiantClusterSize


# In[119]:


# plotting

attackResults.plot(kind = 'scatter',
                   x = 'percentuale',
                   y = 'diameter',
                   s = 90,
                   title = 'Intentional attack',
                   xlim = (0, 101),
                   ylim = (0, max(attackResults.diameter)+1),
                   figsize = (16,12),
                   grid = False,
                   alpha = 0.8,
                   label = 'Tre',
                   antialiased = True)

pyplot.xlabel("Percentuale")
pyplot.ylabel("Diametro")
pyplot.savefig('../img/intentionalAttack_diameter.eps', format='eps', dpi=600)


attackResults.plot(kind = 'scatter',
                   x = 'percentuale',
                   y = 'relativeGiantClusterSize',
                   s = 90,
                   title = 'Intentional attack',
                   xlim = (0, 101),
                   ylim = (0, 1.02),
                   figsize = (16,12),
                   grid = False,
                   alpha = 0.8,
                   label = 'Tre',
                   antialiased = True)

pyplot.xlabel("Percentuale")
pyplot.ylabel("Dimensione relativa del giant cluster")
pyplot.savefig('../img/intentionalAttack_relativeGiantClusterSize.eps', format='eps', dpi=600)



# pyplot.figure(1)
# pyplot.subplot(211)
# ...
# pyplot.subplot(212)
# ...

# x : label or position, default None
# y : label or position, default None
# subplots=True
# sharex=True
# layout=    tuple (rows, columns)
# legend=      False/True/’reverse’
#style : list or dict
#    matplotlib line style per column
#logx : boolean, default False
#    Use log scaling on x axis
#logy : boolean, default False
#    Use log scaling on y axis
#loglog : boolean, default False
#    Use log scaling on both x and y axes
#fontsize : int, default None
#    Font size for xticks and yticks
#colormap : str or matplotlib colormap object, default None
#    Colormap to select colors from. If string, load colormap with that name from matplotlib.
#colorbar : boolean, optional
#    If True, plot colorbar (only relevant for ‘scatter’ and ‘hexbin’ plots)
#table : boolean, Series or DataFrame, default False
#    If True, draw a table using the data in the DataFrame and the data will be transposed to meet matplotlib’s default layout. If a Series or DataFrame is passed, use passed data to draw a table.
#sort_columns : boolean, default False
#    Sort column names to determine plot ordering
#secondary_y : boolean or sequence, default False
#    Whether to plot on the secondary y-axis If a list/tuple, which columns to plot on secondary y-axis
#kwds : keywords
#    Options to pass to matplotlib plotting method



# In[ ]:

# TODO mettere colori corretti e fare plot con tutti
# TODO levare l'asse superiore e l'asse destro


# In[123]:


# correlazione

failureResults.plot(kind = 'scatter',
                   x = 'diameter',
                   y = 'relativeGiantClusterSize',
                   s = 90,
                   title = 'Correlation (random failure)',
                   xlim = (0, max(failureResults.diameter)+1),
                   ylim = (0,1.02),
                   figsize = (16,12),
                   grid = False,
                   alpha = 0.8,
                   label = 'Tre',
                   antialiased = True)

pyplot.xlabel("Diametro")
pyplot.ylabel("Dimensione relativa del giant cluster")


attackResults.plot(kind = 'scatter',
                   x = 'diameter',
                   y = 'relativeGiantClusterSize',
                   s = 90,
                   title = 'Correlation (intentional attack)',
                   xlim = (0, max(attackResults.diameter)+1),
                   ylim = (0,1.02),
                   figsize = (16,12),
                   grid = False,
                   alpha = 0.8,
                   label = 'Tre',
                   antialiased = True)

pyplot.xlabel("Diametro")
pyplot.ylabel("Dimensione relativa del giant cluster")


# In[ ]:



