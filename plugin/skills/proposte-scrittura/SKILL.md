---
name: proposte-scrittura
description: "Scrive il testo delle proposte di progetto europee, prima della firma del Grant Agreement: Part B e sue sezioni (Excellence, Impact, Implementation), abstract, work package, piano di disseminazione ed exploitation, allegati narrativi. Segue il modulo del programma e, se l'utente fornisce il file del modulo, scrive dentro quello. Ancora ogni affermazione alla matrice del bando: stato dell'arte quantificato, KPI con baseline, nessun partner o numero inventato. Usare per: 'scrivi la sezione Impact', 'bozza della Part B', 'descrivi il work package 3 della proposta', 'draft the excellence section', 'write the proposal'. Non usare per: capire che cosa chiede il bando (proposte-analisi-bando); costruire il concept (proposte-concept); valutare una proposta scritta (proposte-revisione); rispondere a un ESR (proposte-risposta-esr); deliverable e report dopo la firma (progetti-); articoli scientifici (paper-); slide (generale-presentazione); email e lettere (generale-scrittura)."
---

# Scrittura di proposte

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.
Per PIC, denominazione e dati del beneficiario: `references/nucleo/identita-cima.md`.

Poi leggere `references/anti-pattern-proposte.md` e, per la matrice,
`references/matrice-bando.md`.

Livello di revisione del dominio: **completo**. La revisione separata la fa
`proposte-revisione` con tre valutatori e un rapporteur; questa skill fa
l'autorevisione e la dichiara.

## Confini

| Richiesta | Chi la prende |
|---|---|
| scrivere la proposta o una sua sezione | questa skill |
| capire che cosa chiede il bando | `proposte-analisi-bando` |
| decidere se l'idea regge, prima di scrivere | `proposte-concept` |
| valutare la proposta con punteggi e soglie | `proposte-revisione` |
| controllare coerenza fra sezioni e limiti | `proposte-coerenza` |
| rispondere all'ESR di una proposta bocciata | `proposte-risposta-esr` |
| deliverable, periodic report, risposta a una review | `progetti-` (dopo la firma) |
| slide del pitch | `generale-presentazione`, che prende da qui i criteri |
| articolo scientifico sugli stessi risultati | `paper-scrittura` |

Il confine con `progetti` e' la **firma del Grant Agreement**, non
l'argomento (`adr/0020`). Se non e' chiaro in che fase siamo, vale la domanda
sola di `progetti-scrittura`: Grant Agreement firmato oppure no.

## Ambito

Testi che vanno dentro una proposta o la accompagnano: Part B e sue sezioni,
concept note, abstract, descrizione di work package e task, piano di
disseminazione ed exploitation, gestione dei rischi, descrizione del
consorzio e dei partner, allegati narrativi, lettere di supporto.

Fuori ambito: il **budget come numeri** (tabelle dei costi, mesi-persona
calcolati, tassi di cofinanziamento). Di quello si scrive la narrativa, non si
calcolano le cifre: se l'utente le chiede, dirlo in una riga.

## Materiali

Chiedere in un solo messaggio cio' che manca, poi procedere comunque con
segnaposto:

1. **Matrice del bando**, o il testo del topic da cui ricavarla.
2. **Modulo del programma**: il file del template, se c'e'. Senza, la
   struttura viene dal profilo del programma.
3. Materiale tecnico: idea, risultati precedenti, dati, metodi,
   infrastrutture, progetti su cui si costruisce.
4. Consorzio: chi c'e' davvero, chi ha confermato, chi manca.
5. Sezione da scrivere e lingua (di norma inglese).

Senza matrice e senza modulo si scrive lo stesso, dicendo in una riga che il
testo non e' ancora ancorato ai criteri del bando.

## Procedura

### 1. La matrice del bando prima del testo

Se l'utente ha gia' la matrice (file o tabella in conversazione), usarla. Se
non ce l'ha ma ha il topic, costruirla come fa `proposte-analisi-bando`:
criteri, pesi, soglie, outcomes alla lettera, requisiti obbligatori, struttura
e limiti. Se non c'e' nessuno dei due, scrivere comunque e dichiararlo.

La matrice serve a due cose mentre si scrive: dice **dove** va ogni risposta e
dice **che cosa** il valutatore cerchera' in quel punto.

### 2. Il modulo del programma

Profili in `references/programma-horizon-europe.md`, `programma-eic.md`,
`programma-interreg.md`, `programma-life.md`, `programma-ucpm.md`. Il modulo
fornito dall'utente prevale sempre sul profilo.

Se l'utente fornisce il **file** del modulo, il testo torna **dentro quel
file**, con le sue sezioni, la sua numerazione e il suo formato
(`references/nucleo/formati-e-file.md`). Non si consegna Markdown da
reimpaginare, e non si tolgono sezioni perche' mancano i dati: si riempiono di
segnaposto.

### 3. Struttura prima del testo

Mostrare l'indice delle sezioni da scrivere, con le pagine indicative. Per
testi oltre le tre pagine, attendere conferma solo se l'indice si discosta dal
modulo.

### 4. Scrittura

Cinque regole che vengono dalla griglia, non dallo stile:

1. **Stato dell'arte quantificato.** Ogni affermazione di superamento porta il
   valore di partenza, il valore atteso e la metrica. Se il numero non c'e':
   `[baseline: ...]`, mai un aggettivo al suo posto.
2. **KPI con baseline.** Ogni indicatore ha valore di partenza, target, metodo
   di misura e fonte. Un KPI senza baseline non e' misurabile e il valutatore
   lo scrive.
3. **Niente dati inventati.** Partner, cifre, mesi-persona, date, pubblicazioni
   e risultati che l'utente non ha fornito sono segnaposto con il ruolo o il
   dato mancante: `[partner: autorita' di protezione civile, da confermare]`.
   I dati verificati di CIMA (denominazione, PIC, sede, qualifiche pubbliche)
   stanno in `references/nucleo/identita-cima.md` e si usano **senza
   chiederli**: non sono invenzione.
4. **Ogni risposta nel suo posto.** La matrice dice in quale sezione o casella
   il valutatore cerca quella cosa. Una risposta giusta scritta altrove non
   prende quei punti.
5. **Gli outcome del bando con le parole del bando.** Richiamarli alla lettera
   almeno una volta, poi tradurli nel progetto. Parafrasarli e basta e' il
   difetto piu' segnalato.

Durante la scrittura, `references/anti-pattern-proposte.md` si applica come
una voce della valutazione, non come criterio principale.

### 5. Autorevisione dichiarata

Prima di consegnare, rileggere il testo come se fosse di un altro gruppo e
controllare, nell'ordine:

- ogni affermazione di ambizione ha un numero o un segnaposto;
- ogni KPI ha la baseline;
- nessun nome, cifra o data che l'utente non abbia fornito;
- ogni sezione risponde a cio' che la matrice le assegna;
- nessuna incoerenza fra impatto, piano di lavoro e risorse;
- i limiti di pagine o caratteri sono rispettati, se noti.

Aprire la nota di autorevisione con la riga della sezione 4a del protocollo:
la revisione fatta nella stessa conversazione tende a essere indulgente. Per
la revisione che conta, offrire `proposte-revisione`, e in chat il pacchetto
valutatore.

## Deroghe allo stile di base

Valgono solo qui, e solo per il testo della proposta.

- **Tabelle ed elenchi** dove il modulo li richiede (work package, deliverable,
  milestone, rischi, KPI, risorse): il modulo vince sulla preferenza per il
  testo disteso.
- **Voce del consorzio**: in inglese "we" e "the consortium", non "CIMA".
  CIMA compare come beneficiario nella descrizione dei partner, dove il modulo
  la chiede.
- **Tempo verbale**: la proposta promette il futuro, quindi "will" al posto
  del passato dei report. Il divieto di inventare non cambia: una promessa
  resta una promessa, un dato resta un dato.
- **Gergo del programma**: i termini del bando (expected outcome, work
  package, deliverable, milestone, TRL) si usano come li usa il bando, anche
  quando `references/nucleo/terminologia.md` preferirebbe altro.

Fuori da questa sezione la deroga non esiste.

## Consegna

- Il testo nel formato del modulo: dentro il file se l'utente lo ha dato,
  altrimenti Markdown strutturato come il modulo.
- **Segnaposto elencati in fondo**, raggruppati per tipo (dati, partner,
  risorse, riferimenti), cosi' chi riceve sa che cosa manca.
- Le sezioni della matrice che il testo non copre ancora.
- La nota di autorevisione, con la riga che dichiara che non e' indipendente.
- Il testo da consegnare non contiene mai frasi rivolte all'utente.
