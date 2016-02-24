# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Relazione Sistemi Complessi

# <markdowncell>

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

# <markdowncell>

# ##1   Reti *scale-free*
# Le reti sono insiemi di oggetti per i quali è possibile una connessione. Gli ultimi 60 anni hanno visto un crescente interesse per esse, perché con le reti è possibile descrivere sistemi dei più disparati tipi nei campi più vari, dalla biologia all'economia, passando per reti elettriche, informatiche, ecosistemi,  e altro ancora. Ancora più importante, negli ultimi vent'anni è stato scoperto che una classe di reti ha proprietà del tutto comuni nonostante l'intrinseca diversità tra sistemi; la modellizzazione di queste reti, come crescita con caratteristiche preferenziali, è dovuta a Barabasi e Albert (1999), e vengono dette *scale free*.
# 
# ###1.1  Teoria
# Proprietà reti, distanze, diametro, clustering, betweenness (correlazione tra between e grado in reti non dirette) scale-freeness di alcune, etc boh?
# 
# ####1.1.1 Modelli di rete esponenziale
# Reticolo -> randomizzazione
# 
# #####Random network
# Descrizione modello
# Mettere un grafo e un grafico del grado esemplificativo
# 
# #####Small World
# Effetto small world
# Descrizione modello
# Mettere un grafo e un grafico esemplificativo
# 
# ####1.1.2 Reti scale-free
# 
# #####Preferential attachment
# Descrizione modello
# Mettere un grafo e un grafico esemplificativo
# 
# ##### Random scale-free?
# 
# ###1.2  Percolazione
# 
# ####1.2.1  Soglia percolativa

# <markdowncell>

# ##2   Raccolta dei dati e costruzione delle reti
# Intro al capitolo in cui si dice da dove è nata l'idea di prendere le antenne da mozilla, l'ipotesi di mesh network, per che cosa sono stati utilizzati quei dati 
# 
# ###2.1 raccolta e gestione dati
# Approfondire e spiegare il più possibile come abbiamo preso i dati, cosa avevamo di ogni antenna, come abbiamo trattato e gestito il database (pandas), dimensione totale del database, scelta di dati aggregati delle rivelazioni per antenna, come lo abbiamo sfoltito (levando colonne inutili e scartando tutti i dati con countrycode diverso da quello ITA), etc etc in sintesi, far venire al prof questa faccia \$_\$  
# nb. Qui o nel sottoparagrafo successivo  mostrare possibile problema con i dati dei range (far vedere istogramma dei range), provare a spiegare perché  (non sono dati ufficiali ma raccolti dalla gente, gps staccato, etc)
# ####2.1.1  Problemi memoria: filtraggio dati
# Eventuale sottoparagrafo in cui si parla solo dei problemi di memoria e di come abbiamo selezionato la roba dal db totale, se necessario.
# 
# ###2.2 Adiacenza e grado
# Dire criterio di linking, definizione distanza, problemi computazionali con funzione distanza geodesica per rete grossa, ripiegare su distanza euclidea, calcolo matrici di adiacenza
# 
# ####2.2.1  Problemi potenza di calcolo
# Eventuale sottoparagrafo in cui si parla solo dei problemi di potenza di calcolo e di come abbiamo abbandonato funzioni più complesse, se necessario
# 
# ####2.3 Gradi e fitgradi
# Networkx -> Grafo -> Distr grado. Cioè spiegare che strumenti abbiamo usato per avere il grafo (networkx), far vedere gli istogrammi più belli possibile delle distr grado, poi far vedere i fit su ogni rete, valutare se separatamente o no
# Conclusioni su quale possa essere il tipo di rete in analisi (esponenziale, powerlaw nella coda destra ma esponente troppo alto, no scalefreeness, tuttavia grado medio alto quindi robusto)
# Valutare se dare un primo valore del diametro, e di qualche altra grandezza topologica importante.

# <markdowncell>

# # 3 Network breakdown
# ######(formerly "Analisi percolativa" ma questo è un titolo noioso, meglio una roba più deep impact ogliea) 
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

# <markdowncell>

# ##Bibliografia
# 
# 1. [A. L. Barabasi and R. Albert, *Emergence of scaling in random networks*, (1999).](http://arxiv.org/pdf/cond-mat/9910332)  
# 2. [R. Albert and A. L. Barabasi, *Statistical mechanic of complex networks*, (2001).](http://arxiv.org/pdf/cond-mat/0106096) 
# 3. [R. Cohen, K. Erez, D. ben-Avraham and S. Havlin, *Resilience of the internet to random breakdown*, (2000).](http://arxiv.org/pdf/cond-mat/0007048)
# 4. [R. Cohen, K. Erez, D. ben-Avraham and S. Havlin, *Breakdown of the internet under intentional attack*, (2001).](http://arxiv.org/pdf/cond-mat/0010251)
# 5. [R. Albert, H. Jeong and A. L. Barabasi, *Error and attack tolerance of complex networks*, (2000).](http://www.nature.com/nature/journal/v406/n6794/pdf/406378a0.pdf)
# 6. [P. Erdős and A. Rényi, *On random graph I.*, (1959).](http://www.renyi.hu/~p_erdos/1959-11.pdf)
# 7. [J. Watts and H. Strogatz, *Collective dynamics of 'small-world' networks*, (1998).](http://www.nature.com/nature/journal/v393/n6684/pdf/393440a0.pdf)
# 8. [A. E. Motter and Y. C. Lai, Cascade-based attacks on complex networks, (2003).](http://arxiv.org/pdf/cond-mat/0301086)

# <markdowncell>

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

# <codecell>


