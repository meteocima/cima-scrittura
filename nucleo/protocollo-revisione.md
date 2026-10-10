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

## 2. Livelli di revisione

Ogni skill di dominio dichiara il proprio livello.

| Livello | Uso tipico | Modalità agenti | Modalità chat |
|---|---|---|---|
| Leggero | email, testi brevi | 1 revisore | autorevisione con checklist |
| Standard | paper, report | 2–3 revisori + sintesi | autorevisione dichiarata + pacchetto revisore |
| Completo | proposte di progetto | 3 valutatori + rapporteur | autorevisione dichiarata + pacchetto revisore |

## 3. Modalità agenti

### Preparazione

1. Salvare il testo da valutare in un file (es. `revisione/bozza.md` o il
   .docx originale) nella cartella di lavoro.
2. Salvare in file anche i materiali di riferimento: bando, linee guida
   della rivista, griglia di valutazione.
3. Lanciare i revisori **in parallelo** (tutti nella stessa chiamata),
   con l'agente indicato dalla skill di dominio.

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
