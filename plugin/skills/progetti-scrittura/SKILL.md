---
name: progetti-scrittura
description: "Scrive i testi tecnici dei progetti già finanziati (Horizon Europe, Interreg, LIFE, UCPM/ECHO e altri): deliverable, parte tecnica di periodic e final report, technical report, executive e publishable summary, DMP. Costruisce una matrice di tracciabilità dalla DoA (Annex 1 del GA) e lega ogni affermazione a task, deliverable e milestone. Usare per: 'scrivi il deliverable', 'bozza del periodic report', 'executive summary del D3.2', 'write the deliverable', 'draft the periodic report Part B', 'technical report'. Non usare per: proposte, bandi, risposta agli ESR (proposte-*); articoli scientifici, anche dai risultati del progetto (paper-*); email di routine al project officer, verbali, comunicati, traduzione di un deliverable (generale-*); revisione di un testo di progetto già scritto (progetti-revisione); risposta ai commenti di una review di progetto (progetti-risposta-review)."
---

# Scrittura di testi di progetto

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.

Poi leggere `references/anti-pattern-progetti.md`.

## Ambito

Testi scritti per la Commissione, le agenzie, il segretariato del
programma o il consorzio, in un progetto con Grant Agreement firmato:

- deliverable di tipo report e note di accompagnamento dei deliverable
  non report (software, dataset, siti);
- parte tecnica dei periodic report e del final report (Part B o
  equivalente);
- technical report, executive summary, publishable summary,
  highlights;
- Data Management Plan.

Fuori ambito: parte finanziaria dei report (financial statement, Use
of Resources, giustificazione dei costi). Se l'utente la chiede,
dirlo in una riga e limitarsi alla parte narrativa che la accompagna.

## Materiali

Chiedere in un solo messaggio ciò che manca, poi procedere comunque
con segnaposto:

1. Grant Agreement o DoA (Annex 1) e ultimo amendment; per Interreg,
   Application Form approvata.
2. Template del deliverable o del report (del programma o del
   consorzio).
3. Programma, reporting period o deliverable da scrivere.
4. Materiale tecnico: dati, risultati, note dei partner, bozze,
   report precedenti, review report.
5. Lingua e destinatario, se non ovvi (di norma inglese).

Senza DoA si può scrivere, ma ogni codice e ogni mese diventa
`[da DoA]` e la consegna lo dice.

## Procedura

### 1. Inquadrare

Identificare tipo di documento, programma e periodo. Leggere il
profilo del programma:

- Horizon Europe: `references/programma-horizon-europe.md`
- Interreg: `references/programma-interreg.md`
- LIFE: `references/programma-life.md`
- UCPM / DG ECHO: `references/programma-ucpm.md`

Il GA e il template del progetto prevalgono sul profilo. Se il profilo
ha più di 12 mesi o se un punto è marcato `[da verificare]` e serve al
testo, verificarlo con ricerca web sulle fonti ufficiali; senza
ricerca web, segnaposto. Per altri programmi (nazionali, regionali,
agenzie) chiedere il template e lavorare solo su quello.

### 2. Matrice DoA

Costruire o aggiornare la matrice secondo `references/matrice-doa.md`.
Per un singolo deliverable basta la parte della matrice che lo
riguarda (WP, task, deliverable collegati, KPI pertinenti).

### 3. Struttura

Seguire il template fornito. Senza template: `references/tipi-documento.md`.
Mostrare l'indice all'utente prima di scrivere testi lunghi (oltre 3
pagine) e attendere conferma solo se l'indice si discosta dal
template.

### 4. Scrittura

- Ogni paragrafo su attività o risultati cita il codice di task,
  deliverable o milestone.
- Risultati con prova: dato, figura, link, DOI, prodotto. Senza prova:
  segnaposto `[prova: …]`, mai un aggettivo al posto del dato.
- KPI sempre con baseline, valore misurato, target, fonte.
- Ogni scostamento: causa concreta, effetto su altri task e
  deliverable, azione correttiva, nuova data, eventuale amendment.
  Raccolti nella sezione del template dedicata.
- Contributo dei partner: solo quello documentato dall'utente.
- Non copiare frasi della DoA al passato: descrivere ciò che è stato
  fatto davvero.
- Limiti di caratteri o pagine: contarli prima della consegna.
- Testi lunghi in chat: una sezione alla volta, con l'indice in testa.

### 5. Controllo prima della revisione

1. Codici e mesi contro la matrice.
2. Anti-pattern del nucleo e di `references/anti-pattern-progetti.md`.
3. Segnaposto elencati.
4. Trattino em assente.

### 6. Revisione (livello standard)

Criteri: `references/griglia-revisione.md`.

- **Deliverable, parte tecnica di periodic e final report, technical
  report**: revisione con due profili (project officer e reviewer
  tecnico esterno) prima della consegna.
- **Executive summary, highlights isolati, note di accompagnamento
  brevi**: autorevisione con la griglia; due profili se l'utente lo
  chiede.
- **Publishable summary e altri testi destinati alla pubblicazione**
  (CORDIS, sito del progetto): in modalità agenti almeno il profilo
  project officer; in chat autorevisione dichiarata e pacchetto
  revisore.

In modalità agenti lanciare `progetti-revisore` due volte in parallelo,
nella stessa chiamata, una per profilo. Preparazione e contenuto del
prompt come in `references/nucleo/protocollo-revisione.md`, sezione 3:

- salvare bozza e matrice nella cartella di lavoro (es.
  `revisione/bozza.md`, `revisione/matrice-doa.md`);
- passare i percorsi assoluti di bozza, matrice, template (se c'è) e
  di questi file della skill: `references/griglia-revisione.md`,
  `references/anti-pattern-progetti.md`, il profilo del programma,
  `references/nucleo/protocollo-revisione.md`;
- profilo: "project officer" oppure "reviewer tecnico esterno";
- percorso del rapporto (es. `revisione/rapporto-po.md`,
  `revisione/rapporto-reviewer.md`);
- nient'altro: niente riassunti della conversazione o intenzioni.

Poi fare la sintesi nel contesto principale (protocollo, sezione 3,
"Sintesi"): punti comuni, divergenze di oltre 1 punto riportate senza
media, correzioni ordinate per impatto. Applicare le correzioni che
non richiedono dati nuovi; per le altre, segnaposto e domanda
all'utente.

## Modalità chat

Senza strumento per i subagent (regola in
`references/nucleo/protocollo-revisione.md`, sezione 1) la skill fa da
sola il lavoro di `progetti-revisore` e consegna comunque il testo
completo.

1. Scrivere e controllare il testo come sopra.
2. Revisione: eseguire nel contesto principale prima il profilo
   project officer, poi il profilo reviewer tecnico esterno, con la
   griglia e il formato del rapporto dell'agente; aprire con la riga
   di autovalutazione dichiarata del protocollo, sezione 4a.
3. Sintesi nel contesto principale, con lo stesso formato.
4. Applicare le correzioni e consegnare il testo rivisto.
5. In fondo, una sola volta: il pacchetto revisore (protocollo,
   sezione 4b) da incollare in una conversazione nuova, con griglia,
   profilo, formato e testo. Si può citare Cowork come modo per avere
   una revisione indipendente.

Dichiarare in una riga che revisione e sintesi non sono indipendenti.

## Deroghe allo stile di base

- **Struttura**: il template del programma o del consorzio prevale
  sulle regole di paragrafo e sugli elenchi; tabelle ed elenchi dove
  il template li prevede.
- **Voce**: "the consortium" o "we" quando il testo è del consorzio;
  "CIMA" solo per il contributo specifico di CIMA. Una voce per
  documento.
- **Titoli**: maiuscole come nel template, anche se in Title Case.
- **Tempi verbali**: past simple per il lavoro del periodo; present
  perfect solo per risultati con effetto in corso; futuro solo per le
  attività del periodo successivo.
- **Terminologia di programma**: usare i termini ufficiali del
  programma (deliverable, output, result, milestone, means of
  verification) con il significato del profilo, anche dove la
  terminologia CIMA suggerirebbe altro.

## Consegna

- Modalità agenti: file .docx o .md nella cartella di lavoro, più la
  matrice e i rapporti di revisione.
- Chat: testo nel messaggio, una sezione alla volta se lungo.
- In fondo, sempre: elenco dei segnaposto; scostamenti dichiarati;
  punti del profilo `[da verificare]` usati; esito della revisione in
  3-5 righe.
