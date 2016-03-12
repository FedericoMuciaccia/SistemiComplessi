
# coding: utf-8

# # Relazione Sistemi Complessi

# <center>**Sommario**</center>
# Lo scopo di questo lavoro è fare un'analisi di rete usando un campione di antenne telefoniche cellulari, ipotizzando di voler costruire una ipotetica *mesh network* con esse. Abbiamo scelto di analizzare il sistema delle antenne comprese entro il Raccordo Anulare di Roma. Non sapendo a priori di quale tipo di rete si tratta, e che tipo di grafo si costruisce da essa, sono state studiate alcune proprietà topologiche e comportamentali dell'insieme di antenne studiate.
# Dopo aver definito il criterio con cui dare un link a due nodi, sono state calcolate le matrici di adiacenza della rete complessiva e di quelle composte solo dalle antenne dei singoli gestori presenti in Italia. La prima parte dell'analisi consiste nell'estrapolare dai grafi ottenuti le distribuzioni dei gradi e nell'affidare all'istogramma dei gradi la forma funzionale che meglio gli si adatti. Avendo così ottenuto indicazioni significative sui tipi di rete in analisi, le abbiamo verficate studiando il comportamento percolativo della rete, mediante rimozione di nodi in due diversi scenari: un attacco intenzionale, che rimuovesse le antenne a partire da quelle con maggior grado, e una caduta random del sistema. I risultati ottenuti sono stati confrontati con modelli di rete esponenziali e scale-free.
# L'esposizione è articolata nel seguente modo:  
# 
# **Nel paragrafo 1** verranno esposte le basi teoriche dello studio effettuato, con particolare accento ai modelli di rete utilizzati come riferimento e ai concetti di percolazione e soglia percolativa.  
# 
# **Nel paragrafo 2** si spiega come sono stati raccolti e organizzati i dati, come è stata definita la rete e quindi con quali criteri è stata definita la matrice di adiacenza. Successivamente, accennando ai problemi computazionali avuti nel gestire la rete complessiva da circa 7000 nodi, verranno calcolate le matrici di adiacenza e le distribuzioni del grado.  
# 
# **Nel paragrafo 3** viene effettuato lo studio percolativo mediante i due scenari di rimozione di nodi,  analizzando l'andamento del diametro e delle dimensioni del cluster più grande con la progressiva caduta delle antenne. I risultati sono stati confrontati con quelli ottenuti dai modelli, i quali hanno rivelato delle ambiguità. Nel caso di attacco random è stato testato infine un ipotetico effetto cascata causato dall'overload delle antenne rimaste (previa rimozione dei grossi hub che servono proprio a scongiurare tale evenienza).
# 

# ## 1   Reti *scale-free*
# Le reti sono insiemi di oggetti per i quali è possibile una connessione. Gli ultimi 60 anni hanno visto un crescente interesse per esse, perché con le reti è possibile descrivere sistemi dei più disparati tipi nei campi più vari, dalla biologia all'economia, passando per reti elettriche, informatiche, ecosistemi,  e altro ancora. Ancora più importante, negli ultimi vent'anni è stato scoperto che una classe di reti ha proprietà del tutto comuni nonostante l'intrinseca diversità tra sistemi; la modellizzazione di queste reti, come crescita con caratteristiche preferenziali, è dovuta a Barabasi e Albert (1999), e vengono dette *scale-free*.
# Per maggior semplicità, nell'esposizione del lavoro svolto verrà sempre assunto che le reti siano dirette e non pesate.
# 
# ### 1.1  Proprietà e grandezze caratteristiche
# Dal punto di vista matematico una rete è rappresentata da un grafo. Gli oggetti costitutivi di un grafo sono i **nodi**, i quali vengono collegati opportunamente tra loro con dei **link** secondo dei criteri che dipendono dal modello (nella costruzione di un grafo teorico) o dalla natura del sistema (per le reti reali). Il numero di nodi della rete, o di una sua parte, è ovviamente la grandezza fondamentale per definirne le dimensioni; il numero e la distribuzione dei link ne descrivono la connettività.
# Prima di procedere alla descrizione dei modelli di rete sopracitati, è utile elencare un glossario di caratteristiche delle reti, spesso determinanti per distinguere un grafo scale-free dagli altri nello studio delle reti reali.
# 
# * Il **grado** di un nodo è il numero di altri nodi a cui è connesso. La connettività di una rete è ben rappresentata dalla **distribuzione del grado**, la cui forma funzionale $P(k)$ la cui forma funzionale è il primo criterio per discriminare una rete scale-free. 
# * alla base di ogni topologia c'è il concetto di **distanza**. La distanza tra due nodi di un grafo è il numero di link che li separa nel più piccolo cammino possibile lungo la rete. Altre quantità topologiche importanti sono:
# 	1. l'**eccentricità di un nodo** e il **diametro**. La prima è la massima delle distanze tra un nodo scelto e tutti gli altri nodi della rete. La seconda è la massima eccentricità tra quelle di tutti i nodi del grafo; detto in termini più generali, il diametro è il minor cammino più grande tra tutte le possibili coppie di nodi della rete.
# 	2. **average path length**, cioè la distanza media tra tutte le possibili coppie di nodi della rete. 
# <!--TODO (correlazione con diametro?)-->
# * Per misurare quanto i nodi di un grafo tendono a creare dei *clusters*, viene definito il **coefficiente di clustering** $C_i$. Dal punto di vista di un vertice $i$ di grado $k_i$, quindi, considerando i nodi a esso collegato, $C_i$ è definito come il rapporto
# $$ C_i = \frac{2E_i}{k_i(k_i-1)},$$
# dove $E_i$ è il numero di link tra i $k_i$ primi vicini del vertice e $k_i(k_i-1)/2$ il numero di link possibili tra essi: cioè il numero di collegamenti necessari perché $i$ con i suoi vicini sia una porzione di grafo *completa*, detta anche *clique*.  
# La media su tutti i nodi dei rispettivi $C_i$ dà un'indicazione su quanto la rete sia complessivamente clusterizzata e quindi può essere preso come coefficiente di clustering globale $C$ della rete. Una definizione più recente di $C$, equivalente alla precedente, lo pone uguale al rapporto tra il numero di triplette di nodi completamente collegate $N_\triangle$ e il numero di triplette che vede i tre nodi collegati da almeno due link $N_\wedge$. In entrambi i casi, più $C$ è vicino a $1$, più si ha clusterizzazione.  
# Il coefficiente di clustering svolge un ruolo importante nel distinguere una rete completamente random da una che presenta caratteristiche di *small-world*: infatti un rete con piccolo diametro tende a avere un $\langle C\rangle$ maggiore di una simile rete puramente casuale costruita con lo stesso numero di nodi e con il medesimo cammino più corto medio. Questo comportamento è stato notato in molte reti reali (Watts, Strogatz, 1998
# <!-- TODO DA METTERE IN BIBLIOGRAFIA-->
# ) .
# 
# 
# * Esistono vari modi per definire quando un nodo è centrale rispetto ad altri. Il primo è più immediato è il suo grado. Altri due tra i più importanti sono la **betweenness** e il **page-rank**. Preso un nodo $i$, il primo è definito come il numero di cammini più corti che è possibile tracciare tra due qualsiasi nodi della rete, purché passino per $i$; il secondo dà una maggior centralità a $i$ maggiore è il numero di link *diretti* verso di esso, tenendo conto anche del rank dei nodi che si collegano a esso. In reti dirette, benché non siano *matematicamente* uguali, betweenness e page-rank sono statisticamente molto correlati al grado, pertanto non verranno analizzati. (fare grafico correlazione grado-betweenness-pagerank)
# 
# ### 1.2 Modelli di rete esponenziale 
# Lo studio delle reti random nasce nel 1959 dai (polacchi?) Erdős e Rényi, i quali per primi modellizzarono la definizione di una rete usando criteri probabilistici. Nel corso dei 30 anni successivi è stato osservato che molte reti reali, a dispetto delle dimensioni, avessero un diametro molto piccolo, portando alla definizione del concetto di *small-worlds* e nel 1987 al modello di Watts e Strogatz.
# In entrambi i casi si parte da una configurazione iniziale di nodi per poi randomizzare i link tra essi. Per questo motivo la distribuzione del grado segue una Poissoniana, con una coda destra caratteristica di forma esponenziale; con un numero sufficiente di nodi e link, la distribuzione del grado si approssima a una gaussiana con un grado medio ben definito.
# 
# #### 1.2.1 Random network
# Il modello di Erdős e Rényi parte da un certo numero $N$ di nodi e $n$ di link. Se poniamo che i nodi siano distinguibili, possono esistere (n sopra N(N-1)/2) 
# <!--TODO DA CONTROLLARE NUM CONF POSS, DISTINGUIBILITÀ-->
# configurazioni equiprobabili tra le quali può esserne presa una in maniera random. Una maniera più articolata per definire una rete random è il criterio binomiale: partire da un set di $N$ nodi e dare a ogni possibile coppia un link con una certa probabilità  $p$. 
# <!--VALUTARE SE TENERE SOLO QUESTA DEFINIZIONE-->
# Il punto più importante di un approccio probabilistico alle reti è lo studio di proprietà dei grafi: ponendo $N \rightarrow \infty$, se la probabilità che una certa proprietà si verifichi tende a 1, si osserva che per reti limitate quella proprietà si verifica con probabilità significativa anche con pochi nodi. Ciò si verifica per molte proprietà, e questo fatto permette di poter trattare le reti per categorie secondo le loro proprietà peculiari.
# Nel caso di un grafo di Erdos e Renyi queste sono:
# 
# * la distribuzione del grado ha una forma di distribuzione binomiale, la quale tende a una poissoniana per $p$ piccole, e a una gaussiana per $\langle k \rangle$ grandi. Questo implica che la topologia della rete è abbastanza omogenea, con molti nodi che hanno approssimativamente lo stesso grado.
# * il diametro tende a essere piccolo, come l'average path length. Con $p$ non troppo piccolo il numero di nodi che abbiano una certa distanza $l$ si può approssimare a $\langle k\rangle^l$; uguagliandolo a $N$ deriva che sia diametro che average path length scalano con buona approssimazione con il logaritmo di N (quindi lentamente), secondo la relazione
# $$l \sim \frac{ln(N)}{ln(\langle k \rangle)}.$$ 
# Molte reti reali presentano simili caratteristiche nei gradi di separazione, che hanno portato alla definizione del termine "small world" per esse.
# * il clustering di una rete ramdom tende a essere molto basso. Infatti, preso un nodo e i suoi primi vicini, la probabilità una coppia di essi sia connessa è $p$. Pertanto su tutto il grafo, il coefficiente di clustering medio è proprio $p$, il quale di solito è abbastanza minore di 1 (con $p = 0.1$ un grafo random diventa già molto connesso, per esempio con $10^4$ nodi avrebbe $\langle k\rangle = 10^3$). Questo fatto, al contrario del diametro, si pone in contrasto con le reti reali, le quali hanno quasi sempre un $\langle C \rangle$; sensibilmente più alto.
# <!-- TODO Mettere un grafo-->
# 
# #### 1.2.2 Small World
# Come abbiamo visto il modello di Erdos e Renyi descrive bene il piccolo diametro delle reti reali, ma non il loro elevato grado di clusterizzazione. Inoltre il coefficiente di clustering di esse è simile per reti con numero di nodi molto diverso. Notando per primi ciò, Watts e Strogatz hanno formulato un modello che meglio si adattasse alle caratteristiche reali delle reti. 
# Il fatto che il coefficiente di clustering non dipende dal numero di nodi è caratteristico dei reticoli, pertanto il punto di partenza del modello di Watts e Strogatz è un reticolo con condizioni al contorno cicliche, i cui $N$ nodi sono collegati ai primi $n$ vicini. Se poniamo, per esempio, $n = 2$, si configura così un anello del tipo:
# 
# <!-- TODO Mettere grafo anello e/con zoom a reticolo -->
# 
# Successivamente si procede a riarrangiare in maniera random i link tra i nodi, con una probabilità $p$ per ogni link di venire modificato. In questo modo si hanno un certo numero di link (in media $pnN$) che invece di essere tra nodi in prossimità, saranno tra nodi più lontani, come nel grafo:
# 
# <!-- TODO Mettere grafo small world-->
# 
# Con questo metodo, a seguito del *rewiring* si ha il rischio che il grafo non sia più connesso. Ponendo $n>1$ ciò può essere evitato, portando la probabilità di avere un grafo non connesso quasi a zero già con $n=2$.
# Con $p \rightarrow 1$ il grafo diventa simile a quello di una rete di Erdos-Renyi con :
# 
# <!-- TODO Mettere grafo anello random e ridiculograph watts-->
# 
# Per avere una rete tipica che abbia un numero di connessioni non troppo elevato, ma non così poco da rischiare da avere un grafo non connesso a seguito dell'operazione di rewiring, possono essere considerati degli $N$ e $n$ tali che $N>>n>>ln(N)>>1$. Con queste condizioni la distribuzione del grado $P(k)$ ha una forma gaussiana la cui media coincide con $n$, con $\sigma$ più piccole per $p$ basse, tendente a una delta di Dirac per $p \rightarrow 0$. Infatti, mentre con $p=0$ si ha un reticolo con grado uguale per ogni nodo, l'operazione random di rewiring introduce una casualità sulla $P(K)$ ben descritta da una gaussiana per $N$ grandi, che però ha una larghezza sensibilmente inferiore a quella di una rete random, portando a una rete ancora più omogenea.  
# 
# Valori tipici di $\langle l \rangle$ per le reti reali sono ben descritti dal modello di Erdos e Renyi 
# secondo l'equazione 
# <!-- TODO mettere ref all'equazione sopra-->
# (Albert, Barabasi 2001 pg 13),
# <!-- TODO sistemare questo riferimento bibliografico e anche gli altri-->
# cioè ci si aspetta scali in modo logaritmico fissato $\langle k \rangle$. In una rete generata secondo il modello di Watts-Strogatz le lunghezze dei cammini, fissato $n \equiv \langle k \rangle$, scalano in media in modo diverso al variare di $p$. Per $p$ molto basse ($p << 1/nN$) le lunghezze caratteristiche sono proporzionali alla dimensione del grafo, il quale è ancora molto simile a una reticolo; abbastanza presto, per $p >> 1/nN$, \footnote{$p >> 10^(-4)$ per una rete con $10^3$ nodi e $P(k)$ centrata in 10} vi è invece un largo intervallo di $p$ che vede già verificarsi il fenomeno small-world, con le lunghezze dei cammini che scalano come $ln(N)$ in accordo con le reti reali.  
# L'altra caratteristica fondamentale di uno small-world è che abbia un clustering abbastanza alto in relazione a una rete puramente random. Per $p = 0$ il reticolo ha un $C(0)$ costante al variare di $N$; all'aumentare di $p$, presa una tripletta chiusa, la probabilità che tutti e tre i link rimangano inalterati è $(1-p)^3$  e i suoi due primi vicini hanno probabilità $p^3$ di vedere almeno uno dei loro link riarrangiato. Dato che $C=N_\triangle/N_\wedge$ e che $N_\wedge$ rimane costante con il rewiring, si può porre 
# $$C(p) \propto N_\triangle (p) \Rightarrow C(p) \sim C(0)(1-p)^3, $$
# con $C(0) \sim 0.75$ per $N$ grande. Ricordando che per il modello di Erdos-Renyi $C_{ER}=p$, e che per modellizzare una rete reale $p$ solitamente è abbastanza piccola dato che $\langle k \rangle = Np$, risulta che per valori di $p \lesssim 0.25$ si hanno velocemente $C_{WS}$ sensibilmente maggiori di $C_{ER}$.
# <!-- mettere grafico con plottino di C_ER e C_WS-->
# <!-- correggere tutti gli erdos con la o giusta-->
# <!-- qui vorrei fare un confronto con reti reali, c'è un grafico in cui lui mette C/kmedio, in cui si vede che le reti reali hanno valori tra 0.1 e 0.01 (pg 14); poi mi dà sta curva che non è C/kmedio ma solo C, però non hanno alcun minimo modo di combaciare queste due cose: se faccio la funzione divisa per un grado medio di 10 viene una cosa piccolissima che non ha senso. In questo modo non riesco a provare che watts strogatz hanno C grande come reti reali rispetto a reti random, e non posso concludere con la frase finale qui sotto-->
# 
# Concludendo, un grafo è considerato small-world se ha contemporaneamente piccole distanze medie e, a differenza dei grafi random,  una clusterizzazione relativamente elevata.
# 
# ### 1.3 Reti scale-free
# Proprietà frattali, distr grado con powerlaw tra due e tre (tre probabilmente non compreso?). Grado medio idealmente infinito a causa di gran numero di nodi con grado alto?
# 
# #### 1.3.1 Preferential attachment
# Descrizione modello
# Mettere un grafo e un grafico esemplificativo
# 
# #### 1.3.2 Random scale-free?
# 
# ### 1.4  Percolazione
# Cosa si intende per percolazione, teoria. Differenza punto di vista di percolazione in formazione di rete e percolazione in distruzione di rete?
# 
# #### 1.3.1  Soglia percolativa
# Vedere le due pubblicazioni di cohen e erez

# ## 2   Raccolta dei dati e costruzione delle reti  
# Intro al capitolo in cui si dice da dove è nata l'idea di prendere le antenne da mozilla, l'ipotesi di mesh network, per che cosa sono stati utilizzati quei dati 
# 
# ### 2.1 raccolta e gestione dati
# Approfondire e spiegare il più possibile come abbiamo preso i dati, cosa avevamo di ogni antenna, come abbiamo trattato e gestito il database (pandas), dimensione totale del database, scelta di dati aggregati delle rivelazioni per antenna, come lo abbiamo sfoltito (levando colonne inutili e scartando tutti i dati con countrycode diverso da quello ITA), etc etc in sintesi, far venire al prof questa faccia \$_\$  
# nb. Qui o nel sottoparagrafo successivo  mostrare possibile problema con i dati dei range (far vedere istogramma dei range), provare a spiegare perché  (non sono dati ufficiali ma raccolti dalla gente, gps staccato, etc)
# 
# #### 2.1.1  Problemi memoria: filtraggio dati
# Eventuale sottoparagrafo in cui si parla solo dei problemi di memoria e di come abbiamo selezionato la roba dal db totale, se necessario.
# 
# ### 2.2 Adiacenza e grado
# Dire criterio di linking, definizione distanza, problemi computazionali con funzione distanza geodesica per rete grossa, ripiegare su distanza euclidea, calcolo matrici di adiacenza
# 
# #### 2.2.1  Problemi potenza di calcolo
# Eventuale sottoparagrafo in cui si parla solo dei problemi di potenza di calcolo e di come abbiamo abbandonato funzioni più complesse, se necessario
# 
# #### 2.3 Gradi e fitgradi
# Networkx -> Grafo -> Distr grado. Cioè spiegare che strumenti abbiamo usato per avere il grafo (networkx), far vedere gli istogrammi più belli possibile delle distr grado, poi far vedere i fit su ogni rete, valutare se separatamente o no
# Conclusioni su quale possa essere il tipo di rete in analisi (esponenziale, powerlaw nella coda destra ma esponente troppo alto, no scalefreeness, tuttavia grado medio alto quindi robusto)
# Valutare se dare un primo valore del diametro, e di qualche altra grandezza topologica importante.

# # 3 Network breakdown
# ###### (formerly "Analisi percolativa" ma questo è un titolo noioso, meglio una roba più deep impact ogliea) 
# Una volta osservate le distribuzioni del grado nelle reti delle quattro compagnie e nella rete complessiva formata da tutte le antenne comprese nell'area metropolitana di Roma, procediamo con lo studio percolativo. In riferimento al lavoro fatto da Albert, Jeong e Barabasi nel 1999, la scelta è stata di simulare due differenti scenari in cui i nodi della rete vengono disabilitati. Nel primo scenario si è ipotizzato un attacco intenzionale che cominciasse dai nodi con maggior grado, nel secondo una rimozione random. 
# Lo scopo è studiare l'andamento, in funzione della percentuale di nodi rimossi, del diametro $D$ della rete e della dimensione del cluster più grande (*Giant Cluster*) rapportata al numero totale di nodi sopravvissuti. A seconda di come la rete si comporterà, sarà possibile dedurne la robustezza nei due scenari, in modo tale da poter confrontare meglio tale comportamento con quello di una rete scale-free, o di una di tipo random.
# Per poter fare questo confronto sono state generate, usando le funzioni di *networkx*, delle reti con i modelli di rete scale free (*preferential attachment*, Barabasi, Albert 1999) e di rete esponenziale (*random network*, Erdős, Renyi 1959 e *small world*, Watts, Strogatz, 1998) e su tutti e tre i modelli abbiamo simulato i due scenari di caduta progressiva della rete. In tutti e cinque i campioni di rete che abbiamo analizzato è stato conteggiata la variazione di $D$ e $GC$ e i grafici ottenuti sono stati messi a confronto a quelli ottenuti con le reti generate secondo i modelli.  
# **DA DECIDERE SE TAGLIARE O SINTETIZZARE** La rete reale ha ovviamente delle contromisure per evitare la caduta delle comunicazioni. Le antenne trasmettono segnali tra loro su due bande di frequenza: una *user-side*, dedicata alle normali trasmissioni tra utenti del servizio, e una dedicata a un complesso sistema di feedback gestito da degli hub (grosse antenne con raggio sui 20 km). Questa struttura gerarchica permette, nel caso di caduta di una antenna o di un improvviso eccessivo carico in una zona circoscritta, che gli hub gestiscano potenza e capacità delle antenne circostanti mentre vengono inviati tecnici per un intervento sul luogo. 
# Questo sistema ha ovviamente un certo tempo di reazione. L'analisi da noi svolta pertanto suppone che la caduta della rete avvenga in un tempo inferiore, in una sorta di approssimazione adiabatica. Inoltre, la sola caduta degli hub sarebbe già sufficiente a compromettere seriamente l'integrità della rete (le antenne avrebbero difficoltà a coordinare le comunicazioni tra loro), ma nella nostra ipotesi di mesh-network distribuita ci interessano soltanto le comunicazioni nelle frequenze user-side. Usando questo modello semplificato siamo riusciti a ottenere alcune informazioni su una ipotetica rete wireless di questa natura.
# 
# 
# ## 3.1 Attacco intenzionale
# Nello scenario di attacco intenzionale ci si aspetta una veloce frammentazione della rete. I cluster diverranno rapidamente più piccoli fino a frammentarsi del tutto entro pochi punti percentuali di nodi rimossi. Nel caso di una rete fortemente connessa come quella in esame ci si aspetta una resistenza maggiore, ma comunque una soglia percolativa bassa (entro il 50%). Se la rete è di tipo scale-free dovrebbe essere più fragile ad attacchi di questo tipo: mentre in una rete random i nodi più connessi sono solo una coda della distribuzione del grado, una rete a power-law ha in proporzione molti più nodi molto connessi.
# Dal punto di vista del diametro della rete, levando i nodi più connessi ci si aspetta che esso aumenti, fino a quando la rete diventa tanto frammentata da essere costituita da clusters con pochissimi nodi. Oltrepassata la soglia di frammentazione quindi il diametro dei clusters più grandi decrescerà rapidamente a zero.
# 
# ### 3.1.1 Risultati
# **inserisci grafici con caption**
# 
# ### 3.1.2 Confronto con i modelli
# **inserisci grafici con caption**  
# NB fare calcolo con rete scale free e random con gradi medi attorno a valori delle nostre reti
# Vedede eventuali discrepanze con quanto atteso
# 
# 
# ## 3.2 Caduta random
# 
# ### 3.2.1 Risultati
# **inserisci grafici con caption**  
# 
# ### 3.2.2 Confronto con i modelli
# **inserisci grafici con caption**  
# **mettere anche grafico della distr del grado dei modelli quando si fa il discorso del modello che non va**  
# Qui va fatto un lungo discorso dato che non appatta nulla. Far vedere che con modello scale free di bar e alb con pendenza 3 in realtà non hai alcuna scalefreeness dato che cade tutto in praticamente una sola decade. Far vedere che comportamento è UGUALE ai modelli esponenziali, e che dipende SOLO dal grado medio, e che quindi l'articolo del 2000 è truffaldino. Testare reti modello più grandi, fino a 10000 per non far fondere il pc e solo andamento gc
# Vedere che succede con preferential attachment generalizzato con esponenti 1,5/2/2,5 a vari valori di gradomedio.
# 
# ## 3.2.3 Effetto cascata
# 

# ## Bibliografia
# 
# 1. [Albert, R. and A. L. Barabasi (2002), *Statistical mechanic of complex networks*, Reviews of modern phyisics **74**, p. 47.](http://arxiv.org/pdf/cond-mat/0106096) 
# 2. [Albert, R., H. Jeong, and A. L. Barabasi (2000), *Error and attack tolerance of complex networks*, Nature **406**, p. 378.](http://www.nature.com/nature/journal/v406/n6794/pdf/406378a0.pdf)
# 3. [Barabasi, A. L. and R. Albert (1999), *Emergence of scaling in random networks*, Science **286**, p. 509.](http://arxiv.org/pdf/cond-mat/9910332)
# 4. [Cohen, R. K. Erez, D. ben-Avraham and S. Havlin (2000), *Resilience of the internet to random breakdown*, Physical Review letters **85**, p. 4626.](http://arxiv.org/pdf/cond-mat/0007048)
# 5. [Cohen, R. K. Erez, D. ben-Avraham and S. Havlin (2001), *Breakdown of the internet under intentional attack*, Physical Review letters **86**, p. 3682.](http://arxiv.org/pdf/cond-mat/0010251)
# 6. [Erdős, P. and A. Rényi (1959), *On random graph I.*, Publicationes Mathematicae Debrecen **6**, p. 290.](http://www.renyi.hu/~p_erdos/1959-11.pdf)
# 7. [Molloy, M. e B. Reed (1995). *A critical point for random graphs with a given degree sequence*. Random structures and algorithms **6**, p. 161.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.24.6195&rep=rep1&type=pdf)
# 8. [Motter, A. E: and Y. C. Lai (2002), *Cascade-based attacks on complex networks*, Physical Review E **66**, p. 065102.](http://arxiv.org/pdf/cond-mat/0301086)
# 9. [Watts, J. and H. Strogatz (1998), *Collective dynamics of 'small-world' networks*, Nature **393**, p. 440.](http://www.nature.com/nature/journal/v393/n6684/pdf/393440a0.pdf)
# 10. [*OpenCellID* (ENAiKOON).](http://opencellid.org/)
# 11. [*Mozilla Location Service* (Mozilla Foundation).](https://location.services.mozilla.com/)
# 
# 

# ##Bibliografia   
# 
# 1. [A. L. Barabasi and R. Albert, *Emergence of scaling in random networks*, (1999).](http://arxiv.org/pdf/cond-mat/9910332) (varie cose teoriche su percolazione, **par1**)  
# 2. [R. Albert and A. L. Barabasi, *Statistical mechanic of complex networks*, (2001).](http://arxiv.org/pdf/cond-mat/0106096) (?? **par1**)  
# 3. [R. Cohen, K. Erez, D. ben-Avraham and S. Havlin, *Resilience of the internet to random breakdown*, (2000).](http://arxiv.org/pdf/cond-mat/0007048) (Dimostrazione teorica su condizione percolativa **par1**, comportamento atteso con random failure **par3**)
# 4. [R. Cohen, K. Erez, D. ben-Avraham and S. Havlin, *Breakdown of the internet under intentional attack*, (2001).](http://arxiv.org/pdf/cond-mat/0010251) (Dimostrazione teorica su condizione percolativa **par1**, comportamento atteso con intentional attack **par3**)
# 5. [R. Albert, H. Jeong and A. L. Barabasi, *Error and attack tolerance of complex networks*](http://www.nature.com/nature/journal/v406/n6794/pdf/406378a0.pdf) (varie definizioni, nomenclatura da prendere con le pinze perché un po' outdated, andamento distribuzione del grado **par2**, andamento di D e GC attesi **par3**)
# 6. [P. Erdős and A. Rényi, *On random graph I.*, (1959)](http://www.renyi.hu/~p_erdos/1959-11.pdf) (fonte primo modello rete esponenziale **par3**)
# 7. [J. Watts and H. Strogatz, *Collective dynamics of 'small-world' networks*, (1998)](http://www.nature.com/nature/journal/v393/n6684/pdf/393440a0.pdf) (fonte modello small world di rete esponenziale)
# 8. [A. E. Motter and Y. C. Lai, Cascade-based attacks on complex networks, (2003)](http://arxiv.org/pdf/cond-mat/0301086) (effetto cascata per overload dei nodi sopravvissuti, da leggere **concl**)
# 

# In[ ]:



