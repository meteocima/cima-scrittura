# cima-scrittura

Plugin di scrittura di Fondazione CIMA per Claude (Cowork e chat).

**Stato: in costruzione.** Sono pronti i domini generale, paper e progetti;
manca proposte. Fino al rilascio resta in uso `cima-writing-style`.

## Cosa fa

- **Generale**: email, lettere, comunicati, verbali, report interni, testi web.
- **Paper**: articoli scientifici, abstract, cover letter, risposta ai
  revisori, peer review simulata prima della sottomissione.
- **Proposte**: analisi del bando, concept, scrittura della proposta,
  valutazione simulata con tre valutatori e rapporteur, controllo di
  coerenza, risposta agli ESR.
- **Progetti**: deliverable, report periodici e technical report di
  progetti già finanziati, revisione dal punto di vista di project
  officer e reviewer.

Tutti i domini condividono le stesse regole: niente dati inventati
(segnaposto `[…]` dove manca un'informazione), verifica di ogni fonte
citata, controllo degli anti-pattern della scrittura generata.

In Cowork la revisione viene fatta da agenti separati che non vedono la
conversazione di scrittura, così il giudizio non è condizionato dalle
intenzioni dell'autore. In chat la revisione è dichiarata come non
indipendente e il plugin prepara un testo da incollare in una
conversazione nuova.

## Per chi sviluppa

Il punto d'ingresso è `CLAUDE.md`, che rimanda al resto. Build e validazione:

```
python3 scripts/build.py --check   # valida
python3 scripts/build.py           # crea dist/cima-scrittura.plugin
```

ESR, proposte e manoscritti riservati vanno in `materiali/`, che non è
versionato. Non vanno mai nel repository.
