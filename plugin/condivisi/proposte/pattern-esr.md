# Pattern dagli ESR reali

Che cosa hanno scritto davvero i valutatori sulle proposte di CIMA, ridotto a
pattern anonimi. Lo leggono il valutatore simulato, per tarare il punteggio,
e chi lavora su un ESR ricevuto, per capire che cosa intende un rilievo e
quanto e' costato. La griglia dice come si valuta (`griglia-valutazione.md`),
gli anti-pattern dicono che cosa evitare in scrittura
(`anti-pattern-proposte.md`); questo file dice come e' andata nei casi veri.

## Da dove vengono e quanto valgono

- Quattro Evaluation Summary Report di proposte con CIMA nel consorzio,
  valutate negli ultimi anni con i criteri di Horizon 2020 e di Horizon
  Europe. Ogni rilievo e' stato confrontato con il passaggio della proposta
  che l'ha provocato.
- **Tutte e quattro sono state finanziate**, con punteggi fra 4 e 5 su ogni
  criterio. Questi pattern dicono che cosa costa mezzo punto in cima alla
  graduatoria, **non** che cosa porta sotto soglia: nessun rilievo qui sotto
  e' una "significant weakness". Le proposte non finanziate arriveranno e
  riempiranno la colonna che oggi e' vuota.
- La colonna **Visto in** conta in quante proposte compare il pattern:
  `F` finanziate, `NF` non finanziate. Un pattern visto una volta e' un
  indizio, non una regola.
- I commenti tipici sono parafrasi generalizzate, non frasi degli ESR.

## 1. Dal rilievo al punteggio

### La convenzione delle etichette

I valutatori chiudono quasi ogni paragrafo con un'etichetta, e il punteggio
del criterio segue da quante ce ne sono e di che peso:

| Etichetta | Che cosa indica | Nella scala [definizioni del modulo] |
|---|---|---|
| "This is a (major) strength" | un aspetto che regge il punteggio | |
| "This is a minor shortcoming" | una lacuna locale, che non mette in dubbio il criterio | compatibile con 5 ("any shortcomings are minor") |
| "This is a shortcoming" | una lacuna che tocca un aspetto del criterio | 4 ("a small number of shortcomings") se poche, 3 ("a number of shortcomings") se molte |
| "significant weakness" | un aspetto non affrontato o non credibile | 2 ("significant weaknesses"); non osservata in questi casi |

Un rilievo puo' anche restare senza etichetta, o arrivare attenuato ("non
esplicito, ma descritto a livello aggregato"): pesa poco.

### Quanto e' costata ogni etichetta

Dodici punteggi di criterio, osservati:

| Rilievi sul criterio | Punteggio osservato |
|---|---|
| nessuno, o una sola minor shortcoming | 5 |
| una sola minor shortcoming | anche 4,5 (un caso) |
| una shortcoming, con o senza minor | fra 4 e 4,5 |
| tre-cinque rilievi non etichettati, oppure una shortcoming con tre rilievi minori | 4,5 |
| una shortcoming che raggruppa tre rilievi, piu' due minor | 4 |

Che cosa ne segue per il valutatore simulato:

- **Una shortcoming non porta a 3.** Nei casi veri porta a 4,5, o a 4 se
  raggruppa piu' rilievi. Il 3 richiede "a number of shortcomings", e nessun
  criterio di questi quattro ESR ci e' arrivato.
- **Una minor shortcoming non toglie il 5.** Un valutatore simulato che toglie
  mezzo punto per ogni dettaglio mancante e' piu' severo di quelli veri.
- **Ogni problema riceve un'etichetta**, con queste parole, prima del
  punteggio: il numero si giustifica con il conto delle etichette.
- **I punti di forza occupano la maggior parte del testo** di un ESR sopra
  soglia, e ciascuno nomina la caratteristica che lo ha meritato (sezione 3).
  Un rapporto simulato fatto solo di difetti non assomiglia a un ESR.

## 2. Pattern per criterio

### Excellence

| # | Debolezza | Come la scrive il valutatore | Etichetta osservata | Come si previene | Visto in |
|---|---|---|---|---|---|
| E1 | Obiettivo con un verbo vago ("migliorare la stima di...", "investigare l'utilita' di...") e nessuna metrica; KPI rinviati a un work package | non e' chiaro come si misurera' il raggiungimento dell'obiettivo | non etichettata o minor | per ogni obiettivo metrica, baseline e valore atteso; se il valore non si puo' fissare ora, quale deliverable lo fissa e quando | F 2, NF 0 |
| E2 | Obiettivi solo in una tabella, senza testo che li spieghi e li leghi a work package e outcome | gli obiettivi sono solo riassunti in una tabella | non etichettata | obiettivi numerati, due-tre righe ciascuno con il work package che li consegna, la tabella come sintesi | F 1, NF 0 |
| E3 | Obiettivi che descrivono componenti da costruire, e non l'uso della tecnologia o del servizio che il topic rende obbligatorio | gli obiettivi riguardano lo sviluppo dei componenti, non l'impiego di cio' che il bando chiede | non etichettata | almeno un obiettivo dedicato all'elemento obbligatorio del topic, nominato con le parole del topic | F 1, NF 0 |
| E4 | Il paragrafo spiega perche' una misura o un'analisi conta, e non come si fa | non e' chiaro come la variabile sara' descritta, caratterizzata e considerata | shortcoming (raggruppata) | una riga ciascuno per campionamento, metodo, metrica ricavata e ruolo nel modello | F 1, NF 0 |
| E5 | Un termine su cui si regge il disegno dello studio ("estremo", "ad alto impatto") non e' mai definito; la definizione e' rinviata a un task | non e' chiaro come saranno caratterizzate le condizioni estreme | shortcoming (raggruppata) | definizione operativa dove il termine compare la prima volta (soglia, percentile, durata, fonte), che il task poi raffina | F 1, NF 0 |
| E6 | Strumenti, app, sensori o sistemi di allerta nuovi senza dire che cosa aggiungono a quelli esistenti; lo stato dell'arte non nomina nessun sistema esistente; l'analisi delle lacune e' rinviata a un task | non e' spiegato che cosa aggiungerebbero gli strumenti proposti a quelli esistenti | shortcoming | una tabella "esistente / proposto" con tre-quattro sistemi nominati e la funzione che a ciascuno manca | F 1, NF 0 |
| E7 | Componente di intelligenza artificiale o modellistica presentata come un elenco di famiglie di algoritmi ("ad esempio... ecc."), con l'architettura lasciata aperta | l'approccio non e' spiegato abbastanza da valutarne la robustezza | minor; in Horizon Europe il modulo obbliga a valutare la robustezza dei sistemi di IA | per ogni modello: dati e numerosita', variabile prevista, riferimento di confronto, schema di validazione, metrica e valore atteso; una scelta e un'alternativa | F 1, NF 0 |
| E8 | La catena di previsione tratta l'uscita come deterministica: non dice come si trattano gli errori di osservazioni e modello, ne' come l'incertezza arriva alla decisione dell'utente | non e' spiegato come l'incertezza iniziale viene gestita fino al risultato finale | shortcoming | errori delle osservazioni e del modello, rappresentazione dell'incertezza nella previsione, e come diventa una soglia o una regola per l'utente | F 1, NF 0 |
| E9 | Nessuna domanda di ricerca esplicita, nessuna assunzione dichiarata: le assunzioni ci sono ma sparse | le assunzioni essenziali non sono esplicitate | shortcoming (le assunzioni); attenuata (le domande) | elenco numerato di domande di ricerca legate a obiettivi e work package; riquadro "assunzioni" con perche' sono plausibili e come si verificano | F 1, NF 0 |
| E10 | Un solo valore numerico fra tutti gli obiettivi; il resto qualitativo | mancano elementi quantitativi | minor | valori attesi anche provvisori, con il deliverable che li conferma | F 2, NF 0 |
| E11 | Dati promessi FAIR, ma senza identificativi persistenti, senza repository nominato, e con la cancellazione come unica cosa detta sul dopo progetto | non e' spiegato come i database resteranno disponibili e trovabili nel tempo | minor | per ogni tipo di dato identificativo, repository e durata dell'impegno dopo la fine del progetto | F 1, NF 0 |
| E12 | TRL finale alto senza TRL di partenza e senza dire in che cosa consiste la dimostrazione finale | il livello di ambizione e' molto alto | non etichettata | TRL di partenza e di arrivo per componente, e che cosa e' l'"ambiente rilevante" della dimostrazione | F 1, NF 0 |
| E13 | La sezione apre con letteratura generale che l'esperto del campo considera nota da tempo | questo e' noto da anni agli operatori del settore | non etichettata, attenuata | aprire con la lacuna specifica che il progetto chiude e con i numeri che intende spostare | F 1, NF 0 |

### Impact

| # | Debolezza | Come la scrive il valutatore | Etichetta osservata | Come si previene | Visto in |
|---|---|---|---|---|---|
| I1 | Impatti solo qualitativi; i soli numeri stanno in un allegato non collegato, oppure sono cifre di contesto molto grandi non legate al progetto | il contributo agli impatti attesi non e' quantificato: mancano baseline, riferimenti e ipotesi | non etichettata o minor | per ogni outcome un ordine di grandezza con baseline e ipotesi, e il rimando ai numeri dell'allegato | F 3, NF 0 |
| I2 | Analisi economica aperta ("si scegliera' il metodo piu' adatto"), misure da valutare non nominate, orizzonte temporale assente | le azioni sono descritte in termini generali, non basate su un'analisi dei bisogni | minor | metodo, misure candidate, orizzonte e bisogno dell'utente a cui risponde ciascuna analisi | F 1, NF 0 |
| I3 | La sezione sugli impatti attesi e' lunga mezza pagina; i benefici che il programma elenca come suoi non sono esplicitati, e il valutatore li deve dedurre | altri impatti positivi in linea con il programma non sono espliciti | minor | una tabella che lega gli outcome alle aree di beneficio che il programma nomina, piu' le ricadute scientifiche e tecnologiche | F 1, NF 0 |
| I4 | La sezione intitolata a disseminazione e sfruttamento contiene solo disseminazione; proprieta' intellettuale assente, anche se i partner portano strumenti propri | sfruttamento e IPR non sono coperti abbastanza, tanto piu' al TRL dichiarato | shortcoming, la principale del criterio | per ogni risultato sfruttabile: proprietario, background, licenza, strada verso l'adozione, regole di accesso nel consortium agreement | F 1, NF 0 |
| I5 | A una barriera specifica (economica, normativa) risponde una mitigazione generica: gli stessi rimandi a comunicazione e work package ripetuti su ogni riga | la mitigazione per quella barriera non e' spiegata | minor | una leva dello stesso tipo della barriera: a una barriera economica, una misura economica | F 1, NF 0 |
| I6 | KPI di comunicazione ambiziosi senza base di partenza | alcuni KPI sono ambiziosi | non etichettata | per ogni KPI il pubblico che i partner raggiungono gia' e come si conta | F 1, NF 0 |
| I7 | Piano economico allegato incompleto: voci di costo mancanti, ipotesi dichiarate "prudenti" ma non mostrate, rapporti fissi fra ricavi | il piano e' buono, con qualche debolezza nel conto economico | non etichettata | conto economico completo con le ipotesi accanto alla tabella, e i numeri dei work package controllati | F 1, NF 0 |

### Quality and efficiency of the implementation

| # | Debolezza | Come la scrive il valutatore | Etichetta osservata | Come si previene | Visto in |
|---|---|---|---|---|---|
| Q1 | Tabella dei rischi quasi tutta a probabilita' bassa, fatta di rischi gestionali generici; l'ipotesi scientifica centrale non compare come rischio; frasi come "non prevediamo rischi rilevanti" | il consorzio vede pochi rischi, il che appare ottimistico; serviva un esame critico delle sfide tecniche e scientifiche | shortcoming | aprire con i quattro-sei rischi tecnici e scientifici veri, valutati con onesta', ciascuno con un'alternativa concreta | F 1, NF 0 |
| Q2 | Poche milestone, con lunghi intervalli fra l'una e l'altra, e l'ultima e' "progetto concluso" | le milestone sono poche per monitorare l'avanzamento | non etichettata | una milestone ogni quattro-sei mesi, ciascuna un punto di verifica con il suo mezzo di verifica | F 1, NF 0 |
| Q3 | Piano di gestione dei dati consegnato una sola volta, all'inizio, e mai aggiornato | il piano non e' rivisto durante il progetto | "deficiency" | versione iniziale, aggiornamento intermedio e versione finale come deliverable distinti | F 1, NF 0 |
| Q4 | Report contrattuali trattati male nell'elenco dei deliverable: periodici e finali contati come deliverable, oppure il report finale assente dove il programma lo vuole fra i deliverable | i report non vanno contati fra i deliverable / il report finale non e' fra i deliverable | non etichettata o minor | seguire la guida del programma: in Horizon Europe i report periodici non sono deliverable; altri programmi chiedono il report finale nell'elenco | F 2, NF 0 |
| Q5 | Deliverable tecnici riservati o classificati senza motivo | alcuni deliverable sono riservati senza giustificazione | minor | pubblici per default; per ogni deliverable riservato una riga con il motivo; "classificato" solo per informazioni classificate UE vere | F 1, NF 0 |
| Q6 | Nessuna struttura di gestione e nessuna procedura di qualita' descritta | non e' fornito un piano di gestione e qualita' | non etichettata | un paragrafo con organi, regole di decisione, revisione interna dei deliverable, escalation, e un deliverable di manuale di progetto all'inizio | F 1, NF 0 |
| Q7 | Uscita di un partner gestita con una frase ("il carico sara' redistribuito") | la procedura per riassegnare i compiti non e' sviluppata | minor | chi decide, come si sceglie il sostituto, in che tempi, come si trattano budget e consegna dei risultati | F 1, NF 0 |
| Q8 | Un partner guida un work package o un'attivita' di valutazione con meno mesi-persona di altri partner nello stesso work package | il partner e' relativamente poco caricato | minor | il leader e' il primo contributore del proprio work package, oppure il testo spiega perche' bastano quei mesi | F 1, NF 0 |
| Q9 | I bisogni degli utenti sono citati in cinque work package e nessuno dice come si rilevano; il KPI misura la partecipazione, non se i bisogni sono soddisfatti | non e' chiaro come i bisogni degli stakeholder saranno rilevati e soddisfatti | shortcoming | un task proprietario della rilevazione, con metodo, deliverable dei requisiti e tracciabilita' dal requisito allo strumento; un KPI di soddisfazione dei requisiti | F 1, NF 0 |
| Q10 | Si promette di misurare un effetto difficile da misurare con un disegno che non lo puo' misurare | i tentativi di misurare l'effetto sono descritti in modo insufficiente | minor | il disegno che misura davvero quella grandezza: popolazione di riferimento, modello, finestra temporale, prodotto finale | F 1, NF 0 |

## 3. Che cosa lodano

Nei quattro ESR i punti di forza sono la maggior parte del testo, e ciascuno
nomina una caratteristica concreta. Quelle che tornano:

- **La catena in tabella**: lacuna, obiettivo, risultato, KPI con valore
  numerico, una riga per obiettivo. Lodata come obiettivi "misurabili" e
  "chiaramente legati agli outcome".
- **Il topic citato voce per voce**: una tabella con ogni sfida o expected
  outcome del bando a sinistra e la risposta del progetto a destra. Lodata in
  tre proposte su quattro come pertinenza e allineamento.
- **Obiettivi con una colonna "misura"**, anche quando poche misure sono
  numeriche.
- **Siti pilota giustificati uno per uno**: contrasto climatico o
  socio-economico, numeri, quali esistono gia' e quali si creano.
- **Riuso dichiarato**: componenti esistenti nominati e collegamenti a
  infrastrutture europee nominate, invece di piattaforme nuove da zero.
- **KPI di impatto con baseline e target** per ogni expected outcome, alle
  scale locale, nazionale e internazionale.
- **Misure di disseminazione e sfruttamento per fase** di progetto, con KPI e
  mesi.
- **Piano dei dati con piu' versioni** e i principi FAIR trattati uno per uno.
- **Rischi con un'alternativa concreta** (per esempio rifare la prova su casi
  passati se i dati in tempo reale non arrivano).
- **Advisory board con lettere di supporto** gia' allegate.
- **Piano economico con prezzi, concorrenti nominati e mercati quantificati.**

Un segnale utile: dove la proposta e' concreta, il valutatore ne riprende le
frasi quasi alla lettera nell'ESR. Una frase che si puo' copiare in un ESR e'
una frase che prende punti.

## 4. Osservazioni trasversali

- **Rinviare a un task cio' che il valutatore vuole vedere ora** costa punti:
  analisi delle lacune, definizioni operative, KPI "che saranno definiti nel
  WP...". Visto in tre proposte su quattro, sotto Excellence e Impact. Il
  valutatore giudica la proposta come e' scritta, e un rinvio e' un vuoto.
- **La sezione piu' corta tende a essere il criterio piu' basso**: in una
  proposta Impact occupava una frazione minima della parte B, ed e' stato il
  criterio con il punteggio piu' basso e con piu' rilievi. Un caso solo, ma
  netto.
- **Una cosa citata ovunque e posseduta da nessuno** (bisogni degli utenti,
  qualita') viene letta come assente.
- **I rilievi sono specifici**: nominano la tabella, il deliverable, il
  partner. Un rapporto simulato con rilievi generici ("la metodologia potrebbe
  essere piu' dettagliata") non dice a chi scrive che cosa cambiare.
