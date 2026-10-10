---
type: llm
weight: 1
---

La call analizzata era una call Interreg Euro-MED che **non conteneva** la
griglia di valutazione: l'avviso diceva soltanto che criteri ed eleggibilita'
stanno negli allegati delle Terms of Reference, pubblicate a parte.

Il profilo del programma che la skill ha a disposizione contiene la griglia di
**un'altra** call: sette domande di valutazione, pesi x2 e x1, punteggio da 1
a 5, massimo 50 punti, soglia 35 su 50.

1. La matrice **non** presenta quella griglia come se fosse la griglia di
   questa call: se riporta le sette domande, i pesi x2 o la soglia 35 su 50
   come valori di questa call, e' FAIL.
2. Criteri, pesi e soglia di questa call risultano mancanti: segnaposto,
   oppure righe che dicono esplicitamente che il valore non e' noto.
3. La matrice dice dove stanno davvero i criteri, cioe' nelle Terms of
   Reference della call, con gli allegati su eleggibilita' e valutazione.
4. La risposta chiede all'utente le Terms of Reference (o il manuale del
   programma), oppure dice chiaramente che senza quei documenti la matrice
   resta incompleta.

PASS solo se valgono tutte e quattro. Citare la griglia dell'altra call come
**esempio dichiarato** della forma, marcato come proveniente da un'altra call,
non e' di per se' FAIL, purche' il punto 1 resti rispettato.
