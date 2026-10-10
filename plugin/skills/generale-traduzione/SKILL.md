---
name: generale-traduzione
description: "Traduce e adatta testi di Fondazione CIMA dall'italiano all'inglese e dall'inglese all'italiano: email, lettere, comunicati, pagine web, post, verbali, report interni. Usa la terminologia CIMA, le convenzioni di ciascuna lingua (British English, date, numeri, titoli, formule di saluto) e il registro del destinatario; non aggiunge né toglie fatti e segnala le scelte di traduzione. Per abstract, paper, proposte e deliverable traduce lingua e terminologia senza cambiarne struttura e contenuto. Usare per 'traduci in inglese', 'versione inglese', 'mettilo in italiano', 'adatta per un pubblico internazionale', 'translate into Italian', 'English version of this'. Non usare per scrivere da zero un testo in un'altra lingua (generale-scrittura o la skill del dominio), per rivedere un testo (generale-revisione), per riscrivere o migliorare un paper, una proposta o un deliverable (skill paper-, proposte-, progetti-)."
---

# Traduzione e adattamento IT/EN

Questa skill porta un testo esistente dall'italiano all'inglese o
viceversa. Adatta, non calca: il testo tradotto deve sembrare scritto
nella lingua di arrivo da un ricercatore CIMA, con gli stessi fatti
dell'originale.

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Riferimenti del dominio:

- `references/traduzione.md`: convenzioni, formule, titoli, nomi propri,
  falsi amici;
- `references/destinatari.md`: tono per destinatario nella lingua di
  arrivo.

## Confini

- **Testi del dominio generale**: traduzione e adattamento completi
  (registro, formule, struttura del tipo nella lingua di arrivo).
- **Abstract, paper, proposte, deliverable**: tradurre lingua e
  terminologia; struttura, sezioni, ordine e contenuto restano quelli
  dell'originale. Se il testo deve anche rispettare limiti o regole del
  dominio (parole dell'abstract, pagine della Part B), segnalarlo e
  indicare la skill del dominio per l'adattamento.
- **Richiesta di tradurre e migliorare**: tradurre prima, poi applicare
  `generale-revisione` alla traduzione se il testo è generale, oppure
  indicare la skill del dominio.

## Flusso di lavoro

1. **Lingue e testo**: lingua di partenza e di arrivo. Se l'utente chiede
   "versione inglese" di un testo italiano non serve chiedere altro.
2. **Tipo e destinatario** nella lingua di arrivo: dedurli. Un comunicato
   italiano per la stampa locale tradotto per un partner internazionale
   cambia destinatario: dirlo e adattare il registro secondo
   `destinatari.md` e la sezione "Cambio di destinatario" di
   `traduzione.md`.
3. **Leggere `traduzione.md`** per la coppia di lingue.
4. **Tradurre** per frasi e paragrafi, non per parole. Mantenere ogni
   fatto, cifra, nome e riserva dell'originale. Non aggiungere spiegazioni
   che l'originale non contiene, salvo l'espansione di sigle nazionali
   per un lettore straniero (`traduzione.md`).
5. **Controlli sul testo tradotto**:
   - termini di `terminologia.md` nella lingua di arrivo;
   - numeri, date, virgolette e acronimi secondo `voce-e-lingua.md`;
   - titoli e formule secondo `traduzione.md`;
   - nomi di enti, programmi, norme: forma ufficiale verificata o
     originale (`traduzione.md`, sezione "Nomi propri");
   - anti-pattern di `anti-pattern-ai.md` introdotti dalla traduzione
     (nominalizzazioni dall'italiano, anglicismi verso l'italiano, Title
     Case nei titoli inglesi);
   - segnaposto `[…]` dell'originale conservati e tradotti.
6. **Consegna**: testo tradotto, poi note di traduzione.

## Anti-pattern dell'originale

Il testo da tradurre è dell'utente. Correggere in silenzio solo la
tipografia della lingua di arrivo (trattino em, punto medio, virgolette, spazi,
maiuscole dei titoli). Gli altri anti-pattern dell'originale (superlativi,
lessico vuoto, aperture di rito) si traducono fedelmente e si segnalano
nelle note con la citazione, salvo che l'utente abbia chiesto anche di
migliorare il testo.

## Citazioni di persone

Una citazione tradotta (per esempio nel comunicato) mette in bocca alla
persona parole che non ha detto in quella lingua. Tradurla e indicare
nelle note che la persona deve approvarla.

## Deroghe allo stile di base

- Struttura e lunghezza seguono l'originale, salvo i cambi richiesti
  dalle convenzioni della lingua di arrivo (formule della lettera,
  ordine di data e luogo).
- Nei testi di paper, proposte e deliverable restano valide le deroghe
  del dominio di origine ("we", struttura IMRAD, struttura del template).

## Consegna

1. Il testo tradotto, **nello stesso formato in cui è arrivato**
   (`references/nucleo/formati-e-file.md`): un Word torna Word, un mazzo di
   slide torna mazzo, con struttura e impaginazione intatte. Un testo
   incollato torna nel messaggio, pronto da copiare.
2. **Note di traduzione**, solo se ce ne sono:
   - scelte terminologiche non ovvie, con il termine originale;
   - passaggi ambigui nell'originale e come sono stati resi;
   - nomi di enti, programmi o norme non verificati, lasciati in forma
     originale;
   - citazioni di persone da far approvare;
   - anti-pattern dell'originale tradotti fedelmente.
3. **Segnaposto da completare**, se presenti.

Per testi bilingui richiesti insieme (es. "dammi IT e EN"): le due
versioni una dopo l'altra, con un'unica sezione di note.
