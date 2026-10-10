---
name: proposte-analisi-bando
description: "Legge il testo di un bando europeo (topic, call conditions, documenti della call) e ne estrae la matrice del bando: criteri di valutazione con pesi e soglie, expected outcomes e impatti nelle parole del bando, requisiti obbligatori, struttura del modulo e limiti di pagine. Ogni voce porta la sua fonte, e cio' che il bando non dice resta segnaposto. Carica il profilo del programma e dichiara dove il topic lo scavalca. Usare per: 'analizza il bando', 'che cosa chiede questo topic', 'criteri di valutazione della call', 'su che cosa saremo valutati', 'analyse the call', 'what does this topic require', 'evaluation criteria'. Non usare per: costruire il concept (proposte-concept) o scrivere la proposta (proposte-scrittura); valutare una proposta gia' scritta (proposte-revisione); rispondere a un ESR (proposte-risposta-esr); deliverable e report di progetti finanziati (progetti-); articoli e abstract (paper-); email, lettere, traduzioni (generale-)."
---

# Analisi del bando

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.
Per PIC, denominazione e dati del beneficiario: `references/nucleo/identita-cima.md`.

Poi leggere `references/matrice-bando.md`, che definisce la matrice e il modo
di marcare la fonte di ogni voce.

Livello di revisione del dominio: **completo**. La matrice non e' un testo da
inviare e non passa dai valutatori: la revisione separata riguarda i testi che
`proposte-revisione` giudica.

## Confini

| Richiesta | Chi la prende |
|---|---|
| capire che cosa chiede un bando, prima di scrivere | questa skill |
| decidere se l'idea regge, prima della proposta | `proposte-concept` |
| scrivere la proposta o una sua sezione | `proposte-scrittura` |
| valutare una proposta gia' scritta, con punteggi | `proposte-revisione` |
| controllare coerenza fra sezioni e sforamento dei limiti | `proposte-coerenza` |
| rispondere all'ESR di una proposta bocciata | `proposte-risposta-esr` |
| capire che cosa chiede un template di deliverable, a progetto avviato | `progetti-scrittura` |

Il confine con `progetti` e' la firma del Grant Agreement, non l'argomento
(`adr/0020`). Un topic si analizza qui anche se CIMA ha gia' altri progetti
finanziati sullo stesso tema.

## Che cosa consegna

La **matrice del bando** nella forma di `references/matrice-bando.md`, cioe':
intestazione del topic; criteri con aspetti, pesi e soglie; expected outcomes
e impatti copiati alla lettera; requisiti obbligatori; struttura del modulo
con i limiti; elenco di cio' che il valutatore deve poter spuntare.

Piu' due cose che l'utente usa subito:

- le voci rimaste `[da bando]`, elencate in fondo: sono le domande da fare al
  National Contact Point o da cercare nei documenti della call;
- dove il topic scavalca il profilo del programma, una riga per ogni voce
  scavalcata.

Dove si possono salvare file, la matrice va in un file `.md` nella cartella di
lavoro, cosi' le altre skill del dominio la ritrovano, e il messaggio ne porta
la sintesi: scavalcamenti del profilo, requisiti obbligatori, voci rimaste
`[da bando]`. Dove non si possono salvare file, la matrice va **per intero nel
messaggio**, una sezione alla volta se e' lunga.

Non e' la stessa cosa della modalita', che dipende dai subagent
(`references/nucleo/protocollo-revisione.md`, sezione 1): qui decide soltanto
se un file si puo' scrivere. In nessuno dei due casi la consegna si ferma a un
riassunto.

## Materiali

Chiedere in un solo messaggio cio' che manca, poi procedere comunque:

1. **Testo del topic**: incollato, allegato, o il suo identificativo e il link
   alla pagina del Funding & Tenders Portal.
2. Documenti della call che il topic cita, se l'utente li ha.
3. Programma e tipo di azione, se non si deducono dal topic.
4. Se e' una procedura in due fasi, quale fase.

Il topic e' un documento **pubblico**: si puo' leggere dalla pagina ufficiale
con la ricerca web, e si puo' cercare per identificativo. Una bozza di
proposta non lo e': vale la sezione "Riservatezza" di
`references/nucleo/vincoli.md`, quindi frasi della proposta non entrano mai
nelle query.

Senza il testo del topic si costruisce lo stesso la matrice dal solo profilo
del programma, con ogni riga marcata `[profilo]` e una riga che dice
all'utente che cosa cambierebbe fornendo il topic. Non fermarsi e non
chiedere due volte.

## Procedura

### 1. Inquadrare

Programma, call ID, topic ID, tipo di azione, scadenza, fase. Il tipo di
azione (RIA, IA, CSA, altro) cambia i criteri e i limiti: se il topic non lo
dice, e' `[da bando]`, non si deduce dal tema.

### 2. Caricare il profilo del programma

| Programma | File |
|---|---|
| Horizon Europe | `references/programma-horizon-europe.md` |
| EIC (Pathfinder, Transition, Accelerator) | `references/programma-eic.md` |
| Interreg (Euro-MED, Alpine Space, ADRION, Marittimo e gli altri) | `references/programma-interreg.md` |

Due profili non si usano come quello di Horizon Europe:

- **EIC**: criteri, soglie, pesi, numero di fasi e limite di pagine cambiano
  con lo **strumento**. Se non si capisce dal testo quale sia (Pathfinder
  Open, Pathfinder Challenges, Transition, Accelerator), chiederlo: senza
  quello il profilo non si puo' applicare, e le voci restano `[da bando]`.
- **Interreg**: la griglia non sta nel profilo e nemmeno nel manuale del
  programma, ma nelle **Terms of Reference della call**, e cambia da una call
  all'altra. Chiedere manuale e ToRs. La griglia di esempio dentro il profilo
  e' di una call sola e **non si copia** su un'altra.

Per gli altri programmi (LIFE, UCPM/ECHO, bandi nazionali e regionali) il
profilo non c'e' ancora: si lavora sul solo testo del topic e si dichiara in
una riga che le regole generali del programma non sono state applicate, come
prevede `references/nucleo/vincoli.md` sezione 4.

Se il profilo ha piu' di 12 mesi, o se una voce `[da verificare]` serve alla
matrice, verificarla con ricerca web sulle fonti ufficiali citate nel profilo.
Senza ricerca web disponibile: segnaposto, mai il valore a memoria.

### 3. Estrarre la matrice

Nell'ordine, perche' ogni passaggio usa il precedente:

1. **Intestazione**: i campi della sezione "Intestazione" della matrice.
2. **Criteri**: i tre criteri del tipo di azione, piu' ogni aspetto che il
   topic aggiunge di suo. Un aspetto nominato dal topic dentro un criterio va
   nella tabella dei criteri, non in una nota a margine: e' li' che il
   valutatore lo cerchera'.
3. **Pesi e soglie**: dal topic se li dichiara, altrimenti dal profilo,
   marcati `[profilo]`. Se ne' topic ne' profilo li danno, `[da bando]`.
   **Mai un numero plausibile**: una soglia inventata fa scrivere la proposta
   contro un bersaglio che non esiste.
4. **Expected outcomes e impatti**: copiati **alla lettera** dal topic, uno
   per riga. Non riassumerli e non tradurli: la proposta dovra' richiamarli
   con le stesse parole, e una parafrasi perde il termine che il valutatore
   cerca.
5. **Requisiti obbligatori**: tutto cio' che il topic impone con "must",
   "should", "are expected to", "mandatory", piu' le condizioni di
   ammissibilita'. Per ciascuno, il tipo: ammissibilita', eleggibilita',
   contenuto.
6. **Struttura e limiti**: sezioni del modulo, limite complessivo e per
   sezione, formato.
7. **Che cosa il valutatore deve poter spuntare**: la chiusura della matrice,
   scritta come la cercherebbe chi valuta.

### 4. Quando topic e profilo dicono cose diverse

Vince il topic, sempre. Il profilo e' una approssimazione del programma; il
topic e' il testo contro cui la proposta viene valutata.

Ogni scavalcamento si dichiara, una riga per voce, nella forma: che cosa dice
il profilo, che cosa dice il topic, che cosa vale. Non correggere il profilo:
il profilo si cambia nel repository, non durante una conversazione.

### 5. Autorevisione prima di consegnare

Tre domande, in questo ordine:

- ogni riga ha una fonte marcata, e nessun numero compare senza?
- ogni expected outcome del topic ha la sua riga, con le parole del topic?
- i requisiti con "must" e "mandatory" sono tutti nella tabella dei requisiti?

Una matrice con una riga sola inventata e' peggio di una matrice con dieci
segnaposto: i segnaposto si vedono, un numero plausibile no.

## Deroghe allo stile di base

- **Tabelle ovunque**: la matrice e' fatta di tabelle, non di paragrafi.
- **Citazioni in lingua originale**: outcomes, impatti e requisiti si copiano
  nella lingua del bando, di norma l'inglese, anche quando il resto della
  consegna e' in italiano. Il commento intorno segue la lingua dell'utente
  (`references/nucleo/voce-e-lingua.md`).

## Limiti

- La matrice dice **su che cosa** si verra' giudicati, non se conviene
  partecipare: la decisione resta dell'utente, e il plugin non stima
  probabilita' di successo.
- Il profilo del programma non sostituisce i documenti della call. Quando una
  voce pesa davvero (una soglia, un limite di pagine, una condizione di
  ammissibilita'), la fonte da citare all'utente e' il documento ufficiale,
  non questa skill.
