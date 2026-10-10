# Giro 0.3.0 come casi eval

Le righe di `prove/0.3.0-dominio-proposte/README.md` che si possono misurare
in cieco. Come si esegue la suite: `prove/README.md`, sezione "La suite
automatica".

## Casi

| Riga | Caso | Che cosa misura | Serve |
|---|---|---|---|
| 2 | `01-matrice-chat` | senza subagent e senza `Write`: `proposte-analisi-bando` si attiva da sola, la matrice arriva **intera nel messaggio**, segue il topic dove scavalca il profilo, nessun numero senza fonte | |
| 1 | `02-matrice-file` | con `Write`: la matrice finisce in un file e il messaggio ne porta la sintesi, con gli stessi vincoli sulle fonti | Write |

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
