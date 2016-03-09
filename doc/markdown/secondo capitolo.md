


<meta charset='utf-8'>
<!-- <link rel="stylesheet" type="text/css" href="../html/relazione.css"> -->
<link rel="stylesheet" type="text/css" href="../html/dataframe.css">


## 2.1 Dati di Mozilla

TODO vedere file markdown

TODO fare una specie di bottone

[Esempio del dataframe MLS](../html/dataframe_example_Mozilla.html)


## 2.2 Selezione dei dati

Una volta scaricati i dati aggregati dalla pagina web [https://location.services.mozilla.com/downloads](https://location.services.mozilla.com/downloads) si sono cominciate le operazioni di selezione dei dati.

Il data sample riguarda tutti i continenti e risulta molto grosso (un file csv di circa 650 MB), per cui è necessario ridurlo il più possibile per poterlo maneggiare col nostro limitato quantitativo di RAM.

Una prima grossolana ma efficiente scrematura riguarda i dati caratterizzati da un mobile county code non italiano, si è pertanto imposta la condizione
<pre><code>
mcc == 222
</code></pre>

Successivamente vengono scartati i dati ritenuti inaffidabili, ovvero con soltanto una rivelazione da parte degli utenti
<pre><code>
samples > 1
</code></pre>

Adesso che il datasample si è ridotto molto possiamo effettuare delle operazioni computazionalmente un po' più pesanti: vogliamo eliminare tutte le rilevazioni al di fuori del Grande Raccordo Anulare, che per semplicità è stato schematizzato come una circonferenza di raggio 10 km con centro esattamente nol Colosseo.

Per far questo serve definire una nozione di distanza. Dato che i nostri sono dati geolocalizzati sarebbe naturale introdurre una distanza geodesica. A tal fine abbiamo usato la libreria `geopy`, che contiene due definizioni differenti:

* Grat circe distance: la distanza geodesica su una sfera. Per due punti non agli antipodi passa sempre una circonferenza di raggio massimo lungo cui scorre la geodesica, ovvero il cammino di minima distanza.
* Vincenty distance: la distanza geodesica su un ellissoide oblato. Tale distanza tiene in conto che la Terra non è una sfera perfetta ma è invece leggermente schiacciata ai poli. Delle due è quella più accurata, ma anche quella più difficile da calcolare numericamente.

L'ulteriore condizione da soddisfare per i dati risulta dunque
<pre><code>
geodesicDistance(place) <= raggioRaccordoAnulare
</code></pre>

Si sono fatte differenti prove sia con `vincenty` (più lenta) che con `great_circle` (leggermente più veloce), ma i tempi di calcolo risultavano comunque spropositati. Pertanto abbiamo fatto una approssimazione: dato che la città di Roma sottende un angolo solido minuscolo rispetto alla totalità del pianeta, abbiamo ritenuto accettabile usare una distanza euclidea, ovviamente trasformando in metri le coordinate angolari di latitudine e longitudine con i relativi fattori di scala, dettati dal raggio terrestre.

La distanza euclidea coinvolge solo quadrati è radici quadrate, risultando nel complesso circa dieci volte più veloce delle altre due concorrenti. Il prezzo da pagare è una leggerissima imprecisione, del tutto trascurabile alle nostre scale.

La funzione utilizzata è pertanto
<pre><code>
def euclideanDistace(x,y):
    return numpy.sqrt(numpy.square(x) + numpy.square(y))
</code></pre>
da notare il fatto che per il calcolo algebrico è stata utilizzata la libreria `numpy` invece che la libreria `math` builtin in Python, poiché è più veloce (è scritta in C) e supporta le operazioni direttamente su vettori di coordinate.

I dati sono stati importati in un dataframe tabulare usando la libreria `pandas`. Questo che ci ha permesso di effettuare facilmente tutte le query necessarie per il filtraggio dei dati.

TODO fare una specie di bottone

[Esempio del dataframe da noi utilizzato](../html/dataframe_example_Roma.html)

A questo punto abbiamo finalmente il nostro datasample della città di Roma: circa 7000 antenne in un file csv agevolmente maneggiabile di circa 1MB.

<img src="../img/map/Roma_non_georeferenziata.svg"/>

Per visualizzare agevolmente i nostri dati serve una mappa georeferenziata, preferibilmente interattiva. A tal fine per il notebook di IPython abbiamo usato la libreria `gmaps`, che dà semplice accesso inline alle mappe di Google Maps dando la possibilità di creare una heatmap, mentre per l'HTML di questa presentazione abbiamo usato le analoghe funzioni della libreria `gmplot`.
<pre><code>
roma = pandas.read_csv("../data/Roma_towers.csv")
coordinate = roma[['lat', 'lon']].values
heatmap = gmaps.heatmap(coordinate)
gmaps.display(heatmap)
</code></pre>
<pre><code>
colosseo = (41.890183, 12.492369)
mappa = gmplot.GoogleMapPlotter(41.890183, 12.492369, 12)
mappa.heatmap(roma.lat.values,roma.lon.values)
mappa.draw("../doc/mappa.html")
</code></pre>
(per scrivere queste poche linee di codice c'è voluto un'intero pomeriggio!)

TODO fare una specie di bottone

[Heatmap delle antenne telefoniche di Roma](../html/heatmap.html)

Dalla mappa si capisce bene quanto sia fitta le rete di antenne Romana.

TODO creare il notebook ordinato "data selection"


## 2.3 Analisi del raggio di copertura delle antenne

Dato che ci servirà fare grafici con scale logaritmiche eliminiamo i dati di antenne che presentano un raggio nullo
<pre><code>
range =! 0
</code></pre>

Il raggio minimo risulta essere 1m, mentre quello massimo 20341m. Dato che il raggio del Grande Raccordo Anulare è circa 10km questo significa che ci saranno antenne con un grado di connessione totale.
TODO forse spostare questa considerazione a quando si è spiegato il criterio di linking.
TODO spiegare la possibile casa di questi valori di raggi così bassi

Facciamo un istogramma log-log per la distribusione del raggio di copertura, sia con la canalizzazione lineare sugli interi, sia con una canalizzazione logaritmica in base 2, per ridurre il rumore sulla coda.
<img src="../img/range/infinite_log_binning.svg"/>
La canalizzazione logaritmica pesata permette di osservare l'andamento ben sotto il singolo conteggio, ampliando di una decade l'intervallo di osservazione.

In figura si può vedere come l'andamento sia abbastanza power-law su diverse decadi, soprattutto fino a `conteggio = 1`. Per verificare ulteriormente questo fatto abbiamo generato anche la curva del frequency-rank, che risulta seguire senza esitazioni il trend delineato dagli istogrammi.
TODO  cercare di spiegare questa power-law.
Il frequency-rank si ottiene ordinando in maniera decrescente il numero di conteggi per ogni canale unitario e associando un relativo ranking intero decrescente ai raggi corrispondenti.
<img src="../img/range/range_distribution.svg"/>

Si è infine analizzata la distribuzione cumulata, lasciata nel grafico seguente non normalizzata.
La distribuzione cumulata $C(x)$ rappresenta la probabilità che la variabile random assuma un valore minore o uguale a $x$.
<img src="../img/range/range_cumulated_distribution.svg"/>
TODO capire l'andamento della cumulata

TODO mettere caption nell'html delle figure

TODO Facendo un fit TODO abbiamo ottenuto il seguerte esponente per l'andamento a potenza: TODO
TODO mettere retta con pendenza con fit a mano spannometrico


## 2.4 matrice di adiacenza e creazione del grafo

calcolare tutta la matrice di adiacenza con la distanza geodesica al posto di quella euclidea risulta pesantissimo ($N^2$ elementi)


spiegare il criterio di linking


## 2.5 distribuzione del grado





