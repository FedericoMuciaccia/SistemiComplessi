
# coding: utf-8

# In[13]:


import numpy

# pyplot is a sub-module of matplotlib
# which doesn't get imported with a simple import matplotlib
import matplotlib.pyplot

# non bisogna fare plottare la figura nel notebook,
# altrimenti il risultante SVG sarà vuoto
# %matplotlib inline


# In[14]:


x = numpy.arange(0,100,0.01)
y = x*numpy.sin(2*numpy.pi*x)

matplotlib.pyplot.plot(y)
# non lo si fa plottare


# In[15]:


# TODO funziona solo una volta sola
# le volte successive che viene eseguito restituisce
# una figura bianca. secondo me bisogna assegrare una
# variabile alla figura, da poi richiamare in seguito
# esempio: myFigure = matplotlib.pyplot.plot(...)
matplotlib.pyplot.savefig("../img/test.svg", format="svg", transparent=True)


# In[ ]:



