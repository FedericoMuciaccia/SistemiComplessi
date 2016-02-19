
# coding: utf-8

# In[31]:

import numpy
import pandas
from matplotlib import pyplot
get_ipython().magic(u'matplotlib inline')
from scipy import stats # TODO vedere perché non fa chiamare il modulo direttamente

import gmaps


# ## Creazione della mappa
# 
# invece che uno scatterplot con dei raggi, la libreria ci consente solo di fare una heatmap (eventualmente pesata)
# 

# In[5]:

roma = pandas.read_csv("../data/Roma_towers.csv")
coordinate = roma[['lat', 'lon']].values


# In[305]:

gmaps.heatmap(coordinate)

# TODO scrivere che dietro queste due semplici linee ci sta un pomeriggio intero di smadonnamenti


# ## Analisi del raggio di copertura delle antenne
# 
# dato che ci servirà fare un grafico con scale logaritmiche eliminiamo i dati con
# > range = 0

# In[6]:


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


# creazione di un istogramma log-log per la distribuzione del raggio di copertura

# In[7]:


pyplot.figure(figsize=(20,8)) # dimensioni in pollici
distribuzioneRange = pyplot.hist(raggi.values,                                 bins=max(raggi)-min(raggi),                                 histtype='step',                                 color='#0066ff')
pyplot.title('Distribuzione della copertura')
pyplot.ylabel("Numero di antenne")
pyplot.xlabel("Copertura [m]")
# pyplot.gca().set_xscale("log")
# pyplot.gca().set_yscale("log")
pyplot.xscale("log")
pyplot.yscale("log")

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



