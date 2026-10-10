---
type: llm
weight: 1
---

La call analizzata era una call UCPM, e **non conteneva** criteri, punteggi
ne' soglie. Dovevano venire dal profilo del programma. Verificare che la
matrice riporti:

1. Tre criteri con questi massimi: Relevance **40**, Quality **30**, Impact
   **30**, su un totale di 100 punti.
2. Soglie per criterio **20 / 15 / 15** e soglia complessiva **65**, con detto
   che servono tutte e due le condizioni.
3. Il legame fra sotto-criteri e **caselle numerate della Part B** (per
   esempio 1.1, 1.2, 1.3, 2.1, 3.1): la matrice dice in quale casella si
   risponde, almeno per alcuni criteri.
4. Limite della Part B: **50 pagine**.

PASS solo se valgono tutte e quattro.
