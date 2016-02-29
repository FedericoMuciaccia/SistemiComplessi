# 3 Network breakdown
###### (formerly "Analisi percolativa" ma questo è un titolo noioso, meglio una roba più deep impact ogliea) 

Una volta osservate le distribuzioni del grado nelle reti delle quattro compagnie e nella rete complessiva formata da tutte le antenne comprese nell'area metropolitana di Roma, procediamo con lo studio percolativo. In riferimento al lavoro fatto da Albert, Jeong e Barabasi nel 1999, la scelta è stata di simulare due differenti scenari in cui i nodi della rete vengono disabilitati. Nel primo scenario si è ipotizzato un attacco intenzionale che cominciasse dai nodi con maggior grado, nel secondo una rimozione random. 
Lo scopo è studiare l'andamento, in funzione della percentuale di nodi rimossi, del diametro $D$ della rete e della dimensione del cluster più grande (*Giant Cluster*) rapportata al numero totale di nodi sopravvissuti. A seconda di come la rete si comporterà, sarà possibile dedurne la robustezza nei due scenari, in modo tale da poter confrontare meglio tale comportamento con quello di una rete scale-free, o di una di tipo random.
Per poter fare questo confronto sono state generate, usando le funzioni di *networkx*, delle reti con i modelli di rete scale free (*preferential attachment*, Barabasi, Albert 1999) e di rete esponenziale (*random network*, Erdős, Renyi 1959 e *small world*, Watts, Strogatz, 1998) e su tutti e tre i modelli abbiamo simulato i due scenari di caduta progressiva della rete. In tutti e cinque i campioni di rete che abbiamo analizzato è stato conteggiata la variazione di $D$ e $GC$ e i grafici ottenuti sono stati messi a confronto a quelli ottenuti con le reti generate secondo i modelli.  
**DA DECIDERE SE TAGLIARE O SINTETIZZARE** La rete reale ha ovviamente delle contromisure per evitare la caduta delle comunicazioni. Le antenne trasmettono segnali tra loro su due bande di frequenza: una *user-side*, dedicata alle normali trasmissioni tra utenti del servizio, e una dedicata a un complesso sistema di feedback gestito da degli hub (grosse antenne con raggio sui 20 km). Questa struttura gerarchica permette, nel caso di caduta di una antenna o di un improvviso eccessivo carico in una zona circoscritta, che gli hub gestiscano potenza e capacità delle antenne circostanti mentre vengono inviati tecnici per un intervento sul luogo. 
Questo sistema ha ovviamente un certo tempo di reazione. L'analisi da noi svolta pertanto suppone che la caduta della rete avvenga in un tempo inferiore, in una sorta di approssimazione adiabatica. Inoltre, la sola caduta degli hub sarebbe già sufficiente a compromettere seriamente l'integrità della rete (le antenne avrebbero difficoltà a coordinare le comunicazioni tra loro), ma nella nostra ipotesi di mesh-network distribuita ci interessano soltanto le comunicazioni nelle frequenze user-side. Usando questo modello semplificato siamo riusciti a ottenere alcune informazioni su una ipotetica rete wireless di questa natura.


## 3.1 Attacco intenzionale
** TODO NB quando dico "ci si aspetta" forse va fatto riferimento a condizione di percolazione teorica **
Nello scenario di attacco intenzionale ci si aspetta una veloce frammentazione della rete. I cluster diverranno rapidamente più piccoli fino a frammentarsi del tutto entro pochi punti percentuali di nodi rimossi. Nel caso di una rete fortemente connessa come quella in esame ci si aspetta una resistenza maggiore, ma comunque una soglia percolativa bassa (approssimativamente entro il 50%). Se la rete è di tipo scale-free dovrebbe essere più fragile ad attacchi di questo tipo: mentre in una rete random i nodi più connessi sono solo una coda della distribuzione del grado, una rete a power-law ha in proporzione molti più nodi molto connessi.
Dal punto di vista del diametro della rete, levando i nodi più connessi ci si aspetta che esso aumenti, fino a quando la rete diventa tanto frammentata da essere costituita da clusters con pochissimi nodi. Oltrepassata la soglia di frammentazione quindi il diametro dei clusters più grandi decrescerà rapidamente a zero.

### 3.1.1 Risultati
**inserisci grafici con caption**

### 3.1.2 Confronto con i modelli
**inserisci grafici con caption**  
NB fare calcolo con rete scale free e random con gradi medi attorno a valori delle nostre reti
Vedede eventuali discrepanze con quanto atteso

## 3.2 Caduta random

### 3.2.1 Risultati
**inserisci grafici con caption**  

### 3.2.2 Confronto con i modelli
**inserisci grafici con caption**  
**mettere anche grafico della distr del grado dei modelli quando si fa il discorso del modello che non va**  
Qui va fatto un lungo discorso dato che non appatta nulla. Far vedere che con modello scale free di bar e alb con pendenza 3 in realtà non hai alcuna scalefreeness dato che cade tutto in praticamente una sola decade. Far vedere che comportamento è UGUALE ai modelli esponenziali, e che dipende SOLO dal grado medio, e che quindi l'articolo del 2000 è truffaldino. Testare reti modello più grandi, fino a 10000 per non far fondere il pc e solo andamento gc
Vedere che succede con preferential attachment generalizzato con esponenti 1,5/2/2,5 a vari valori di gradomedio.

### 3.2.3 Effetto cascata
