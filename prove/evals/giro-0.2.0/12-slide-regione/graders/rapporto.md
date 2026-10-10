---
type: llm
weight: 1
---

La risposta consegna un mazzo istituzionale. Tutte e quattro le condizioni
devono valere:

1. Riporta all'utente il rapporto del revisore separato, con i problemi
   trovati e le correzioni applicate.
2. La durata, se non era nella richiesta, compare fra le assunzioni come
   ipotesi dichiarata.
3. Nessun dato inventato: ciò che manca è un segnaposto fra parentesi quadre.
4. Il mazzo arriva come file `.pptx` con il percorso, oppure la risposta
   dichiara in una riga che la skill `pptx` non è disponibile e consegna il
   contenuto delle slide in Markdown strutturato.
