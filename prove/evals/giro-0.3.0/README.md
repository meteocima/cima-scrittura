# Giro 0.3.0 come casi eval

Le righe di `prove/0.3.0-dominio-proposte/README.md` che si possono misurare
in cieco. Come si esegue la suite: `prove/README.md`, sezione "La suite
automatica".

## Casi

| Riga | Caso | Che cosa misura | Serve |
|---|---|---|---|
| 2 | `01-matrice-senza-file` | la matrice segue il topic dove scavalca il profilo, nessun numero senza fonte, consegna completa nel messaggio | |
| 1 | `02-matrice-file` | con `Write`: la matrice finisce in un file e il messaggio ne porta la sintesi | Write |
| 5 | `03-profilo-eic` | riconosce lo strumento EIC e prende dal profilo soglie, pesi e limite che la call non dice | |
| 6 | `04-profilo-interreg` | non copia su una call la griglia di un'altra call che sta nel profilo | |
| 8 | `05-profilo-life` | quattro criteri da 20 punti, peso 1,5 su Impact dentro la soglia, 120 pagine | |
| 9 | `06-profilo-ucpm` | punteggi legati alle caselle numerate della Part B, doppia soglia | |
| 11 | `07-impact-senza-file` | sezione Impact senza dati: tutto a segnaposto, KPI con baseline, outcome alla lettera | |
| 12 | `08-impact-modulo` | il testo torna dentro il file del modulo, con le sezioni non richieste intatte | Write |
| 14 | `09-concept-senza-file` | quattro blocchi, partner come ruoli a segnaposto, tabella di copertura | |
| 17 | `10-valutazione-agenti` | tre `proposte-valutatore` e il `proposte-rapporteur` lanciati davvero, difetti trovati, punteggi con scala e soglie | Write |
| 18 | `11-valutazione-senza-file` | senza poter salvare file: consegna completa, dichiarazione veritiera dell'indipendenza, stessi punteggi e soglie | |
| 21 | `12-risposta-esr` | ogni rilievo dell'ESR ha la sua riga con la posizione, nessuna modifica dichiarata che non esiste | |
| 24 | `13-coerenza` | `proposte-verificatore` lanciato, incoerenze riportate in coppia, limite preso dal bando, nessun punteggio | Write |

## Due cose imparate il 2026-10-10, che cambiano come si scrivono i casi

### Il materiale non deve insegnare la risposta

I file in `prove/0.3.0-dominio-proposte/materiali/` portavano in testa
l'elenco dei tranelli che contenevano ("tre divergenze volute", "sei difetti
piantati"). Una sessione misurata lo ha fatto notare da sola: aveva letto
quali difetti doveva trovare, quindi trovarli non dimostrava niente.

Ora il materiale dice solo di essere inventato, e che cosa si misura sta nel
`nota.md` del caso, che la sessione figlia non vede. La suite e' stata
rieseguita da capo dopo la correzione: alcuni casi che prima davano 1.00 sono
scesi, e quelli sono i numeri che contano.

### `allowed_tools` non toglie i subagent

Un caso con `allowed_tools: [Read, Glob, Grep, Skill]` **puo' lo stesso**
lanciare `Agent` e `Task`: la concessione governa gli strumenti protetti
(`Write`, `Bash`, `Edit`, `WebFetch`, MCP), non i subagent. Misurato sul caso
11, che in due esecuzioni su tre ha lanciato i tre valutatori.

Conseguenza: **la modalita' chat non si misura da qui**. Togliere `Write`
misura che cosa succede quando non si possono salvare file, che e' un'altra
cosa. I casi si chiamano `-senza-file` per questo. La modalita' chat vera,
cioe' l'assenza dei subagent, resta una prova a mano con lo zip della skill
caricato in una conversazione.

Dove il comportamento legittimo puo' essere doppio, i grader non premiano una
strada: chiedono che la consegna sia completa e che **dichiari il vero** su
quanto e' indipendente.

## Costi misurati il 2026-10-10

Casi di solo instradamento: da 0,15 a 0,19 dollari. Casi di contenuto senza
agenti: da 0,41 a 0,88. I due casi di valutazione: da 2,4 a 2,9, perche'
lanciano tre valutatori e un rapporteur. La suite del giro, undici casi con
`--runs 1`, costa circa 11 dollari.
