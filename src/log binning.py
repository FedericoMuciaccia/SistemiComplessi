
# coding: utf-8

# ## logaritmic (base 2) binning in log-log (base 10) plots of integer histograms

# In[1]:

import numpy


# In[132]:

# a = range(1, 129)
a = range(1, 14) # TODO vedere quando non si parte da 1
# print a

def  integerLogHistogram(integerData):
    if 0 in integerData:
        return "error: log2(0) = ?"

# int arrotonda all'intero inferiore
linMin = min(a)
linMax = max(a)

print linMin, linMax

logStart = int(numpy.log2(linMin))
logStop = int(numpy.log2(linMax))

print logStart, logStop

nLogBins = logStop - logStart + 1

print nLogBins

logBins = numpy.logspace(logStart, logStop, num=nLogBins, base=2, dtype=int)
print logBins

# 1,2,4,8,16,32,64,128,256,512,1024


# In[133]:

nPartialLinBins = 2**logStop - 2**logStart + 1

print nPartialLinBins

a = numpy.ones(nPartialLinBins, dtype=int)


# In[134]:

a
len(a)


# In[139]:



def numberArray(n):
    return n * numpy.ones(n, dtype=int)

pesi = map(numberArray, logBins)

print pesi

pesi = []

for i in logBins:
    numpy.append(pesi, numberArray(logBins[i -1]))

# TODO vedere numpy.nditer(logBins)

print pesi

b = logBins.astype(float)

print b

print numberArray(8)

c = 1/b

print c


# In[136]:

logWeights = 


# In[ ]:




# In[137]:


linStart = 2**logStop + 1
linStop = linMax

print linStart, linStop

nOtherLinBins = linStop - linStart + 1

print nLinBins

linBins = numpy.linspace(linStart, linStop, num=nOtherLinBins, dtype=int)

print linBins


# In[138]:

linWeights = numpy.ones(nOtherLinBins, dtype=int)

print linWeights

print len(linBins), len(linWeights)


# In[ ]:




# In[ ]:




# In[74]:

bins = numpy.append(logBins, linBins)

print bins


# In[ ]:

weights = numpy.append(logWeights, linWeights)

print weights

