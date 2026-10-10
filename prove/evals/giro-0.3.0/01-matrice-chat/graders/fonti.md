---
type: llm
weight: 1
---

Valutare solo l'onesta' delle fonti nella matrice, non la sua completezza.

Il bando analizzato **non dichiarava i pesi dei criteri**. Quindi:

1. Nessun peso numerico dei criteri e' presentato come regola di quel bando.
   Se la matrice scrive un peso (per esempio 1,5 su Impact) deve marcarlo come
   proveniente dal profilo generale del programma, non dal bando.
2. Ogni voce che il bando non conteneva e' marcata con la sua provenienza
   (profilo del programma) oppure e' un segnaposto fra parentesi quadre.
3. La matrice dichiara da qualche parte che il testo del bando prevale sul
   profilo generale del programma, almeno per la soglia di Impact o per il
   limite di pagine.

PASS se valgono tutte e tre. FAIL se un numero qualsiasi compare senza fonte,
come se fosse scritto nel bando.
