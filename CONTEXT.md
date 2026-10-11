# cima-scrittura

Glossario del linguaggio con cui si parla **del plugin**: skill, agenti,
nucleo, revisione, modalità di esecuzione.

Non confonderlo con `nucleo/terminologia.md`, che è un'altra cosa: quello
è la terminologia **dei testi che il plugin produce** (allerta, early
warning system, DEWETRA), destinata agli utenti finali e caricata dentro
le skill. Questo file non entra nel plugin e non viene letto da Claude a
runtime: serve a chi sviluppa il repository.

## Domini

**Dominio**:
Una delle quattro famiglie di testi che il plugin copre, identificata da
un prefisso obbligatorio nei nomi di skill e agenti: `generale-`,
`paper-`, `proposte-`, `progetti-`. Il prefisso decide anche quali file
condivisi la build inietta nella skill.
_Evitare_: area, categoria, modulo.

**Proposte**:
Il dominio dei testi scritti **prima** della firma del Grant Agreement:
proposta, bando, Part B, ESR.

**Progetti**:
Il dominio dei testi scritti **dopo** la firma del Grant Agreement:
deliverable, periodic report, technical report, risposte a review.
Il confine con `proposte` è la firma, non l'argomento: la risposta agli
ESR di una proposta resta in `proposte` anche se il progetto è poi
partito.

## Composizione del plugin

**Nucleo**:
Le regole valide in ogni dominio e in ogni lingua, con fonte unica in
`nucleo/`: vincoli, anti-pattern AI, verifica fonti, voce e lingua,
terminologia, protocollo di revisione. Le skill non lo riscrivono, lo
leggono.
_Evitare_: base comune, core, regole generali.

**File condiviso**:
Un riferimento comune a più skill dello stesso dominio, con fonte unica
in `plugin/condivisi/<dominio>/`. Sta al dominio come il nucleo sta al
plugin.
_Evitare_: file comune duplicato, copia.

**Riferimento**:
Un file che una skill legge mentre lavora, raggiungibile da `references/`
nel plugin costruito. Tre provenienze: il nucleo, i file condivisi del
dominio, i file propri della skill. La skill cita sempre il percorso
finale, non la provenienza.
_Evitare_: allegato, risorsa, documentazione.

**Skill**:
Un compito completo che il plugin sa svolgere, con un SKILL.md che lo
istruisce. Deve consegnare il risultato completo anche senza agenti.

**Agente**:
Un contesto separato che la skill lancia per un passaggio che richiede
indipendenza di giudizio. Non conosce i percorsi delle skill: li riceve
nel prompt. Aggiunge indipendenza, non funzioni.

## Revisione

**Revisione**:
Leggere un testo già scritto e produrre un **rapporto** di problemi
secondo una checklist o una griglia. Non comprende la riscrittura.
_Evitare_: controllo, correzione, "review" da solo in italiano. "Peer
review" fa eccezione, perché è un termine fisso: vedi sotto.

**Autorevisione**:
Revisione svolta dallo stesso contesto che ha scritto il testo. Sempre
dovuta prima della consegna, mai sufficiente da sola per un testo
destinato alla pubblicazione.

**Revisione separata**:
Revisione svolta da un contesto che vede solo il testo e i criteri, non
la conversazione in cui il testo è nato. È il meccanismo descritto da
`nucleo/protocollo-revisione.md`; "chi scrive non valuta" è il principio
che lo motiva.
_Evitare_: revisione esterna, doppio controllo. "Revisione indipendente"
è accettabile: è la formula con cui la chiede l'utente.

**Livello di revisione**:
Quanta revisione un dominio richiede: **leggero**, **standard**,
**completo**. Ogni skill dichiara il proprio. Determina quanti revisori
servono in modalità agenti, non che cosa la skill consegna.

**Tipo di intervento**:
Che cosa l'utente vuole indietro da una skill di revisione: un
**rapporto**, una **correzione** (refusi, grammatica, convenzioni) o una
**riscrittura**. Si deduce dal verbo della richiesta. Da non confondere
con il livello di revisione: quello dice quanta revisione serve, questo
che cosa si consegna. Una riscrittura fa diventare scrittura l'intervento,
con le regole della scrittura.

**Revisore**:
L'agente che svolge una revisione separata. Prende il nome del ruolo
reale che simula: `revisore` dove il mondo reale dice reviewer (paper,
progetti, comunicazione istituzionale), `valutatore` dove dice evaluator
(proposte). Non modifica mai il testo che valuta.

**Rapporto**:
L'output di una revisione: problemi citati con il passaggio esatto,
correzioni ordinate, e punteggi solo dove il dominio ha una griglia con
scala. Scritto nella lingua in cui scrive l'utente, non in quella del
testo.

**Pacchetto revisore**:
In modalità chat, il blocco pronto da copiare in una conversazione nuova
per ottenere comunque una revisione separata. Sostituto dell'agente, non
scorciatoia: si offre, non si impone.

**Peer review**:
Il processo reale con cui una rivista fa valutare un manoscritto da altri
ricercatori. Termine fisso del mestiere, che resta in inglese anche dentro un
testo italiano: "revisione paritaria" non lo dice nessuno. Quello che fa
`paper-revisione` è una **peer review simulata**, e si chiama così per intero,
perché il simulato è la parte che conta.
_Evitare_: revisione paritaria, mock review (fuori dalle frasi d'innesco, dove
invece serve perché è quello che la gente digita).

**Review**:
In inglese e solo nel dominio progetti, la revisione **reale** della
Commissione o dell'agenzia sul progetto in corso. Ciò che arriva da una
review (review report, deliverable respinto) va a
`progetti-risposta-review`, non alle skill di revisione.

## Strumenti di giudizio

**Checklist**:
Elenco di controlli con una gravità per voce (bloccante, importante,
minore), senza scala numerica. Tipico del livello leggero.

**Griglia**:
Elenco di criteri con una scala di punteggio e un profilo che la applica.
Tipica dei livelli standard e completo.

**Matrice**:
Tabella estratta da un documento reale fornito dall'utente (la DoA per
`progetti`, il testo del topic per `proposte`) che diventa la fonte di
verità del contenuto. Prevale sempre sui profili generici.
_Evitare_: tabella di tracciabilità, mappa.

**Profilo**:
Un punto di vista scritto che qualcuno o qualcosa impone. Tre specie, da
qualificare sempre: profilo di **revisore** (project officer, reviewer
tecnico), profilo di **programma** (Horizon Europe, Interreg, LIFE,
UCPM), profilo di **rivista**. Ogni profilo di programma o rivista porta
una data di verifica e perde autorità quando invecchia.

**Anti-pattern**:
Un difetto riconoscibile della scrittura generata (nucleo) o tipico di un
dominio. Si cita con il passaggio esatto, non si corregge in silenzio.

## Esecuzione

**Modalità agenti**:
Lo stato in cui lo strumento per lanciare subagent è disponibile. Si
deduce dagli strumenti, mai chiedendolo all'utente.
Resta tale anche dove non si possono salvare file: i materiali senza
percorso passano nel prompt, per intero (`docs/adr/0021`).
_Evitare_: Cowork, Claude Code, "in locale". Gli ambienti sono esempi di
una modalità, non la modalità.

**Modalità chat**:
Lo stato in cui quello strumento non c'è. Ogni passaggio che in modalità
agenti farebbe un agente viene svolto nel contesto principale, con lo
stesso formato di output e dichiarando che non è indipendente.
_Evitare_: modalità degradata, fallback. Consegna lo stesso risultato,
con meno indipendenza di giudizio.

## Sviluppo del repository

**Sessione**:
Una conversazione di sviluppo con Claude su questo repository. Non ha
niente a che vedere con la modalità chat, che riguarda invece come girano
le skill una volta rilasciate.
_Evitare_: chat (ambiguo), istanza, thread.

**Sessione hub**:
La sessione che tiene il brief, il glossario, gli ADR, il nucleo, gli
script e il rilascio, e che integra le pull request. Una sola alla volta.

**Sessione di dominio**:
Una sessione che lavora su un solo prefisso, sul branch
`dominio/<prefisso>`. Non modifica il nucleo né il brief: propone.

**ADR**:
Un file in `docs/adr/` che registra una decisione e il perché. Il brief
dice che cosa vale oggi, l'ADR perché ci siamo arrivati e che cosa
abbiamo scartato.

## Testo

**Segnaposto**:
Parentesi quadre che tengono il posto di un dato che non c'è, es.
`[numero di partner]`, `[da verificare: …]`, `[stima indicativa: da
confermare]`. Alternativa unica all'invenzione, ed elencati in fondo alla
consegna perché l'utente veda subito cosa manca.
_Evitare_: TBD, XXX, testo provvisorio.

**Mazzo**:
Una presentazione come oggetto unico: le slide, la loro sequenza e le note di
chi parla. Si costruisce copiando il template CIMA, non ricostruendolo.
_Evitare_: slideshow, pacchetto di slide. "Presentazione" è il sinonimo
accettato, ed è la parola usata nei nomi (`generale-presentazione`); "slide"
indica la singola pagina.

**Scaletta**:
L'elenco numerato che precede il mazzo: per ogni slide il layout, il titolo e
che cosa sostiene. Si costruisce e si mostra prima di montare il file, perché
un mazzo si corregge sulla scaletta, non sulle slide.
_Evitare_: outline, struttura, indice.

**Deroga**:
Uno scostamento dichiarato da `nucleo/voce-e-lingua.md` che un dominio si
concede perché il formato lo impone (IMRAD, template di deliverable,
elenchi in un verbale). Vive in una sezione apposita del SKILL.md: fuori
da lì non esiste.

**Consegna**:
Ciò che la skill restituisce all'utente, nell'ordine fissato dal SKILL.md:
il testo, poi segnaposto, fonti, esito della revisione, assunzioni. Il
testo da inviare non contiene mai frasi rivolte all'utente.
