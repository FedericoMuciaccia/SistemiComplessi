
# coding: utf-8

# In[14]:

import numpy

import matplotlib # TODO bug in ipython? (sometime can't call the module directly)
from matplotlib import pyplot

import scipy
from scipy import stats
from scipy import optimize

get_ipython().magic(u'matplotlib inline')


# In[15]:

import math

def poissoniana(x, mu):
    return (numpy.exp(-mu) * mu**x)/ (scipy.misc.factorial(x)) # if x >= 0


# In[16]:

x = numpy.linspace(1,1000,1000)
# y = poissoniana(x, 3)
y = dataframeGradi.Tre.values


# In[17]:

popt, pcov = scipy.optimize.curve_fit(poissoniana, x, y)


# In[18]:

y, x = numpy.histogram(dataframeGradi.aggregati.values, bins = 3)


# In[19]:

min(dataframeGradi.aggregati.values)


# In[20]:

len(y),len(x)


# In[21]:

y,x


# In[22]:

arr = [5,5,5,5,5,6,6,6,7,7]

y, x = numpy.histogram(numpy.array(arr), bins=(5,6,7,8))


# In[23]:

y,x


# In[24]:

pyplot.hist(arr, bins=(5,6,7,8))


# In[25]:

pyplot.hist(arr, bins=3)


# In[26]:

pyplot.hist(arr, bins=3, align="left")


# In[27]:

pyplot.hist(arr, bins=(5,6,7,8), align="mid")


# In[28]:

pyplot.hist(arr, bins=(5,6,7,8), align="left")


# In[29]:

def integerHistogram(integerData):
    integerData = [5,5,5,5,5,6,6,6,7,7]
    minimum = min(integerData)
    maximum = max(integerData)
    integerBins = maximum - minimum + 1
    numberSet = numpy.linspace(minimum, maximum, integerBins)
    y, x = numpy.histogram(arr, bins=(5,6,7,8))
    


# In[30]:

numpy.histogram(arr, bins=(5,6,7,8))


# In[31]:

integerData = [5,5,5,5,5,6,6,6,7,7,9,10,10]
minimum = min(integerData)
maximum = max(integerData)
integerBins = maximum - minimum + 1
numberSet = numpy.linspace(minimum, maximum, integerBins, dtype=int)
min(integerData), max(integerData)


# In[32]:

numberSet


# In[33]:

numpyBins = numberSet + [minimum+1]


# In[34]:

numpyBins


# 
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.transpose.html
# http://stackoverflow.com/questions/17779316/un-normalized-gaussian-curve-on-histogram
# !!!    http://glowingpython.blogspot.it/2012/07/distribution-fitting-with-scipy.html
# http://danielhnyk.cz/fitting-distribution-histogram-using-python/
# http://stackoverflow.com/questions/19736080/creating-dataframe-from-a-dictionary-where-entries-have-different-lengths
# !!!    https://plot.ly/pandas/histograms/
# https://www.python.org/dev/peps/pep-0008/
# http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
# http://docs.scipy.org/doc/scipy/reference/stats.html
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html#scipy.stats.poisson
# http://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.bincount.html#numpy.bincount
# http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linspace.html
# 
# 
# 
# 
# 

# In[ ]:



