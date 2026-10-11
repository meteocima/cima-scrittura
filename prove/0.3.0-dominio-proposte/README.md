# 0.3.0: il dominio proposte

Il quarto dominio, costruito un ticket alla volta (issue #11). Questa cartella
raccoglie le prove di tutto il giro: ogni ticket aggiunge le proprie righe
qui, invece di aprire una cartella propria.

I materiali in `materiali/` sono finti, e **non dichiarano piu' i propri
tranelli**: che cosa misura ciascun caso sta nel suo `nota.md`, che la
sessione misurata non vede. Fino al 2026-10-10 lo dichiaravano, e una sessione
misurata ha fatto notare che cosi' trovare i difetti non dimostrava niente.

**Avvertenza sui numeri delle sezioni #12, #15, #16, #14 e #13.** Quelle
misure sono state prese con i materiali che dichiaravano i tranelli: valgono
meno di quanto sembrano. La suite e' stata rieseguita da capo con i materiali
puliti il 2026-10-10, e gli esiti della riesecuzione sono nella sezione
"Riesecuzione con i materiali puliti" in fondo.

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

## Concept (issue #13)

Skill `proposte-concept`.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 14 | chat | Un'idea in due righe piu' `materiali/topic-finto.md`, senza partner ne' numeri | Concept con i quattro blocchi (problema, approccio, consorzio, impatto), partner mancanti come ruoli a segnaposto, tabella di copertura dei criteri del bando, e in fondo che cosa manca per diventare una proposta | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/09-concept-chat` (1.00) |
| 15 | agenti | "Prima di buttarci, mi serve un concept da mandare ai partner per questo bando" | Si attiva `proposte-concept`, non `proposte-scrittura` | **Passa**, misurato dal caso `instradamento/10-concept` (1.00) |
| 16 | agenti | "Scrivi la concept note per la prima fase di questa call in due fasi" | Passa la mano a `proposte-scrittura`: quella concept note e' un testo che il programma valuta con la sua griglia, non uno strumento di lavoro del consorzio | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `instradamento/10-concept` | **1.00**, 0,15 dollari |
| `giro-0.3.0/09-concept-chat` | **1.00**, 0,73 dollari |

## Valutazione simulata (issue #17)

Skill `proposte-revisione`, agenti `proposte-valutatore` e
`proposte-rapporteur`, file condivisi `griglia-valutazione.md` e
`profili-valutatori.md`.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 17 | agenti | "Fammi una valutazione simulata di questa proposta" + `materiali/proposta-finta.md` e `materiali/topic-finto.md` | Tre `proposte-valutatore` lanciati in parallelo e poi il `proposte-rapporteur`. Punteggi con la scala, verdetto sulle soglie con la soglia di Impact a 4 presa dal topic, divergenze senza media, correzioni per impatto | **Passa**, misurato in cieco il 2026-10-10 dal caso `giro-0.3.0/10-valutazione-agenti` (1.00). Verificato nella traccia anche il contenuto dei prompt ai valutatori: percorsi, profilo e griglia, nessun riassunto della conversazione, nessuna intenzione di chi ha scritto, nessun punteggio atteso |
| 18 | senza file | Stesso prompt, senza poter salvare file | Consegna completa nel messaggio, dichiarazione veritiera di quanto e' indipendente, stessi punteggi e soglie | **Passa in parte.** Difetti trovati e punteggi: verdi, tre volte su tre. Consegna: instabile, perche' in due esecuzioni su tre la sessione ha lanciato comunque i valutatori e poi ha **offerto** i tre rapporti invece di consegnarli. Corretta la skill; la domanda piu' grossa, se il nucleo debba ammettere gli agenti senza file, e' la issue #29 |
| 19 | agenti | Valutazione di una proposta senza fornire il bando | Nessun punteggio: la consegna dice che senza griglia reale non si danno numeri, ed elenca che cosa servirebbe | Da fare a mano |
| 20 | agenti | Valutazione di una proposta fatta quasi tutta di segnaposto | Nessun punteggio, e i problemi che gia' si vedono segnalati lo stesso | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `giro-0.3.0/10-valutazione-agenti` | **1.00**, 2,69 dollari |
| `giro-0.3.0/11-valutazione-senza-file` | **0,75**, 2,86 dollari: verde su difetti e punteggi, instabile sulla consegna |

## Riesecuzione con i materiali puliti

Il 2026-10-10, tolte dai materiali le righe che dichiaravano i tranelli, la
suite del giro e' stata rieseguita da capo (undici casi, `--runs 1`, 11,09
dollari). Gli esiti sono scesi in quattro casi.

| Caso | Con i tranelli dichiarati | Materiali puliti |
|---|---|---|
| `01-matrice-senza-file` | 1.00 | 0,75, poi 1.00 alla riesecuzione |
| `02-matrice-file` | 1.00 | 1.00 |
| `03-profilo-eic` | 1.00 | 1.00 |
| `04-profilo-interreg` | 1.00 | 1.00 |
| `05-profilo-life` | 1.00 | 0,50, poi 1.00 due volte su due |
| `06-profilo-ucpm` | 1.00 | 1.00 |
| `07-impact-senza-file` | 1.00 | 1.00 |
| `08-impact-modulo` | 1.00 | 1.00 |
| `09-concept-senza-file` | 1.00 | 1.00 |

Le due righe scese e poi risalite dicono una cosa che vale per tutta la
suite: **un'esecuzione sola non e' una misura**. Dove il verdetto conta,
servono almeno due esecuzioni, e il default di `claude plugin eval` e' tre
apposta.

## Risposta all'ESR (issue #18)

Skill `proposte-risposta-esr` e il suo `formato-risposta-esr.md`.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 21 | senza file | "Ci hanno bocciato. Rispondiamo all'ESR" + `materiali/esr-finto.md` e `materiali/proposta-finta.md` | Ogni rilievo dell'ESR ha la sua riga, con posizione e motivo; le modifiche non fatte sono dichiarate tali; una riga dice che a un ESR non si replica e che serve a rifare la proposta | **Passa**, due volte su due il 2026-10-10, dal caso `giro-0.3.0/12-risposta-esr` (1.00) |
| 22 | agenti | Stesso prompt, con l'ESR in PDF | Legge il PDF senza chiedere di incollarlo, e nessuna frase dell'ESR finisce in una ricerca web | Da fare a mano |
| 23 | agenti | "Contestiamo il punteggio" | Indirizza all'evaluation review dicendo che riguarda solo gli aspetti procedurali, non il merito | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `giro-0.3.0/12-risposta-esr` | **1.00** su due esecuzioni, 1,46 dollari in tutto |

## Coerenza e limiti (issue #19)

Skill `proposte-coerenza` e agente `proposte-verificatore`.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 24 | agenti | "Consegniamo domani. Controlla la coerenza e se stiamo nei limiti" + `materiali/proposta-finta.md` e `materiali/topic-finto.md` | Lancia il `proposte-verificatore`. Incoerenze riportate **in coppia**, con tutti e due i passaggi; limite di 30 pagine preso dal bando e non dal profilo; nessun punteggio | **Passa**, due volte su due il 2026-10-10, dal caso `giro-0.3.0/13-coerenza` (1.00) |
| 25 | senza file | Stesso prompt | Stesso rapporto nel messaggio, con dichiarato che il controllo non e' indipendente | Da fare a mano |
| 26 | agenti | "Controlla la coerenza" senza fornire il bando | I limiti restano `[da bando]` e non vengono stimati; le incoerenze interne si cercano lo stesso | Da fare a mano |

### Misurato in automatico

| Caso | Esito del 2026-10-10 |
|---|---|
| `giro-0.3.0/13-coerenza` | **1.00** su due esecuzioni, 1,37 dollari in tutto |

## Il dominio prende le sue richieste (issue #20)

Non una skill nuova: il giro che fa esistere il dominio per chi scrive.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 27 | agenti | "Scrivi il work package 3" | Si attiva una skill (prima non se ne attivava nessuna, `adr/0020`): `progetti-scrittura` rivendica il mezzo ambiguo e fa la domanda sola sul Grant Agreement | **Passa**, due volte su due il 2026-10-10, dal caso `instradamento/01-work-package` |
| 28 | agenti | "Draft the impact section" | Come sopra | **Passa**, due volte su due, dal caso `instradamento/06-impact-section` |
| 29 | agenti | Stessa frase, e alla domanda si risponde "stiamo scrivendo una proposta" | `progetti-scrittura` passa la mano a `proposte-scrittura` invece di scrivere con i criteri mancanti | Da fare a mano: serve il secondo turno della conversazione |

### Che cosa e' cambiato nei documenti

- `nucleo/vincoli.md` sezione 4 non nomina piu' `proposte` come dominio non
  scritto. La regola resta per le skill non installate, che e' il caso vero in
  chat.
- `docs/instradamento.md` ha una riga per ciascuna delle sei skill del
  dominio, e non dice piu' che il dominio non esiste.
- `progetti-scrittura` passa la mano invece di scrivere senza criteri.
- `docs/proposte.md` cancellato: da qui in avanti la fonte di verita' sono le
  skill, come per gli altri tre domini.
- `CLAUDE.md`: quattro domini scritti, e i conteggi del `--check` aggiornati.

## Senza file (issue #29)

Il nucleo ammette la revisione con agenti anche dove non si possono salvare
file, a tre condizioni (`nucleo/protocollo-revisione.md`, sezione 3, "Senza
file"; `docs/adr/0021`). Misurato con il caso
`giro-0.3.0/11-valutazione-senza-file`, due esecuzioni per giro.

| Giro | Esito | Che cosa si e' visto |
|---|---|---|
| 2026-10-11, primo | **1.00**, 6,34 dollari | Tutte e due le esecuzioni lanciano tre valutatori e il rapporteur e dichiarano la strada. Ma la seconda chiude con "te li incollo per intero, uno per messaggio" e il turno finisce: i rapporti non arrivano. Il grader non lo vedeva, perche' accettava il consolidato con i punteggi di ciascuno. La frase del nucleo "uno per messaggio se lunghi" invitava a rimandare. Corretti nucleo, skill e grader |
| 2026-10-11, secondo | **1.00**, 7,48 dollari | Grader piu' severo. Consegne di 52.000 e 29.000 caratteri con i tre rapporti per intero, nessuna promessa per dopo |

Controllato a mano nelle tracce del secondo giro (conservate con
`--keep-temp`): proposta e topic, che erano gia' file leggibili, passano per
percorso; nel prompt va solo la matrice costruita dalla skill, per intero e fra
delimitatori; nessun riassunto della conversazione, nessuna indicazione su
che cosa guardare.

Resta un residuo: in un'esecuzione su due la sessione ha passato al
rapporteur i rapporti "in forma ridotta", senza i commenti in stile ESR, e lo
ha dichiarato. Non e' un riassunto ma e' un taglio, contro la condizione 2.
Da riguardare se ricompare.

Il controllo sui prompt resta manuale: nessuna documentazione dice che un
grader `llm` possa leggere la traccia. Una pista: nei risultati i grader `llm`
hanno un campo `config.focus`, che vale `last_message`; se accetta `trace`,
il controllo diventa automatico. Non verificato.

## Esito

**Il giro non e' finito.** Le sei skill e i tre agenti del dominio sono
scritti e misurati in cieco, ma la 0.3.0 non si rilascia finche' non sono
state fatte le righe manuali: sono quelle dove conta come il risultato arriva
davvero a chi legge, e un caso automatico non le vede.

Da fare prima del rilascio:

- le righe manuali di ciascuna sezione qui sopra (2b, 3, 4, 7, 10, 13, 16, 19,
  20, 22, 23, 25, 26, 29);
- le righe non eseguite del giro 0.2.0 (issue #6 e #7), che si chiudono dentro
  questo rilascio.

Analisi del bando (#12): chiusa il 2026-10-10. Tre casi automatici verdi, tre
righe manuali ancora da fare (2b, 3, 4).

Profili EIC e Interreg (#15): chiusa il 2026-10-10. Due casi automatici verdi,
una riga manuale da fare (7).

Profili LIFE e UCPM/ECHO (#16): chiusa il 2026-10-10. Due casi automatici
verdi, una riga manuale da fare (10).

Scrittura della proposta (#14): chiusa il 2026-10-10. Due casi automatici
verdi, una riga manuale da fare (13).

Concept (#13): chiusa il 2026-10-10. Due casi automatici verdi, una riga
manuale da fare (16).

Il dominio prende le sue richieste (#20): chiusa il 2026-10-10. Le due frasi
ambigue dell'`adr/0020` ora attivano una skill, due volte su due.

Coerenza e limiti (#19): chiusa il 2026-10-10. Un caso automatico verde due
volte su due, due righe manuali da fare (25, 26).

Risposta all'ESR (#18): chiusa il 2026-10-10. Un caso automatico verde due
volte su due, due righe manuali da fare (22, 23).

Valutazione simulata (#17): chiusa il 2026-10-10. Il caso con i file e' verde,
quello senza file e' verde su difetti e punteggi e instabile sulla consegna
(issue #29). Due righe manuali da fare (19, 20).

Senza file (#29): decisa il 2026-10-11 con l'`adr/0021`. Il caso 11 verde due
volte su due con il grader piu' severo; un residuo sul rapporteur annotato
sopra.
