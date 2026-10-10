---
name: generale-revisione
description: "Rilegge e migliora testi già scritti dall'utente per Fondazione CIMA, in italiano e in inglese: email, lettere, comunicati, verbali, report interni, testi web e social. Segnala con citazione esatta anti-pattern AI, problemi di tono rispetto al destinatario e di struttura, fatti da confermare e fonti da verificare; riscrive solo se richiesto. È il punto d'ingresso per 'rivedi questo testo' senza contesto: se riconosce un paper, una proposta o un deliverable rimanda al dominio giusto. Usare per 'rivedi', 'rileggi', 'correggi', 'migliora questa email', 'controlla il tono', 'sistema questo testo', 'review this', 'proofread', 'improve this text', 'check the tone'. Non usare per scrivere un testo nuovo (generale-scrittura), per tradurre (generale-traduzione), per peer review di manuscript (skill paper-), valutazione di proposte (proposte-), revisione di deliverable e report di progetto (progetti-)."
---

# Revisione di testi generali CIMA

Questa skill rivede testi scritti dall'utente o da colleghi. Livello di
revisione: **leggero** (`references/nucleo/protocollo-revisione.md`,
sezione 2).

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.

Riferimenti del dominio:

- `references/checklist.md`: checklist di revisione;
- `references/tipologie.md`: struttura attesa per tipo di testo;
- `references/destinatari.md`: tono atteso per destinatario.

## Riconoscere il testo

Prima di rivedere, capire che cosa è il testo.

| Segnali nel testo | Dominio |
|---|---|
| Abstract, Introduction, Methods, Results; manuscript; risposta a reviewer di una rivista; cover letter all'editor | paper |
| Excellence, Impact, Implementation; work package; call, topic; ESR | proposte |
| Deliverable D[n].[n]; periodic report; Grant Agreement, DoA; risposta a un project officer su un report | progetti |
| email, lettera, comunicato, verbale, report interno, pagina web, post | questa skill |

Se il testo appartiene a un altro dominio, dirlo in una riga e indicare la
skill (`paper-revisione`, `proposte-revisione`, `progetti-revisione`). Se
l'utente vuole comunque una rilettura qui, o se la skill del dominio non è
disponibile, procedere con la checklist di questa skill e dire che non
copre i criteri specifici di quel dominio (griglie di valutazione, regole
della rivista, aderenza alla DoA).

Testi misti (per esempio una email che accompagna un deliverable):
rivedere la email qui, rimandare il deliverable.

## Livello di intervento

Dedurlo dalla richiesta:

| Richiesta | Cosa consegnare |
|---|---|
| "rivedi", "rileggi", "review", "cosa ne pensi" | rapporto con i problemi; nessuna riscrittura |
| "correggi", "proofread" | testo corretto (refusi, grammatica, anti-pattern evidenti, convenzioni) ed elenco delle modifiche |
| "migliora", "sistema", "improve", "rendilo più…" | testo riscritto ed elenco delle modifiche principali |
| "controlla il tono" | rapporto limitato alle sezioni D e B della checklist |

Nel dubbio tra rapporto e riscrittura: consegnare il rapporto e offrire
la riscrittura in una riga.

## Flusso di lavoro

1. **Lingua dei commenti**: quella in cui scrive l'utente, anche se il
   testo è in un'altra lingua (`voce-e-lingua.md`).
2. **Tipo e destinatario**: dedurli dal testo. Se il destinatario non è
   deducibile e cambia il giudizio sul tono, una sola domanda; altrimenti
   dichiarare l'assunzione nel rapporto.
3. **Leggere tutto** il testo prima di giudicare.
4. **Checklist**: applicare `checklist.md` sezione per sezione. Per gli
   anti-pattern, citare il passaggio esatto invece di riscrivere in
   silenzio (`anti-pattern-ai.md`, ultima riga).
5. **Fatti**: non verificare i dati propri dell'utente (risultati,
   date interne), ma segnalare quelli che sembrano incoerenti tra loro.
   Non aggiungere fatti.
6. **Fonti citate nel testo**: verificarle con `verifica-fonti.md` e
   riportare l'esito (verificata, dati discordanti, non trovata). Senza
   strumento di ricerca, elencarle come da verificare.
7. **Consegna** secondo il livello di intervento.

In una riscrittura: mantenere i fatti dell'autore, non aggiungerne;
inserire segnaposto dove il testo è vago e serve un dato; applicare poi
l'autorevisione con `checklist.md` alla nuova versione.

## Secondo parere indipendente

Il testo non è stato scritto in questa conversazione, quindi la revisione
nel contesto principale non ha il pregiudizio dell'autore. Il revisore
separato si usa **solo** quando l'utente lo chiede ("fallo controllare da
qualcuno che non ha visto la conversazione", "secondo parere",
"revisione indipendente"), tipicamente dopo una riscrittura. Senza
questa richiesta le due sezioni seguenti non si applicano: si consegna
il rapporto o il testo rivisto e basta.

## Modalità agenti

Strumento per lanciare subagent disponibile (`Agent` o `Task`):

1. Salvare il testo da valutare (originale o versione riscritta) nella
   cartella di lavoro: `revisione/testo-[tipo].md`, o usare il file
   originale se l'utente l'ha fornito come file.
2. Costruire i percorsi assoluti a partire dalla cartella base di questa
   skill, indicata al caricamento.
3. Lanciare l'agente `generale-revisore` con un prompt che contiene solo:
   percorso del testo; tipo e destinatario; percorsi di
   `references/tipologie.md`, `references/destinatari.md`,
   `references/checklist.md` e dei file in `references/nucleo/`
   (vincoli, anti-pattern-ai, voce-e-lingua, terminologia,
   protocollo-revisione); formato (sezione 5 del protocollo, senza
   punteggi); lingua del rapporto (quella in cui scrive l'utente,
   `voce-e-lingua.md`); percorso del rapporto `revisione/rapporto-[tipo].md`.
   Niente riassunti della conversazione o spiegazioni delle modifiche
   fatte.
4. Presentare il rapporto all'utente e proporre le correzioni, senza
   difendere la versione riscritta.

Se il lancio fallisce, passare alla modalità chat e dirlo in una riga.

## Modalità chat

Strumento per lanciare subagent non disponibile:

1. Se il testo da valutare è una riscrittura fatta in questa
   conversazione, rivederla con `checklist.md` nel contesto principale,
   aprendo il rapporto con la riga di `protocollo-revisione.md`,
   sezione 4a; se è il testo originale dell'utente, la revisione già
   fatta vale come parere non condizionato e va detto in una riga.
2. Stesso formato del revisore (sezione 5 del protocollo, senza
   punteggi).
3. Se il testo è una riscrittura fatta in questa conversazione, offrire
   il pacchetto revisore (sezione 4b del protocollo) in un unico blocco
   da copiare in una conversazione nuova; per il testo originale
   offrirlo solo se l'utente insiste. Si può citare Cowork una
   sola volta, come modo per avere una revisione indipendente.

Consegnare comunque il risultato completo, senza chiedere all'utente di
cambiare ambiente.

## Formato del rapporto

Sezione 5 di `protocollo-revisione.md`, senza Punteggi:

```
## Sintesi
## Problemi
| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
## Punti di forza
## Cosa manca
```

Per testi brevi (una email) basta Sintesi e tabella dei problemi. Ordinare
i problemi per gravità. Citazioni esatte, tra virgolette, nella lingua del
testo.

Dopo il rapporto, se presenti: fonti con esito della verifica;
assunzioni su tipo e destinatario.

## Deroghe allo stile di base

Nessuna oltre a quelle dei tipi di testo in `tipologie.md` (email
interne, verbali, post social, lettere ufficiali): un testo di quel tipo
si giudica con le regole del suo tipo.
