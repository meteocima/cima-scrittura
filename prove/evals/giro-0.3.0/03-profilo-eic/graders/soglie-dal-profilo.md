---
type: llm
weight: 1
---

La call analizzata era una call EIC Pathfinder Open, e **non conteneva**
criteri, soglie, pesi ne' limiti di pagine. Quei valori dovevano venire dal
profilo del programma. Verificare che la matrice li riporti:

1. Riconosce lo strumento: dice che si tratta di EIC Pathfinder Open, non
   genericamente "EIC" o "Horizon Europe".
2. Soglie per criterio: **4** su Excellence, **3,5** su Impact, **3** su
   Quality and efficiency of the implementation.
3. Pesi: **50%** Excellence, **30%** Impact, **20%** Implementation.
4. Limite della Part B: **22 pagine**.

Se la matrice riporta invece le soglie generali di Horizon Europe (3 per
criterio, 10 complessiva) o un limite di 40 o 45 pagine, e' FAIL: vuol dire
che ha caricato il profilo sbagliato.

PASS solo se valgono tutte e quattro.
