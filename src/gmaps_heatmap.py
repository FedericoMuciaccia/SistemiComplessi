
# coding: utf-8

# In[1]:

import gmaps
import pandas


# In[2]:

# import numpy

# coordinate = ((41.899903, 12.335295), (41.900682, 12.694846))
# data = numpy.array(coordinate)

# gmaps.heatmap(data)


# In[3]:

roma = pandas.read_csv("../data/roma_towers.csv")
coordinate = roma[['lat', 'lon']].values


# In[4]:

gmaps.heatmap(coordinate)


# In[ ]:



