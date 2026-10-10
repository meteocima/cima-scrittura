# Dominio proposte: prove e note

Prompt di prova e note di sviluppo. Fuori dal plugin: non viene distribuito.

Il dominio si costruisce un ticket alla volta (issue #11). Questo file cresce
con lui: oggi c'e' solo la prima fetta.

## Skill e agenti

- `proposte-analisi-bando`: estrae la matrice del bando dal testo del topic.
- Previsti e non ancora scritti: `proposte-concept`, `proposte-scrittura`,
  `proposte-revisione`, `proposte-coerenza`, `proposte-risposta-esr`; agenti
  `proposte-valutatore`, `proposte-rapporteur`, `proposte-verificatore`.

Finche' non esistono, le skill che li nominano nei confini valgono come
indicazione di dove andra' la richiesta, e vale
`nucleo/vincoli.md` sezione 4: si consegna comunque, dicendo quali criteri
mancano.

## File condivisi tra le skill del dominio

Stanno in `plugin/condivisi/proposte/`. Regole in
`../scrivere-una-skill.md`, sezione "Riferimenti".

| File | Usato da |
|---|---|
| `matrice-bando.md` | `proposte-analisi-bando`, e tutte le skill del dominio quando esisteranno |
| `programma-horizon-europe.md` | `proposte-analisi-bando` |
| `programma-eic.md` | `proposte-analisi-bando` |
| `programma-interreg.md` | `proposte-analisi-bando` |

## Profili dei programmi

Un profilo di **valutazione** per programma, da non confondere con il profilo
di **reporting** dello stesso programma in `condivisi/progetti/`: stesso
programma, capitoli diversi (`adr/0020`).

Costruiti da fonti ufficiali con ricerca web, mai a memoria. Ogni profilo ha
in fondo la sezione "Che cosa questo profilo non dice". Aggiornarli almeno una
volta l'anno o quando cambia un template.

| Programma | Stato |
|---|---|
| Horizon Europe | fatto il 2026-10-10, su work programme 2026-2027 |
| EIC | fatto il 2026-10-10, su work programme 2026 (seconda modifica) |
| Interreg | fatto il 2026-10-10, su manuale e ToRs di Euro-MED |
| LIFE, UCPM/ECHO | issue #16 |

Due profili si leggono in modo diverso dagli altri, e la skill lo dice:
nell'**EIC** criteri e soglie cambiano con lo strumento (Pathfinder,
Transition, Accelerator), e in **Interreg** la griglia non sta nel profilo ne'
nel manuale del programma, ma nelle Terms of Reference della singola call. Il
profilo di Interreg contiene la griglia di una call documentata: serve a
sapere che forma ha, non si copia su un'altra call.

## Prompt di regressione

Da rifare quando si tocca il dominio. Dicono quale skill deve attivarsi.

| # | Prompt | Skill attesa |
|---|---|---|
| 1 | "Analizza questo topic" + file del topic | `proposte-analisi-bando` |
| 2 | "Su che cosa saremo valutati con questo bando?" | `proposte-analisi-bando` |
| 3 | "Quali sono i criteri di valutazione di questa call?" | `proposte-analisi-bando` |
| 4 | "What does this topic require from the consortium?" | `proposte-analisi-bando` |
| 5 | "Scrivi il work package 3" | `progetti-scrittura`, che fa la domanda sul Grant Agreement e passa la mano se siamo prima (issue #20) |

## Note di sviluppo

**Il topic prevale sul profilo.** E' la regola che tiene insieme il dominio:
il profilo e' una approssimazione del programma, il topic e' il testo contro
cui la proposta viene valutata. Ogni prova del dominio dovrebbe contenere
almeno una voce in cui le due fonti divergono, perche' e' li' che si vede se
la regola e' stata applicata o solo scritta.

**Niente numeri senza fonte.** Una soglia plausibile inventata e' il difetto
piu' pericoloso del dominio: non si vede, e fa scrivere la proposta contro un
bersaglio che non esiste. I segnaposto si vedono, quindi sono sempre meglio.
