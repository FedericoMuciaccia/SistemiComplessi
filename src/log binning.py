
# coding: utf-8

# ## logaritmic (base 2) binning in log-log (base 10) plots of integer histograms

# In[67]:

import numpy

import matplotlib.pyplot

get_ipython().magic(u'matplotlib inline')


# In[114]:


DA BUTTARE


def  logBinnedStepPlot(histogramResults):
    if 0 in integerData:
        return "error: log2(0) = ?"

# y, binEdges = np.histogram(...)

# plt.bar(bin_edges[:-1], hist, width=1) and plt.xlim(min(bin_edges), max(bin_edges))

# plt.plot(x, y, ls='steps')

values, binEdges, others = histogramResults


# In[120]:


DA BUTTARE

binEdges = range(1,20)
print binEdges # TODO vedere quando non si parte da 1

# int arrotonda all'intero inferiore
linMin = min(binEdges)
linMax = max(binEdges)

print linMin, linMax

logStart = int(numpy.log2(linMin))
logStop = int(numpy.log2(linMax))

print logStart, logStop

nLogBins = logStop - logStart + 1

print nLogBins

logBins = numpy.logspace(logStart, logStop, num=nLogBins, base=2, dtype=int)
print logBins

# 1,2,4,8,16,32,64,128,256,512,1024

linStart = 2**logStop + 1
linStop = linMax

print linStart, linStop

nLinBins = linStop - linStart + 1

print nLinBins

linBins = numpy.linspace(linStart, linStop, num=nLinBins, dtype=int)

print linBins

bins = numpy.append(logBins, linBins)

print bins

print len(bins)


# In[121]:


DA BUTTARE


# uso le proprietà dei logaritmi in base 2:
# 2^(n+1) - 2^n = 2^n
divisoriDatiCanalizzatiLog = numpy.delete(logBins, -1)

print divisoriDatiCanalizzatiLog

divisoriDatiCanalizzatiLin = numpy.ones(nLinBins, dtype=int)

print divisoriDatiCanalizzatiLin

print len(divisoriDatiCanalizzatiLin)

divisoriDatiCanalizzati = numpy.append(divisoriDatiCanalizzatiLog, divisoriDatiCanalizzatiLin)

print divisoriDatiCanalizzati

print len(divisoriDatiCanalizzati)


# In[113]:


x = numpy.concatenate(([0], bins))
conteggi = values
y = numpy.concatenate(([0], conteggi, [0]))
matplotlib.pyplot.plot(x, y)

matplotlib.pyplot.xscale('log')
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.step(x, y, where='post') #where = mid OR post
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.ylim(0,10)


# In[86]:

numpy.concatenate([0], conteggi, [0])


# In[ ]:




# In[ ]:



