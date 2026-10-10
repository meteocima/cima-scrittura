# Changelog

## [0.2.0] in lavorazione

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
