
## Analisi del raggio di copertura delle antenne

Dato che ci servirà fare grafici con scale logaritmiche eliminiamo i dati di antenne che presentano un raggio nullo
```
range =! 0
```

Il raggio minimo risulta essere 1m, mentre quello massimo 20341m. Dato che il raggio del Grande Raccordo Anulare è circa 10km questo significa che ci saranno antenne con un grado di connessione totale.
TODO forse spostare questa considerazione a quando si è spiegato il criterio di linking.
TODO spiegare la possibile casa di questi valori di raggi così bassi

Facciamo un istogramma log-log per la distribusione del raggio di copertura, sia con la canalizzazione lineare sugli interi, sia con una canalizzazione logaritmica in base 2, per ridurre il rumore sulla coda.
TODO inserire figura con entrambe le canalizzazioni, con quella logatimica in risalto, più spessa ed evidente, con inoltra una linea tenue che segna il valore massimo.
In figura si può vedere come l'andamento sia inaspettatamente abbastanza power-law su diverse decadi.
TODO  crcare di spiegare questo fatto.

Facendo un fit TODO abbiamo ottenuto il seguarte esponente per l'andamento a potenza: TODO


TODO mettere retta con pendenza con fit a mano spannometrico
