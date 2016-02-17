
# coding: utf-8

# In[1]:

import numpy
import pandas
from matplotlib import pyplot
get_ipython().magic(u'matplotlib inline')

import gmaps


# ## Creazione della mappa
# 
# invece che uno scatterplot con dei raggi, la libreria ci consente solo di fare una heatmap (eventualmente pesata)
# 

# In[2]:

roma = pandas.read_csv("../data/roma_towers.csv")
coordinate = roma[['lat', 'lon']].values


# In[30]:

gmaps.heatmap(coordinate)


# ## Analisi del raggio di copertura delle antenne
# 
# dato che ci servirà fare un grafico con scale logaritmiche eliminiamo i dati con
# > range = 0

# In[29]:


# condizioni di filtro
raggioMin = 1
raggioMax = 1000
raggiPositivi = roma.range >= raggioMin
raggiCorti = roma.range < raggioMax

# query con le condizioni
raggi = roma[raggiPositivi & raggiCorti].range

print min(raggi), max(raggi)


# In[25]:


distribuzioneRange = pyplot.hist(raggi.values,bins=max(raggi)-min(raggi), histtype='step')
pyplot.title('Range distribution')
pyplot.xlabel("Degree")
pyplot.ylabel("Frequency")

pyplot.gca().set_xscale("log")
pyplot.gca().set_yscale("log")


# In[26]:

distribuzioneRange = pyplot.hist(raggi.values,bins=100, histtype='step')
pyplot.title('Range distribution')
pyplot.xlabel("Degree")
pyplot.ylabel("Frequency")

pyplot.gca().set_xscale("log")
pyplot.gca().set_yscale("log")


# In[ ]:



