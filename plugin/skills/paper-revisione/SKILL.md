---
name: paper-revisione
description: Peer review simulata di un manoscritto scientifico degli autori CIMA prima della sottomissione - due o tre revisori con profili diversi (metodologico, di dominio, applicativo) e un editor che sintetizza, controlla la conformità alla rivista e decide (accept, minor, major, reject). In Cowork lancia revisori indipendenti in parallelo; in chat svolge tutti i passaggi. Triggers - "revisione del paper", "peer review simulata", "cosa direbbero i revisori", "pre-submission review", "mock review", "review my manuscript". Non usare per - referaggio di manoscritti altrui ricevuti come revisore (vietato o limitato dalle policy delle riviste), risposta ai commenti ricevuti (paper-risposta-revisori), scrittura di sezioni (paper-scrittura), proposte di progetto (proposte-*), deliverable e report (progetti-*), testi generici e traduzioni (generale-*).
---

# Peer review simulata prima della sottomissione

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.

Livello di revisione del dominio: **standard** (2–3 revisori + sintesi).

## Deroghe allo stile di base

- I rapporti dei revisori seguono le convenzioni della peer review:
  commenti numerati, divisi in major e minor, anche in forma di elenco.
- **Lingua**: il rapporto è nella lingua dell'utente
  (`voce-e-lingua.md`). La sezione "Commenti per gli autori" si scrive
  in inglese se l'utente lo chiede, per avere un'idea di come arriverebbe
  dalla rivista.

## Limite d'uso

Solo manoscritti di cui l'utente è autore o coautore. Se il testo è un
manoscritto altrui ricevuto per referaggio, non procedere: le policy
di diversi editori vietano di generare il report con l'AI o di caricare
il manoscritto su strumenti AI (es. Copernicus: "Referee comments and
reports should always be written by persons"; Nature Portfolio chiede ai
revisori di non caricarlo su strumenti non sicuri). Dirlo in una riga.

## 1. Raccogliere i materiali

- **Manoscritto** completo (file o testo), con didascalie. Se le figure
  mancano, i revisori giudicano dalle didascalie e lo dichiarano.
- **Rivista e tipo di articolo**. Senza rivista: revisione con le regole
  generali e conformità non controllata, dichiarato nel rapporto.
- Facoltativi: supplemento, guida della rivista, cover letter. La
  cover letter contiene le intenzioni degli autori: va solo all'editor,
  mai ai revisori né nel pacchetto revisore (come nelle riviste reali).

## 2. Caricare le regole della rivista

| Editore | File |
|---|---|
| Elsevier | `references/rivista-elsevier.md` |
| Nature Portfolio | `references/rivista-nature-portfolio.md` |
| Copernicus / EGU | `references/rivista-copernicus.md` |
| AGU | `references/rivista-agu.md` |
| AMS | `references/rivista-ams.md` |
| RMetS / Wiley | `references/rivista-rmets.md` |

Regole comuni dell'editore, poi la sezione della rivista. Voci
`[da verificare]` rilevanti per la conformità: verificarle con la
ricerca web sulla pagina ufficiale, oppure riportarle nel rapporto come
"non controllato". Rivista di un editore non elencato: chiedere la guida
all'utente o leggerla dalla fonte ufficiale, mai a memoria. La guida
fornita dall'utente prevale sul profilo.

## 3. Scegliere i revisori

Profili in `references/profili-revisori.md`:

- **Revisore A, metodologico**: sempre.
- **Revisore B, di dominio**: sempre. Il campo (idrologia,
  meteorologia, clima, rischio, telerilevamento…) si ricava dal
  manoscritto e dall'ambito della rivista.
- **Revisore C, applicativo**: per riviste e articoli orientati all'uso
  (es. NHESS, Meteorological Applications, Weather and Forecasting,
  Earth's Future) o su richiesta dell'utente.
- **Editor**: sempre; sintesi, conformità, decisione.

Griglia comune: `references/griglia-revisione.md`.
Formati dei rapporti: `references/formato-rapporto.md`.

## 4. Modalità agenti

Si usa quando è disponibile lo strumento per lanciare subagent (regola
in `references/nucleo/protocollo-revisione.md`, sezione 1).

1. Creare nella cartella di lavoro la sottocartella `revisione-paper/`.
   Salvare il manoscritto come `revisione-paper/manoscritto.md` (o
   copiare il .docx originale) e gli eventuali materiali forniti, la
   cover letter a parte. Nei prompt usare sempre percorsi assoluti.
2. Lanciare **in parallelo** (nella stessa chiamata) un agente
   `paper-revisore` per ciascun revisore scelto. Il prompt contiene solo:
   - percorso del manoscritto e dei materiali (non la cover letter);
   - percorsi assoluti di `references/griglia-revisione.md`,
     `references/formato-rapporto.md`, del profilo della rivista
     (`references/rivista-*.md`) e di `references/nucleo/anti-pattern-ai.md`
     e `references/nucleo/verifica-fonti.md` (la skill conosce la propria
     cartella base: costruire i percorsi da lì);
   - il profilo del revisore, copiato da `profili-revisori.md`, con il
     campo di dominio;
   - nome della rivista e tipo di articolo;
   - lingua del rapporto (quella dell'utente) e lingua dei "Commenti
     per gli autori" (inglese se l'utente lo ha chiesto);
   - il percorso del rapporto: `revisione-paper/rapporto-A.md`, `-B`,
     `-C`.

   Mai nel prompt: riassunti della conversazione, intenzioni degli
   autori, punti di forza da notare, giudizi anticipati.
3. Quando i rapporti sono pronti, lanciare l'agente `paper-editor` con:
   percorsi dei rapporti, del manoscritto (per la conformità e per
   controllare le citazioni dei revisori), dell'eventuale cover letter,
   del profilo della rivista, di `griglia-revisione.md` e
   `formato-rapporto.md`; nome della rivista e tipo di articolo; lingua
   della decisione; percorso di uscita
   `revisione-paper/decisione-editor.md`.
4. Presentare all'utente la decisione dell'editor e la lista di
   correzioni, con i percorsi dei singoli rapporti. Non contestare i
   rapporti per difendere il testo: se un giudizio nasce da
   un'informazione assente dal manoscritto, la correzione è aggiungerla.
5. Proporre le correzioni, in ordine di impatto. Riscrivere solo su
   richiesta, rispettando la policy sull'AI della rivista (per le riviste
   Copernicus solo interventi su leggibilità e lingua del testo degli
   autori).

Se un lancio fallisce, passare alla modalità chat e dirlo in una riga.

## Modalità chat

Senza subagent la skill svolge da sola, nel contesto principale, il
lavoro di ogni `paper-revisore` e del `paper-editor`, con le stesse
regole e gli stessi formati. Dichiararlo in una riga all'inizio.

1. Aprire il rapporto con la frase della sezione 4a del protocollo
   (revisione nella stessa conversazione, tende all'indulgenza).
2. Per ogni revisore scelto, in sequenza: rileggere il manoscritto
   come se fosse di un altro gruppo, partire dalla ricerca delle
   debolezze, applicare la griglia e scrivere il rapporto completo nel
   formato di `formato-rapporto.md`. Non citare né riprendere i
   rapporti precedenti: ogni rapporto cita solo il manoscritto.
   Verificare i riferimenti citati nel manoscritto con le stesse regole
   dell'agente (ricerca web solo con titoli, autori, DOI e nomi di
   dataset o modelli, mai frasi del manoscritto).
3. Svolgere il passaggio dell'editor sui rapporti appena scritti:
   punti condivisi, divergenze senza media, controllo di conformità con
   la "Checklist di conformità" del profilo, decisione e lista di
   correzioni.
4. Consegnare tutto: rapporti A, B (e C), decisione dell'editor, lista
   di correzioni. In chat, se lungo, un rapporto per messaggio.
5. Offrire il **pacchetto revisore** (protocollo, sezione 4b): un blocco
   da incollare in una nuova conversazione con profilo del revisore,
   griglia, regole, formato, ambito e "Checklist di conformità" della
   rivista dal profilo (o l'indicazione di allegare la guida) e testo
   completo del manoscritto, senza cover letter. Spiegare
   in una riga perché: una conversazione nuova non conosce le intenzioni
   degli autori.
6. In fondo, una sola riga: in Cowork i revisori lavorano in contesti
   indipendenti.

## Consegna

- Decisione simulata e motivazione (2–4 frasi).
- Lista di correzioni ordinata per impatto sulla decisione.
- Divergenze tra revisori, con entrambe le posizioni.
- Conformità alla rivista: voci mancanti e voci non controllate.
- Rapporti completi (file in Cowork, messaggi in chat).
- Riferimenti citati dai revisori e non verificati, se presenti.

La decisione è una simulazione: non prevede l'esito reale e va
presentata così, senza percentuali di accettazione.
