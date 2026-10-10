# Brief di architettura: plugin `cima-scrittura`

**Leggere per intero prima di lavorare su qualsiasi parte del plugin.**
Questo file è la fonte delle decisioni condivise. Lo modifica solo la chat
hub; le chat di dominio propongono modifiche (vedi "Flusso di lavoro").

Versione brief: 1 · Ultimo aggiornamento: 2026-10-10

---

## 1. Obiettivo

Un solo plugin di scrittura per Fondazione CIMA, usabile in Cowork e in
chat, che copre tre domini:

| Dominio | Prefisso | Copre |
|---|---|---|
| Generale | `generale-` | email, lettere, comunicati stampa, verbali, report interni, testi per web e social, deliverable e report periodici di progetti già finanziati |
| Paper | `paper-` | articoli scientifici, abstract per conferenze, cover letter, risposta ai revisori, revisione pre-sottomissione |
| Proposte | `proposte-` | proposte di progetto (Horizon Europe, EIC, Interreg, LIFE, UCPM/ECHO, altri): analisi del bando, concept, scrittura, valutazione simulata, coerenza, risposta agli ESR |

Il plugin sostituisce `cima-writing-style` v0.1.0 (copia in `legacy/`).
Quando il nuovo plugin è pronto, il vecchio va disinstallato per evitare
attivazioni doppie.

## 2. Principi

1. **Nucleo unico.** Vincoli, anti-pattern AI, verifica fonti, voce,
   terminologia e protocollo di revisione esistono in un solo posto
   (`nucleo/`). Le skill non li riscrivono: li leggono.
2. **Chi scrive non valuta.** Ogni dominio ha una revisione in contesto
   separato secondo `nucleo/protocollo-revisione.md`.
3. **Funziona ovunque, meglio in Cowork.** Le skill funzionano in chat; gli
   agenti aggiungono indipendenza in Cowork. Nessuna skill deve
   dipendere da un agente per funzionare.
4. **Ambiente dedotto, non chiesto.** Strumento subagent disponibile =
   modalità agenti; altrimenti modalità chat.
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

- `generale-scrittura`: email, lettere, comunicati, verbali, report,
  deliverable e report periodici UE (post-finanziamento), testi web.
  Riprende tipologie e toni per destinatario del legacy.
- `generale-revisione`: rilettura di testi dell'utente con checklist
  anti-pattern e tono; in modalità agenti 1 revisore.

Agenti: `generale-revisore` (opzionale, valutare se serve davvero).

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
Riferimenti da costruire: linee guida delle riviste più usate da CIMA
(da chiedere all'utente quali), checklist di reporting pertinenti.

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

## 6. Confini tra domini (instradamento)

Le descrizioni delle skill si sovrappongono su parole come "scrivi",
"draft", "review", "proposal", "abstract". Regole:

| Richiesta | Va a |
|---|---|
| proposta, bando, call, topic, Part B, ESR, work package, consorzio (pre-finanziamento) | proposte |
| deliverable, periodic report, technical report di un progetto in corso | generale |
| paper, manuscript, articolo, journal, revisori, rebuttal, cover letter | paper |
| abstract per conferenza o rivista | paper |
| abstract di una proposta | proposte |
| email, lettera, comunicato, post, verbale, testo web | generale |
| "rivedi questo testo" senza contesto | generale, che rimanda se riconosce un paper o una proposta |

Ogni descrizione include una clausola "Non usare per…" coerente con questa
tabella. La chat hub verifica l'instradamento con prompt di prova prima
del rilascio.

## 7. Flusso di lavoro tra chat

- **Chat hub** (questa): BRIEF.md, `nucleo/`, `scripts/`, `plugin.json`,
  README, integrazione, test di instradamento, rilascio.
- **Chat di dominio**: solo `plugin/skills/<prefisso>-*` e
  `plugin/agents/<prefisso>-*`.
- Ogni chat di dominio lavora su un branch `dominio/<prefisso>` e apre una
  pull request verso `main`. La chat hub integra.
- Modifiche al nucleo o al brief proposte da una chat di dominio: aprire
  una issue su GitHub con titolo `[nucleo] …` o `[brief] …`, oppure
  annotarle nella descrizione della pull request.
- Materiali riservati (ESR, proposte, manoscritti): mai nel repository.
  Si caricano direttamente nella chat che ne ha bisogno.

### Prompt di avvio per una chat di dominio

```
Lavoriamo al dominio <generale|paper|proposte> del plugin cima-scrittura
(repo meteocima/cima-scrittura). Leggi per intero BRIEF.md e i file in
nucleo/, poi crea il branch dominio/<prefisso>. Lavora solo nei file del
tuo prefisso. Prima di scrivere le skill proponimi il piano del dominio.
```

## 8. Decisioni aperte

1. Deliverable e report periodici: restano in `generale` o diventano un
   dominio `progetti` (post-finanziamento)? Default attuale: `generale`.
2. Modello dei valutatori: `inherit` o diverso dallo scrittore? Decidere
   dopo il test di accettazione delle proposte.
3. `generale-revisore` come agente: serve o basta l'autorevisione?
4. Riviste di riferimento per il dominio paper: elenco da chiedere.
5. Verificare che le skill del plugin compaiano anche in chat per
   l'organizzazione CIMA (gli agenti funzionano solo in Cowork).

## 9. Build e test

```
python3 scripts/build.py           # assembla in dist/, valida, crea il .plugin
python3 scripts/build.py --check   # solo validazione
```

La build fallisce se: manca `plugin.json` o un campo obbligatorio; una
skill non ha `name`/`description` validi; un SKILL.md cita un file in
`references/` che non esiste; un file del plugin contiene il trattino em;
un nome non rispetta prefisso e kebab-case.

Output: `dist/cima-scrittura/` (plugin assemblato),
`dist/cima-scrittura.plugin` (per Cowork), `dist/skills/<nome>.zip` (per il
caricamento delle singole skill in chat).
