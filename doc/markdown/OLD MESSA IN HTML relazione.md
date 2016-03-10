


<meta charset='utf-8'>
<!-- <link rel="stylesheet" type="text/css" href="../html/relazione.css"> -->
<link rel="stylesheet" type="text/css" href="../html/dataframe.css">

## Cosa vogliamo fare
















## 2 GeoData: where and why

### Google Location Service

#### GPS and battery drain

La geolocalizzazione dei dispositivi, soprattutto quelli mobile, sta rapidamente diventando parte intergrante del nostro modo quotidiano di fruire la tecnologia.
Si usa nel navigatore stradale, per impostare automaticamente il luogo di cui desideriamo le previsioni del tempo o da cui vogliamo prendere un treno o un aereo, per aggiungere informazioni contestuali alle fotografie che scattiamo e tanto altro ancora.

Il modo storicamente utilizzato per effettuare la geolocalizzazione è per via satellitare, tramite il GPS. Ma il GPS ha due tipi di problemi:

* è dannatamente lento ad agganciare un numero congruo di satelliti, tali da poter registrare una posizione accurata,
* consuma un sacco di energia.
Soprattutto il secondo punto è in palese conflitto con l'esigenza dei moderni dispositivi portabili di avere una ampia autonomia energerica.

Per porre rimedio a questo fatto, Google ha via via comiciato ad utilizzare altri tipi alternativi di geolocalizzazione, per comporre un sistema ibrido.

1. Un primo grado di grossolana geolocalizzazione avviene tramite le celle della rete telefonica, a cui tutti gli smartphone sono connessi. La precisione è dell'ordine delle centinaia di metri.
2. Un secondo grado, molto più accurato, viene realizzato tramite le reti wifi visibili in quell'istante dal dispositivo. La precisione è dell'ordine di qualche decina di metri.
3. Infine, solo se il compito richiesto richiede una precisione ulteriore, si accende il GPS, per un risultato con la precisione inferiore al metro. Il cominciare da una stima della posizione più che accettabile riduce di molto la durata delle operazioni a GPS acceso, consentendo un drastico risparmio della batteria.

#### Geolocalization via WiFi

La diffusione del Wifi è ormai capillare, soprattutto in contesto cittadino. Virtualmente c'è un router WiFi in ogni appartamento.
Mentre camminiamo per la città col WiFi dello smartphone acceso, captiamo in ogni punto decine di segnali.
Se è nota la posizione di questi router e la potenza del segnale da loro emesso è possibile triangolare la nostra posizione con una notevole precisione, dovuta sia al fatto che un segnale WiFi ha un raggio tipico di una trentina di metri, sia dovuto all'ingente numero di segnali coi quali si sta triangolando, tipicamente più di una decina.

Quindi per sapere la mia posizione devo avere accesso a una mappa delle posizioni di tutti i router.
E come si costruisce questa mappa? Esattamente al contrario: camminando per la città con GPS acceso, avendo dunque un'alta precisione sulla posizione del dispositivo, e triangolando la posizione di tutti i router visibili combinando tutte le rilevazioni del tracciato.

Dunque Google ha mappato tutti i WiFi di tutto il globo per dare la possibilità agli utenti dei suoi servizi come Google Maps (e delle applicazioni che si appoggiano alle sue API) di ottenere la propria localizzazione con una buona precisione è un consumo di batteria risibile.
La precisione è arrivata ad essere dell'ordine dei 5 metri e i tempi di accesso pressoché istantanei: di fatto rendendo inutile accendere il GPS nella maggior parte dei casi.

Questo tipo di localizzazione ha inoltre un altro grande vantaggio: funziona anche sottoterra e dentro gli edifici, luoghi normalmente inaccessibili al segnale GPS, di natura satellitare.

Ovviamente la mappa dei router WiFi è in continua evoluzione, per cui il modo più conveniente per redigerla è sfruttando il crowdsourcing: ai milioni di utenti ignari giornalmente in moto per la città viene acceso il GPS un paio di volte al giorno per pochi secondi, in un momento di inutilizzo del dispositivo, e in questo modo si crea velocemente una mappa complessiva e quotidianamente aggiornata, a beneficio di tutti.

Tutto questo è tremendamente intelligente ed efficiente.
C'è un solo grande problema: i dati sono chiusi.

### Mozilla Location Service

Mozilla è da sempre impegnata per lo svilutto di tecnologie web aperte e standardizzate. Avendo riconosciuta la centralità della geolocalizzazione e la crescita esponenziale di siti ed applicazioni location-aware, ha deciso di ricalcare le orme di Google e fondare il suo servizio di geolocalizzazione usando WiFi ed antenne cellulari: [Mozilla Location Service](https://location.services.mozilla.com/).

<iframe src="../html/MLS_header.html"></iframe>

La mappatura viene fatta dagli utenti su base puramente volontaria, utilizzando l'apposita applicazione [Mozilla Stumbler](https://play.google.com/store/apps/details?id=org.mozilla.mozstumbler)

![Mozilla Stumbler](https://location.services.mozilla.com/static/images/mozstumbler.png)

Il progetto è ormai maturo e, come si può osservare dalla seguente mappa, la copertura del mondo è molto capillare.

TODO mettere bottone

<!-- [Mozilla Location Service wolrd coverage](../html/MLS_map.html) -->
Mozilla Location Service wolrd coverage
<iframe src="../html/MLS_map.html"></iframe>

Mozilla Location Service funziona sia con le antenne cellulari che con i WiFi, soltanto che attulamente i dati della mappa WiFi (mostrati approssimati nella mappa precedente) non possono essere resi pubblici per questioni relative alle norme sulla privacy vigenti sia negli Stati Uniti sia in altre nazioni.

Pertanto gli unici dati attualmente liberamente disponibili sono quelli sulle antenne radio delle varie generazioni: 2G (GSM), 3G (UMTS), 4G (LTE).  
I dati forniti da Mozilla sono un'estensione di quelli già disponibili sulla piattaforma [OpenCellID](http://opencellid.org/), anche loro open.

Questi sono dunque i dati che abbiamo analizzato in questa nostra tesina.
































## 2.2 Data selection

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

<!-- [Esempio del dataframe da noi utilizzato](../html/dataframe_example_Roma.html) -->
Esempio del dataframe da noi utilizzato
<iframe src="../html/dataframe_example_Roma.html"></iframe>

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

<!-- [Heatmap delle antenne telefoniche di Roma](../html/heatmap.html) -->
Heatmap delle antenne telefoniche di Roma
<iframe src="../html/heatmap.html"></iframe>

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












## 2.4 Matrice di adiacenza e creazione del grafo

calcolare tutta la matrice di adiacenza con la distanza geodesica al posto di quella euclidea risulta pesantissimo ($N^2$ elementi)


spiegare il criterio di linking


## 2.5 Distribuzione del grado











## 3.3 Ottimizzazione del codice




## 3.4 Strategie di attacco

L'esigenza di provare a parallelizzare il codice ci ha portato a due versioni differenti della funzione di attacco intenzionale: una sequenziale e una parallela. Entrambe le varianti rimuovono circa l'1% dei nodi per volta.
* la funzione sequenziale elimina l'insieme dell'1% dei nodi più importanti, analizza la rete e calcola il prossimo insieme di 1% di nodi da rimuove.
* la funzione parallela ha invece un comportamento più adiabatico: guarda il grafo iniziale e fa una classifica assoluta dei nodi per importanza, rimuovendone di volta in volta l'1% in maniera ordinata.

Possiamo supporre che un reale attacco alla rete sia portato avanti con modalità adiabatiche: un ipotetico terrorista piazza nella notte delle cariche esplosive sotto le antenne che ritiene fondamentali e poi le fa scoppiare durante il giorno tutte in una volta.
A titolo di esempio, possiamo immaginare che l'attacco si consideri riuscito quando metà dell'area metropolitana rimane isolata senza possibilità di comunicare. Questo è il parametro finale in base al quale viene scelta la sequenza di antenne da far esplodere.

Ma chi garantisce che questa sequenza coincide con gli N nodi di grado maggior all'istante iniziale?
In altre parole: è questa una strategia *ottimale*?  
La risposta è no!
la strategia ottimale è quella che, a parità di risultato, coinvolge il minor numero di antenne fatte eplodere, anche per minimizzare il rischio di essere scoperto nella notte mentre piazza l'esplosivo in giro per la città.

Tale strategia può essere evidenziata solo da una simulazione **sequenziale**, fatta facendo evolvere la rete passo per passo, secondo una strategia di *steepest descent*. Questo garantisce di trovare la strategia ottimale, soprattutto se vengono inclusi anche gli effetti a cascata dovuti all'overload e alla saturazione di banda. Dal grafico sottostante si evince comunque che non c'è molta differenza tra procedere con un campionamento all'1% o eseguire una simulazione di attacco nodo per nodo, per cui ad ogni modo il costo computazionale complessivo non risulta eccessivo.

TODO inserire grafico di confronto per "Roma totale" tra parallelo 1%, sequenziale 1% e sequenziale step-by-step

TODO in futuro inserire nel plot anche gli affetti a cascata, per far vedere che la curva crolla prima

Nel caso di random failure (escludendo gli effetti di saturazione a cascata) non c'è invece alcuna differenza tra l'approccio sequenziale e quello **parallelo**, rendendo il secondo algorimo preferibile nel caso si voglia sfruttare tutta la potenza delle moderne cpu multicore.

Riassumendo:
* Nel caso di intentional attack è doveroso usare un approccio sequenziale.
* Nel caso di random failure è consigliabile utilizzare un approccio parallelo.











