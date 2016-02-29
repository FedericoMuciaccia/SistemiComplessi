
# coding: utf-8

# In[3]:

import numpy, networkx, pandas

# import graph_tool
# from graph_tool.all import *

from matplotlib import pyplot

get_ipython().magic(u'matplotlib inline')


# In[ ]:




# In[ ]:




# In[ ]:




# In[2]:

gestori = ["Tim", "Tre"]
colori = ['#004184','#018ECC']


# In[3]:


# plotting



# legge i dati scritti su disco,
# in modo da non dover rifare sempre il calcolo
# e rendere indipendente dal resto questo blocco di codice
for provider, colore in zip(gestori, colori):
    failureResults = pandas.read_csv('../data/percolation/randomFailure_{0}.csv'.format(provider))
    attackResults = pandas.read_csv('../data/percolation/intentionalAttack_{0}.csv'.format(provider))
    


# TODO mettere colori corretti per i plot con tutti
# TODO levare l'asse superiore e l'asse destro

# facecolor='green',                   
# # **{'color': colore}


# TODO
#/usr/lib/python2.7/dist-packages/matplotlib/collections.py:571: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
#  if self._edgecolors == str('face'):


# initialize the figure
#figura = pyplot.figure(figsize=(20,12))


    pyplot.scatter(x = failureResults.percentuale,
                   y = failureResults.diameter,
                   s = 90,
                   #figsize = (16,12),
                   #grid = False,
                   # alpha = 0.8,
                   label = provider,
                   color = colore,
                   antialiased = True,
                   marker = 'o')

pyplot.alpha = 0.1
pyplot.xlim = (0, 101)
pyplot.ylim = (0, 15)    # TODO        
pyplot.title('Random failure')
pyplot.xlabel("Percentuale")
pyplot.ylabel("Diametro")
pyplot.legend(loc='best', frameon=False)
#pyplot.savefig('../img/percolation/randomFailure_diameter.eps', format='eps', dpi=600)



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
                   antialiased = True,
                   marker = 'o')

#pyplot.xlabel("Percentuale")
#pyplot.ylabel("Dimensione relativa del giant cluster")
#pyplot.savefig('../img/percolation/randomFailure_relativeGiantClusterSize.eps', format='eps', dpi=600)



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

#pyplot.xlabel("Percentuale")
#pyplot.ylabel("Diametro")
#pyplot.savefig('../img/percolation/intentionalAttack_diameter.eps', format='eps', dpi=600)



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

#pyplot.xlabel("Percentuale")
#pyplot.ylabel("Dimensione relativa del giant cluster")
#pyplot.savefig('../img/percolation/intentionalAttack_relativeGiantClusterSize.eps', format='eps', dpi=600)



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

percentuali = []
diametriFailure = []

for provider, colore in zip(gestori, colori):
    failureResults = pandas.read_csv('../data/percolation/randomFailure_{0}.csv'.format(provider))
    attackResults = pandas.read_csv('../data/percolation/intentionalAttack_{0}.csv'.format(provider))
    percentuali.append(failureResults.percentuale)
    diametriFailure.append(failureResults.diameter)



pyplot.scatter(x = failureResults.percentuale,
                   y = failureResults.diameter,
                   #s = 90,
                   #figsize = (16,12),
                   #grid = False,
                   alpha = 0.8,
                   #label = provider,
                   color = colore,
                   antialiased = True,
                   marker = 'o')

pyplot.xlim = (0, 101)
pyplot.ylim = (0, 15)    # TODO        
pyplot.title('Random failure')
pyplot.xlabel("Percentuale")
pyplot.ylabel("Diametro")
pyplot.legend(loc='best', frameon=False)
#pyplot.savefig('../img/percolation/randomFailure_diameter.eps', format='eps', dpi=600)


# # GRAFICI seabornosi

# In[48]:

gestori = ["Tim", "Vodafone", "Wind", "Tre"]
colori = ['#004184','#ff3300','#ff8000','#018ECC']


# In[49]:

failureFrames = []
attackFrames = []

for provider in gestori:
    failureResults = pandas.read_csv('../data/percolation/randomFailure_{0}.csv'.format(provider))
    attackResults = pandas.read_csv('../data/percolation/intentionalAttack_{0}.csv'.format(provider))
    failureResults['Compagnia'] = provider
    attackResults['Compagnia'] = provider
    failureFrames.append(failureResults)
    attackFrames.append(attackResults)
    
failureFinal = pandas.concat(failureFrames)
attackFinal = pandas.concat(attackFrames)


# In[53]:

import seaborn
#grafici attack
attackFinal.head()

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#grafico andamento D
seaborn.lmplot('percentuale', 'diameter', data=attackFinal, fit_reg=False, 
               size = 7, aspect = 1.7778,  
               hue='Compagnia', palette = colori, 
                scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attacco: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,60)
pyplot.savefig('../img/federico/attackD_Final', format='eps', dpi=1000)


#grafico andamento GC
seaborn.lmplot('percentuale', 'relativeGiantClusterSize', data=attackFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Compagnia', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attacco: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('../img/federico/attackGC_Final', format='eps', dpi=1000)


# In[54]:

#grafici failure
failureFinal.head()

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#grafico andamento D
seaborn.lmplot('percentuale', 'diameter', data=failureFinal, fit_reg=False, 
               size = 7, aspect = 1.7778,  
               hue='Compagnia', palette = colori, 
                scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
#pyplot.ylim(0,max(diametro)+2)
pyplot.savefig('../img//federico/failureD_Final', format='eps', dpi=1000)


#grafico andamento GC
seaborn.lmplot('percentuale', 'relativeGiantClusterSize', data=failureFinal, fit_reg=False,
           size = 7, aspect = 1.7778,
           hue='Compagnia', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
pyplot.savefig('../img/federico/failureGC_Final', format='eps', dpi=1000)

