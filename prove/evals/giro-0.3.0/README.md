# Giro 0.3.0 come casi eval

Le righe di `prove/0.3.0-dominio-proposte/README.md` che si possono misurare
in cieco. Come si esegue la suite: `prove/README.md`, sezione "La suite
automatica".

## Casi

| Riga | Caso | Che cosa misura | Serve |
|---|---|---|---|
| 2 | `01-matrice-chat` | senza subagent e senza `Write`: `proposte-analisi-bando` si attiva da sola, la matrice arriva **intera nel messaggio**, segue il topic dove scavalca il profilo, nessun numero senza fonte | |
| 1 | `02-matrice-file` | con `Write`: la matrice finisce in un file e il messaggio ne porta la sintesi, con gli stessi vincoli sulle fonti | Write |
| 5 | `03-profilo-eic` | riconosce lo strumento EIC e prende dal profilo soglie, pesi e limite di pagine che la call non dice | |
| 6 | `04-profilo-interreg` | non copia su una call la griglia di un'altra call che sta nel profilo | |
| 8 | `05-profilo-life` | quattro criteri da 20 punti, peso 1,5 su Impact dentro la soglia, 120 pagine | |
| 9 | `06-profilo-ucpm` | punteggi legati alle caselle numerate della Part B, doppia soglia | |
| 11 | `07-impact-chat` | sezione Impact senza dati: tutto a segnaposto, KPI con baseline, outcome alla lettera | |
| 12 | `08-impact-modulo` | il testo torna dentro il file del modulo, con le sezioni non richieste intatte | Write |

I due casi sono la stessa richiesta con gli strumenti diversi, e hanno esito
atteso diverso apposta: e' li' che si vede se la skill distingue "non posso
lanciare subagent" da "non posso salvare file". Se i due esiti attesi fossero
uguali, la coppia non starebbe guardando la differenza che conta.

`01-matrice-chat` misura la **modalita' chat** senza bisogno di una persona in
chat: `allowed_tools` non contiene ne' `Agent` ne' `Task`, che e' il modo in
cui il protocollo definisce la modalita'
(`nucleo/protocollo-revisione.md`, sezione 1). Non sostituisce la prova a mano
dove quello che si guarda e' come un file arriva davvero a chi legge.

L'instradamento del dominio sta con gli altri, in
`prove/evals/instradamento/09-analisi-bando`.
