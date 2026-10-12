# Anti-pattern dei testi di proposta

Si aggiungono a `references/nucleo/anti-pattern-ai.md`, non lo sostituiscono.
Sono i difetti che un valutatore di proposte nota per primi. Ogni voce:
pattern, perche' pesa, come si corregge.

> Da dove vengono. Le voci marcate [REA] sono difetti che la Commissione
> stessa elenca come ricorrenti: REA, Common mistakes to avoid when applying
> for Horizon Europe funding,
> https://rea.ec.europa.eu/news/common-mistakes-avoid-when-applying-horizon-europe-funding-2023-02-09_en
> (letta il 2026-10-10). Le altre vengono da come e' scritta la griglia nei
> profili di programma in `references/programma-*.md`: dove la griglia chiede
> una cosa precisa, non darla e' un difetto. Le voci marcate [ESR] le hanno
> segnalate i valutatori veri negli ESR di proposte CIMA: il dettaglio, con il
> peso sul punteggio, sta in `references/pattern-esr.md`.

## La regola che spiega quasi tutte le voci

Il valutatore giudica la proposta **come e' stata consegnata, non per quello
che potrebbe diventare**, e ha istruzione di non raccomandare modifiche: una
lacuna non diventa una richiesta di chiarimento, diventa un punto in meno
(`programma-horizon-europe.md`, sezione "Come ragiona il valutatore"). Da qui
discende che ogni cosa non scritta e' una cosa persa, e che scriverla in modo
vago equivale quasi sempre a non scriverla.

## Stato dell'arte e ambizione

- **"Beyond the state of the art" senza numeri.** La frase piu' frequente e
  piu' vuota del mestiere. Dire di superare lo stato dell'arte senza dire di
  quanto, rispetto a che cosa e misurato come, lascia il valutatore senza
  niente da spuntare. Correzione: il valore di partenza (chi lo ha pubblicato,
  quando), il valore atteso, la metrica. Se i numeri non ci sono, segnaposto
  `[baseline: ...]`, mai un aggettivo.
- **Stato dell'arte come rassegna bibliografica.** Elencare che cosa hanno
  fatto gli altri senza dire che cosa manca. Correzione: ogni lavoro citato
  chiude con il limite che questa proposta toglie.
- **Ambizione dichiarata invece che mostrata.** "Highly innovative",
  "groundbreaking", "unique". Correzione: togliere l'aggettivo e lasciare il
  confronto.
- **"Uniquely positioned".** Dice che siamo bravi, non che cosa sappiamo fare.
  Correzione: la competenza con la prova (progetto, pubblicazione, dato,
  infrastruttura), o niente.
- **Obiettivi che non si possono misurare** [ESR]. "Migliorare la stima
  di...", "investigare l'utilita' di...", con i KPI rinviati a un work
  package. Correzione: per ogni obiettivo metrica, baseline e valore atteso;
  se il valore non si puo' fissare ora, il deliverable che lo fissa.
- **Rinviare a un task quello che il valutatore vuole vedere ora** [ESR].
  "Un'analisi delle lacune sara' svolta in un task dedicato", "i KPI saranno
  definiti nel corso del progetto". Per il valutatore e' un vuoto.
  Correzione: la versione di oggi nel testo, anche provvisoria, e il task che
  la raffina.
- **Strumento nuovo senza confronto con gli esistenti** [ESR]. Un sistema di
  allerta, una piattaforma, un'app, senza nominare quelli che ci sono gia'.
  Correzione: tre-quattro sistemi esistenti nominati e la funzione che a
  ciascuno manca.
- **Troppi obiettivi, o obiettivi troppo ambiziosi** [REA]. Il valutatore
  legge una proposta che non sta in piedi nei tempi e nel budget. Correzione:
  meno obiettivi, ciascuno misurabile e verificabile.

## Impatto

- **Impatto generico.** "The project will have a significant impact on
  society". Correzione: chi beneficia, di che cosa, in che misura, quando, e
  che cosa deve succedere perche' accada.
- **Confondere risultati, output, outcome e impatto** [REA]. Sono quattro cose
  diverse, e la griglia le distingue. Correzione: il risultato e' cio' che il
  progetto produce, l'outcome il cambiamento nei destinatari, l'impatto
  l'effetto piu' largo e piu' lontano.
- **Parafrasare il work programme** [REA]. Ricopiare gli expected outcome con
  altre parole e' il modo piu' veloce per non dire niente. Correzione:
  tradurli nel proprio progetto, dicendo quale pezzo del risultato atteso
  tocca a chi e quando.
- **KPI senza baseline** [ESR]. Un KPI senza valore di partenza non e' misurabile, e
  il valutatore lo scrive. Correzione: baseline, target, metodo di misura,
  fonte del dato. Senza il valore di partenza, `[baseline: ...]`.
- **Disseminazione standard.** Sito, logo, newsletter, social, un workshop
  finale. Correzione: per ogni misura, il gruppo destinatario e perche'
  quella misura lo raggiunge; le attivita' che il programma pesa di piu'
  (standardizzazione, uptake da parte delle autorita', replica) scritte come
  attivita' con responsabile e tempi.
- **Nessun piano oltre la fine del progetto.** LIFE pesa esplicitamente
  sostenibilita' e potenziale di replica, UCPM la sostenibilita' e il
  leveraging degli investimenti. Correzione: chi continua, con quali risorse,
  a partire da quale decisione gia' presa.

## Piano di lavoro e risorse

- **Work package che sono capitoli, non lavoro.** Titoli tematici senza
  attivita' quantificate. Correzione: per ogni task, che cosa si fa, quanto
  (numero di test, misure, casi, campagne), chi lo fa e perche' serve.
- **Budget che non corrisponde al carico di lavoro** [REA]. E' la prima
  incoerenza che il valutatore cerca, e i template la nominano esplicitamente.
  Correzione: mesi-persona coerenti con le attivita' descritte e con la
  tabella di budget.
- **Rischi generici** [ESR]. "Delay in data collection", "partner withdrawal",
  con mitigazione "regular meetings". Correzione: rischi specifici del lavoro
  proposto, con probabilita', effetto sul piano e azione concreta.
- **Rischi tutti bassi** [ESR]. Il consorzio valuta quasi tutto a probabilita'
  bassa e l'ipotesi scientifica centrale non compare: il valutatore lo legge
  come ottimismo. Correzione: aprire con i rischi tecnici e scientifici veri,
  valutati con onesta', ciascuno con un'alternativa.
- **Deliverable di gestione mal posti** [ESR]. Piano dei dati consegnato una
  volta e mai aggiornato, report periodici contati come deliverable,
  deliverable tecnici riservati senza motivo, tre milestone in tutto il
  progetto. Correzione: piano dei dati in piu' versioni, i report secondo la
  guida del programma, un motivo per ogni deliverable riservato, una
  milestone di verifica ogni quattro-sei mesi.
- **Nessun work package di gestione**, o gestione senza struttura decisionale.
  Correzione: come si decide, chi decide, con quali tempi.

## Consorzio

- **Partner descritti dal sito web.** Paragrafi istituzionali che non dicono
  che cosa fara' quel partner. Correzione: il ruolo nel progetto, i task, la
  competenza che lo giustifica.
- **Consorzio squilibrato taciuto** [ESR]. Un partner che compare solo per
  completare la geografia. Correzione: dargli un ruolo vero o toglierlo.
- **Partner inventati.** Mai. Un partner che non ha confermato e' un
  segnaposto con il ruolo che servirebbe, non un nome plausibile.

## Lingua e forma

- **Buzzword al posto di termini concreti** [REA]: "paradigm shift",
  "holistic", "cutting-edge", "state-of-the-art solution", "AI-powered".
  Correzione: il termine tecnico esatto, o niente.
- **Sovrascrittura** [REA]. Periodi lunghi e sotto-clausole che nascondono la
  risposta. Il valutatore legge decine di proposte: se deve cercare la
  risposta, non la trova. Correzione: la risposta nella prima frase del
  paragrafo.
- **Rispondere nel posto sbagliato.** In UCPM ogni sotto-criterio vale punti
  dentro una casella precisa del modulo; in Interreg ogni domanda rimanda a
  una sezione dell'Application Form. Una risposta giusta scritta altrove non
  prende quei punti. Correzione: seguire la mappa della matrice del bando.
- **Riempire il limite di pagine.** Il template di Horizon Europe lo dice da
  solo: gli esperti raramente guardano con favore una proposta inutilmente
  lunga. Correzione: togliere, non aggiungere.
- **Link per aggirare il limite.** I valutatori hanno istruzione di ignorare i
  link che espandono la proposta. Correzione: se conta, sta dentro.

## Coerenza fra sezioni

E' la famiglia di difetti che i valutatori trovano per primi, perche' si vede
senza conoscere il tema.

- impatti promessi che nessun work package produce;
- KPI che compaiono nell'impatto e non nel piano di lavoro;
- numeri diversi per la stessa cosa in due sezioni;
- date e durate che non tornano fra Gantt, task e deliverable;
- partner citato nel testo e assente dalla tabella delle risorse.

Correzione: prima della consegna, il controllo di coerenza
(`proposte-coerenza` quando esiste, altrimenti la stessa lista a mano).
