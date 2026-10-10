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

### Modificato
- `build.py`: sottocartelle ammesse in `plugin/condivisi/<dominio>/`.
- Protocollo di revisione: ai livelli standard e completo, autorevisione
  ammessa per testi brevi scritti da soli, mai per testi da pubblicare.
- `build.py --check` lavora in una cartella temporanea invece che in
  `dist/.check/`.

### Deciso
- Riviste di riferimento del dominio paper: gruppo Elsevier, gruppo
  Nature, GMD.
- `generale-revisore` solo per testi pubblici o istituzionali e su
  richiesta; protocollo di revisione aggiornato per il livello leggero
  (brief v3).
- Ogni skill deve consegnare il risultato completo anche in chat, senza
  agenti: regola nel brief (v4) e nel protocollo di revisione; la build
  blocca le skill che nominano un agente senza sezione "Modalità chat".
- La traduzione di qualsiasi testo va a `generale-traduzione` (brief v5).
