# 0.3.0: il dominio proposte

Il quarto dominio, costruito un ticket alla volta (issue #11). Questa cartella
raccoglie le prove di tutto il giro: ogni ticket aggiunge le proprie righe
qui, invece di aprire una cartella propria.

I materiali in `materiali/` sono finti. Il topic di prova e' costruito con tre
divergenze volute rispetto al profilo del programma (soglia di Impact a 4,
limite di 30 pagine, pesi non dichiarati), per misurare la regola che tiene
insieme il dominio: il testo del bando prevale sul profilo.

## Analisi del bando (issue #12)

Skill `proposte-analisi-bando`, file condivisi `matrice-bando.md` e
`programma-horizon-europe.md` (profilo di valutazione).

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 1 | agenti | "Analizza questo topic" + `materiali/topic-finto.md` | Si attiva `proposte-analisi-bando`. Matrice salvata in un file della cartella di lavoro; nel messaggio la sintesi con gli scavalcamenti, i requisiti obbligatori e le voci `[da bando]`. Soglia Impact 4 e limite 30 pagine presi dal topic. Pesi non dichiarati dal topic: marcati come profilo, mai inventati | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/02-matrice-file` (punteggio 1.00, tre grader su tre). La matrice e' finita in un file, la sintesi nel messaggio, la soglia 4 e le 30 pagine vengono dal topic con lo scavalcamento dichiarato |
| 2 | chat | Stesso prompt, senza strumento per i subagent e senza possibilita' di salvare file | Stessa matrice **per intero nel messaggio**; nessuna richiesta di cambiare ambiente; consegna completa | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/01-matrice-chat` (punteggio 1.00, quattro grader su quattro). La sessione dichiara in una riga che non puo' salvare file e consegna la matrice intera |
| 2b | chat | Stesso prompt con lo zip della skill caricato in una conversazione claude.ai, allegando il topic invece di metterlo su disco | Come la riga 2, piu': il topic allegato viene letto senza chiedere di incollarlo | Da fare a mano. Il caso automatico misura la consegna senza subagent, non come il materiale arriva in una conversazione vera |
| 3 | agenti | "Su che cosa saremo valutati per il topic HORIZON-CL3-2026-DRS-01-99?" senza allegare il testo | Si attiva la skill, che chiede il testo del topic in un messaggio solo e intanto costruisce la matrice dal solo profilo, con ogni riga marcata `[profilo]` | Da fare a mano |
| 4 | agenti | "Analizza questo topic" + un topic di un programma senza profilo (per esempio un bando LIFE) | Costruisce la matrice dal solo testo del topic e dichiara in una riga che le regole generali del programma non sono state applicate, come prevede `nucleo/vincoli.md` sezione 4 | Da fare a mano |

### Misurato in automatico

Casi in `prove/evals/`, eseguiti con `claude plugin eval` su sessioni figlie
che non hanno letto gli esiti attesi. Comando e opzioni: `prove/README.md`,
sezione "La suite automatica".

| Caso | Che cosa misura | Esito del 2026-10-10 |
|---|---|---|
| `instradamento/09-analisi-bando` | la skill si attiva da sola su una richiesta che nomina un topic e chiede i criteri | **1.00**, 0,19 dollari |
| `giro-0.3.0/01-matrice-chat` | senza subagent e senza `Write`: skill attivata, matrice intera nel messaggio, nessun numero senza fonte, consegna completa | **1.00**, 0,60 dollari |
| `giro-0.3.0/02-matrice-file` | con `Write`: matrice nel file, sintesi nel messaggio, nessun numero senza fonte | **1.00**, 0,52 dollari |

### Che cosa e' cambiato mentre si provava

Il caso `01-matrice-chat` era stato scritto con `Write` fra gli strumenti, e
la sessione ha salvato la matrice su file: il giudice, che vede solo la
risposta, ha letto un riassunto e ha dato FAIL. Il difetto era doppio.

- Nella prova: una sessione che puo' scrivere file non misura la consegna in
  chat. Tolto `Write`, il caso misura quello che dice di misurare.
- Nella skill: `SKILL.md` legava il file alla **modalita'**, che invece
  dipende dai subagent. Il file dipende da un'altra cosa, cioe' se si possono
  scrivere file. Le due condizioni erano confuse in una riga sola, ora sono
  separate.

La riga vecchia resta qui perche' e' la memoria di che cosa si rompe
facilmente: in questo dominio la domanda "che cosa vede chi giudica" vale
anche per i grader, non solo per i valutatori.

## Esito

Da riempire a fine giro: data, ambienti provati, che cosa e' stato corretto
prima di rilasciare.

Analisi del bando (#12): chiusa il 2026-10-10. Tre casi automatici verdi, tre
righe manuali ancora da fare (2b, 3, 4).
