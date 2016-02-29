##2   Raccolta dei dati e costruzione delle reti
Intro al capitolo in cui si dice da dove è nata l'idea di prendere le antenne da mozilla, l'ipotesi di mesh network, per che cosa sono stati utilizzati quei dati 

###2.1 raccolta e gestione dati
Approfondire e spiegare il più possibile come abbiamo preso i dati, cosa avevamo di ogni antenna, come abbiamo trattato e gestito il database (pandas), dimensione totale del database, scelta di dati aggregati delle rivelazioni per antenna, come lo abbiamo sfoltito (levando colonne inutili e scartando tutti i dati con countrycode diverso da quello ITA), etc etc in sintesi, far venire al prof questa faccia \$_\$  
nb. Qui o nel sottoparagrafo successivo  mostrare possibile problema con i dati dei range (far vedere istogramma dei range), provare a spiegare perché  (non sono dati ufficiali ma raccolti dalla gente, gps staccato, etc)
####2.1.1  Problemi memoria: filtraggio dati
Eventuale sottoparagrafo in cui si parla solo dei problemi di memoria e di come abbiamo selezionato la roba dal db totale, se necessario.

###2.2 Adiacenza e grado
Dire criterio di linking, definizione distanza, problemi computazionali con funzione distanza geodesica per rete grossa, ripiegare su distanza euclidea, calcolo matrici di adiacenza

####2.2.1  Problemi potenza di calcolo
Eventuale sottoparagrafo in cui si parla solo dei problemi di potenza di calcolo e di come abbiamo abbandonato funzioni più complesse, se necessario

####2.3 Gradi e fitgradi
Networkx -> Grafo -> Distr grado. Cioè spiegare che strumenti abbiamo usato per avere il grafo (networkx), far vedere gli istogrammi più belli possibile delle distr grado, poi far vedere i fit su ogni rete, valutare se separatamente o no
Conclusioni su quale possa essere il tipo di rete in analisi (esponenziale, powerlaw nella coda destra ma esponente troppo alto, no scalefreeness, tuttavia grado medio alto quindi robusto)
Valutare se dare un primo valore del diametro, e di qualche altra grandezza topologica importante.