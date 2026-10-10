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

## Profili EIC e Interreg (issue #15)

File condivisi `programma-eic.md` e `programma-interreg.md`, piu' la tabella
dei programmi dentro `proposte-analisi-bando`.

I due profili non si usano come quello di Horizon Europe, e le prove guardano
proprio quello: nell'EIC decide lo **strumento**, in Interreg la griglia non
sta nel profilo ma nelle **Terms of Reference della call**.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 5 | chat | "Analizza questa call" + `materiali/call-eic-finta.md`, che non dice criteri ne' soglie | Riconosce lo strumento (Pathfinder Open) e prende dal profilo soglie 4 / 3,5 / 3, pesi 50 / 30 / 20 e limite di 22 pagine, marcati come profilo. Se escono le soglie generali di Horizon Europe, ha caricato il profilo sbagliato | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/03-profilo-eic` (1.00, due grader su due piu' l'attivazione) |
| 6 | chat | "Analizza questa call" + `materiali/call-interreg-finta.md`, che rimanda agli allegati delle ToRs | Non copia la griglia dell'altra call che sta nel profilo: criteri, pesi e soglia restano `[da bando]`, con detto che stanno nell'Annex III delle ToRs, e chiede quei documenti. Le due condizioni di partecipazione finiscono fra i requisiti di eleggibilita' | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/04-profilo-interreg` (1.00, due grader su due piu' l'attivazione). La consegna nomina la griglia di EURO-MED06 e dichiara di non applicarla perche' e' di un'altra call e di un altro tipo di progetto |
| 7 | agenti | "Analizza questa call" + `materiali/call-eic-finta.md` senza dire lo strumento, con il testo che non lo rende ovvio | Chiede quale strumento EIC, invece di applicare il profilo a caso | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `giro-0.3.0/03-profilo-eic` | **1.00**, 0,69 dollari |
| `giro-0.3.0/04-profilo-interreg` | **1.00**, 0,46 dollari |

## Profili LIFE e UCPM/ECHO (issue #16)

File condivisi `programma-life.md` e `programma-ucpm.md`. Sono i due programmi
piu' lontani dal modello Horizon: LIFE valuta su **quattro** criteri da 20
punti con il peso su Impact che entra nella soglia, UCPM lega ogni
sotto-criterio a una **casella numerata** della Part B con i suoi punti.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 8 | chat | "Analizza questa call" + `materiali/call-life-finta.md`, che non dice criteri ne' soglie | Quattro criteri 0-20, soglia 10 per criterio e 55 complessiva, peso 1,5 su Impact con la soglia calcolata dopo la pesatura, limite di 120 pagine | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/05-profilo-life` (1.00) |
| 9 | chat | "Analizza questa call" + `materiali/call-ucpm-finta.md` | Relevance 40, Quality 30, Impact 30 su 100, soglie 20/15/15 piu' la complessiva 65 come doppia condizione, sotto-criteri legati alle caselle della Part B, limite di 50 pagine | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/06-profilo-ucpm` (1.00) |
| 10 | agenti | "Analizza questa call" + una call LIFE in due fasi | Riconosce che alla prima fase si invia una concept note e che alcune sezioni non si compilano, invece di chiedere la proposta intera | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `giro-0.3.0/05-profilo-life` | **1.00**, 0,41 dollari |
| `giro-0.3.0/06-profilo-ucpm` | **1.00**, 0,55 dollari |

## Scrittura della proposta (issue #14)

Skill `proposte-scrittura` e file condiviso `anti-pattern-proposte.md`.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 11 | chat | "Scrivi la sezione Impact della proposta per questo topic" + `materiali/topic-finto.md`, senza dare partner ne' numeri | Testo completo della sezione, con ogni dato mancante a segnaposto e l'elenco dei segnaposto in fondo. KPI con baseline o segnaposto al posto della baseline. Almeno un expected outcome richiamato alla lettera | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/07-impact-chat` (1.00) |
| 12 | agenti | Stesso prompt piu' `materiali/modulo-parte-b-finto.md` | Il testo torna **dentro** il file del modulo: sezioni e numerazione intatte, comprese quelle non richieste, tabella 2.3 compilata con segnaposto invece che cancellata | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/08-impact-modulo` (1.00). Controllato anche il file prodotto, non solo la risposta: 219 righe, intestazioni e sezione 3 intatte, 102 segnaposto, outcomes del bando copiati alla lettera nella tabella |
| 13 | agenti | "Scrivi la sezione Impact" con il budget gia' deciso dall'utente e la richiesta di calcolare i mesi-persona | Dice in una riga che il budget come numeri e' fuori ambito e scrive la narrativa | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `giro-0.3.0/07-impact-chat` | **1.00**, 0,61 dollari |
| `giro-0.3.0/08-impact-modulo` | **1.00**, 0,61 dollari |

## Esito

Da riempire a fine giro: data, ambienti provati, che cosa e' stato corretto
prima di rilasciare.

Analisi del bando (#12): chiusa il 2026-10-10. Tre casi automatici verdi, tre
righe manuali ancora da fare (2b, 3, 4).

Profili EIC e Interreg (#15): chiusa il 2026-10-10. Due casi automatici verdi,
una riga manuale da fare (7).

Profili LIFE e UCPM/ECHO (#16): chiusa il 2026-10-10. Due casi automatici
verdi, una riga manuale da fare (10).

Scrittura della proposta (#14): chiusa il 2026-10-10. Due casi automatici
verdi, una riga manuale da fare (13).
