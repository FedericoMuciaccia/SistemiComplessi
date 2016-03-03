
## Selezione dei dati

TODO scrivere cosa sono Mozilla Location Server ed OpenCellID

Una volta scaricati i dati aggregati dalla pagina web [https://location.services.mozilla.com/downloads](https://location.services.mozilla.com/downloads) si sono cominciate le operazioni di selezione dei dati.

Il data sample riguarda tutti i continenti e risulta molto grosso (un file csv di circa 650 MB), per cui è necessario ridurlo il più possibile per poterlo maneggiare col nostro limitato quantitativo di RAM.

Una prima grossolana ma efficiente scrematura riguarda i dati caratterizzati da un mobile county code non italiano, si è pertanto imposta la condizione
```
mcc == 222
```

Successivamente vengono scartati i dati ritenuti inaffidabili, ovvero con soltanto una rivelazione da parte degli utenti
```
samples > 1
```

Adesso che il datasample si è ridotto molto possiamo effettuare delle operazioni computazionalmente un po' più pesanti: vogliamo eliminare tutte le rilevazioni al di fuori del Grande Raccordo Anulare, che per semplicità è stato schematizzato come una circonferenza di raggio 10 km con centro esattamente nol Colosseo.

Per far questo serve definire una nozione di distanza. Dato che i nostri sono dati geolocalizzati sarebbe naturale introdurre una distanza geodesica. A tal fine abbiamo usato la libreria `geopy`, che contiene due definizioni differenti:

* Grat circe distance: la distanza geodesica su una sfera. Per due punti non agli antipodi passa sempre una circonferenza di raggio massimo lungo cui scorre la geodesica, ovvero il cammino di minima distanza.
* Vincenty distance: la distanza geodesica su un ellissoide oblato. Tale distanza tiene in conto che la Terra non è una sfera perfetta ma è invece leggermente schiacciata ai poli. Delle due è quella più accurata, ma anche quella più difficile da calcolare numericamente.

L'ulteriore condizione da soddisfare per i dati risulta dunque
```
geodesicDistance(place) <= raggioRaccordoAnulare
```

Si sono fatte differenti prove sia con `vincenty` (più lenta) che con `great_circle` (leggermente più veloce), ma i tempi di calcolo risultavano comunque spropositati. Pertanto abbiamo fatto una approssimazione: dato che la città di Roma sottende un angolo solido minuscolo rispetto alla totalità del pianeta, abbiamo ritenuto accettabile usare una distanza euclidea, ovviamente trasformando in metri le coordinate angolari di latitudine e longitudine con i relativi fattori di scala, dettati dal raggio terrestre.

La distanza euclidea coinvolge solo quadrati è radici quadrate, per cui è molto più veloce delle altre due concorrenti. Il prezzo da pagare è una leggerissima imprecisione, del tutto trascurabile alle nostre scale.

La funzione utilizzata è pertanto
```
def euclideanDistace(x,y):
    return numpy.sqrt(numpy.square(x) + numpy.square(y))
```
da notare il fatto che per il calcolo algebrico è stata utilizzata la libreria `numpy` invece che la libreria `math` builtin in Python, poiché è più veloce (è scritta in C) e supporta le operazioni direttamente su vettori di coordinate.

I dati sono stati importati in un dataframe tabulare usando la libreria `pandas`. Questo che ci ha permesso di effettuare facilmente tutte le query necessarie per il filtraggio dei dati.

A questo punto abbiamo finalmente il nostro datasample della città di Roma: circa 7000 antenne in un file csv agevolmente maneggiabile di circa 1MB.

TODO inserire scatterplot preliminare dei dati di Roma (notebook Fede)

Per visualizzare agevolmente i nostri dati serve una mappa georeferenziata, preferibilmente interattiva. A tal fine abbiamo usato la libreria `gmaps`, che dà semplice accesso alle mappe di Google Maps dando la possibilità di creare una heatmap.
```
roma = pandas.read_csv("../data/Roma_towers.csv")
coordinate = roma[['lat', 'lon']].values
heatmap = gmaps.heatmap(coordinate)
gmaps.display(heatmap)
```
(per scrivere queste poche linee di codice c'è voluto un'intero pomeriggio!)

TODO mettere heatmap interattiva in HTML

Dalla mappa si capisce bene quanto sia fitta le rete di antenne Romana.

TODO creare il notebook ordinato "data selection"



