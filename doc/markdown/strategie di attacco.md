
## Strategie di attacco

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


