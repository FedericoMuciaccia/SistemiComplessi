# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Relazione Sistemi Complessi

# <markdowncell>

# ###Sommario

# <markdowncell>

# ##1   Reti *scale-free*
# ###1.1  Teoria
# ###1.2  Percolazione
# ####1.2.1  Soglia percolativa

# <markdowncell>

# ##2   Dati
# ###2.1  Perché?
# ###2.2  Come?
# ###2.3  Database->Distanza (criterio linking) -> Adiacenza
# ####2.3.1  Problemi memoria: filtraggio dati
# ####2.3.2  Problemi potenza di calcolo
# ###2.4  Networkx -> Grafo -> Distr grado

# <markdowncell>

# ##3  Analisi percolativa
# Una volta osservate le distribuzioni del grado nelle reti delle quattro compagnie e nella rete complessiva formata da tutte le antenne comprese nell'area metropolitana di Roma, procediamo con uno studio percolativo. In riferimento allo studio fatto da Barabasi, Albert e Jeong nel 1999, la scelta è stata di simulare due differenti scenari in cui i nodi della rete vengono disabilitati. Nel primo scenario si è ipotizzato un attacco intenzionale che cominciasse dai nodi con maggior grado, nel secondo una rimozione random.   
# Lo scopo è studiare l'andamento, in funzione della percentuale di nodi rimossi, del diametro $D$ della rete e della dimensione del cluster più grande (*Giant Cluster*) rapportara al numero totale di nodi sopravvissuti. A seconda di come la rete si comporterà, sarà possibile dedurne la robustezza nei due scenari, in modo tale da poter confrontare meglio tale comportamento con quello di una rete scale-free, o di una di tipo random.  
# Per poter fare questo confronto sono state generate, usando le funzioni di *networkx*, delle reti con i modelli di rete scale free (*preferential attachment*, Barabasi, Albert 1999) e di rete esponenziale (*random network*, Erdős, Renyi 1959 e *small world*, Watts, Strogatz, 1998) e su tutti e tre i modelli abbiamo simulato i due scenari di caduta progressiva della rete. In tutti e cinque i campioni di rete che abbiamo analizzato è stato conteggiata la variazione di $D$ e $GC$ e i grafici ottenuti sono stati messi a confronto a quelli ottenuti con le reti generate secondo i modelli.
# 
# ###3.1  Attacco intenzionale
# Nello scenario di attacco intenzionale si ipotizza che la rete perda nodi a cominciare da quello con il grado maggiore.
# ####3.1.2  Modelli
# 
# ####3.1.1  Rete completa, compagnie
# 
# ###3.2  Rottura random
# ####3.2.1  Rete completa, compagnie
# ####3.2.2  Modelli

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


