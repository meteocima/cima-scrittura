---
name: generale-scrittura
description: "Scrive testi del dominio generale per Fondazione CIMA, in italiano e in inglese: email esterne e interne, lettere ufficiali e istituzionali (ministeri, Regioni, enti locali, organizzazioni internazionali), comunicati stampa, verbali anche da trascrizione o appunti, report interni, testi web, post social. Applica il nucleo CIMA: niente dati inventati, segnaposto per ciò che manca, verifica delle fonti, controllo anti-pattern AI. Usare per 'scrivi una email', 'bozza di lettera', 'comunicato stampa', 'fai il verbale', 'post per LinkedIn', 'draft an email', 'write a letter', 'press release', 'meeting minutes', 'social post'. Non usare per abstract, articoli, cover letter e risposte ai revisori (skill paper-), proposte, bandi ed ESR (proposte-), deliverable, report e risposte di merito a review di progetti finanziati (progetti-), rilettura di un testo esistente (generale-revisione), traduzioni (generale-traduzione)."
---

# Scrittura generale CIMA

Questa skill scrive i testi quotidiani e istituzionali di Fondazione CIMA.
Livello di revisione: **leggero** (`references/nucleo/protocollo-revisione.md`,
sezione 2).

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Riferimenti del dominio:

- `references/tipologie.md`: struttura e regole per ogni tipo di testo, e
  quali tipi richiedono il revisore separato;
- `references/destinatari.md`: tono per destinatario;
- `references/checklist.md`: checklist di autorevisione;
- `references/esempi.md`: esempi prima e dopo.

## Confini

| Richiesta | Cosa fare |
|---|---|
| email, lettera, comunicato, verbale, report interno, testo web, post | questa skill |
| abstract per conferenza o rivista, articolo, cover letter, risposta ai revisori | dominio paper |
| proposta, bando, Part B, ESR, abstract di una proposta | dominio proposte |
| deliverable, report periodico, technical report di un progetto finanziato | dominio progetti |
| email di routine a un project officer (date, riunioni, logistica, invio di documenti) | questa skill; il report allegato va a progetti |
| risposta di merito a project officer o reviewer di progetto (review report, deliverable respinto, chiarimenti) | `progetti-risposta-review` |
| rileggere un testo già scritto dall'utente | `generale-revisione` |
| tradurre un testo | `generale-traduzione` |

Se la richiesta appartiene a un altro dominio, dirlo in una riga e
indicare la skill. Se quella skill non è disponibile, svolgere comunque il
compito applicando il nucleo, e dire che mancano le regole specifiche del
dominio.

## Flusso di lavoro

1. **Lingua.** Dedurla secondo `voce-e-lingua.md`. Se è ambigua, una sola
   domanda.
2. **Tipo e destinatario.** Dedurli dalla richiesta. Leggere la sezione del
   tipo in `tipologie.md` e quella del destinatario in `destinatari.md`.
   Se il tipo non è chiaro, una sola domanda. Se manca solo il
   destinatario, procedere col registro più probabile e dichiararlo.
3. **Fatti.** Usare solo ciò che l'utente ha fornito (messaggio, file,
   thread inoltrati). Per ogni dato che serve e manca, un segnaposto
   `[…]`. Non fare una raffica di domande: scrivere la bozza con i
   segnaposto. Chiedere prima solo se manca l'informazione che decide il
   senso del testo (per esempio: accettiamo o rifiutiamo?).
4. **Fonti.** Se il testo cita studi, dati di terzi, norme o documenti,
   seguire `verifica-fonti.md` prima di scrivere.
5. **Bozza.** Seguire la struttura del tipo. Guardare `esempi.md` per il
   tipo, se c'è un esempio.
6. **Autorevisione.** Sempre: applicare `checklist.md` (sezioni A–E) e
   correggere.
7. **Revisione separata.** Se il tipo la richiede secondo la tabella di
   `tipologie.md` (lettere ufficiali, comunicati, testi web e social
   pubblici) o se l'utente la chiede per qualsiasi testo: sezione
   "Revisione separata" sotto. Negli altri casi l'autorevisione basta.
8. **Consegna.** Formato nella sezione "Consegna".

## Verbale da trascrizione o appunti

Seguire `tipologie.md`, sezione 5, sottosezione "Verbale da trascrizione o
appunti". In breve: leggere tutto, sintetizzare, separare decisioni e
discussione, attribuire solo ciò che è chiaro, marcare ogni incertezza con
`[da verificare: …]`, tabella delle azioni con responsabile e scadenza o
segnaposto. Trascrizioni lunghe: dire nella consegna quali parti non è
stato possibile interpretare.

## Revisione separata

Serve per i tipi indicati in `tipologie.md` e quando l'utente la chiede.
La modalità si deduce dagli strumenti disponibili
(`protocollo-revisione.md`, sezione 1).

## Modalità agenti

Strumento per lanciare subagent disponibile (`Agent` o `Task`):

1. Salvare la bozza in un file nella cartella di lavoro dell'utente
   (la cartella collegata o, se manca, la cartella di output della
   sessione): `revisione/bozza-[tipo].md`.
2. Costruire i percorsi assoluti dei riferimenti a partire dalla cartella
   base di questa skill, indicata al caricamento.
3. Lanciare l'agente `generale-revisore` con un prompt che contiene
   **solo** quanto segue:

   ```
   Testo da valutare: [percorso assoluto della bozza]
   Tipo di testo: [tipo, come in tipologie.md]
   Destinatario: [destinatario, come in destinatari.md]
   Riferimenti:
   - [base]/references/tipologie.md
   - [base]/references/destinatari.md
   - [base]/references/checklist.md
   - [base]/references/nucleo/vincoli.md
   - [base]/references/nucleo/anti-pattern-ai.md
   - [base]/references/nucleo/voce-e-lingua.md
   - [base]/references/nucleo/terminologia.md
   - [base]/references/nucleo/protocollo-revisione.md
   Formato: protocollo-revisione.md, sezione 5, senza punteggi.
   Lingua del rapporto: [lingua in cui scrive l'utente]
   Rapporto da scrivere in: [cartella di lavoro]/revisione/rapporto-[tipo].md
   ```

   Niente riassunti della conversazione, intenzioni, scelte fatte o
   giudizi anticipati (`protocollo-revisione.md`, "Cosa passare al
   revisore"). Se il revisore deve sapere un fatto, il fatto deve stare
   nel testo.
4. Leggere il rapporto. Non contestarlo per difendere la bozza.
5. Applicare le correzioni che non richiedono nuove informazioni o scelte
   dell'utente; elencare le altre come proposte.

Se il lancio fallisce, passare alla modalità chat e dirlo in una riga.

## Modalità chat

Strumento per lanciare subagent non disponibile:

1. Svolgere la revisione nel contesto principale con la stessa
   `checklist.md`, rileggendo il testo come se fosse di un altro gruppo e
   partendo dalle debolezze.
2. Aprire il rapporto con la riga di `protocollo-revisione.md`, sezione 4a.
3. Usare lo stesso formato del revisore (sezione 5 del protocollo, senza
   punteggi), nella lingua in cui scrive l'utente. Per testi brevi basta la tabella dei problemi.
4. Applicare le correzioni come al punto 5 della modalità agenti e
   consegnare il testo finale completo.
5. Per comunicati, lettere ufficiali e testi web pubblici offrire in fondo
   il pacchetto revisore (sezione 4b del protocollo) in un unico blocco da
   copiare in una conversazione nuova. Si può citare Cowork una sola
   volta, come modo per avere una revisione indipendente.

Non fermarsi e non chiedere all'utente di cambiare ambiente: il testo
finale arriva comunque.

## Deroghe allo stile di base

Rispetto a `voce-e-lingua.md`:

- **Email interne**: "noi" e registro informale ammessi; saluti e firme
  ridotti o assenti.
- **Verbali**: elenchi e tabelle ammessi per presenti, decisioni e azioni.
- **Post social**: frasi più brevi, paragrafi di una riga, hashtag e
  menzioni forniti dall'utente. Emoji restano vietate.
- **Lettere ufficiali**: struttura e formule della sezione 3 di
  `tipologie.md` prevalgono sulla regola dei paragrafi brevi quando un
  riferimento lungo (norma, protocollo) lo richiede.

## Consegna

- **Testi brevi** (email, post, lettere fino a una pagina): nel messaggio,
  pronti da copiare, senza frasi introduttive.
- **Testi lunghi** (report interni, verbali lunghi, pagine web): in
  modalità agenti un file .md o .docx nella cartella di lavoro, se
  l'utente non chiede altro; in chat nel messaggio, una sezione alla volta
  se molto lungo.
- Dopo il testo, in quest'ordine e solo se presenti:
  1. **Segnaposto da completare**: elenco di tutti i `[…]` inseriti.
  2. **Fonti**: verificate, corrette o non trovate.
  3. **Revisione**: per i testi con revisione separata, sintesi del
     rapporto in 2–4 righe, correzioni applicate, proposte aperte. Per
     gli altri, una riga che dice che l'autorevisione è stata fatta.
  4. **Assunzioni**: tipo, destinatario o lingua dedotti e non dichiarati.
- Mai inserire nel testo da inviare frasi rivolte all'utente.
