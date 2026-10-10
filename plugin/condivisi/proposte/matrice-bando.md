# Matrice del bando

La matrice e' il riferimento di ogni testo del dominio proposte: dice su che
cosa la proposta verra' giudicata, con quale peso, sotto quale soglia e' fuori
e quali voci il valutatore deve poter spuntare. Si costruisce una volta per
topic e si riusa.

E' il gemello della matrice DoA del dominio progetti, e fa il lavoro opposto:
la matrice DoA verifica l'aderenza a un contratto firmato, la matrice del
bando estrae i criteri con cui sarai giudicato (`adr/0020`).

## La regola che decide i conflitti

**Il topic prevale sul profilo del programma.** Il profilo
(`references/programma-*.md`) e' una approssimazione del programma; il topic
e' il testo contro cui la proposta viene valutata davvero, e puo' cambiare
criteri, pesi, soglie, struttura e limiti. Quando le due fonti dicono cose
diverse, vince il topic, e la matrice lo dichiara nella colonna della fonte.

Quando il topic non dice niente su una voce, la voce **non si riempie con il
profilo di nascosto**: si riporta il valore del profilo marcandolo come tale,
cosi' chi legge sa che e' una approssimazione e non una regola del bando.

## Fonti, in ordine di precedenza

1. Testo del topic e call conditions sul Funding & Tenders Portal.
2. Documenti della call citati dal topic (work programme della destination,
   guide del programma, template specifici).
3. Profilo del programma in `references/programma-<nome>.md`.
4. Informazioni date dall'utente in conversazione.

Mai a memoria. Se il topic non e' stato fornito e non e' leggibile, la matrice
si costruisce lo stesso dal profilo, con ogni riga marcata `[profilo]` e una
riga sola che dice all'utente che cosa cambia se fornisce il topic.

## Come si marca ogni riga

Ogni voce della matrice porta la **fonte**:

| Marca | Significato |
|---|---|
| `[topic]` | sta nel testo del topic o nelle call conditions |
| `[profilo]` | viene dal profilo del programma, il topic non ne parla |
| `[utente]` | lo ha detto l'utente in conversazione |
| `[da bando]` | nessuna fonte lo dice: segnaposto, da cercare nel bando |

Un valore plausibile senza fonte non si scrive. Una soglia inventata fa
scrivere la proposta contro un bersaglio che non esiste.

## Cosa estrarre

### Intestazione

| Campo | Valore | Fonte |
|---|---|---|
| Programma e call ID | | |
| Topic ID e titolo | | |
| Tipo di azione (RIA, IA, CSA, altro) | | |
| Scadenza, e fase (unica, prima, seconda) | | |
| Budget della call e budget indicativo per progetto | | |
| Numero di progetti attesi | | |
| Durata attesa | | |
| Composizione minima del consorzio | | |
| Lump sum oppure costi reali | | |
| TRL di partenza e di arrivo, dove il topic li dice | | |

### Criteri, pesi, soglie

| # | Criterio | Aspetti che il topic nomina | Peso | Soglia | Fonte |
|---|---|---|---|---|---|

Dove il topic aggiunge aspetti propri a un criterio (per esempio un requisito
di cooperazione internazionale dentro Impact), l'aspetto va in questa tabella,
non in una nota: e' li' che il valutatore lo cerchera'.

### Expected outcomes e impatti

Si copiano **alla lettera** dal topic, uno per riga, perche' la proposta deve
poterli richiamare con le stesse parole.

| # | Outcome o impatto, nelle parole del topic | Dove la proposta risponde | Fonte |
|---|---|---|---|

La colonna "dove la proposta risponde" resta vuota in fase di analisi: la
riempiono le skill che scrivono.

### Requisiti obbligatori

Tutto cio' che il topic impone con "must", "should", "are expected to",
"mandatory", piu' le condizioni di ammissibilita' che la proposta deve
soddisfare da sola.

| # | Requisito | Tipo (ammissibilita', eleggibilita', contenuto) | Dove si soddisfa | Fonte |
|---|---|---|---|---|

Voci che il topic nomina spesso e che e' facile non vedere: attivita' di
clustering con altri progetti finanziati, cofinanziamento o contributi in
natura, coinvolgimento di categorie specifiche di partecipanti, dati aperti e
data management, dimensione di genere, etica e sicurezza, lingua, uso di
infrastrutture o dataset indicati.

### Struttura e limiti

| Sezione del modulo | Contenuto richiesto | Limite | Fonte |
|---|---|---|---|

Il limite complessivo e quello per sezione, se esiste, piu' il formato
imposto: pagine, caratteri, font, margini. Dove il topic non dice niente,
valgono i limiti del profilo, marcati `[profilo]`.

### Che cosa il valutatore deve poter spuntare

La chiusura della matrice: l'elenco delle cose che devono essere
**trovabili** nella proposta, una per riga, scritte come le cercherebbe chi
valuta. Serve a scoprire prima della consegna che manca una sezione
obbligatoria, non dopo.

| # | Voce | Criterio a cui serve | Presente |
|---|---|---|---|

## Quando la matrice e' finita

Una matrice e' utilizzabile quando ogni criterio ha peso e soglia (o dice che
non li ha trovati), ogni outcome del topic ha la sua riga, e i requisiti
obbligatori sono elencati con il tipo. Le righe `[da bando]` rimaste si
elencano in fondo alla consegna come segnaposto: sono le domande da fare al
National Contact Point o da cercare nei documenti della call.
