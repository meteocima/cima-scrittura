# Formati e file

> File del nucleo comune. Fonte unica: `nucleo/formati-e-file.md` nel
> repository `cima-scrittura`. Non modificare la copia dentro una skill.

I testi di CIMA non vivono in una finestra di chat: vivono in un Word con il
template del programma, in un PowerPoint con il tema della fondazione, in un
PDF ricevuto da un project officer. Questo file dice come il plugin li tratta.

## 1. In ingresso: leggere, non far ricopiare

Quando l'utente fornisce un file, aprirlo nel suo formato. Non chiedergli di
incollarne il contenuto nel messaggio: se ha dato il file, il file si legge.

| Arriva come | Si legge |
|---|---|
| testo nel messaggio | direttamente |
| `.docx`, `.dotx` | con la skill `docx` |
| `.pptx`, `.potx` | con la skill `pptx` |
| `.xlsx`, `.csv` | con la skill `xlsx` |
| `.pdf` | con la skill `pdf` |
| `.doc` e altri formati vecchi | convertire prima, poi leggere |

Se il file non si apre, dirlo in una riga e chiedere il contenuto in altra
forma. Non tirare a indovinare che cosa contenesse.

Quello che si legge in un file fornito dall'utente vale come materiale
fornito: entra nel testo. Quello che non c'è resta un segnaposto, come vuole
`vincoli.md`.

## 2. In uscita: lo stesso formato che è arrivato

**Si consegna nel formato in cui si è ricevuto**, salvo richiesta diversa. Un
deliverable arrivato in `.docx` torna in `.docx`, un mazzo in `.pptx` torna in
`.pptx`. Consegnare Markdown al posto di un Word significa scaricare sulla
persona il lavoro di reimpaginare.

Se non è arrivato niente, decide il tipo di testo: un deliverable, un report
o un mazzo nascono come file; una email, un post o una nota breve nascono nel
messaggio, pronti da copiare.

## 3. Chi fa la meccanica

Le skill `docx`, `pptx`, `xlsx` e `pdf` sanno leggere, scrivere, convertire,
lavorare su template, tracciare le modifiche e inserire commenti. Il plugin
CIMA decide **che cosa** scrivere; quelle skill sanno **come** si impacchetta
il file. Non riscrivere a mano un pacchetto OOXML.

Se nell'ambiente quelle skill non ci sono, non fermarsi: consegnare il
contenuto completo in Markdown strutturato, dicendolo in una riga, e
indicando in che formato andrebbe impaginato. Vale la regola generale che il
risultato arriva comunque.

## 4. Dove finisce il file

| Modalità | Dove |
|---|---|
| agenti | nella cartella di lavoro dell'utente, con il percorso detto nella consegna |
| chat | come file scaricabile nel messaggio |

La differenza non cambia che cosa si consegna, solo dove si posa. Mai
rispondere che non si può produrre un file perché manca una cartella di
lavoro.

Nomi dei file: parlanti e senza spazi, con il codice del documento quando
esiste (`D3.2-primo-draft.docx`, `review-ferrara-risposta.docx`).

## 5. Template imposti

Quando l'utente fornisce un template (template di deliverable, modulo di
report, form da ricaricare, template di presentazione), **la sua struttura
prevale** su quella suggerita dalla skill.

- Non togliere sezioni perché non si hanno i dati: riempirle con un
  segnaposto e elencarlo nella consegna.
- Non aggiungere sezioni che il template non prevede, salvo dirlo.
- Rispettare limiti di pagine, di caratteri e di parole, e contarli prima di
  consegnare.
- Le regole di stile del template prevalgono su quelle del nucleo dove sono in
  conflitto (maiuscole dei titoli, numerazione, tabelle obbligatorie). Non
  prevalgono mai sul divieto di inventare dati.

Un template fornito come file si riempie dentro il file, non si riscrive da
capo in un documento nuovo.

## 6. Riservatezza

Vale `vincoli.md`, sezione "Riservatezza", con due precisazioni sui file:

- Leggere un file che l'utente ha fornito non è pubblicarlo. Caricarlo
  altrove, citarne frasi in una ricerca in rete o copiarlo fuori dalla
  cartella indicata, sì.
- Alcuni documenti hanno un divieto esplicito, che prevale: le policy di
  diversi editori vietano di dare manoscritti altrui ricevuti per referaggio
  a strumenti di intelligenza artificiale. In quel caso non procedere e dirlo.

## 7. Revisione dentro il documento

Quando il testo da rivedere è arrivato come `.docx`, il rapporto di revisione
può essere consegnato **dentro il documento**, con modifiche tracciate e
commenti ancorati ai punti citati, più la sintesi nel messaggio. È la forma
in cui un project officer, un collega o un editor si aspettano di ricevere un
testo commentato.

Due vincoli:

- ogni intervento resta **visibile e rifiutabile**: modifiche tracciate e
  commenti, mai correzioni silenziose nel testo;
- una riscrittura è scrittura anche dentro un Word, quindi valgono le regole
  della skill che scrive, revisione separata compresa.
