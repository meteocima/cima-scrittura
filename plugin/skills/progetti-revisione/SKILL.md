---
name: progetti-revisione
description: "Rivede un testo di un progetto già finanziato (deliverable, parte tecnica di periodic o final report, technical report, executive summary) come lo leggerebbero il project officer e un reviewer tecnico esterno: aderenza alla DoA, risultati dimostrati e non solo dichiarati, scostamenti spiegati, KPI con valore misurato. Produce un rapporto con punteggi, problemi citati e correzioni ordinate. Usare per: 'rivedi il deliverable', 'controlla il periodic report', 'passerebbe la review?', 'review this deliverable', 'check our technical report before submission', 'simulate the project review'. Non usare per: valutazione simulata di una proposta o di un ESR (proposte-*); peer review di un articolo (paper-*); rilettura di email, lettere o comunicati (generale-*); scrivere un testo di progetto da zero (progetti-scrittura); rispondere a commenti già ricevuti (progetti-risposta-review)."
---

# Revisione di testi di progetto

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.

Poi leggere `references/griglia-revisione.md` e
`references/anti-pattern-progetti.md`.

## Ambito

Revisione simulata di un testo di progetto scritto dall'utente o dal
consorzio, prima dell'invio. Livello di revisione: standard (due
profili più sintesi). Il risultato è un rapporto, non una riscrittura:
la skill riscrive solo se l'utente lo chiede, e in quel caso
consegna anche il testo rivisto.

Se il testo è una proposta, un paper o un testo istituzionale breve,
dirlo in una riga e indicare la skill del dominio giusto.

## Materiali

- Testo da rivedere (file o testo incollato).
- DoA o Grant Agreement, oppure una matrice DoA già costruita.
- Template del programma o del consorzio, se c'è.
- Programma e periodo; review report o raccomandazioni precedenti, se
  il report deve darne conto.

Senza DoA la revisione si fa, ma i criteri A1 e la tabella
"Tracciabilità" diventano "non verificabili" e la sintesi lo dice.

## Procedura

1. **Inquadrare**: tipo di testo, programma, periodo. Leggere il
   profilo del programma:
   - Horizon Europe: `references/programma-horizon-europe.md`
   - Interreg: `references/programma-interreg.md`
   - LIFE: `references/programma-life.md`
   - UCPM / DG ECHO: `references/programma-ucpm.md`
2. **Matrice**: costruire o riprendere la matrice DoA secondo
   `references/matrice-doa.md`, limitata a ciò che il testo copre.
3. **Completezza formale**: confrontare il testo con il template
   (sezioni, limiti di caratteri, tabelle obbligatorie).
4. **Revisione con i due profili** della griglia: project officer e
   reviewer tecnico esterno.
5. **Sintesi** nel contesto principale (protocollo, sezione 3,
   "Sintesi"): punti condivisi dai due profili per primi; divergenze di
   oltre 1 punto riportate con entrambe le posizioni, senza media;
   correzioni ordinate per impatto sul giudizio.
6. **Esito simulato** solo per deliverable e report, con la regola
   della griglia e la dicitura che è una regola del plugin.

### Modalità agenti

Lanciare `progetti-revisore` due volte in parallelo, nella stessa
chiamata, come in `references/nucleo/protocollo-revisione.md`,
sezione 3:

- salvare il testo (o usare il file originale) e la matrice nella
  cartella di lavoro, es. `revisione/bozza.md` e
  `revisione/matrice-doa.md`;
- passare i percorsi assoluti di testo, matrice, template e di questi
  file della skill: `references/griglia-revisione.md`,
  `references/anti-pattern-progetti.md`, il profilo del programma,
  `references/nucleo/protocollo-revisione.md`,
  `references/nucleo/vincoli.md`;
- profilo: "project officer" in una istanza, "reviewer tecnico
  esterno" nell'altra;
- percorso del rapporto: `revisione/rapporto-po.md` e
  `revisione/rapporto-reviewer.md`;
- se serve, la richiesta dell'esito simulato;
- nient'altro: niente riassunti della conversazione, giudizi
  anticipati o intenzioni degli autori.

Leggere i due rapporti, scrivere la sintesi in
`revisione/sintesi.md` e presentarla all'utente. Non contestare i
rapporti per difendere il testo: se un giudizio nasce da
un'informazione che il testo non dà, la correzione è aggiungerla.

## Modalità chat

Senza strumento per i subagent (regola in
`references/nucleo/protocollo-revisione.md`, sezione 1) la skill fa da
sola il lavoro dei due `progetti-revisore` e della sintesi, e consegna
il rapporto completo.

1. Aprire con la riga di autovalutazione dichiarata del protocollo,
   sezione 4a, adattata: la revisione è fatta nella stessa
   conversazione in cui il testo è stato fornito e discusso.
2. Eseguire il profilo project officer, poi il profilo reviewer tecnico
   esterno, ciascuno con il formato del rapporto dell'agente, partendo
   dalla ricerca delle debolezze e citando i passaggi.
3. Fare la sintesi con lo stesso formato.
4. Dichiarare in una riga che i due profili e la sintesi non sono
   indipendenti.
5. In fondo, una sola volta: il pacchetto revisore (protocollo,
   sezione 4b) con griglia, un profilo per blocco, formato del
   rapporto e testo, da incollare in conversazioni nuove. Si può
   citare Cowork come modo per avere una revisione indipendente.

## Formato del rapporto all'utente

Formato comune (protocollo, sezione 5) con le aggiunte della griglia:

```
## Sintesi
## Punteggi (A1-A7 project officer, B1-B7 reviewer tecnico)
## Problemi
## Tracciabilità
## Dichiarato senza prova
## Punti di forza
## Cosa manca
## Divergenze tra i profili
## Correzioni ordinate per impatto
## Esito simulato (se pertinente)
```

Commenti nella lingua in cui scrive l'utente; citazioni del testo
nella lingua originale. Gli anti-pattern si segnalano con la citazione
esatta, senza riscrivere in silenzio.

## Deroghe allo stile di base

- Il rapporto usa tabelle ed elenchi: è un documento di lavoro.
- Termini ufficiali del programma in inglese anche nel rapporto in
  italiano (deliverable, milestone, means of verification, output,
  result).
