## 1   Reti *scale-free*
Le reti sono insiemi di oggetti per i quali è possibile una connessione. Gli ultimi 60 anni hanno visto un crescente interesse per esse, perché con le reti è possibile descrivere sistemi dei più disparati tipi nei campi più vari, dalla biologia all'economia, passando per reti elettriche, informatiche, ecosistemi,  e altro ancora. Ancora più importante, negli ultimi vent'anni è stato scoperto che una classe di reti ha proprietà del tutto comuni nonostante l'intrinseca diversità tra sistemi; la modellizzazione di queste reti, come crescita con caratteristiche preferenziali, è dovuta a Barabasi e Albert (1999), e vengono dette *scale-free*.
Per maggior semplicità, nell'esposizione del lavoro svolto verrà sempre assunto che le reti siano dirette e non pesate.

### 1.1  Proprietà e grandezze caratteristiche
Dal punto di vista matematico una rete è rappresentata da un grafo. Gli oggetti costitutivi di un grafo sono i **nodi**, i quali vengono collegati opportunamente tra loro con dei **link** secondo dei criteri che dipendono dal modello (nella costruzione di un grafo teorico) o dalla natura del sistema (per le reti reali). l numero di nodi della rete, o di una sua parte, è ovviamente la grandezza fondamentale per definirne le dimensioni; il numero e la distribuzione dei link ne descrivono la connettività.
Prima di procedere alla descrizione dei modelli di rete sopracitati, è utile elencare un glossario di caratteristiche delle reti, spesso determinanti per distinguere un grafo scale-free dagli altri nello studio delle reti reali.

* Il **grado** di un nodo è il numero di altri nodi a cui è connesso. La connettività di una rete è ben rappresentata dalla **distribuzione del grado**, la cui forma funzionale è il primo criterio per discriminare una rete scale-free.
* alla base di ogni topologia c'è il concetto di **distanza**. La distanza tra due nodi di un grafo è il numero di link che li separa nel più piccolo cammino possibile lungo la rete. Altre quantità topologiche importanti sono:
	1. l'**eccentricità di un nodo** e il **diametro**. La prima è la massima delle distanze tra un nodo scelto e tutti gli altri nodi della rete. La seconda è la massima eccentricità tra quelle di tutti i nodi del grafo; detto in termini più generali, il diametro è il minor cammino più grande tra tutte le possibili coppie di nodi della rete.
	2. **average path length**, cioè la distanza media tra tutte le possibili coppie di nodi della rete (correlazione con diametro?)
* Per misurare quanto i nodi di un grafo tendono a creare dei *clusters*, viene definito il **coefficiente di clustering** $C_i$. Dal punto di vista di un vertice $i$ di grado $k_i$, quindi, considerando i nodi a esso collegato, $C_i$ è definito come il rapporto
$$ C_i = \frac{2E_i}{k_i(k_i-1)},$$
dove $E_i$ è il numero di link tra i $k_i$ primi vicini del vertice e $k_i(k_i-1)/2$ il numero di link possibili tra essi: cioè il numero di collegamenti necessari perché $i$ con i suoi vicini sia una porzione di grafo *completa*, detta anche *clique*. La media su tutti i nodi dei rispettivi $C_i$ dà un'indicazione su quanto la rete sia complessivamente clusterizzata. In entrambi i casi, più $C$ è vicino a $1$, più si ha clusterizzazione.  
Il coefficiente di clustering svolge un ruolo importante nel distinguere una rete completamente random da una che presenta caratteristiche di *small-world*: infatti un rete con piccolo diametro tende a avere un $\braket(C)$ maggiore di una simile rete puramente casuale costruita con lo stesso numero di nodi e con il medesimo cammino più corto medio. Questo comportamento è stato notato in molte reti reali. (Watts, Strogatz, 1998 DA METTERE IN BIBLIOGRAFIA) (valutare se mettere l'equivalente definizione con le triplette chiuse/aperte)


* Esistono vari modi per definire quando un nodo è centrale rispetto ad altri. Il primo è più immediato è il suo grado. Altri due tra i più importanti sono la **betweenness** e il **page-rank**. Preso un nodo $i$, il primo è definito come il numero di cammini più corti che è possibile tracciare tra due qualsiasi nodi della rete, purché passino per $i$; il secondo dà una maggior centralità a $i$, maggiore è il numero di link *diretti* verso di esso, tenendo conto anche del rank dei nodi che si collegano a esso. In reti dirette, benché non siano *matematicamente* uguali, betweenness e page-rank sono statisticamente molto correlati al grado, pertanto non verranno analizzati. (fare grafico correlazione grado-betweenness-pagerank)

###1.2 Modelli di rete esponenziale 
Lo studio delle reti random nasce nel 1959 dai (polacchi?) Erdős e Rényi, i quali per primi modellizzarono la definizione di una rete usando criteri probabilistici. Nel corso dei 30 anni successivi è stato osservato che molte reti reali, a dispetto delle dimensioni, avessero un diametro molto piccolo, portando alla definizione del concetto di *small-worlds* e nel 1987 al modello di Watts e Strogatz.
In entrambi i casi si parte da una configurazione iniziale di nodi per poi randomizzare i link tra essi. Per questo motivo la distribuzione del grado segue una Poissoniana, con una coda destra caratteristica di forma esponenziale; con un numero sufficiente di nodi e link, la distribuzione del grado si approssima a una gaussiana con un grado medio ben definito.

#### 1.2.1 Random network
Il modello di Erdős e Rényi parte da un certo numero $N$ di nodi e $n$ di link. Se poniamo che i nodi siano distinguibili, possono esistere (n sopra N(N-1)/2) (TODO DA CONTROLLARE NUM CONF POSS, DISTINGUIBILITÀ) configurazioni equiprobabili tra le quali può esserne presa una in maniera random. Una maniera più articolata per definire una rete random è il criterio binomiale: partire da un set di $N$ nodi e dare a ogni possibile coppia un link con una certa probabilità  $p$. (VALUTARE SE TENERE SOLO QUESTA DEFINIZIONE)
Il punto più importante di un approccio probabilistico alle reti è lo studio di proprietà dei grafi: ponendo $N \rightarrow \infinite$, se la probabilità che una certa proprietà si verifichi tende a 1, si osserva che per reti limitate quella proprietà si verifica con probabilità significativa anche con pochi nodi. Ciò si verifica per molte proprietà, e questo fatto permette di poter trattare le reti per categorie secondo le loro proprietà peculiari.
Nel caso di un grafo di Erdos e Renyi queste sono:

* la distribuzione del grado ha una forma di distribuzione binomiale, la quale tende a una poissoniana per $p$ piccole, e a una gaussiana per $\braket{k}$ grandi.
* il diametro tende a essere piccolo, come l'average path length. Con $p$ non troppo piccolo il numero di nodi che abbiano una certa distanza $l$ si può approssimare a $\braket{k}^l$; uguagliandolo a $N$ deriva che sia diametro che average path length scalano con buona approssimazione con il logaritmo di N (quindi lentamente), secondo la relazione
$l \sim \frac{ln(N)}{ln(\braket{k})}. Molte reti reali presentano simili caratteristiche nei gradi di separazione, che hanno portato alla definizione del concetto di small-world.
* il clustering di una rete ramdom tende a essere molto basso. Infatti, preso un nodo e i suoi primi vicini, la probabilità una coppia di essi sia connessa è $p$. Pertanto su tutto il grafo, il coefficiente di clustering medio è proprio $p$, il quale di solito è abbastanza minore di 1 (con $p = 0.1$ un grafo random diventa già molto connesso). Questo fatto, al contrario del diametro, si pone in contrasto con le reti reali, le quali hanno quasi sempre un $\braket{C}$ sensibilmente più alto.

**Mettere un grafo e un grafico del grado (e eventualmente altre grandezze) esemplificativo**

#### 1.2.2 Small World
Effetto small world
Descrizione modello
Mettere un grafo e un grafico grado (e eventualmente altre grandezze) esemplificativo
nb come le reti random *ma* un clustering sensibilmente più elevato
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
