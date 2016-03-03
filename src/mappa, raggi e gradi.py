
# coding: utf-8

# In[2]:

import numpy
import pandas

import matplotlib
from matplotlib import pyplot
get_ipython().magic(u'matplotlib inline')

import scipy
from scipy import stats # TODO vedere perché non fa chiamare il modulo direttamente

import gmaps


# ## Creazione della mappa
# 
# invece che uno scatterplot con dei raggi, la libreria ci consente solo di fare una heatmap (eventualmente pesata)
# 

# In[3]:

roma = pandas.read_csv("../data/Roma_towers.csv")
coordinate = roma[['lat', 'lon']].values


# In[3]:

heatmap = gmaps.heatmap(coordinate)
gmaps.display(heatmap)

# TODO scrivere che dietro queste due semplici linee ci sta un pomeriggio intero di smadonnamenti


# ## Analisi del raggio di copertura delle antenne
# 
# dato che ci servirà fare un grafico con scale logaritmiche teniamo solo i dati con
# > range =! 0

# In[4]:


# condizioni di filtro
raggioMin = 1
# raggioMax = 1000
raggiPositivi = roma.range >= raggioMin
# raggiCorti = roma.range < raggioMax

# query con le condizioni
#romaFiltrato = roma[raggiPositivi & raggiCorti]
romaFiltrato = roma[raggiPositivi]
raggi = romaFiltrato.range

print max(raggi)


# In[16]:


# logaritmic (base 2) binning in log-log (base 10) plots of integer histograms

def logBinnedHist(histogramResults):
    """
    histogramResults = numpy.histogram(...)
        OR matplotlib.pyplot.hist(...)
    
    returns x, y
    to be used with matplotlib.pyplot.step(x, y, where='post')
    """
    
    values, binEdges, others = histogramResults
    
    # print binEdges
    
    # TODO
    # if 0 in binEdges:
    #     return "error: log2(0) = ?"
    
    # print len(values), len(binEdges)
    
    # print binEdges # TODO vedere quando non si parte da 1
    
    # int arrotonda all'intero inferiore
    linMin = min(binEdges)
    linMax = max(binEdges)
    
    # print linMin, linMax
    
    logStart = int(numpy.log2(linMin))
    logStop = int(numpy.log2(linMax))
    
    # print logStart, logStop
    
    nLogBins = logStop - logStart + 1
    
    # print nLogBins
    
    logBins = numpy.logspace(logStart, logStop, num=nLogBins, base=2, dtype=int)
    # print logBins
    
    # 1,2,4,8,16,32,64,128,256,512,1024
    
    ######################
    
    linStart = 2**logStop + 1
    linStop = linMax
    
    # print linStart, linStop
    
    nLinBins = linStop - linStart + 1
    
    # print nLinBins
    
    linBins = numpy.linspace(linStart, linStop, num=nLinBins, dtype=int)
    
    # print linBins
    
    ######################
    
    bins = numpy.append(logBins, linBins)
    
    # print bins
    
    # print len(bins)
    
    totalValues, binEdges, otherBinNumbers = scipy.stats.binned_statistic(raggi.values,
                                                                         raggi.values,
                                                                         statistic='count',
                                                                         bins=bins)
    
    # print totalValues
    # print len(totalValues)
    
    # uso le proprietà dei logaritmi in base 2:
    # 2^(n+1) - 2^n = 2^n
    correzioniDatiCanalizzatiLog = numpy.delete(logBins, -1)
    
    # print correzioniDatiCanalizzatiLog
    
    # print len(correzioniDatiCanalizzatiLog)
    
    correzioniDatiCanalizzatiLin = numpy.ones(nLinBins, dtype=int)
    
    # print correzioniDatiCanalizzatiLin
    
    # print len(correzioniDatiCanalizzatiLin)
    
    correzioniDatiCanalizzati = numpy.append(correzioniDatiCanalizzatiLog, correzioniDatiCanalizzatiLin)
    
    # print correzioniDatiCanalizzati
    
    # print len(correzioniDatiCanalizzati)
    
    
    
    
    x = numpy.concatenate(([0], bins))
    conteggi = totalValues/correzioniDatiCanalizzati
    
    # TODO caso speciale per il grafico di sotto
    # (per non fare vedere la parte oltre l'ultima potenza di 2)
    l = len(correzioniDatiCanalizzatiLin)
    conteggi[-l:] = numpy.zeros(l, dtype='int')
    
    y = numpy.concatenate(([0], conteggi, [0]))
    
    return x, y


# In[17]:


# creazione di un istogramma log-log per la distribuzione del raggio di copertura

# TODO provare a raggruppare le code
# esempio: con bins=100
# oppure con canalizzazione a logaritmo di 2, ma mediato
# in modo che venga equispaziato nel grafico logaritmico
# il programma vuole pesati i dati e non i canali
# si potrebbe implementare una mappa che pesa i dati
# secondo la funzione divisione intera per logaritmo di 2
# TODO mettere cerchietto che indica il range massimo oppure scritta in rosso "20341 m!"
# TODO spiegare perché ci sono così tanti conteggi a 1,2,4,... metri
# TODO ricavare il range dai dati grezzi, facendo un algoritmo di clustering
# sulle varie osservazioni delle antenne. machine learning?
# TODO scrivere funzione che fa grafici logaritmici con canali
# equispaziati nel plot logaritmico (canali pesati)

# impostazioni plot complessivo
# pyplot.figure(figsize=(20,8)) # dimensioni in pollici
pyplot.figure(figsize=(15,15))
matplotlib.pyplot.xlim(10**0,10**5)
matplotlib.pyplot.ylim(10**-3,10**2)
pyplot.title('Distribuzione del raggio di copertura')
pyplot.ylabel("Numero di antenne")
pyplot.xlabel("Copertura [m]")
# pyplot.gca().set_xscale("log")
# pyplot.gca().set_yscale("log")
pyplot.xscale("log")
pyplot.yscale("log")

# lin binning
distribuzioneRange = pyplot.hist(raggi.values,
                                bins=max(raggi)-min(raggi),
                                histtype='step',
                                color='#3385ff',
                                label='lin binning')

# log_2 binning
x, y = logBinnedHist(distribuzioneRange)
matplotlib.pyplot.step(x, y, where='post', color='#ff3300', linewidth=2, label='log_2 weighted binning') #where = mid OR post
# matplotlib.pyplot.plot(x, y)

# linea verticale ad indicare il massimo grado
pyplot.axvline(x=max(raggi), color='#808080', linestyle='dotted', label='max range (20341m)')

# legenda e salvataggio
pyplot.legend(loc='lower left', frameon=False)
pyplot.savefig('../img/range/range_distribution.eps', format='eps', dpi=600)



# In[ ]:




# In[ ]:

# TODO fare funzione cumulativa di Capocci e anche altra cosa (vedere foglietti)


# In[ ]:




# In[ ]:




# In[ ]:




# In[8]:

# TODO vedere se il grafo finale non è scale free, 
# non è reticolo geometrico.
# è una specie di vetro


# In[9]:

# Tre = roma.net == 99
# treCell = roma[Tre].reset_index(drop=True)
# treCell

# TODO snellire il dataframe iniziale levando le colonne inutili

dataframe = pandas.read_csv("../data/cell_towers_diff-2016012100.csv")
troncato = dataframe[50:70]
ordinato = troncato.reset_index(drop=True)
ordinato


# In[10]:


# criteri di filtro per le compagnie telefoniche
isTim = roma.net == 1
isWind = roma.net == 88
isVodafone = roma.net == 10
isTre = roma.net == 99

# creazione dei dataframe separati per gestore
tim = roma[isTim].reset_index(drop=True)
wind = roma[isWind].reset_index(drop=True)
vodafone = roma[isVodafone].reset_index(drop=True)
tre = roma[isTre].reset_index(drop=True)
 


# In[11]:

tim = romaFiltrato[isTim].reset_index(drop=True)
wind = romaFiltrato[isWind].reset_index(drop=True)
vodafone = romaFiltrato[isVodafone].reset_index(drop=True)
tre = romaFiltrato[isTre].reset_index(drop=True)


# In[12]:

compagnie = ['Tim','Wind','Vodafone','Tre','aggregati']

colori = ['#0066ff','#ff8000','#ff3300','#99ccff','#4d4d4d']

valori = [tim.range.values, wind.range.values, vodafone.range.values, tre.range.values, raggi.values]

pyplot.figure(figsize=(20,8)) # dimensioni in pollici
distribuzioneRangeTutti = pyplot.hist(valori,                                 bins=max(raggi)-min(raggi),                                 histtype='step',                                 label=compagnie,                                 color=colori
                                )
pyplot.title('Distribuzione della copertura')
pyplot.ylabel("Numero di antenne")
pyplot.xlabel("Copertura [m]")
# pyplot.gca().set_xscale("log")
# pyplot.gca().set_yscale("log")
pyplot.xscale("log")
pyplot.yscale("log")
pyplot.legend()

# TODO prendere colori aggiornati dal notebook di Iuri
# TODO mettere la legenda coi loghi delle compagnie
# oppure mettere direttamente le scritte del colore corrispondente,
# magari anche attaccate al relativo istogramma
# TODO levare il bordo del riquadro della legenda
# TODO provare istogramma stacked, in modo da dare il totale
# TODO scrivere che dietro il futuro istogramma equispaziato ci sta un giorno di lavoro


# TODO (futuristico):
# vedere se esiste un modo per mettere due o più computer in rete a fare una piccola grid, per condividere la potenza di calcolo, la memoria ram e lo spazio su disco
# 
# ## TODO prove da sistemare per canalizzazione logaritmic in base 2

# In[13]:

pyplot.figure(figsize=(20,8))
distribuzioneRange = pyplot.hist(raggi.values,                                 bins=div,                                 histtype='step')
pyplot.title('PROVA, CON CANALI NON ANCORA PESATI')
pyplot.xscale("log")
pyplot.yscale("log")


# In[14]:

a,b,c = distribuzioneRange


# In[15]:

a1 = numpy.append(a.astype(int), 0)


# In[16]:

b1 = b.astype(int)


# In[17]:

a1


# In[18]:

b1


# In[19]:

div = numpy.logspace(start=0, stop=15, num=16, base=2).astype(int) # max = 20341
div


# In[20]:

a2 = a1/div
a2


# In[21]:

pyplot.scatter(y=a2,x=div)
pyplot.xscale("log")
pyplot.yscale("log")


# In[22]:

# TODO vedere se le due slope del grafico log-log possono essere
# messe in relazione con le due slode della legge
# di Heap e di Zipf (o come cavolo si scrivono)


# In[23]:

# TODO esterno:

# datigenerati = numpy.random.normal(0,1, 10000)
# b = pylab.hist(datigenerati,bins=100, histtype='step')
# plottare la gaussiana di origine, 
# fare i residui e vedere che il loro istogramma 
# è di nuovo gaussiano e farne un fit e vedere 
# se il residui dei residui sono gaussiani, 
# che al mercato mio padre comprò


# In[24]:

# TODO
# fit e lot della distribuzione del grado con i due modelli di rete
# Erdos Renyi
# preferential attachement di Barabasi Albert


# ## distribuzione del grado
# 
# si fa un plot logaritmico unificato e poi i relativi fit con i vari modelli di rete

# In[25]:


gradi = [numpy.loadtxt("../data/DistrGrado_{0}".format(compagnia)) for compagnia in compagnie]

# dataframeGradi = pandas.DataFrame(numpy.transpose(gradi))

# grado = grafo.degree().values
# grado = numpy.loadtxt("../data/DistrGrado_{0}",compagnia)


# In[26]:

pyplot.figure(figsize=(20,8)) # dimensioni in pollici
distribuzioneRangeTutti = pyplot.hist(gradi,                                 bins=max(gradi[-1])-min(gradi[-1]),                                 histtype='step',                                 label=compagnie,                                 color=colori
                                )
pyplot.title('Degree distribution')
pyplot.ylabel("Frequency")
pyplot.xlabel("Degree")
# pyplot.gca().set_xscale("log")
# pyplot.gca().set_yscale("log")
pyplot.xscale("log")
pyplot.yscale("log")
pyplot.legend()


# ###  altro approccio, con i dataframe

# In[27]:

dictGradi = dict()
for label in compagnie:
    dictGradi[label] = numpy.loadtxt("../data/DistrGrado_{0}".format(label)).astype(int)

dictGradi


# In[28]:


# TODO vedere se c'è un metodo migliore rispetto a transpose()
dataframeGradi = pandas.DataFrame.from_dict(dictGradi, orient='index').transpose()
# TODO attenzione ai valori NaN nei posti vuoti


# In[41]:

canali = int(max(dataframeGradi.aggregati)-min(dataframeGradi.aggregati))

kwds = {
    "bins": canali,
    "histtype": 'step',
    # "color": colori,
    #"fill": True,
    #"alpha": 0.25,
    #"linestyle": "solid",
    #"edgecolor": "black"
}

dataframeGradi.plot(kind='hist', loglog=True, figsize=(20,8), **kwds)


# In[ ]:



