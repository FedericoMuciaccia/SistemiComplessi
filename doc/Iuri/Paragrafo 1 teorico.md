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
* Per misurare quanto i nodi di un grafo tendono a creare dei *clusters*, viene definito il **coefficiente di clustering**. 
* centralità e vari tipi di centralità: betweenness dire che in reti dirette strettamente correlato a distr grado, pagerank, altro?

### 1.2 Modelli di rete esponenziale
Reticolo -> randomizzazione, distribuzione del grado di forma gaussiana, grado medio ben definito

#### 1.2.1 Random network
Descrizione modello
Mettere un grafo e un grafico del grado (e eventualmente altre grandezze) esemplificativo

#### 1.2.2 Small World
Effetto small world
Descrizione modello
Mettere un grafo e un grafico grado (e eventualmente altre grandezze) esemplificativo

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
