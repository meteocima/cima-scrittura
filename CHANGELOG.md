# Changelog

## [Non rilasciato]

### Aggiunto
- Brief di architettura (`BRIEF.md`).
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
  scartate (15 ADR, di cui uno aperto).

### Modificato
- Brief v7: la sezione 8 diventa l'indice degli ADR; "chat hub" e "chat di
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
