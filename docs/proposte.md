# Dominio proposte: specifica

Unico dominio non ancora scritto. Gli altri tre hanno le skill come fonte di
verità; qui la specifica serve ancora. Livello di revisione: **completo**.

## Skill e agenti previsti

Skill: `proposte-analisi-bando`, `proposte-concept`, `proposte-scrittura`,
`proposte-revisione`, `proposte-coerenza`, `proposte-risposta-esr`.
Agenti: `proposte-valutatore` (parametrizzato per profilo esperto),
`proposte-rapporteur`, `proposte-verificatore` (coerenza formale).

La sessione che scrive il dominio può ridefinire l'elenco dentro il proprio
prefisso, rispettando livello di revisione e confini.

## Programmi

Horizon Europe, EIC, Interreg, LIFE, UCPM/ECHO, altri. Un **motore unico** più
un **profilo per programma** in `references/programmi/<programma>.md`: criteri,
pesi, soglie, struttura del modulo, limiti di pagine, gergo del valutatore,
data di verifica. I profili si costruiscono da documenti ufficiali correnti
verificati con ricerca web, mai a memoria.

La **matrice del bando**, estratta dal testo reale del topic, prevale sempre
sul profilo generico.

## Revisione

Tre valutatori più rapporteur, come nel processo europeo. Stesso brief, tre
profili esperti diversi: scientifico, applicativo/utenti finali,
gestionale/implementazione. Il rapporteur riporta le divergenze maggiori di un
punto senza mediarle.

I valutatori simulati non inventano punteggi "realistici" senza griglia.

## Calibrazione

Con proposte ed ESR reali di CIMA, che restano in `materiali/` (non
versionato) o si caricano direttamente nella conversazione che ne ha bisogno.
Nel plugin vanno solo **pattern anonimizzati**: tipo di debolezza, commento
tipico, effetto sul punteggio. Mai nomi, partner, budget.

Questo lavoro si fa nell'app, non qui: vedi la sezione "Dove fare cosa" di
`CLAUDE.md`.

## Stile

Gli anti-pattern del nucleo più quelli tipici degli ESR: state of the art non
quantificato, impatto generico, KPI senza baseline, disseminazione standard,
rischi generici, "uniquely positioned", buzzword, incoerenze fra sezioni.

Deroghe probabili: tabelle ed elenchi dove il modulo li richiede; "we" o "the
consortium" invece di "CIMA".

## Test di accettazione

Valutazione cieca di una proposta CIMA già valutata, con confronto fra il
punteggio simulato e l'ESR reale. È anche il test che chiude `adr/0015`.
