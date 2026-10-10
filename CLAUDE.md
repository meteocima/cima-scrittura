# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Cosa è questo repository

Sorgente del plugin Claude `cima-scrittura` (skill e agenti di scrittura
per Fondazione CIMA, in italiano). Non è un progetto software: il
"codice" sono file Markdown di istruzioni, più uno script Python che li
assembla, valida e impacchetta.

Tre file si dividono il lavoro, e vanno letti prima di toccare il plugin:
**`BRIEF.md`** descrive l'architettura corrente ed è la fonte in caso di
conflitto; **`CONTEXT.md`** è il glossario del repository (dominio,
nucleo, revisione, modalità, segnaposto: parole che qui hanno un
significato preciso); **`docs/adr/`** tiene una decisione per file con il
perché e le alternative scartate. Qui c'è solo ciò che serve per
orientarsi fra i tre.

## Comandi

```bash
python3 scripts/build.py --check   # solo validazione, in cartella temporanea
python3 scripts/build.py           # assembla in dist/, valida, impacchetta
```

Non esiste una suite di test: `--check` è il controllo da eseguire dopo
ogni modifica a `nucleo/`, `plugin/` o `scripts/build.py`. Non c'è modo di
validare una singola skill; la validazione è sempre su tutto il plugin.

Output della build (tutto in `dist/`, non versionato):
`dist/cima-scrittura/` (plugin assemblato), `dist/cima-scrittura.plugin`
(Cowork), `dist/skills/<nome>.zip` (caricamento di una singola skill in
chat).

La validazione statica non sostituisce la prova sul campo: prima di un
rilascio ogni skill va provata in chat senza subagent (deve consegnare il
risultato completo) e in Cowork (deve usare gli agenti previsti). I prompt
di prova stanno in `plugin/skills/<skill>/README-dominio.md`.

## Architettura

### Composizione a build time: il sorgente non è il plugin

Le skill vengono caricate una per una (in chat), quindi una skill non può
leggere i file di un'altra. `scripts/build.py` risolve questo copiando i
file comuni dentro ogni skill:

1. `nucleo/*.md` → `references/nucleo/` di **ogni** skill;
2. `plugin/condivisi/<dominio>/**/*.md` → `references/` delle sole skill
   di quel dominio (dominio = prefisso del nome della skill);
3. `README-dominio.md` e `.gitkeep` sono esclusi dal pacchetto.

Conseguenze pratiche:

- I percorsi `references/nucleo/vincoli.md` citati nei SKILL.md esistono
  solo nel plugin costruito. Nel sorgente le skill **non** contengono
  `references/nucleo/`, e la build fallisce se ce lo trovano.
- Una regola del nucleo si cambia in `nucleo/`, mai in una copia dentro
  `dist/`.
- Un file che serve a più skill dello stesso dominio si mette in
  `plugin/condivisi/<dominio>/`, non duplicato nelle skill: la build si
  ferma se trova la copia. `nucleo/` è un nome riservato lì dentro.
- `dist/` può contenere residui di build precedenti (è ignorato da git):
  non leggerlo come se fosse il sorgente.

### Domini

Quattro prefissi obbligatori per skill e agenti: `generale-`, `paper-`,
`proposte-`, `progetti-` (il quinto elemento, `nucleo/`, è comune). Il
prefisso decide anche quali file condivisi vengono iniettati. La tabella
di instradamento tra domini, che ogni `description` deve rispettare con
la sua clausola "Non usare per…", è in `BRIEF.md` §6.

Stato: `generale` e `progetti` sono scritti; `paper` e `proposte`
mancano. `legacy/cima-writing-style/` è la copia di riferimento del
plugin che `cima-scrittura` sostituirà, non va modificata.

### Due modalità, un solo risultato

Ogni skill deve portare a termine il compito **anche senza subagent**.
L'ambiente si deduce dagli strumenti disponibili (`Agent`/`Task` presente
= modalità agenti), mai chiedendolo all'utente; la regola è in
`nucleo/protocollo-revisione.md` §1 e vale per ogni passaggio delegato a
un agente, non solo per la revisione. Per questo ogni SKILL.md che nomina
un agente del plugin ha due sezioni parallele, `## Modalità agenti` e
`## Modalità chat`: la seconda esegue nel contesto principale lo stesso
lavoro, con lo stesso formato di output, dichiarando che non è
indipendente. La build blocca una skill che nomina un agente senza avere
`## Modalità chat`.

Gli agenti non conoscono i percorsi delle skill: la skill costruisce i
percorsi assoluti dalla propria cartella base e li passa nel prompt. Il
prompt contiene solo testo, tipo, destinatario, riferimenti e formato del
rapporto: mai riassunti della conversazione o intenzioni dell'autore
(è il punto del protocollo "chi scrive non valuta").

## Convenzioni imposte dalla build

`scripts/build.py` fallisce su: nome non kebab-case o senza prefisso di
dominio; `name` del frontmatter diverso dalla cartella o dal nome file;
`description` mancante, oltre 1024 caratteri o con parentesi angolari;
SKILL.md che cita un file `references/` inesistente; agente senza blocchi
`<example>` nella description, o con `model`/`color` fuori dai valori
ammessi; **trattino em (—) in qualsiasi file del plugin o del nucleo**
(unica esenzione: `anti-pattern-ai.md`, che lo nomina per vietarlo).
Avvisi (non bloccanti): SKILL.md oltre 3000 parole, description senza
clausola "Non usare", SKILL.md che non richiama `vincoli.md`.

Il divieto del trattino em vale anche nelle istruzioni e nei commenti:
gli esempi vengono imitati dal modello. Vale per i file del plugin, non
per questo file o per il brief.

Altre convenzioni non verificate automaticamente (vedi `BRIEF.md` §4):
istruzioni in italiano, imperativo, rivolte a Claude; prima sezione
`## Prima di tutto` identica in tutte le skill che producono o rivedono
testo; sezione `## Deroghe allo stile di base` per ogni scostamento da
`voce-e-lingua.md`; segnaposto `[…]` per ogni dato mancante, elencati in
fondo alla consegna.

## Flusso di lavoro

Il repository è diviso per ruolo della sessione di sviluppo ("sessione"
è una conversazione con Claude su questo repo, da non confondere con la
"modalità chat" in cui girano le skill):

- **Sessione hub**: `BRIEF.md`, `CONTEXT.md`, `docs/adr/`, `nucleo/`,
  `scripts/`, `plugin.json`, `README.md`, integrazione delle PR, test di
  instradamento, rilascio.
- **Sessione di dominio**: solo `plugin/skills/<prefisso>-*`,
  `plugin/agents/<prefisso>-*` e `plugin/condivisi/<dominio>/`, su un
  branch `dominio/<prefisso>`, con PR verso `main`.

Se una modifica al nucleo o al brief serve mentre si lavora su un
dominio, non applicarla: proporla nella descrizione della PR o in una
issue con titolo `[nucleo] …` o `[brief] …`. Una decisione presa diventa
un file in `docs/adr/` più una riga nell'indice di `BRIEF.md` §8; un
termine chiarito diventa una voce in `CONTEXT.md`. Il `CHANGELOG.md` si
aggiorna nella stessa modifica.

Messaggi di commit in italiano, minuscoli, nella forma
`<ambito>: <cosa cambia>` (es. `progetti: file comuni in
plugin/condivisi/progetti (brief v5)`), con il riferimento alla sezione
del brief quando la modifica ne discende.

## Materiali riservati

ESR, proposte, manoscritti e deliverable reali stanno in `materiali/`,
che non è versionato, e non entrano mai nel repository né negli esempi
delle skill: nel plugin vanno solo pattern anonimizzati.
