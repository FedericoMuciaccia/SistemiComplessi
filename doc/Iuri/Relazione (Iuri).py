
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

# ## 2 Reti *scale-free
# Le reti sono insiemi di oggetti per i quali è possibile una connessione. Gli ultimi 60 anni hanno visto un crescente interesse per esse, perché con le reti è possibile descrivere sistemi dei più disparati tipi nei campi più vari, dalla biologia all'economia, passando per reti elettriche, informatiche, ecosistemi,  e altro ancora. Ancora più importante, negli ultimi vent'anni è stato scoperto che una classe di reti ha proprietà del tutto comuni nonostante l'intrinseca diversità tra sistemi; la modellizzazione di queste reti, come crescita con caratteristiche preferenziali, è dovuta a \textcite{Barbalbert1999}, e vengono dette scale-free.
# 
# Per maggior semplicità, nell'esposizione del lavoro svolto verrà sempre assunto che le reti siano dirette e non pesate.
# 
# ### 2.1 Proprietà e grandezze caratteristiche
# Dal punto di vista matematico una rete è rappresentata da un grafo. Gli oggetti costitutivi di un grafo sono i **nodi**, i quali vengono collegati opportunamente tra loro con dei **link** secondo dei criteri che dipendono dal modello (nella costruzione di un grafo teorico) o dalla natura del sistema (per le reti reali). Il numero di nodi della rete, o di una sua parte, è ovviamente la grandezza fondamentale per definirne le dimensioni; il numero e la distribuzione dei link ne descrivono la connettività.
# 
# Prima di procedere alla descrizione dei modelli di rete sopracitati, è utile elencare un glossario di caratteristiche delle reti, spesso determinanti per distinguere un grafo scale-free dagli altri nello studio delle reti reali.
# 
# **Grado** Il grado di un nodo è il numero di altri nodi a cui è connesso. La connettività di una rete è ben rappresentata dalla **distribuzione del grado**, la cui forma funzionale $P(k)$ la cui forma funzionale è il primo criterio per discriminare una rete scale-free. 
# 
# **Distanze** alla base di ogni topologia c'è il concetto di distanza. La distanza tra due nodi di un grafo è definita come il numero di link che li separa nel più piccolo cammino possibile lungo la rete. Altre quantità topologiche importanti sono:
# * l'**eccentricità di un nodo**, è la massima delle distanze tra un nodo scelto e tutti gli altri nodi della rete;
# * il **diametro** è la massima eccentricità tra quelle di tutti i nodi del grafo; detto in termini più generali, il diametro è il minor cammino più grande tra tutte le possibili coppie di nodi della rete;
# * l'**average path length**, cioè la distanza media tra tutte le possibili coppie di nodi della rete.
# <!-- TODO (correlazione con diametro?)-->
# 
# **Custering** Per misurare quanto i nodi di un grafo tendono a creare dei clusters, viene definito il coefficiente di clustering $C_i$. Dal punto di vista di un vertice $i$ di grado $k_i$, quindi, considerando i nodi a esso collegato, $C_i$ è definito come il rapporto
# $$C_i = \frac{2E_i}{k_i(k_i-1)},$$
# dove $E_i$ è il numero di link tra i $k_i$ primi vicini del vertice e $k_i(k_i-1)/2$ il numero di link possibili tra essi: cioè il numero di collegamenti necessari perché $i$ con i suoi vicini sia una porzione di grafo *completa*, detta anche *clique*.  
# La media su tutti i nodi dei rispettivi $C_i$ dà un'indicazione su quanto la rete sia complessivamente clusterizzata e quindi può essere preso come coefficiente di clustering globale $C$ della rete. Una definizione più recente di $C$, equivalente alla precedente, lo pone uguale al rapporto tra il numero di triplette di nodi completamente collegate $N_\triangle$ e il numero di triplette che vede i tre nodi collegati da almeno due link $N_\wedge$. In entrambi i casi, più $C$ è vicino a $1$, più si ha clusterizzazione.
# 
# Il coefficiente di clustering svolge un ruolo importante nel distinguere una rete completamente random da una che presenta caratteristiche di *small-world*: infatti un rete con piccolo diametro tende a avere un $\langle C\rangle$ maggiore di una simile rete puramente casuale costruita con lo stesso numero di nodi e con il medesimo cammino più corto medio. Questo comportamento è stato notato in molte reti reali \parencite{Watts1998}.
# 
# **Centralità** Esistono vari modi per definire quando un nodo è centrale rispetto ad altri. Il primo è più immediato è il suo grado. Altri due tra i più importanti sono la **betweenness** e il **page-rank**. Preso un nodo $i$, il primo è definito come il numero di cammini più corti che è possibile tracciare tra due qualsiasi nodi della rete, purché passino per $i$; il secondo dà una maggior centralità a $i$ maggiore è il numero di link *diretti* verso di esso, tenendo conto anche del rank dei nodi che si collegano a esso. 
# 
# In reti dirette, benché non siano *matematicamente* uguali, betweenness e page-rank sono statisticamente molto correlati al grado, pertanto non verranno analizzati. 
# <!-- % 	TODO (fare grafico correlazione grado-betweenness-pagerank) -->
# 
# ### 2.2 Modelli di rete esponenziale
# Lo studio delle reti random nasce dagli ungheresi \textcite{Erdos1959}, i quali per primi modellizzarono la definizione di una rete usando criteri probabilistici. Nel corso dei 40 anni successivi è stato osservato che molte reti reali, a dispetto delle dimensioni, avessero un diametro molto piccolo, portando alla definizione del concetto di *small-worlds* e al modello di \textcite{Watts1998}.
# 
# In entrambi i casi si parte da una configurazione iniziale di nodi per poi randomizzare i link tra essi. Per questo motivo la distribuzione del grado segue una Poissoniana, con una coda destra caratteristica di forma esponenziale; con un numero sufficiente di nodi e link, la distribuzione del grado si approssima a una gaussiana con un grado medio ben definito.
# 
# #### 2.2.1 Random network
# Il modello di Erdős e Rényi parte da un certo numero $N$ di nodi e $n$ di link. Se poniamo che i nodi siano distinguibili, possono esistere $\binom{n}{N(N-1)/2)}$
# <!-- %TODO DA CONTROLLARE NUM CONF POSS, DISTINGUIBILITÀ-->
# configurazioni equiprobabili tra le quali può esserne presa una in maniera random. Una maniera più articolata per definire una rete random è il criterio binomiale: partire da un set di $N$ nodi e dare a ogni possibile coppia un link con una certa probabilità  $p$. 
# <!-- TODO VALUTARE SE TENERE SOLO QUESTA DEFINIZIONE--> -->
# Il punto più importante di un approccio probabilistico alle reti è lo studio di proprietà dei grafi: ponendo $N \rightarrow \infty$, se la probabilità che una certa proprietà si verifichi tende a 1, si osserva che per reti limitate quella proprietà si verifica con probabilità significativa anche con pochi nodi. Ciò si verifica per molte proprietà, e questo fatto permette di poter trattare le reti per categorie secondo le loro proprietà peculiari.
# 
# Nel caso di un grafo di Erdős e Renyi queste sono:
# 
# * la distribuzione del grado ha una forma di distribuzione binomiale, la quale tende a una poissoniana per $p$ piccole, e a una gaussiana per $\langle k \rangle$ grandi. Questo implica che la topologia della rete è abbastanza omogenea, con molti nodi che hanno approssimativamente lo stesso grado;
# 
# * con $N$ grande, il diametro tende a essere piccolo, come l'average path length. Con $p$ non troppo piccolo il numero di nodi che abbiano una certa distanza una lunghezza $l$ si può approssimare a $\langle k\rangle^l$; uguagliandolo a $N$ deriva che diametro e average path length scalano con buona approssimazione con il logaritmo di N, secondo la relazione
# <!-- 	\label{eq:lunghezze} -->
# $$l \sim \frac{ln(N)}{ln(\langle k \rangle)}$$
# Molte reti reali presentano simili caratteristiche nei gradi di separazione, che hanno portato alla definizione del termine "small world" per esse;
# 
# * il clustering di una rete ramdom tende a essere molto basso. Infatti, preso un nodo e i suoi primi vicini, la probabilità una coppia di essi sia connessa è $p$. Pertanto su tutto il grafo, il coefficiente di clustering medio è proprio $p$, il quale di solito è abbastanza minore di 1 (con $p = 0.1$ un grafo random diventa già molto connesso, per esempio con $10^4$ nodi avrebbe $\langle k\rangle = 10^3$). Questo fatto, al contrario del diametro, si pone in contrasto con le reti reali, le quali hanno quasi sempre un $\langle C \rangle$ sensibilmente più alto.
# 
# #### 2.2 Small World
# Come abbiamo visto il modello di Erdős e Renyi descrive bene il piccolo diametro delle reti reali, ma non il loro elevato grado di clusterizzazione. Inoltre il coefficiente di clustering di esse è simile per reti con numero di nodi molto diverso. Notando per primi ciò, Watts e Strogatz hanno formulato un modello che meglio si adattasse alle caratteristiche reali delle reti. 
# 
# Il fatto che il coefficiente di clustering non dipende dal numero di nodi è caratteristico dei reticoli, pertanto il punto di partenza del modello di Watts e Strogatz è un reticolo con condizioni al contorno cicliche, i cui $N$ nodi sono collegati ai primi $n$ vicini. Se poniamo, per esempio, $n = 2$, si configura così un anello del tipo:
# 
# 
# ![Reticolo ciclico.](fig:ring)
# 
# Successivamente si procede a riarrangiare in maniera random i link tra i nodi, con una probabilità $p$ per ogni link di venire modificato. In questo modo si hanno un certo numero di link (in media $pnN$) che invece di essere tra nodi in prossimità, saranno tra nodi più lontani, come nel grafo:
# 
# ![p=0](fig:WSp0)
# ![p=0.03](fig:WSp3)
# ![p=0.3](fig:WSp30)
# ![p=1](fig:WSp100)
# 
# 
# Con questo metodo, a seguito del *rewiring* si ha il rischio che il grafo non sia più connesso. Ponendo $n>1$ ciò può essere evitato, portando la probabilità di avere un grafo non connesso quasi a zero già con $n=2$.
# Con $p \rightarrow 1$ il grafo diventa simile a quello di una rete di Erdős-Renyi:
# 
# ![Grafo random](fig:confrontoGraforandom)
# ![Grafo small-world](fig:confrontoGrafosmall)
# ![Confronto $P(k)$](fig:confrontoGradigauss)
# 
# Per avere una rete tipica che abbia un numero di connessioni non troppo elevato, ma non così poco da rischiare da avere un grafo non connesso a seguito dell'operazione di rewiring, possono essere considerati degli $N$ e $n$ tali che $N>>n>>ln(N)>>1$. Con queste condizioni la distribuzione del grado $P(k)$ ha una forma gaussiana la cui media coincide con $n$, con $\sigma$ più piccole per $p$ basse, tendente a una delta di Dirac per $p \rightarrow 0$. Infatti, mentre con $p=0$ si ha un reticolo con grado uguale per ogni nodo, l'operazione random di rewiring introduce una casualità sulla $P(K)$ ben descritta da una gaussiana per $N$ grandi, che però ha una larghezza sensibilmente inferiore a quella di una rete random, portando a una rete ancora più omogenea.  
# 
# Valori tipici di $\langle l \rangle$ per le reti reali sono ben descritti dal modello di Erdős e Renyi secondo l'equazione 
# \ref{eq:lunghezze}
# <!-- TODO REF A EQUAZIONE DA SISTEMARE -->
# \parencite{Barbalbert2002}, cioè ci si aspetta scali in modo logaritmico fissato $\langle k \rangle$. In una rete generata secondo il modello di Watts-Strogatz le lunghezze dei cammini, fissato $n \equiv \langle k \rangle$, scalano in media in modo diverso al variare di $p$. Per $p$ molto basse ($p << 1/nN$) le lunghezze caratteristiche sono proporzionali alla dimensione del grafo, il quale è ancora molto simile a una reticolo; abbastanza presto, per $p >> 1/nN$, 
# \footnote{$p >> 10^(-4)$ per una rete con $10^3$ nodi e $P(k)$ centrata in 10} 
# <!-- TODO COSA FARE CON NOTA A PIE? -->
# vi è invece un largo intervallo di $p$ che vede già verificarsi il fenomeno small-world, con le lunghezze dei cammini che scalano come $ln(N)$ in accordo con le reti reali.  
# 
# L'altra caratteristica fondamentale di uno small-world è che abbia un clustering abbastanza alto in relazione a una rete puramente random. Per $p = 0$ il reticolo ha un $C(0)$ costante al variare di $N$; all'aumentare di $p$, presa una tripletta chiusa, la probabilità che tutti e tre i link rimangano inalterati è $(1-p)^3$  e i suoi due primi vicini hanno probabilità $p^3$ di vedere almeno uno dei loro link riarrangiato. Dato che $C=N_\triangle/N_\wedge$ e che $N_\wedge$ rimane costante con il rewiring, si può porre 
# $$C(p) \propto N_\triangle (p) \Rightarrow C(p) \sim C(0)(1-p)^3, $$
# con $C(0) \sim 0.75$ per $N$ grande. Ricordando che per il modello di Erdős-Renyi $C_{ER}=p$, e che per modellizzare una rete reale $p$ solitamente è abbastanza piccola dato che $\langle k \rangle = Np$, risulta che per valori di $p \lesssim 0.25$ si hanno velocemente $C_{WS}$ sensibilmente maggiori di $C_{ER}$.
# 
# ![Confronto clustering.](fig:confrontoC)
# 
# Concludendo, un grafo è considerato small-world se ha contemporaneamente piccole distanze medie e, a differenza dei grafi random,  una clusterizzazione relativamente elevata. Pertanto il modello di Watts e Strogatz descrive in maniera soddisfacente reti che abbiano queste caratteristiche, purché non siano scale-free.
# 
# ### 2.3 Reti scale-free
# Molte importanti reti reali di grandi dimensioni hanno la notevole caratteristica di avere un certo livello di invarianza di scala. Questa è manifestata da una distribuzione del grado che segue una funzione a legge di potenza $P(k)\sim k^{-\gamma}$, con $\gamma$ compreso quasi sempre tra $2$ e $3$, in maniera sempre più esatta al crescere di $k$. Mentre le reti random possono riprodurre una $P(k)$ arbitrario, e quindi anche una *power-law*, ma non riescono a generare grafi connessi e con $\langle l \rangle$ non definibile \parencite{Barbalbert2002}, le reti small-world riproducono bene le proprietà di clustering e cammini medi, ma non possono portare a $P(k)$ power-law. Serve pertanto un modello che riproduca piccoli diametri, grandi clustering e $P(k)$ a legge di potenza.
# 
# I modelli di Erdős-Renyi e Watts-Strogatz partono da una configurazione di nodi e poi distribuiscono o riarrangiano i link con una certa probabilità *uniforme* per tutti i link. Le reti reali, tuttavia, spesso partono da un certo numero piccolo di nodi e successivamente crescono. Il primo punto chiave del modello formulato da Barabasi e Albert è proprio il concetto di crescita: la rete parte a $t=0$ con $m_0$ nodi e a ogni step temporale si aggiunge alla rete un nodo con un certo numero $m < m_0$ di link da assegnare agli altri nodi esistenti. Il secondo riguarda il fatto che la probabilità di *attachment* di un nuovo nodo agli altri non è uniforme su tutti i nodi ma preferenziale: il *preferential attachment* dà quindi una maggiore probabilità $\Pi (k_i)$ di collegamento di un nodo nuovo a un certo nodo $i$ in maniera proporzionale al suo grado, secondo la formula
# $$\Pi (k_i) = \frac{k_i}{\sum_j k_j}.$$
# 
# La costruzione della rete avviene in modo dinamico, pertanto il grado di un nodo $i$ sarà funzione crescente del suo tempo di vita nella rete, con una probabilità di attachment dei nuovi nodi a $i$ anch'essa dipendente da $t$. Pertanto, con l'andare del tempo il grado di $i$ aumenterà sempre più velocemente. Approssimando $k_i$ a una variabile continua per $t$ grandi, dato che 
# $$\frac{dk_i}{dt} = m \Pi (k_i) = m \frac{k_i}{\sum_{j=1}^{N-1} k_j} = m \frac{k_i}{2mt - m} = \frac{k_i}{2t - 1} \sim \frac{k_i}{2t},$$
# dove $m$ è il numero di link aggiunti per iterazione, ponendo quindi la condizione iniziale per il nodo $i$, $k_i(t_i) = m$
# $$ \Rightarrow k_i(t) = m (\frac{t}{t_i})^\frac{1}{2}. $$
# 
# Ovviamente se il grado di un nodo è funzione di $t$, anche la $P(k)$ lo sarà. Definendo $P(k_i(t)<k)$ la probabilità che un nodo $i$ abbia un grado minore di un certo valore $k$, la distribuzione del grado $P(k)$ può essere derivata ponendola uguale a $dP(k_i(t)<k)/dk$, ottenendo per $t\rightarrow \infty$:
# $$ P(k)\sim 2m^2 k^{-3}. $$
# 
# ![Albero scale-free](fig:barabalbero)
# 
# 
# Il modello di Barabasi e Albert è un modello minimale, importantissimo perché il primo in grado di riprodurre un grafo che mostrasse un'invarianza di scala, ma che in alcuni aspetti mal si accorda con quelle reti reali con caratteristiche scale-free. Per cominciare la distribuzione del grado è una legge di potenza con esponente $3$,ma le reti scale-free solitamente hanno un esponente inferiore, seppur maggiore di $2$. Benché non sia possibile calcolare in modo analitico $\langle l\rangle$ e $C$ per una rete di Barabasi-Albert, da simulazioni numeriche è possibile ottenerne quantità caratteristiche. 
# 
# Il cammino medio risulta sottostimato rispetto alle reti reali e il coefficiente di clustering non è costante con l'aumentare di $N$ come per le reti reali ma diminuisce, anche se più lentamente di una rete random
# \footnote{Ovviamente il coefficiente di clustering dipende dal numero $m$ di link generati per ogni nuovo nodo. Con $m = 1$ il clustering è nullo dato che il grafo è un albero, mentre $C \neq 0$ per $m>1$ e cresce all'aumentare di $m$, mantenendosi comunque al di sotto dei valori di reti reali con parametri simili.} 
# <!-- TODO CHE FARE CON NOTA -->
# \parencite{Barbalbert2002}. Per questo motivo il modello iniziale è stato integrato e reso più complesso.  
# 
# ![Confronto $P(k)$](fig:confrontoGradi)
# 
# ### 2.4 Percolazione
# Per percolazione, in analogia con i liquidi, si intende il passaggio di informazione da un lato all'altro di una rete. Nello specifico, quando si fa uno studio percolativo di una rete, si cerca l'esistenza o meno di un cluster che ricopra l'intera rete (*spanning cluster*, o *giant cluster*). Il giant cluster è definito come quella componente di una rete le cui dimensioni sono dello stesso ordine della dimensione della rete complessiva (e quindi gli altri nodi o cluster minori hanno dimensioni di ordini inferiore), cioè il rapporto tra le sue dimensioni e le dimensioni dell'intera rete è $\sim 1$.
# 
# Tipicamente uno studio percolativo su una rete random consiste nell'individuare, durante la costruzione della rete partendo da $N$ nodi scollegati, la soglia percolativa $p_c$, cioè la probabilità di creazione link tale che compaia lo spanning cluster. Nel caso di una rete costruita con il modello di Barabasi-Albert la questione non si pone, dato che per definizione questa è composta da un solo cluster in crescita progressiva. Inoltre, dato che una rete di antenne cellulari nasce con una progettazione molto dettagliata in modo che venga costruita già oltre la soglia percolativa, nel caso in esame non è praticabile né interessante individuare $p_c$ in costruzione. In questo caso ha più senso individuare la soglia percolativa per distruzione della rete. 
# 
# Uno studio per distruzione può avere più approcci che portano a soglie diverse:
# * se si parte da una rete con uno spanning cluster, rimuovendo link tra tutte le coppie di nodi connesse con una certa probabilità, si avrà una $p_d$ oltre la quale la rete non percola più. In questo caso $p_{d_{link}} = 1-p$ soltanto se si parte da un grafo completamente connesso.
# <!--  %TODO BARBASI LO CHIAMA UN PROBLEMA DI BOND PERCOLATION INVERSO, CHE SIGNIFICA? --> 
# * in alternativa si possono rimuovere i nodi in maniera random. In questo caso, rimuovendo un nodo si rimuovono in un colpo solo tutti i link a esso collegati, portanto quindi a una $p_{d_{nodo}} \neq p_{d_{link}}$. Si può dare una probabilità maggiore ai nodi con grado più alto per simulare un attacco mirato.
# * in maniera opposta a un attachment progressivo, può essere usata un metodo di distruzione progressiva, nel quale si rimuove un nodo per volta e si simula la rimozione successiva con la rete risultante dalla rimozione precedente. Nel caso di una rimozione random, la differenza di questo metodo progressivo con quello diretto è poco significativa, ma risulta molto differente con l'attacco intenzionale, come spiegato in maniera più dettagliata nel paragrafo \ref{subsec:simulazione}
# <!-- TODO RIFERIMENTO A PARAGRAFO DA SISTEMARE -->
# . Per rimozione progressiva dei nodi, che sia random o intenzionale, la soglia percolativa è espressa come la frazione critica $f$ di nodi rimossi, rispetto al numero di nodi originale, oltre la quale non si ha più uno spanning cluster.
# 
# #### 2.4.1 Soglia percolativa
# Nel caso di rimozione di nodi da una rete, è interessante determinare quale è la frazione $f$ di nodi che è necessario rimuovere per avere una frammentazione completa della rete. Un criterio per stabilire l'esistenza del giant cluster si basa sull'approssimazione che la rete sia abbastanza frammentata da poter trascurare i cicli. In questa situazione se esiste il cluster che copre tutta la rete è ridotto con buona approssimazione a un albero, e quindi si ha che, preso un nodo qualsiasi connesso al giant cluster, questo sia connesso a almeno un altro nodo \parencite{Cohen2000}. 
# 
# Definiamo quindi la probabilità $q$ che un link scelto a caso non porti a un nodo che non faccia parte del giant cluster. Se $q<1$ significa che esiste almeno un nodo che porti al giant cluster, e quindi il giant cluster esiste. L'intento è sapere quando è $1$, per far ciò possiamo calcolare $q$ definendola come la probabilità $P_{\rightarrow}(k)$ che un link scelto a caso porti a un nodo di grado $k$, per la probabilità $q^{k-1}$che gli altri $k-1$ nodi non portino al giant cluster, sommato su tutti i possibili gradi:
# $$q = \sum_k P_{\rightarrow}(k) q^{k-1},$$
# <!-- 	\label{eq:condizione} -->
# Se definiamo a sua volta $P_{\rightarrow}(k)$ come la probabilità di avere un nodo di grado $k$, per il numero di link possibili con cui possiamo ottenerlo (cioè il suo grado), allora $P_{\rightarrow}(k)$ diventa
# $$P_{\rightarrow}(k) = \frac{P(k)k}{\sum_{k'}P(k')k'} = \frac{P(k)k}{\langle k \rangle}$$
# $$\Rightarrow q = \frac{1}{\langle k \rangle}\sum_k P(k)kq^{k-1} $$
# Questa è uan funzione parametrica e ricorsiva. Chiamandola $F(q)$ e studiandola si ha che ha derivate prima e seconda positive, pertanto è sempre crescente e convessa; inoltre si ha che $F(1) = 1$ e $F(0)>0$. Tutto ciò vale per qualsiasi parametro $k$. 
# 
# Risolvendo l'equazione $q = F(q)$ si ottiene la condizione secondo cui il giant cluster non può esistere. Infatti, se esiste una soluzione oltre a quella banale per $q=1$, significa che l'equazione 
# \ref{eq:condizione}
# <!-- TODO REF A EQUAZIONE DA SISTEMARE -->
# è verificata per valori di $q<1$ e che quindi il giant cluster esiste. Come si può vedere dalla figura 
# \ref{fig:banalita}
# <!-- TODO REF A FIGURA DA SISTEMARE -->
# , si può adottare un metodo grafico: la retta e la curva si intersecano sempre in due punti, il primo con $F'(q)<q'=1$ e il secondo con $F'(q) \geq 1$. Dato che uno dei due deve sempre essere $F(1)=1$, se 
# <!-- \label{eq:soluzione} -->
# $$F'(q=1) \geq 1 $$
# significa che esiste un altro punto di intersezione per $q<1$ e quindi esiste il giant cluster.
# Svolgendo $d_qF|_{q=1} \geq 1$ si ottiene la condizione di esistenza dello spanning cluster in termini del grado, o criterio di \textcite{Molloy1995}:
# <!--  \label{eq:criterion} -->
# $$\frac{\langle k^2\rangle}{\langle k \rangle}\geq 2.$$
# 
# Questo risultato è valido per ogni tipo di rete \parencite{Cohen2000}.
# 
# Un nodo con un grado iniziale $k_0$ avrà, dopo la rimozione di una frazione $f$ di nodi, un grado k con una probabilità dettata da una distribuzione binomiale $B_{p,k_0}(k)$, e quindi la nuova distribuzione dei gradi sarà $P(k) = \sum_{k_0} P(k_0)B_{p,k_0}(k)$. Ricavando i nuovi $\langle k \rangle$ e $\langle k^2 \rangle$ si ottiene che la frazione di nodi rimossi necessaria perché si verifichi che $\langle k^2\rangle/\langle k \rangle = 2$, e cioè il grafo sia completamente frammentato, è 
# <!--  \label{eq:criterionfreq} -->
# $$f = 1 - \frac{1}{\frac{\langle k^2 \rangle}{\langle k \rangle}-1}$$
# 
# Nel caso specifico di una rete costruita con il modello di Barabasi-Albert, questa avrà $P(k)\propto k^{-\alpha}$, che spazierà da un minimo $m$ e un massimo $K$. In questo caso, ponendo $K\gg m \gg 1$, si può approssimare $k$ a una grandezza continua e si ottengono due comportamenti a seconda del valore di $\alpha$:
# $$\frac{\langle k^2\rangle}{\langle k \rangle} = c \frac{2-\alpha}{3-\alpha},$$
# con
# * **$\alpha > 3 \Rightarrow c\sim m.$** Si ha una transizione allo stato completamente frammentato per valori di $f<1$
# * **$\alpha < 3 \Rightarrow c=c(K).$** La transizione dipende dal valore di $K$, per cui esiste per reti finite, ma per $K \rightarrow \infty$ $f\rightarrow1$.
# 
# Nel caso dell'attacco intenzionale la percentuale $f$ è ottenuta per via numerica. Dato inoltre il peculiare metodo di attacco scelto, sarebbe necessario uno studio progressivo che a ogni iterazione tenga conto del taglio dei $k$ più grandi e ricalcoli la $P(k)$ per ottenere il rapporto $\frac{\langle k^2 \rangle}{\langle k \rangle}$. Risulterebbe pertanto più conveniente effettuare simulazioni numeriche direttamente sui modelli \parencite{Cohen2001}.
# 
# In ogni caso, a livello qualitativo, come nel caso di attacco random ci si aspettava una maggiore resistenza da parte delle reti scale-free, a causa del grande numero di nodi poco connessi che garantisce una $P(k)$ a legge di potenza con un opportuno $\alpha$, nel caso dell'attacco intenzionale ci si aspetta una certa fragilità. Infatti le reti scale free sono costruite attorno ai nodi più connessi, si può supporre quindi che rimuoverli per primi provochi un deterioramento più veloce rispetto a una rete random con uguale grado medio \parencite{Barbalbert2002}.
# ![Soluzione banale.](fig:banale)
# ![Soluzione non banale.](fig:nonbanale)
# 
# 
# [fig:ring]: ./img/Teoria/zoomring.svg "Il punto di partenza del modello Watts-Strogatz: un reticolo con condizioni al contorno cicliche."
# 
# <!-- TODO da mettere un caption unico e tutte le figure assieme 
# \caption[Generazione con modello Watts-Strogatz.]{Generazione di grafi con il modello Watts-Strogatz a differenti $p$ di rewiring.}
# -->
# [fig:WSp0]: ./img/Teoria/ringnet.svg "$p = 0$"
# [fig:WSp3]: ./img/Teoria/smallworld.svg "$p = 0.03$"
# [fig:WSp30]: ./img/Teoria/random-smallworld.svg "$p = 0.3$"
# [fig:WSp100]: ./img/Teoria/totalrandomwatts.svg "$p = 1$"
# 
# <!-- TODO da mettere un caption unico e tutte le figure assieme 
# \caption[Confronto grafi random.]{Confronto tra due grafi da 100 nodi: uno generato con il modello Erdos-Renyi ($p=7\%$) e uno con il modello Watts-Strogatz partendo da un reticolo con nodi connessi ai primi 3 vicini e il 100\% di probabilità di rewiring. A parte la somiglianza dei grafi, le distribuzioni del grado hanno simile comportamento.}
# -->
# [fig:confrontoGraforandom]: ./img/Teoria/Erdosmodel.svg "Grafo random"
# [fig:confrontoGrafosmall]: ./img/Teoria/Wattsmodel.svg "Grafo small-world"
# [fig:confrontoGradigauss]: ./img/Teoria/ComparDegExp.svg "Confronto $P(k)$"
# 
# [fig:confrontoC]: ./img/Teoria/ConfrontoC.svg "Confronto tra i coefficienti di clustering teorici dei due modelli, al variare del rispettivo parametro $p$."
# 
# [fig:barabalbero]: ./img/Teoria/Barabalbert1.svg "Esempio di grafo generato con il modello di Barabasi-Albert. Con $m=1$ è evidente la struttura frattale, ma essendo un grafo ad albero il clustering è nullo."
# 
# [fig:confrontoGradi]: ./img/Teoria/CompareSameN.svg "Confronto tra le distribuzioni del grado dei tre modelli esposti."
# 
# <!-- Todo da mettere un caption unico e tutte le figure assieme
# \caption[Esistenza soluzione non banale.]{Confronto tra il caso in cui $F(q)=q$ ha solo la soluzione banale $q=1$, e il caso in cui esiste una soluzione per $q<1$.}
# -->
# [fig:banale]: ./img/Teoria/Banale.svg "Solo $q=1$"
# [fig:nonbanale]: ./img/Teoria/Bonbanale.svg "Esistenza di $q<1$"
# 

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


