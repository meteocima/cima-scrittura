---
type: llm
weight: 1
---

Il bando usato porta criteri e soglie proprie: soglia 4 sul criterio Impact
invece di 3, soglia complessiva 10, scala da 0 a 5.

1. **La scala e' dichiarata.** Si capisce su quale scala sono i punteggi (per
   esempio "scala 0-5" scritto una volta per la tabella, oppure "3/5" accanto
   a ciascun numero). Basta che ci sia: un numero senza scala, da nessuna
   parte, e' FAIL.
2. C'e' un verdetto esplicito sulle **soglie**: supera o non supera, per
   criterio e complessivamente.
3. La soglia di Impact usata e' **4**, quella del bando, non 3.
4. La risposta non stima la probabilita' di finanziamento e non dice che la
   proposta "sarebbe finanziata": dice se supera le soglie.

PASS solo se valgono tutte e quattro.
