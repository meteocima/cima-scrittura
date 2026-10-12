# 0.3.2: calibrazione del dominio proposte su ESR reali

Primo giro della issue #22. Da quattro proposte CIMA finanziate e dai loro
ESR nasce `plugin/condivisi/proposte/pattern-esr.md`: come i valutatori veri
etichettano le debolezze, quanto costa ciascuna nel punteggio, e 30 pattern
anonimi collegati ai tre criteri. Lo leggono `proposte-revisione` (e gli
agenti `proposte-valutatore`) e `proposte-risposta-esr`; la griglia vi rimanda
per tarare il punteggio; gli anti-pattern marcano [ESR] le voci confermate.

I materiali reali stanno in `materiali/proposte-esr/`, non versionati, con la
tabella di lavoro `calibrazione.md` da cui il file e' stato ricavato.

## Limite dichiarato

Le quattro proposte sono tutte sopra soglia (punteggi fra 4 e 5 su ogni
criterio). La calibrazione dice quindi che cosa costa mezzo punto in alto,
non che cosa porta sotto soglia. Il giro si completa con le proposte non
finanziate che l'utente fornira'.

## Controlli fatti qui

| Controllo | Esito |
|---|---|
| `python3 scripts/build.py --check` | 16 skill, 8 agenti, 0 avvisi (2026-10-12) |
| grep dei token sensibili (acronimi, partner, codici di call, numeri di proposta, cifre) su `plugin/`, `prove/`, `CHANGELOG.md` | zero risultati; la lista sta in `materiali/proposte-esr/token-sensibili.txt` |
| agente fresco che legge solo `pattern-esr.md` e prova a riconoscere i progetti | nessun progetto, partner o punteggio riconosciuto; indicate otto frasi che restringevano la ricerca (anni e tipi di azione, durata, pagine, un decimale insolito, il lessico di un programma), tutte generalizzate |

## Prove da fare nell'app

Con una proposta vera gia' valutata, in una cartella fuori dal repository.
Per non rovinare la prova cieca della issue #21, usare una proposta diversa
da quella che servira' li', oppure fare questa prova dopo.

| # | Ambiente | Richiesta | Esito atteso | Esito reale |
|---|---|---|---|---|
| 1 | Cowork, modalita' agenti | "Fammi una valutazione simulata di questa proposta" con proposta e topic | ogni rilievo dei tre rapporti porta un'etichetta (strength, minor shortcoming, shortcoming); nessun criterio scende a 3 per una sola shortcoming; i punti di forza nominano la caratteristica che li merita | |
| 2 | chat singola con lo zip di `proposte-revisione` | la stessa | come la 1, nel contesto principale e con la dichiarazione che la valutazione non e' indipendente | |
| 3 | Cowork | "Lavoriamo sull'ESR" con un ESR vero | per ogni rilievo l'etichetta letta nell'ESR e, se c'e', il pattern di `pattern-esr.md` che gli corrisponde | |
