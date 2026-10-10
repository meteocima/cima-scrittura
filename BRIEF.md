# Brief di architettura: plugin `cima-scrittura`

**Leggere per intero prima di lavorare su qualsiasi parte del plugin.**
Questo file è la fonte delle decisioni condivise. Lo modifica solo la chat
hub; le chat di dominio propongono modifiche (vedi "Flusso di lavoro").

Versione brief: 6 · Ultimo aggiornamento: 2026-10-10

---

## 1. Obiettivo

Un solo plugin di scrittura per Fondazione CIMA, usabile in Cowork e in
chat, che copre quattro domini:

| Dominio | Prefisso | Copre |
|---|---|---|
| Generale | `generale-` | email, lettere, comunicati stampa, verbali, report interni, testi per web e social |
| Paper | `paper-` | articoli scientifici, abstract per conferenze, cover letter, risposta ai revisori, revisione pre-sottomissione |
| Proposte | `proposte-` | proposte di progetto (Horizon Europe, EIC, Interreg, LIFE, UCPM/ECHO, altri): analisi del bando, concept, scrittura, valutazione simulata, coerenza, risposta agli ESR |
| Progetti | `progetti-` | progetti già finanziati: deliverable, report periodici (parte tecnica), technical report, risposte a project officer e reviewer di progetto |

Proposte e Progetti sono le due fasi dello stesso ciclo: prima e dopo la
firma del Grant Agreement.

Il plugin sostituisce `cima-writing-style` v0.1.0 (copia in `legacy/`).
Quando il nuovo plugin è pronto, il vecchio va disinstallato per evitare
attivazioni doppie.

## 2. Principi

1. **Nucleo unico.** Vincoli, anti-pattern AI, verifica fonti, voce,
   terminologia e protocollo di revisione esistono in un solo posto
   (`nucleo/`). Le skill non li riscrivono: li leggono.
2. **Chi scrive non valuta.** Ogni dominio ha una revisione in contesto
   separato secondo `nucleo/protocollo-revisione.md`.
3. **Il risultato arriva sempre, meglio in Cowork.** In chat, senza
   agenti, ogni skill porta a termine l'intero compito: ogni passaggio
   che in Cowork farebbe un agente (revisione, sintesi del rapporteur,
   verifica di coerenza, decisione dell'editor) viene eseguito nel
   contesto principale. Gli agenti aggiungono indipendenza di giudizio,
   non funzioni. Una skill non si ferma, non consegna a metà e non
   chiede all'utente di passare a Cowork.
4. **Ambiente dedotto, non chiesto.** Strumento subagent disponibile =
   modalità agenti; altrimenti modalità chat. La regola di rilevamento è
   in `nucleo/protocollo-revisione.md`, sezione 1, e vale per ogni
   passaggio affidato a un agente, non solo per la revisione.
5. **Niente invenzioni, mai.** Vale anche per i valutatori simulati: non
   inventano punteggi "realistici" senza griglia.

## 3. Struttura del repository

```
cima-scrittura/
├── BRIEF.md                 # questo file
├── README.md                # per gli utenti CIMA
├── CHANGELOG.md
├── nucleo/                  # fonte unica del nucleo comune
│   ├── vincoli.md
│   ├── anti-pattern-ai.md
│   ├── verifica-fonti.md
│   ├── voce-e-lingua.md
│   ├── terminologia.md
│   └── protocollo-revisione.md
├── plugin/                  # sorgente del plugin (senza nucleo)
│   ├── .claude-plugin/plugin.json
│   ├── condivisi/<dominio>/ # riferimenti comuni alle skill di un dominio
│   ├── skills/<prefisso-nome>/SKILL.md (+ references/)
│   └── agents/<prefisso-nome>.md
├── scripts/build.py         # assembla, valida, impacchetta
├── materiali/               # NON versionato: ESR, proposte, paper riservati
├── legacy/cima-writing-style/
└── dist/                    # NON versionato: output della build
```

### Come il nucleo arriva nelle skill

In chat le skill vengono caricate una per una, quindi una skill non può
leggere file di un'altra. Per questo `scripts/build.py` copia `nucleo/`
dentro ogni skill, in `references/nucleo/`, al momento della build.

- Nel sorgente le skill **non** contengono `references/nucleo/`.
- Nel SKILL.md si fa riferimento ai file come `references/nucleo/vincoli.md`
  ecc.: i percorsi sono validi nel plugin costruito.
- Chi vuole cambiare una regola del nucleo modifica `nucleo/`, mai la copia.

Lo stesso meccanismo vale per i riferimenti comuni a più skill dello
stesso dominio (es. `tipologie.md` per scrittura e revisione):

- stanno in `plugin/condivisi/<dominio>/` (`<dominio>` = prefisso senza
  trattino: `generale`, `paper`, `proposte`, `progetti`);
- `build.py` li copia in `references/` di ogni skill di quel dominio,
  sottocartelle comprese (es. `condivisi/proposte/programmi/` diventa
  `references/programmi/`); `nucleo/` è un nome riservato;
- nel SKILL.md si citano come `references/<file>.md` o
  `references/<sottocartella>/<file>.md`;
- il sorgente delle skill non deve contenerne copie: la build si ferma.

## 4. Convenzioni

### Nomi

- Plugin: `cima-scrittura`. Skill e agenti in kebab-case con prefisso di
  dominio: `proposte-analisi-bando`, `paper-revisione`,
  `generale-scrittura`. Agenti: `proposte-valutatore`, `paper-revisore`.
- Lingua delle istruzioni (SKILL.md, agenti): **italiano**, imperativo,
  rivolte a Claude. Esempi e frammenti di testo nella lingua del testo
  prodotto.

### SKILL.md

- Frontmatter: `name`, `description`. Descrizione in italiano, terza
  persona, max ~900 caratteri, con frasi d'innesco IT ed EN e una
  clausola **"Non usare per…"** che rimanda alle skill degli altri domini
  (vedi sezione 6).
- Corpo sotto le 3.000 parole; dettagli in `references/`.
- Prima sezione obbligatoria, identica in tutte le skill che producono o
  rivedono testo:

  ```markdown
  ## Prima di tutto
  Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
  Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
  Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
  e `references/nucleo/terminologia.md`.
  Per la revisione: `references/nucleo/protocollo-revisione.md`.
  ```

- Ogni skill dichiara le eventuali **deroghe** a `voce-e-lingua.md` in una
  sezione "Deroghe allo stile di base".
- Ogni skill che nomina un agente del plugin ha una sezione
  **"## Modalità chat"** che dice, passaggio per passaggio, come la skill
  svolge da sola il lavoro di quell'agente (per la revisione: sezione 4
  del protocollo; per sintesi e verifiche: stesse regole e stesso
  formato di output, nel contesto principale, dichiarandolo in una
  riga). `build.py` blocca la build se la sezione manca.
- Mai usare il trattino em (—) nei file del plugin, nemmeno nelle
  istruzioni: gli esempi vengono imitati.

### Agenti

- Frontmatter: `name`, `description` con blocchi `<example>`, `model`,
  `color`, `tools`. Valutatori: `color: cyan`; scrittori: `magenta`.
- Strumenti minimi: i valutatori hanno `Read`, `Glob`, `Grep`, `Write` (per
  il rapporto) e, se il dominio lo prevede, `WebSearch`. Mai strumenti
  per modificare il testo valutato.
- **Gli agenti non conoscono i percorsi delle skill.** La skill che lancia
  l'agente gli passa nel prompt i percorsi assoluti di griglie e
  riferimenti (la skill conosce la propria cartella base al caricamento).
- Il prompt di lancio segue `protocollo-revisione.md`, sezione "Cosa
  passare al revisore".
- `model`: `inherit` di default. Per i valutatori si può provare un modello
  diverso dallo scrittore per aumentare la diversità di giudizio; decisione
  da prendere dopo i test (sezione 8).

### Output

- Testi lunghi in modalità agenti: file .docx o .md nella cartella di
  lavoro dell'utente. In chat: nel messaggio, una sezione alla volta se
  lungo.
- Segnaposto `[…]` per ogni dato mancante, elencati in fondo alla consegna.

## 5. Specifiche per dominio

Le chat di dominio possono ridefinire l'elenco delle skill dentro il
proprio prefisso; vanno rispettati livello di revisione e confini.

### 5.1 Generale (livello di revisione: leggero)

Base di partenza: `legacy/cima-writing-style/` (SKILL.md, audience-tones,
good-bad-examples). Skill previste:

- `generale-scrittura`: email, lettere, comunicati, verbali, report
  interni, testi web e social. Riprende tipologie e toni per
  destinatario del legacy. Deliverable e report di progetto vanno a
  `progetti`.
- `generale-revisione`: rilettura di testi dell'utente con checklist
  anti-pattern e tono. È l'ingresso per "rivedi questo testo" senza
  contesto.
- `generale-traduzione`: traduzione e adattamento IT/EN di qualsiasi
  testo (vedi §6).

Riferimenti comuni in `plugin/condivisi/generale/`: tipologie,
destinatari, checklist.

Revisione in modalità agenti: `generale-revisore` (1 revisore, solo
`Read`, `Glob`, `Grep`, `Write` per il rapporto). In `generale-scrittura`
è obbligatorio per comunicati stampa, lettere ufficiali e istituzionali,
testi web e social pubblici, e si usa per qualsiasi testo quando l'utente
lo chiede; email e verbali: autorevisione con checklist. In
`generale-revisione` si usa solo su richiesta, perché il testo non è
stato scritto in quella conversazione e la revisione nel contesto
principale non ha il pregiudizio dell'autore.

Agenti: `generale-revisore`.

### 5.2 Paper (livello: standard)

Skill previste:

- `paper-scrittura`: sezioni IMRAD, abstract, titolo, cover letter.
  Deroghe: struttura IMRAD, convenzioni della rivista prevalgono.
- `paper-revisione`: peer review simulata pre-sottomissione, 2–3 revisori
  con profili diversi (metodologico, di dominio, editor della rivista).
- `paper-risposta-revisori`: risposta punto per punto ai commenti,
  con tabella commento → modifica → posizione nel testo.

Agenti: `paper-revisore` (parametrizzato per profilo), `paper-editor`
(sintesi e decisione simulata: accept / minor / major / reject).
Riviste di riferimento (decise con l'utente): riviste del gruppo
Elsevier, riviste del gruppo Nature (Nature Portfolio) e Geoscientific
Model Development (GMD, Copernicus/EGU). Un profilo per editore o
rivista in `references/riviste/<nome>.md` (struttura, limiti, sezioni
obbligatorie come disponibilità di codice e dati, data di verifica),
costruito da guide for authors correnti verificate con ricerca web, mai a
memoria. Da chiarire nella chat di dominio: se estendere GMD alle altre
riviste Copernicus/EGU usate da CIMA (es. HESS, NHESS), che condividono
gran parte delle regole. Riferimenti da costruire anche: checklist di
reporting pertinenti.

### 5.3 Proposte (livello: completo)

Decisioni già prese con l'utente:

- Programmi: Horizon Europe, EIC, Interreg, LIFE, UCPM/ECHO, altri.
  Un **motore unico** + un **profilo per programma** in
  `references/programmi/<programma>.md` (criteri, pesi, soglie, struttura
  del modulo, limiti di pagine, gergo del valutatore, data di verifica).
  I profili si costruiscono da documenti ufficiali correnti, verificati
  con ricerca web, mai a memoria.
- La **matrice del bando** estratta dal testo reale del topic prevale
  sempre sul profilo generico.
- Revisione: **3 valutatori + rapporteur**, come nel processo EU. Stesso
  brief, tre profili esperti diversi (scientifico, applicativo/utenti
  finali, gestionale/implementazione). Il rapporteur riporta le divergenze
  > 1 punto senza mediarle.
- **Calibrazione** con proposte ed ESR reali di CIMA, forniti dall'utente
  in `materiali/` (non versionato). Nel plugin vanno solo **pattern
  anonimizzati** (tipo di debolezza → commento tipico → effetto sul
  punteggio), senza nomi, partner, budget.
- Skill di stile propria (`proposte-stile` o sezione di riferimento): con
  gli stessi anti-pattern del nucleo più quelli tipici degli ESR (state of
  the art non quantificato, impatto generico, KPI senza baseline,
  disseminazione standard, rischi generici, "uniquely positioned",
  buzzword, incoerenze tra sezioni). Deroghe: tabelle ed elenchi dove il
  modulo li richiede; "we / the consortium" invece di "CIMA".

Skill previste: `proposte-analisi-bando`, `proposte-concept`,
`proposte-scrittura`, `proposte-revisione`, `proposte-coerenza`,
`proposte-risposta-esr`.
Agenti: `proposte-valutatore` (parametrizzato per profilo esperto),
`proposte-rapporteur`, `proposte-verificatore` (coerenza formale).

Test di accettazione: valutazione cieca di una proposta CIMA già valutata,
confronto tra punteggio simulato e ESR reale.

### 5.4 Progetti (livello: standard)

Dominio aggiunto con la versione 2 del brief (decisione 1). Copre i
testi dei progetti già finanziati, scritti per la Commissione, le
agenzie o il consorzio. Riferimento principale di ogni testo: il
Grant Agreement e la descrizione dell'azione (DoA / Annex 1), che
l'utente fornisce o carica.

Skill previste (la chat di dominio può ridefinirle):

- `progetti-scrittura`: deliverable, parte tecnica dei report periodici,
  technical report, executive summary. Ogni affermazione su attività e
  risultati va ricondotta a task, deliverable e milestone della DoA.
- `progetti-revisione`: revisione simulata dal punto di vista di project
  officer e reviewer esterni di progetto: aderenza alla DoA, risultati
  dimostrati e non solo dichiarati, scostamenti spiegati, KPI con valore
  misurato.
- `progetti-risposta-review`: risposta del consorzio a review report,
  deliverable respinti, richieste di chiarimento di PO, Joint
  Secretariat, agenzie o monitor: tabella commento, posizione,
  risposta, modifica; testo di accompagnamento; follow-up.

Riferimenti comuni in `plugin/condivisi/progetti/`: matrice DoA,
anti-pattern di dominio, griglia di revisione, profili dei programmi
(Horizon Europe, Interreg, LIFE, UCPM), ciascuno con data di verifica e
punti da verificare.

Revisione: deliverable, parte tecnica dei report, technical report e
risposte a review con due profili e sintesi. Executive summary,
highlights e note brevi scritti da soli: autorevisione con la griglia,
salvo richiesta. Publishable summary e altri testi destinati alla
pubblicazione: in modalità agenti almeno il profilo project officer
(eccezione ammessa da `protocollo-revisione.md`, sezione 2).

Agenti: `progetti-revisore` (parametrizzato per profilo: project officer,
reviewer tecnico).
Deroghe probabili: struttura imposta dal template del deliverable;
"the consortium" / "we" invece di "CIMA" quando il testo è del consorzio.
Confine con `proposte`: la risposta agli ESR di una proposta resta in
`proposte`; i commenti di una review di progetto in corso vanno a
`progetti`.

## 6. Confini tra domini (instradamento)

Le descrizioni delle skill si sovrappongono su parole come "scrivi",
"draft", "review", "proposal", "abstract". Regole:

| Richiesta | Va a |
|---|---|
| proposta, bando, call, topic, Part B, ESR, work package, consorzio (pre-finanziamento) | proposte |
| deliverable, periodic report, technical report, review di un progetto in corso, Grant Agreement, DoA | progetti |
| risposta di merito a project officer o reviewer di progetto (review report, deliverable respinto, chiarimenti su un report) | progetti (`progetti-risposta-review`) |
| email di routine al project officer (date, riunioni, logistica, invio di documenti) | generale |
| paper, manuscript, articolo, journal, revisori, rebuttal, cover letter | paper |
| abstract per conferenza o rivista | paper |
| abstract di una proposta | proposte |
| email, lettera, comunicato, post, verbale, testo web | generale |
| "rivedi questo testo" senza contesto | generale, che rimanda se riconosce un paper o una proposta |
| traduci, translate (qualsiasi testo) | generale (`generale-traduzione`): per abstract, paper, proposte e deliverable traduce lingua e terminologia senza cambiare struttura e contenuto; per adattarli ai limiti del dominio rimanda alla skill di quel dominio |

Ogni descrizione include una clausola "Non usare per…" coerente con questa
tabella. La chat hub verifica l'instradamento con prompt di prova prima
del rilascio.

## 7. Flusso di lavoro tra chat

- **Chat hub** (questa): BRIEF.md, `nucleo/`, `scripts/`, `plugin.json`,
  README, integrazione, test di instradamento, rilascio.
- **Chat di dominio**: solo `plugin/skills/<prefisso>-*`,
  `plugin/agents/<prefisso>-*` e `plugin/condivisi/<dominio>/`.
- Ogni chat di dominio lavora su un branch `dominio/<prefisso>` e apre una
  pull request verso `main`. La chat hub integra.
- Modifiche al nucleo o al brief proposte da una chat di dominio: aprire
  una issue su GitHub con titolo `[nucleo] …` o `[brief] …`, oppure
  annotarle nella descrizione della pull request.
- Materiali riservati (ESR, proposte, manoscritti): mai nel repository.
  Si caricano direttamente nella chat che ne ha bisogno.

### Prompt di avvio per una chat di dominio

```
Lavoriamo al dominio <generale|paper|proposte|progetti> del plugin cima-scrittura
(repo meteocima/cima-scrittura). Leggi per intero BRIEF.md e i file in
nucleo/, poi crea il branch dominio/<prefisso>. Lavora solo nei file del
tuo prefisso. Prima di scrivere le skill proponimi il piano del dominio.
```

## 8. Decisioni

### Prese

1. Deliverable e report periodici diventano il dominio `progetti`
   (sezione 5.4). Deciso il 2026-10-10.
2. Riviste di riferimento per il dominio paper: gruppo Elsevier, gruppo
   Nature, GMD (sezione 5.2). Deciso il 2026-10-10.
3. Le skill del plugin devono comparire anche in chat per
   l'organizzazione CIMA (gli agenti funzionano solo in Cowork):
   confermato dall'utente il 2026-10-10. Da verificare in pratica al
   primo rilascio.
4. `generale-revisore` si fa, ma si usa solo per testi pubblici o
   istituzionali e su richiesta; email e verbali con autorevisione
   (sezione 5.1). Riga "Leggero" di `nucleo/protocollo-revisione.md`
   aggiornata di conseguenza. Deciso il 2026-10-10.
5. Riferimenti comuni di dominio in `plugin/condivisi/<dominio>/`,
   iniettati da `build.py` come il nucleo (sezione 3). Proposto dalla
   chat del dominio generale (PR #1), deciso il 2026-10-10.
6. La traduzione di qualsiasi testo va a `generale-traduzione`, che non
   cambia struttura e contenuto dei testi degli altri domini (sezione 6).
   PR #1, deciso il 2026-10-10.
7. Dominio progetti: aggiunta `progetti-risposta-review`; email di
   routine al PO a `generale`, risposte di merito a `progetti`;
   autorevisione per summary brevi scritti da soli, ma revisore per i
   testi destinati alla pubblicazione. `build.py` accetta sottocartelle
   in `plugin/condivisi/<dominio>/`. Deciso il 2026-10-10.

### Aperte

1. **Modello dei valutatori.** Tecnicamente possibile: il campo `model`
   degli agenti accetta `inherit`, `sonnet`, `opus`, `haiku` (già
   validato da `build.py`). Limiti: vale solo in modalità agenti; i
   modelli sono della stessa famiglia, quindi la diversità di giudizio è
   minore di quella data da contesto separato e profili diversi; la
   disponibilità dipende dal piano dell'organizzazione. Decidere con il
   test di accettazione delle proposte: stessa proposta valutata con
   `inherit` e con un modello diverso, confronto con l'ESR reale.

## 9. Build e test

```
python3 scripts/build.py           # assembla in dist/, valida, crea il .plugin
python3 scripts/build.py --check   # solo validazione, in una cartella temporanea
```

La build fallisce se: manca `plugin.json` o un campo obbligatorio; una
skill non ha `name`/`description` validi; un SKILL.md cita un file in
`references/` che non esiste; un file del plugin contiene il trattino em;
un nome non rispetta prefisso e kebab-case; un SKILL.md nomina un agente
del plugin senza avere la sezione "## Modalità chat"; `plugin/condivisi/`
contiene una cartella che non è un dominio; il sorgente di una skill
contiene una copia di un file di `plugin/condivisi/<dominio>/`.

Prima di ogni rilascio, ogni skill si prova in due ambienti: chat senza
subagent (deve consegnare il risultato completo) e Cowork (deve usare gli
agenti previsti).

Output: `dist/cima-scrittura/` (plugin assemblato),
`dist/cima-scrittura.plugin` (per Cowork), `dist/skills/<nome>.zip` (per il
caricamento delle singole skill in chat).
