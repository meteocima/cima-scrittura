# Una riscrittura è scrittura

`generale-revisione` non produce sempre un rapporto: su "migliora" o
"sistema" consegna un testo riscritto. Fino a oggi il revisore separato
restava facoltativo anche in quel caso, perché la regola guardava la
porta d'ingresso (revisione, non scrittura) invece di guardare chi ha
scritto il testo che si sta per inviare.

Risultato: lo stesso comunicato stampa aveva il revisore obbligatorio se
chiesto a `generale-scrittura` e facoltativo se chiesto a
`generale-revisione`, pur essendo in entrambi i casi uscito da quella
conversazione. Il pregiudizio dell'autore, che ADR 0005 vuole evitare,
era tornato senza che nessuna regola se ne accorgesse.

Da ora, quando una skill riscrive un testo, la nuova versione vale come
scritta lì: se il tipo di testo richiede il revisore separato, il
revisore è obbligatorio in modalità agenti, anche senza richiesta
dell'utente. Rapporto e correzione di refusi restano fuori: lì il testo
è ancora dell'utente.

Deciso il 2026-10-10.
