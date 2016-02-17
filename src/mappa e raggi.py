
# coding: utf-8

# In[303]:

import numpy
import pandas
from matplotlib import pyplot
get_ipython().magic(u'matplotlib inline')

import gmaps


# ## Creazione della mappa
# 
# invece che uno scatterplot con dei raggi, la libreria ci consente solo di fare una heatmap (eventualmente pesata)
# 

# In[304]:

roma = pandas.read_csv("../data/roma_towers.csv")
coordinate = roma[['lat', 'lon']].values


# In[305]:

gmaps.heatmap(coordinate)

# TODO scrivere che dietro queste due semplici linee ci sta un pomeriggio intero di smadonnamenti


# ## Analisi del raggio di copertura delle antenne
# 
# dato che ci servirà fare un grafico con scale logaritmiche eliminiamo i dati con
# > range = 0

# In[306]:


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

# In[307]:


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


# In[308]:

# TODO vedere se il grafo finale non è scale free, 
# non è reticolo geometrico.
# è una specie di vetro


# In[309]:

# Tre = roma.net == 99
# treCell = roma[Tre].reset_index(drop=True)
# treCell

# TODO snellire il dataframe iniziale levando le colonne inutili

dataframe = pandas.read_csv("../data/cell_towers_diff-2016012100.csv")
troncato = dataframe[50:70]
ordinato = troncato.reset_index(drop=True)
ordinato


# In[310]:


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
 


# In[311]:

tim = romaFiltrato[isTim].reset_index(drop=True)
wind = romaFiltrato[isWind].reset_index(drop=True)
vodafone = romaFiltrato[isVodafone].reset_index(drop=True)
tre = romaFiltrato[isTre].reset_index(drop=True)


# In[312]:

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

# In[415]:

pyplot.figure(figsize=(20,8))
distribuzioneRange = pyplot.hist(raggi.values,                                 bins=div,                                 histtype='step')
pyplot.title('PROVA, CON CANALI NON ANCORA PESATI')
pyplot.xscale("log")
pyplot.yscale("log")


# In[385]:

a,b,c = distribuzioneRange


# In[402]:

a1 = numpy.append(a.astype(int), 0)


# In[403]:

b1 = b.astype(int)


# In[404]:

a1


# In[405]:

b1


# In[406]:

div = numpy.logspace(start=0, stop=15, num=16, base=2).astype(int) # max = 20341
div


# In[411]:

a2 = a1/div
a2


# In[414]:

pyplot.scatter(y=a2,x=div)
pyplot.xscale("log")
pyplot.yscale("log")


# In[ ]:

# TODO vedere se le due slope del grafico log-log possono essere
# messe in relazione con le due slode della legge
# di Heap e di Zipf (o come cavolo si scrivono)

