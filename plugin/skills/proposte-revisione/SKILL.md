---
name: proposte-revisione
description: "Valutazione simulata di una proposta europea prima della scadenza, come la farebbe la Commissione: tre valutatori con profili diversi (scientifico, applicativo e utenti finali, gestionale) piu' un rapporteur che consolida, riporta le divergenze senza mediarle e dice se le soglie sono superate. I punteggi vengono dalla griglia reale del bando: senza griglia, nessun punteggio. Dove l'ambiente lo permette lancia valutatori indipendenti in parallelo; altrimenti svolge tutti i passaggi nel contesto principale e lo dichiara. Usare per: 'valutazione simulata', 'come la valuterebbero', 'che punteggio prende', 'mock evaluation', 'evaluate my proposal'. Non usare per: scrivere o riscrivere la proposta (proposte-scrittura); capire i criteri del bando (proposte-analisi-bando); solo coerenza fra sezioni e limiti (proposte-coerenza); rispondere a un ESR ricevuto (proposte-risposta-esr); deliverable e report (progetti-revisione); manoscritti (paper-revisione); testi generici (generale-revisione)."
---

# Valutazione simulata di una proposta

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Poi leggere `references/griglia-valutazione.md`,
`references/profili-valutatori.md` e `references/anti-pattern-proposte.md`.

Livello di revisione del dominio: **completo** (3 valutatori piu' rapporteur).

## Confini

| Richiesta | Chi la prende |
|---|---|
| valutazione simulata di una proposta prima della scadenza | questa skill |
| incoerenze fra sezioni e sforamento dei limiti, senza punteggi | `proposte-coerenza` |
| scrivere o correggere il testo della proposta | `proposte-scrittura` |
| criteri, pesi e soglie del bando | `proposte-analisi-bando` |
| rispondere all'ESR di una valutazione vera | `proposte-risposta-esr` |
| revisione di un deliverable o di un report | `progetti-revisione` |
| peer review simulata di un manoscritto | `paper-revisione` |

## 1. Raccogliere i materiali

- **Proposta** completa o la parte da valutare, con le tabelle. Se mancano
  sezioni, i valutatori lo dichiarano e ne tengono conto.
- **Matrice del bando**, o il testo del topic da cui ricavarla. E' il
  materiale piu' importante: senza, non ci sono punteggi
  (`references/griglia-valutazione.md`, sezione 2).
- Programma e strumento, per caricare il profilo giusto.
- Facoltativi: allegati, lettere di supporto, ESR di una versione precedente.

Se la matrice manca ma c'e' il topic, costruirla prima: e' il passaggio che
rende la valutazione qualcosa di piu' di un parere.

## 2. Preparare la cartella

Dove si possono scrivere file, creare `valutazione/` nella cartella di
lavoro: la proposta in formato leggibile (`proposta.md`), la matrice
(`matrice-bando.md`) e i materiali. Se la proposta arriva in Word o PDF,
ricavarne una versione leggibile: i valutatori hanno strumenti minimi apposta
e non devono poter toccare il documento.

Se i file non si riescono a salvare, seguire
`references/nucleo/protocollo-revisione.md`, sezione 3, "Senza file": i
valutatori ricevono nel prompt, per intero, cio' che non ha gia' un percorso
leggibile (di solito la matrice, e la proposta se e' arrivata in Word o PDF),
il rapporteur i tre rapporti; se non ci stanno interi, modalita' chat. In ogni
caso i tre rapporti e il consolidato arrivano per intero nella stessa risposta,
non promessi per dopo.

## Modalità agenti

Si usa quando e' disponibile lo strumento per lanciare subagent (regola in
`references/nucleo/protocollo-revisione.md`, sezione 1).

1. Lanciare **in parallelo**, nella stessa chiamata, tre agenti
   `proposte-valutatore`, uno per profilo. Il prompt di ciascuno contiene
   solo:
   - percorso della proposta e dei materiali;
   - percorso della matrice del bando;
   - percorsi assoluti di `references/griglia-valutazione.md`,
     `references/anti-pattern-proposte.md`, del profilo del programma
     (`references/programma-*.md`) e di
     `references/nucleo/protocollo-revisione.md` e `references/nucleo/vincoli.md`
     (la skill conosce la propria cartella base: costruire i percorsi da li');
   - il profilo del valutatore, copiato da `profili-valutatori.md`, con il
     campo di dominio;
   - la lingua del rapporto;
   - il percorso del rapporto: `valutazione/rapporto-A.md`, `-B`, `-C`.

   Mai nel prompt: riassunti della conversazione, intenzioni di chi ha
   scritto, spiegazioni di scelte, punti di forza da notare, giudizi
   anticipati, punteggi attesi.
2. Quando i tre rapporti sono pronti, lanciare `proposte-rapporteur` con i
   percorsi dei tre rapporti, della matrice, della griglia, la lingua e il
   percorso di uscita `valutazione/consolidato.md`. Il rapporteur **non**
   riceve la proposta.
3. Presentare all'utente il consolidato e i percorsi dei singoli rapporti.
   Non contestare i rapporti per difendere la proposta: se un giudizio nasce
   da un'informazione assente dal testo, la correzione e' aggiungerla al
   testo.
4. Proporre le correzioni in ordine di impatto. Riscrivere solo su richiesta,
   e allora vale `proposte-scrittura`.

Se un lancio fallisce, passare alla modalita' chat e dirlo in una riga.

## Modalità chat

Senza subagent la skill svolge da sola, nel contesto principale, il lavoro dei
tre `proposte-valutatore` e del `proposte-rapporteur`, con le stesse regole e
gli stessi formati. Dichiararlo in una riga all'inizio.

1. Aprire con la frase della sezione 4a del protocollo: questa valutazione e'
   fatta nella stessa conversazione in cui la proposta e' stata scritta, e
   tende a essere piu' indulgente di una valutazione indipendente.
2. Per ciascuno dei tre profili, in sequenza: rileggere la proposta come se
   fosse di un altro consorzio, partire dalla ricerca delle debolezze,
   applicare la griglia e scrivere il rapporto completo nel formato della
   sezione 5 di `references/griglia-valutazione.md`. Non citare ne' riprendere
   i rapporti precedenti: ogni rapporto cita solo la proposta.
3. Svolgere il passaggio del rapporteur sui tre rapporti appena scritti:
   punti condivisi, divergenze senza media, quadro dei punteggi con le
   soglie, correzioni in ordine di impatto.
4. Consegnare tutto: i tre rapporti e il consolidato. In chat, se lungo, un
   rapporto per messaggio.
5. Offrire il **pacchetto valutatore** (protocollo, sezione 4b): un blocco da
   incollare in una conversazione nuova, con profilo del valutatore, griglia,
   regole, formato, criteri e soglie dalla matrice, e testo completo della
   proposta. Spiegare in una riga perche': una conversazione nuova non conosce
   le intenzioni di chi ha scritto.
6. In fondo, una sola riga: in un ambiente con subagent i tre valutatori
   lavorano in contesti indipendenti.

## Consegna

- Quadro dei punteggi per criterio, con la **scala** a fianco, e il verdetto
  sulle **soglie**: supera o non supera, per criterio e complessivamente.
- Divergenze fra valutatori, con tutte le posizioni e senza media.
- Lista di correzioni ordinata per impatto sul giudizio.
- Rapporti completi (file in modalita' agenti, messaggi in chat).
- Se la proposta e' arrivata come `.docx`, i problemi possono essere riportati
  dentro il documento con commenti e modifiche tracciate
  (`references/nucleo/formati-e-file.md`, sezione 7). Lo fa la skill, non i
  valutatori.

Quando mancano la griglia o il testo, la consegna lo dice al posto dei
punteggi, come prevede la sezione 2 della griglia.

La valutazione e' una simulazione: non prevede l'esito reale, non stima
probabilita' di successo e si presenta cosi'.
