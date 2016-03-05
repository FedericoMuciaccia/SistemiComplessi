
# coding: utf-8

# In[1]:

import numpy, pandas
from matplotlib import pyplot


# In[ ]:

# TODO vedere se il grafo finale non è scale free, 
# non è reticolo geometrico.
# è una specie di vetro


# In[2]:

# Tre = roma.net == 99
# treCell = roma[Tre].reset_index(drop=True)
# treCell

# TODO snellire il dataframe iniziale levando le colonne inutili

dataframe = pandas.read_csv("../data/cell_towers_diff-2016012100.csv")
troncato = dataframe[50:70]
ordinato = troncato.reset_index(drop=True)
ordinato


# In[ ]:


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
 


# In[ ]:

tim = romaFiltrato[isTim].reset_index(drop=True)
wind = romaFiltrato[isWind].reset_index(drop=True)
vodafone = romaFiltrato[isVodafone].reset_index(drop=True)
tre = romaFiltrato[isTre].reset_index(drop=True)


# In[ ]:

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

# In[ ]:

pyplot.figure(figsize=(20,8))
distribuzioneRange = pyplot.hist(raggi.values,                                 bins=div,                                 histtype='step')
pyplot.title('PROVA, CON CANALI NON ANCORA PESATI')
pyplot.xscale("log")
pyplot.yscale("log")


# In[ ]:

a,b,c = distribuzioneRange
a1 = numpy.append(a.astype(int), 0)
b1 = b.astype(int)
a1
b1
div = numpy.logspace(start=0, stop=15, num=16, base=2).astype(int) # max = 20341
div
a2 = a1/div
a2


# In[ ]:

pyplot.scatter(y=a2,x=div)
pyplot.xscale("log")
pyplot.yscale("log")


# In[ ]:

# TODO vedere se le due slope del grafico log-log possono essere
# messe in relazione con le due slode della legge
# di Heap e di Zipf (o come cavolo si scrivono)


# In[ ]:

# TODO esterno:

# datigenerati = numpy.random.normal(0,1, 10000)
# b = pylab.hist(datigenerati,bins=100, histtype='step')
# plottare la gaussiana di origine, 
# fare i residui e vedere che il loro istogramma 
# è di nuovo gaussiano e farne un fit e vedere 
# se il residui dei residui sono gaussiani, 
# che al mercato mio padre comprò


# In[ ]:

# TODO
# fit e lot della distribuzione del grado con i due modelli di rete
# Erdos Renyi
# preferential attachement di Barabasi Albert


# ## distribuzione del grado
# 
# si fa un plot logaritmico unificato e poi i relativi fit con i vari modelli di rete

# In[ ]:


gradi = [numpy.loadtxt("../data/DistrGrado_{0}".format(compagnia)) for compagnia in compagnie]

# dataframeGradi = pandas.DataFrame(numpy.transpose(gradi))

# grado = grafo.degree().values
# grado = numpy.loadtxt("../data/DistrGrado_{0}",compagnia)


# In[ ]:

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

# In[ ]:

dictGradi = dict()
for label in compagnie:
    dictGradi[label] = numpy.loadtxt("../data/DistrGrado_{0}".format(label)).astype(int)

dictGradi


# In[ ]:


# TODO vedere se c'è un metodo migliore rispetto a transpose()
dataframeGradi = pandas.DataFrame.from_dict(dictGradi, orient='index').transpose()
# TODO attenzione ai valori NaN nei posti vuoti


# In[ ]:

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

# TODO funzione numpy.diff per la correlazione connessa
numpy.diff([0,4,6,2,8,9,7,0,1])


# In[ ]:




# In[ ]:




# In[ ]:



