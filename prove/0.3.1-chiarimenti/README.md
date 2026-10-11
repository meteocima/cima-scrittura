# 0.3.1: caricare la skill prima di chiedere chiarimenti

Otto descrizioni dicono di caricare la skill prima di chiedere chiarimenti,
come quella di `progetti-scrittura` dopo la issue #35 (issue #36,
`docs/adr/0023`). La 0.3.1 e' uscita il 2026-10-11 **senza** queste prove,
per scelta: si fanno dopo, con calma.

Le prove si fanno solo in Cowork con Sonnet, perche' in Claude Code il
difetto non si vede: alle sessioni dell'eval il riquadro delle domande non e'
offerto. Ogni riga: cinque conversazioni nuove, solo la frase indicata,
contare in quante si attiva la skill. Passa con quattro su cinque o piu'.
Se una skill resta sotto, la frase si toglie dalla sua descrizione
(`adr/0023`).

Prima di cominciare: reinstallare il plugin, chiudere e riaprire Cowork.

| # | Skill | Frase | Esito atteso | Esito reale |
|---|---|---|---|---|
| 1 | `generale-scrittura` | "Scrivi una email al Comune" | si attiva la skill | |
| 2 | `generale-presentazione` | "Prepara le slide per il kickoff del progetto" | si attiva la skill | |
| 3 | `paper-scrittura` | "Mi serve un abstract per EGU" | si attiva la skill | |
| 4 | `paper-risposta-revisori` | "Dobbiamo rispondere ai revisori" | si attiva la skill | |
| 5 | `proposte-scrittura` | "Scrivi la sezione Impact della proposta" | si attiva la skill | |
| 6 | `proposte-concept` | "Mi serve un concept da mandare ai partner" | si attiva la skill | |
| 7 | `proposte-analisi-bando` | "Su che cosa saremo valutati in questo bando?" | si attiva la skill | |
| 8 | `progetti-risposta-review` | "Il project officer ha respinto il deliverable" | si attiva la skill | |
| 9 | `progetti-scrittura`, poi `proposte-scrittura` | "Scrivi il work package 3", e alla domanda "stiamo scrivendo una proposta" | il secondo turno passa a `proposte-scrittura`: e' la riga 29 della 0.3.0, mai provata con Sonnet al secondo turno | |

## Gia' misurato prima del rilascio

`prove/evals/instradamento/` in Claude Code con `--model sonnet`, il
2026-10-11, dopo la modifica: controlla che l'instradamento non si sia rotto,
non l'effetto in Cowork. Esito nella sezione qui sotto.

| Giro | Esito | Costo |
|---|---|---|
| dieci casi, `--runs 1`, `--model sonnet` | 10 su 10 | 1,11 dollari |
