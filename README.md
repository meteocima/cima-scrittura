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

Il plugin funziona in due ambienti, e sceglie da solo come comportarsi
guardando gli strumenti che ha, senza chiedere niente.

- Dove può lanciare agenti separati (Cowork, Claude Code), la revisione la fa
  un contesto che non ha visto nascere il testo: il giudizio non è
  condizionato dalle intenzioni di chi ha scritto.
- In chat, dove gli agenti non ci sono, ogni passaggio viene svolto lo stesso
  e il risultato arriva completo. La revisione però viene dallo stesso
  contesto che ha scritto, e il plugin lo dichiara: per i testi che contano
  prepara un blocco da incollare in una conversazione nuova, per avere
  comunque un parere indipendente.

Stesso prodotto, quindi, con una garanzia diversa. Ogni aggiornamento del
plugin si prova in tutti e due gli ambienti prima di uscire (`prove/`).

Il plugin lavora sui documenti nel formato in cui arrivano: legge un Word, un
PowerPoint o un PDF e restituisce lo stesso formato, rispetta i template
imposti e può riconsegnare un testo rivisto con le modifiche tracciate.

## Per chi sviluppa

Il punto d'ingresso è `CLAUDE.md`, che rimanda al resto. Build e validazione:

```
python3 scripts/build.py --check   # valida
python3 scripts/build.py           # crea dist/cima-scrittura.plugin
```

ESR, proposte e manoscritti riservati vanno in `materiali/`, che non è
versionato. Non vanno mai nel repository.
