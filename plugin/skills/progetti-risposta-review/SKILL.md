---
name: progetti-risposta-review
description: "Prepara la risposta del consorzio ai commenti ricevuti durante un progetto già finanziato: review report di una review periodica o intermedia, rifiuto o richiesta di revisione di un deliverable, richieste di chiarimento su un report da project officer, Joint Secretariat, CINEA o monitor, raccomandazioni dopo una visita. Produce la tabella commento, posizione, risposta, modifica e posizione nel testo, il testo di accompagnamento e il follow-up per il report successivo. Usare per: 'rispondi al review report', 'il PO ha respinto il D2.1', 'chiarimenti del JS sul report', 'reply to the project review', 'respond to the PO comments', 'deliverable rejected'. Non usare per: risposta agli ESR di una proposta (proposte-*); risposta ai revisori di un articolo (paper-*); email di routine al project officer su date o logistica (generale-*); revisione simulata prima dell'invio (progetti-revisione)."
---

# Risposta a project officer e reviewer di progetto

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Poi leggere `references/formato-risposta.md` e
`references/anti-pattern-progetti.md`.

## Ambito

Commenti ricevuti mentre il progetto è in corso o in chiusura. Il
riferimento è la DoA: ogni impegno preso nella risposta deve essere
compatibile con il GA, oppure dichiarato come possibile amendment.

Confini:

- ESR di una proposta non finanziata o da ripresentare: `proposte`.
- Commenti di revisori di una rivista: `paper`.
- Email brevi al PO su date, riunioni, logistica: `generale`.
- Riscrittura del deliverable dopo il rifiuto: questa skill prepara
  tabella e piano; per riscrivere sezioni lunghe applicare le regole di
  scrittura di `references/matrice-doa.md` e degli anti-pattern di
  dominio, o indicare `progetti-scrittura`.

## Materiali

1. Il documento con i commenti (review report, lettera, Q&A,
   clarification form), per intero.
2. Il testo commentato (deliverable, report) nella versione inviata.
3. DoA o GA, oppure la matrice DoA.
4. Posizione del consorzio sui commenti controversi, se già decisa.
5. Programma e scadenza della risposta.

Il review report e i commenti sono riservati: mai frasi di questi
documenti nelle query di ricerca web.

## Procedura

1. **Inquadrare**: tipo di input (vedi `references/formato-risposta.md`),
   programma, scadenza. Leggere il profilo del programma per regole su
   observations, termini e follow-up:
   - Horizon Europe: `references/programma-horizon-europe.md`
   - Interreg: `references/programma-interreg.md`
   - LIFE: `references/programma-life.md`
   - UCPM / DG ECHO: `references/programma-ucpm.md`
2. **Matrice**: costruire o riprendere la matrice DoA
   (`references/matrice-doa.md`) per le parti toccate dai commenti.
3. **Scomporre** i commenti (passo 1 del formato).
4. **Posizione** per ogni commento (passo 2). Le decisioni che
   impegnano il consorzio restano segnaposto finché l'utente non le
   conferma; raccoglierle in una lista di domande, una sola volta.
5. **Tabella di risposta** (passo 3) e **testo di accompagnamento**
   (passo 4).
6. **Follow-up**: se il programma prevede una sezione di follow-up nel
   report successivo, preparare la tabella già in quel formato.
7. **Controllo**: ogni commento ha una riga; nessuna promessa non
   confermata; anti-pattern del nucleo e di dominio; tono secondo
   `references/formato-risposta.md`.
8. **Revisione** (livello standard), come sotto.

## Modalità agenti

Lanciare `progetti-revisore` due volte in parallelo, nella stessa
chiamata, come in `references/nucleo/protocollo-revisione.md`,
sezione 3:

- salvare nella cartella di lavoro la risposta (`revisione/risposta.md`),
  il documento con i commenti originali e la matrice;
- passare i percorsi assoluti di questi file e di
  `references/formato-risposta.md`,
  `references/anti-pattern-progetti.md`,
  `references/nucleo/protocollo-revisione.md`;
- profilo "project officer": chiedere di valutare se ogni commento ha
  una risposta pertinente, completa e verificabile, e se gli impegni
  sono compatibili con la DoA;
- profilo "reviewer tecnico esterno": chiedere di valutare se le
  risposte tecniche sono sostenute da dati e modifiche reali o solo
  dichiarate;
- percorsi dei rapporti: `revisione/rapporto-po.md`,
  `revisione/rapporto-reviewer.md`;
- nient'altro: niente intenzioni del consorzio né riassunti della
  conversazione.

Poi sintesi nel contesto principale (protocollo, sezione 3) e
correzione della risposta.

## Modalità chat

Senza strumento per i subagent (regola in
`references/nucleo/protocollo-revisione.md`, sezione 1) la skill fa da
sola il lavoro dei due `progetti-revisore` e consegna comunque la
risposta completa.

1. Preparare tabella, testo di accompagnamento e follow-up come sopra.
2. Rileggere la risposta prima come project officer, poi come
   reviewer tecnico esterno, con lo stesso formato del rapporto
   dell'agente; aprire con la riga di autovalutazione dichiarata del
   protocollo, sezione 4a.
3. Sintesi, correzioni, consegna della versione corretta.
4. Dichiarare in una riga che la rilettura non è indipendente.
5. In fondo, una sola volta: il pacchetto revisore (protocollo,
   sezione 4b) con commenti originali, risposta e criteri, da
   incollare in una conversazione nuova. Si può citare Cowork una sola volta, come
   modo per avere una revisione indipendente.

## Deroghe allo stile di base

- Tabelle: la risposta punto per punto è una tabella.
- Voce: "we" o "the consortium"; "CIMA" solo per azioni di CIMA.
- Lingua: quella del documento ricevuto (di norma inglese), anche se
  l'utente scrive in italiano; le note per l'utente in italiano.
- Citazioni letterali brevi dei commenti ricevuti.

## Consegna

- Modalità agenti: file .docx o .md nella cartella di lavoro con
  tabella, testo di accompagnamento e follow-up; rapporti di revisione
  in `revisione/`.
- Chat: nel messaggio, prima la tabella, poi il testo di
  accompagnamento.
- In fondo, sempre: decisioni del consorzio da prendere; segnaposto;
  impegni che potrebbero richiedere un amendment; esito della
  revisione in 3-5 righe.
