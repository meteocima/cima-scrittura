# Protocollo di revisione: chi scrive non valuta

> File del nucleo comune. Fonte unica: `nucleo/protocollo-revisione.md`
> nel repository `cima-scrittura`. Non modificare la copia dentro una
> skill. Le skill di dominio definiscono griglie, profili dei revisori e
> livello di revisione; questo file definisce il meccanismo, uguale per
> tutti.

## Principio

Un testo valutato dallo stesso contesto che l'ha scritto riceve un
giudizio troppo indulgente: il valutatore conosce le intenzioni
dell'autore e legge quello che voleva scrivere, non quello che ha
scritto. La revisione deve quindi avvenire in un contesto separato, che
vede solo il testo e i criteri.

## 1. Rilevare l'ambiente

Non chiedere all'utente dove si trova: dedurlo dagli strumenti
disponibili.

- **Modalità agenti**: è disponibile lo strumento per lanciare subagent
  (`Agent` o `Task`). Tipicamente Cowork o Claude Code.
- **Modalità chat**: lo strumento non c'è. Tipicamente claude.ai in chat.

In caso di dubbio (strumento presente ma il lancio fallisce), passare alla
modalità chat e dirlo in una riga.

La regola vale per **ogni passaggio** che una skill affida a un agente
(revisione, sintesi, verifica di coerenza, decisione dell'editor), non
solo per la revisione. In modalità chat:

- eseguire quei passaggi nel contesto principale, uno dopo l'altro, con
  le stesse regole e lo stesso formato di output dell'agente;
- dichiarare in una riga quali passaggi non sono indipendenti;
- consegnare comunque il risultato completo: non fermarsi, non chiedere
  all'utente di passare a Cowork. Si può citare Cowork una sola volta,
  in fondo, come modo per avere una revisione indipendente.

## 2. Livelli di revisione

Ogni skill di dominio dichiara il proprio livello. Al livello leggero la
skill elenca anche i tipi di testo che richiedono il revisore separato in
modalità agenti (tipicamente quelli pubblici o firmati a nome
dell'istituzione); per gli altri basta l'autorevisione con checklist,
salvo richiesta dell'utente.

Ai livelli standard e completo una skill può indicare tipi di testo
brevi e scritti da soli (per esempio un executive summary) per cui basta
l'autorevisione con la griglia, salvo richiesta dell'utente. L'eccezione
non vale per i testi destinati alla pubblicazione: per questi, in
modalità agenti, almeno un revisore.

Le due modalità consegnano lo stesso prodotto con una **garanzia diversa**.
In modalità agenti il giudizio viene da un contesto che non ha visto nascere
il testo; in modalità chat viene dallo stesso contesto che lo ha scritto, che
lo dichiara. Non è una differenza da nascondere: la skill la dichiara in una
riga e, per i testi che contano, offre il pacchetto revisore. Chi sceglie
dove lavorare sta scegliendo anche quanto vale la revisione che riceve.

| Livello | Uso tipico | Modalità agenti | Modalità chat |
|---|---|---|---|
| Leggero | email, testi brevi | 1 revisore per i testi indicati dalla skill e su richiesta; altrimenti autorevisione con checklist | autorevisione con checklist |
| Standard | paper, report | 2–3 revisori + sintesi | autorevisione dichiarata + pacchetto revisore |
| Completo | proposte di progetto | 3 valutatori + rapporteur | autorevisione dichiarata + pacchetto revisore |

## 3. Modalità agenti

### Preparazione

1. Salvare il testo da valutare in un file nella cartella di lavoro. Se il
   testo arriva in un formato che il revisore non può aprire da solo (Word,
   PowerPoint, PDF), ricavarne una versione leggibile e passare quella: il
   revisore ha strumenti minimi apposta, e non deve poter toccare il
   documento. Vale per ogni materiale, non solo per il testo: un template in
   Word passato come `.docx` a un revisore che legge solo testo è un
   riferimento che non arriva. Per un mazzo di slide passare anche una
   griglia di anteprime: densità e leggibilità dal solo testo non si vedono.
2. Salvare in file anche i materiali di riferimento: bando, linee guida
   della rivista, **griglia di valutazione**. Senza la griglia il revisore se
   ne inventa una, e due revisori se ne inventano due diverse.
3. Lanciare i revisori **in parallelo** (tutti nella stessa chiamata),
   con l'agente indicato dalla skill di dominio.

**Se i file non si riescono a salvare, la modalità agenti non è praticabile:
passare alla modalità chat e dirlo in una riga.** Non chiedere a un agente di
salvare al posto tuo, e meno che mai al revisore: il revisore ha `Write` solo
per il proprio rapporto, e usarlo come scrivano annulla la separazione per cui
esiste.

### Cosa passare al revisore

Il prompt del revisore contiene **solo**:

- il percorso del testo da valutare;
- i percorsi dei materiali di riferimento (bando, griglia, linee guida);
- il profilo del revisore (es. "esperto scientifico di idrologia",
  "rappresentante degli utenti finali");
- il formato di output richiesto;
- il percorso dove scrivere il rapporto.

Il prompt **non** contiene: riassunti della conversazione, intenzioni
dell'autore, spiegazioni di scelte, punti di forza da notare, giudizi
anticipati ("è una buona bozza"), punteggi attesi. Se un'informazione
serve al revisore, deve stare nel testo o nei materiali di riferimento,
come per un revisore reale.

### Regole per il revisore

- Leggere tutto il testo prima di giudicare.
- **Debolezze prima del punteggio**: elencare problemi e punti di forza,
  poi assegnare il punteggio.
- **Ogni giudizio cita il passaggio** (sezione + frase o tabella). Un
  giudizio senza citazione non conta.
- Segnalare anche ciò che **manca** rispetto ai criteri.
- Non riscrivere il testo: indicare il problema e la direzione della
  correzione.
- Non ammorbidire: il rapporto serve all'autore, non va consegnato a terzi.
- Applicare `anti-pattern-ai.md` come una voce della valutazione, non come
  criterio principale.

### Sintesi (rapporteur)

Quando i revisori sono più di uno, un agente di sintesi (o il contesto
principale, se la skill lo prevede) legge solo i rapporti e produce:

- punti condivisi da più revisori (priorità alta);
- **divergenze** superiori a 1 punto sulla scala o giudizi opposti sullo
  stesso passaggio: riportarle con entrambe le posizioni, senza fare la
  media;
- lista di correzioni ordinata per impatto sul giudizio finale.

### Dopo la revisione

Il contesto principale (lo scrittore) riceve il rapporto, lo presenta
all'utente e propone le correzioni. Non contesta il rapporto per
difendere la bozza: se un giudizio è sbagliato per un'informazione
mancante nel testo, la correzione è aggiungere l'informazione al testo.

## 4. Modalità chat

Senza subagent non c'è indipendenza di contesto. Fare due cose.

### a) Autovalutazione dichiarata

Eseguire la revisione con la stessa griglia e lo stesso formato, aprendo
il rapporto con questa riga:

> Questa revisione è fatta nella stessa conversazione in cui il testo è
> stato scritto: tende a essere più indulgente di una revisione
> indipendente.

Per ridurre l'indulgenza: rileggere il testo come se fosse di un altro
gruppo, partire dalla ricerca delle debolezze, citare i passaggi.

### b) Pacchetto revisore

Offrire un blocco unico da copiare in una **nuova conversazione**, che
contenga:

1. il ruolo e il profilo del revisore;
2. la griglia e le regole della sezione "Regole per il revisore";
3. il formato di output;
4. il testo completo da valutare e, se brevi, i materiali di riferimento
   (altrimenti l'indicazione di allegarli).

Spiegare in una riga perché: una conversazione nuova non conosce le
intenzioni dell'autore, quindi giudica il testo per quello che è.

## 5. Formato comune del rapporto

```
## Sintesi
[2–4 frasi: giudizio complessivo e problema principale]

## Punteggi (se la griglia li prevede)
| Criterio | Punteggio | Motivazione in una riga |

## Problemi
| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
Gravità: bloccante / importante / minore

## Punti di forza
[solo quelli che un valutatore citerebbe, con posizione]

## Cosa manca
[elementi richiesti dai criteri e assenti dal testo]
```

Le skill di dominio possono aggiungere sezioni (es. commenti in stile ESR
per le proposte) ma non toglierne.

**Testo troppo incompleto per essere valutato.** Se quello che arriva è in
gran parte segnaposto, non assegnare punteggi: un punteggio minimo su un
testo che non esiste ancora sembra un giudizio e non lo è. Scrivere invece,
al posto dei punteggi, che non c'è abbastanza testo da valutare ed elencare
che cosa serve perché la revisione abbia senso. I problemi che si vedono già
si segnalano lo stesso.

### Rapporto dentro il documento

Quando il testo è arrivato come `.docx`, il rapporto può essere riportato
**dentro il documento**, con modifiche tracciate e commenti ancorati ai punti
citati, più la sintesi nel messaggio. Regole e vincoli in
`formati-e-file.md`, sezione 7.

Lo fa la skill, non il revisore: il revisore consegna il rapporto nel formato
qui sopra, la skill lo riporta nel documento. Cosi' chi valuta non ha mai gli
strumenti per modificare il testo valutato.
