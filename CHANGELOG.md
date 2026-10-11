# Changelog

## [0.3.0] in lavorazione

Il quarto dominio, `proposte`, costruito un ticket alla volta (issue #11).
Tutte le prove del giro stanno in `prove/0.3.0-dominio-proposte/`.

La 0.3.0 assorbe la 0.2.0, che non esce da sola: le sue voci qui sotto
escono con questo rilascio, e le sue righe ancora da eseguire (issue #6 e #7)
fanno parte delle prove della 0.3.0. I tag `v0.2.0-rc1` e `v0.2.0-rc2`
restano come memoria dei due giri di prova.

### Aggiunto
- Skill `proposte-analisi-bando`: estrae dal testo di un topic la matrice del
  bando (criteri, pesi, soglie, expected outcomes nelle parole del bando,
  requisiti obbligatori, struttura del modulo e limiti), con la fonte di ogni
  voce e segnaposto dove il bando tace (issue #12).
- `plugin/condivisi/proposte/matrice-bando.md`: forma della matrice e regola
  che decide i conflitti, cioe' il topic prevale sul profilo del programma.
- `plugin/condivisi/proposte/programma-horizon-europe.md`: profilo di
  **valutazione** di Horizon Europe, costruito il 2026-10-10 da work programme
  2026-2027, modulo di valutazione V4.0 e application form V5.1. Da non
  confondere con il profilo di **reporting** dello stesso programma in
  `condivisi/progetti/` (ADR 0020).
- `plugin/condivisi/proposte/programma-eic.md` e `programma-interreg.md`:
  profili di valutazione di EIC e Interreg, costruiti il 2026-10-10 da EIC
  Work Programme 2026 e da manuale e Terms of Reference di Interreg Euro-MED
  (issue #15). Nell'EIC criteri e soglie cambiano con lo strumento; in
  Interreg la griglia sta nelle ToRs della singola call, non nel profilo.
- `plugin/condivisi/proposte/programma-life.md` e `programma-ucpm.md`:
  profili di valutazione di LIFE e UCPM/ECHO, costruiti il 2026-10-10 dai call
  document LIFE-2026-SAP-ENV e UCPM-2026-TRACK 1 (issue #16). LIFE valuta su
  quattro criteri da 20 punti con il peso su Impact dentro la soglia; UCPM
  lega ogni sotto-criterio a una casella numerata della Part B.
- Skill `proposte-scrittura`: scrive il testo della proposta dentro il modulo
  del programma, con stato dell'arte quantificato, KPI con baseline e nessun
  dato inventato; dichiara le deroghe allo stile di base (tabelle, elenchi,
  voce del consorzio, gergo del programma). Con lei
  `plugin/condivisi/proposte/anti-pattern-proposte.md`, i difetti che un
  valutatore nota per primi (issue #14).
- Skill `proposte-concept`: i quattro blocchi dell'idea (problema, approccio,
  consorzio, impatto) prima di scrivere la proposta, con la tabella di
  copertura dei criteri del bando e l'elenco di che cosa manca per diventare
  una proposta (issue #13).
- Skill `proposte-revisione` e agenti `proposte-valutatore` e
  `proposte-rapporteur`: valutazione simulata con tre profili esperti in
  contesti separati piu' un rapporteur che riporta le divergenze senza
  mediarle e dichiara il superamento delle soglie. Con loro
  `griglia-valutazione.md` (il motore, con la regola che senza griglia reale
  non si danno punteggi) e `profili-valutatori.md` (issue #17).
- Skill `proposte-risposta-esr`: scompone i rilievi dell'Evaluation Summary
  Report uno per uno, con la posizione presa e il motivo, tenendo separato
  cio' che e' gia' fatto da cio' che e' solo deciso. Dice che a un ESR non si
  replica e che l'unica strada formale, l'evaluation review, riguarda solo gli
  aspetti procedurali (issue #18).
- Skill `proposte-coerenza` e agente `proposte-verificatore`: controllo
  formale prima della consegna, con le incoerenze fra sezioni riportate in
  coppia (tutti e due i passaggi citati) e il conteggio dei limiti contro il
  bando, senza punteggi e senza giudizi di merito (issue #19).
- `prove/domini/proposte.md` e i primi casi eval del dominio:
  `instradamento/09-analisi-bando` e `giro-0.3.0/01-matrice-chat`, che misura
  la modalita' chat togliendo `Agent` e `Task` dagli strumenti della sessione
  figlia.

### Modificato
- Il dominio `proposte` prende le sue richieste (issue #20): `instradamento.md`
  ha una riga per ciascuna delle sei skill, `progetti-scrittura` passa la mano
  invece di scrivere senza i criteri del bando, `nucleo/vincoli.md` sezione 4
  non nomina piu' il dominio fra quelli non scritti, e `docs/proposte.md` e'
  cancellato: la fonte di verita' sono le skill. Le due frasi ambigue
  dell'ADR 0020 ("scrivi il work package 3", "draft the impact section") ora
  attivano una skill, misurato due volte su due.
- Senza file la revisione resta agli agenti (issue #29, ADR 0021):
  `nucleo/protocollo-revisione.md` ha una sottosezione "Senza file" che
  ammette i materiali nel prompt, per intero e solo se non hanno gia' un
  percorso, e torna alla modalita' chat quando non ci stanno interi o non si
  possono dare come testo. Gli otto agenti sanno che un materiale puo'
  arrivare nel prompt e che senza percorso di uscita il rapporto e' la
  risposta. `proposte-revisione` e `proposte-coerenza` rinviano al nucleo;
  la riga sulla consegna completa dei rapporti passa nel nucleo.
- Profili `rivista-elsevier.md` e `rivista-rmets.md` completati (issue #10):
  le guide delle sei riviste Elsevier e delle quattro RMetS, che gli
  strumenti di ricerca non aprivano, sono state lette da un browser il
  2026-10-11. Le circa 70 voci `[da verificare]` diventano regole con fonte:
  limiti di parole, abstract, highlights, graphical abstract, stile dei
  riferimenti, livello della data policy, CRediT, testo della dichiarazione
  sull'AI, tipo di peer review e APC. Restano aperti solo i punti che le
  guide non trattano. ADR 0013 registra la lacuna chiusa.
- `plugin.json`: versione 0.3.0. Le righe del giro 0.2.0 non ancora eseguite
  (issue #6 e #7) restano valide e si chiudono dentro questo rilascio.

## [0.2.0] mai rilasciata da sola, esce con la 0.3.0

### Aggiunto
- `nucleo/formati-e-file.md`: il plugin legge e consegna i documenti nel
  formato in cui arrivano (Word, PowerPoint, Excel, PDF), rispetta i template
  imposti e puo' restituire una revisione dentro il documento con modifiche
  tracciate (ADR 0018).
- Skill `generale-presentazione` e agente `generale-revisore-presentazione`:
  mazzi di slide con il tema CIMA per tutti i domini, con griglia di revisione
  propria (ADR 0019). Il template e' in
  `plugin/skills/generale-presentazione/references/tema-cima.pptx`.
- `prove/`: un ciclo di verifica per aggiornamento, con almeno una prova per
  ambiente, e i prompt di regressione per dominio in `prove/domini/`.
  `build.py --check` avvisa quando la versione non ha la sua cartella.
- `prove/evals/giro-0.2.0/`: le righe misurabili del giro 0.2.0 come casi per
  `claude plugin eval`, con i materiali portati dallo `scaffold_script`. Le
  righe chat restano a mano, perche' l'eval da' sempre lo strumento `Agent`.
  I grader sugli agenti accettano `Agent` e `Task`. Il caso del comunicato
  diventa la riga 17. `prove/README.md` spiega come si esegue e quanto costa.

### Modificato
- Il punto medio e' vietato come il trattino em, nel nucleo e nei controlli
  bloccanti della build (ADR 0014).
- `plugin.json`: versione 0.2.0, descrizione e parole chiave aggiornate, via
  il nome di prodotto dalla descrizione.

## [Non rilasciato]

### Aggiunto
- Nucleo comune: vincoli, anti-pattern AI, verifica fonti, voce e lingua,
  terminologia, protocollo di revisione.
- Script di build e validazione (`scripts/build.py`).
- Copia di riferimento di `cima-writing-style` v0.1.0 in `legacy/`.
- Quarto dominio `progetti` (deliverable e report di progetti finanziati),
  separato da `generale` (brief v2).
- Dominio generale (PR #1): skill `generale-scrittura`,
  `generale-revisione`, `generale-traduzione`; agente `generale-revisore`.
- `plugin/condivisi/<dominio>/`: riferimenti comuni alle skill di un
  dominio, iniettati dalla build (brief v5).

- Dominio progetti: skill `progetti-scrittura`, `progetti-revisione`,
  `progetti-risposta-review`; agente `progetti-revisore`; file comuni in
  `plugin/condivisi/progetti/` (brief v6).
- `CLAUDE.md`: guida per chi sviluppa con Claude Code.
- `CONTEXT.md`: glossario del repository (dominio, nucleo, revisione,
  modalità, segnaposto), distinto da `nucleo/terminologia.md`, che è la
  terminologia dei testi prodotti.
- `docs/adr/`: una decisione per file, con il perché e le alternative
  scartate (17 ADR, di cui uno aperto).
- Dominio paper: skill `paper-scrittura`, `paper-revisione`,
  `paper-risposta-revisori`; agenti `paper-revisore` e `paper-editor`;
  profili di sei editori e quattro conferenze in `plugin/condivisi/paper/`.
- `docs/`: `scrivere-una-skill.md` (convenzioni per skill e agenti),
  `instradamento.md` (confini fra domini), `proposte.md` (specifica del
  dominio non ancora scritto), `prove/<dominio>.md` (prompt di prova).

### Rimosso
- `BRIEF.md`: sciolto nei file che hanno già la sua materia, perché era
  diventato copia di `build.py`, delle skill e della struttura delle cartelle
  (ADR 0017).
- `legacy/cima-writing-style/`: resta nella storia git, il plugin è installato
  a parte e il dominio generale che ne doveva nascere è scritto.
- Branch e worktree per dominio: si lavora su `main` (ADR 0016).

### Modificato
- `README-dominio.md` dalle cartelle delle skill a `docs/prove/<dominio>.md`:
  il sorgente del plugin resta solo plugin, e la build non deve più escluderli.
- ADR 0013: i profili di rivista sono sei per editore, non tre per rivista.
- Brief v7 (poi sciolto): la sezione 8 diventa l'indice degli ADR; "chat hub" e "chat di
  dominio" diventano "sessione hub" e "sessione di dominio", per non
  confonderle con la modalità chat in cui girano le skill.
- `generale-revisione`: "livello di intervento" diventa "tipo di
  intervento", per non confonderlo con il livello di revisione del nucleo.
- `plugin/condivisi/generale/`: le intestazioni chiedevano di modificare
  tutte le copie insieme, istruzione superata dalla fonte unica di
  dominio (ADR 0004) e contraria al controllo della build.
- `build.py`: sottocartelle ammesse in `plugin/condivisi/<dominio>/`.
- Protocollo di revisione: ai livelli standard e completo, autorevisione
  ammessa per testi brevi scritti da soli, mai per testi da pubblicare.
- `build.py --check` lavora in una cartella temporanea invece che in
  `dist/.check/`.

### Deciso

Dalla versione 7 del brief ogni decisione ha il suo file in `docs/adr/`.

- Una riscrittura è scrittura: se una skill di revisione riscrive un testo
  pubblico, il revisore separato diventa obbligatorio come in
  `generale-scrittura` (ADR 0011).
- Le decisioni architetturali si registrano in `docs/adr/` invece che
  nell'elenco numerato del brief (ADR 0001).
- Riviste di riferimento del dominio paper: gruppo Elsevier, gruppo
  Nature, GMD.
- `generale-revisore` solo per testi pubblici o istituzionali e su
  richiesta; protocollo di revisione aggiornato per il livello leggero
  (brief v3).
- Ogni skill deve consegnare il risultato completo anche in chat, senza
  agenti: regola nel brief (v4) e nel protocollo di revisione; la build
  blocca le skill che nominano un agente senza sezione "Modalità chat".
- La traduzione di qualsiasi testo va a `generale-traduzione` (brief v5).
