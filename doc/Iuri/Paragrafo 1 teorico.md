## 1   Reti *scale-free*
Le reti sono insiemi di oggetti per i quali è possibile una connessione. Gli ultimi 60 anni hanno visto un crescente interesse per esse, perché con le reti è possibile descrivere sistemi dei più disparati tipi nei campi più vari, dalla biologia all'economia, passando per reti elettriche, informatiche, ecosistemi,  e altro ancora. Ancora più importante, negli ultimi vent'anni è stato scoperto che una classe di reti ha proprietà del tutto comuni nonostante l'intrinseca diversità tra sistemi; la modellizzazione di queste reti, come crescita con caratteristiche preferenziali, è dovuta a Barabasi e Albert (1999), e vengono dette *scale-free*.
Per maggior semplicità, nell'esposizione del lavoro svolto verrà sempre assunto che le reti siano dirette e non pesate.

### 1.1  Proprietà e grandezze caratteristiche
Prima di procedere alla descrizione dei modelli di rete sopracitati, è utile elencare un glossario di caratteristiche delle reti, spesso determinanti per distinguere un grafo scale-free dagli altri nello studio delle reti reali.

* Gli oggetti costitutivi di una rete sono i **nodi**, i quali vengono collegati opportunamente tra loro con dei link secondo dei criteri che dipendono dal modello (nella costruzione di un grafo teorico) o dalla natura del sistema (per le reti reali). Il numero di nodi della rete, o di una sua parte, è ovviamente la grandezza fondamentale per definirne le dimensioni. 
* Il **grado** di un nodo è il numero di altri nodi a cui è connesso. La connettività di una rete è ben rappresentata dalla **distribuzione del grado**, la cui forma funzionale è il primo criterio per discriminare una rete scale-free.
* alla base di ogni topologia c'è il concetto di **distanza**. La distanza tra due nodi di un grafo è il numero di link che li separa nel più piccolo cammino possibile lungo la rete. Altre quantità topologiche importanti sono:
	1. l'**eccentricità di un nodo** e il **diametro**. La prima è la massima delle distanze tra un nodo scelto e tutti gli altri nodi della rete. La seconda è la massima eccentricità tra quelle di tutti i nodi del grafo; detto in termini più generali, il diametro è il minor cammino più grande tra tutte le possibili coppie di nodi della rete.
	2. **average path length**, cioè la distanza media tra tutte le possibili coppie di nodi della rete (correlazione con diametro?)
* Per misurare quanto i nodi di un grafo tendono a creare dei *clusters*, viene definito il **coefficiente di clustering** $C_i$. Dal punto di vista di un vertice $i$ di grado $k_i$, quindi, considerando i nodi a esso collegato, $C_i$ è definito come il rapporto
$$ C_i = \frac{2E_i}{k_i(k_i-1)},$$
dove $E_i$ è il numero di link tra i $k_i$ primi vicini del vertice e $k_i(k_i-1)/2$ il numero di link possibili tra essi: cioè il numero di collegamenti necessari perché $i$ con i suoi vicini sia una porzione di grafo *completa*, detta anche *clique*. La media su tutti i nodi dei rispettivi $C_i$ dà un'indicazione su quanto la rete sia complessivamente clusterizzata. In entrambi i casi, più $C$ è vicino a $1$, più si ha clusterizzazione.  
Il coefficiente di clustering svolge un ruolo importante nel distinguere una rete completamente random da una che presenta caratteristiche di *small-world*: infatti un rete con piccolo diametro tende a avere un $\braket(C)$ maggiore di una simile rete puramente casuale costruita con lo stesso numero di nodi e con il medesimo cammino più corto medio. Questo comportamento è stato notato in molte reti reali. (Watts, Strogatz, 1998 DA METTERE IN BIBLIOGRAFIA)


* Esistono vari modi per definire quando un nodo è centrale rispetto ad altri. Il primo è più immediato è il suo grado. Altri due tra i più importanti sono la **betweenness** e il **page-rank**. Preso un nodo $i$, il primo è definito come il numero di cammini più corti che è possibile tracciare tra due qualsiasi nodi della rete, purché passino per $i$; il secondo dà una maggior centralità a $i$, maggiore è il numero di link *diretti* verso di esso, tenendo conto anche del rank dei nodi che si collegano a esso. In reti dirette, benché non siano *matematicamente* uguali, betweenness e page-rank sono statisticamente molto correlati al grado, pertanto non verranno analizzati. (fare grafico correlazione grado-betweenness-pagerank)

### 1.2 Modelli di rete esponenziale
Reticolo -> randomizzazione, distribuzione del grado di forma gaussiana, grado medio ben definito


#### 1.2.1 Random network
Descrizione modello
Mettere un grafo e un grafico del grado (e eventualmente altre grandezze) esemplificativo

#### 1.2.2 Small World
Effetto small world
Descrizione modello
Mettere un grafo e un grafico grado (e eventualmente altre grandezze) esemplificativo
da Wikipedia
(A graph is considered small-world, if its average local clustering coefficient \bar{C} is significantly higher than a random graph constructed on the same vertex set, and if the graph has approximately the same mean-shortest path length as its corresponding random graph.)
ecco spiegato perché distribuzione grado ha sigma più piccola in watts strogatz che erdos renyi

### 1.3 Reti scale-free
Proprietà frattali, distr grado con powerlaw tra due e tre (tre probabilmente non compreso?). Grado medio idealmente infinito a causa di gran numero di nodi con grado alto?

#### 1.3.1 Preferential attachment
Descrizione modello
Mettere un grafo e un grafico esemplificativo

#### 1.3.2 Random scale-free?

### 1.4  Percolazione
Cosa si intende per percolazione, teoria. Differenza punto di vista di percolazione in formazione di rete e percolazione in distruzione di rete?

#### 1.3.1  Soglia percolativa
Vedere le due pubblicazioni di cohen e erez
