# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Cosa è questo repository

Sorgente del plugin Claude `cima-scrittura`, che fa scrivere a Fondazione CIMA
i suoi testi in quattro domini: `generale` (email, lettere, comunicati,
verbali, testi web), `paper` (articoli, abstract, risposta ai revisori),
`proposte` (proposte di progetto europee) e `progetti` (deliverable e report
di progetti finanziati).

Non è un progetto software: il "codice" sono file Markdown di istruzioni, più
uno script Python che li assembla, valida e impacchetta. Si scrive quindi per
due lettori insieme, Claude che eseguirà le istruzioni e la persona di CIMA
che manterrà il file.

Stato: `generale`, `progetti` e `paper` sono scritti; `proposte` no.

## Comandi

```bash
python3 scripts/build.py --check   # solo validazione, in cartella temporanea
python3 scripts/build.py           # assembla in dist/, valida, impacchetta
```

Non esiste una suite di test: `--check` è il controllo da eseguire dopo ogni
modifica a `nucleo/`, `plugin/` o `scripts/build.py`, e vale sempre su tutto
il plugin. Oggi dice: 9 skill, 4 agenti, 0 avvisi.

Output in `dist/`, non versionato: il plugin assemblato, `cima-scrittura.plugin`
e uno zip per skill in `dist/skills/`.

## Architettura

### Il sorgente non è il plugin

Le skill vengono caricate una per una, quindi una skill non può leggere i file
di un'altra. `scripts/build.py` risolve il problema copiando i file comuni
dentro ogni skill al momento della build:

1. `nucleo/*.md` in `references/nucleo/` di **ogni** skill;
2. `plugin/condivisi/<dominio>/**/*.md` in `references/` delle sole skill di
   quel dominio, dove il dominio è il prefisso del nome della skill.

Quindi: i percorsi `references/nucleo/…` citati nei SKILL.md esistono solo nel
plugin costruito; una regola del nucleo si cambia in `nucleo/`, mai in una
copia; e le duplicazioni visibili in `dist/` non sono un errore da accorpare
(`docs/adr/0003`). Il sorgente di una skill che contiene una di quelle copie fa
fallire la build.

### Due modalità, un solo risultato

Ogni skill porta a termine il compito **anche senza subagent**. La modalità si
deduce dagli strumenti disponibili (`Agent` o `Task` presente = modalità
agenti), mai chiedendola all'utente. Ogni passaggio che in modalità agenti
farebbe un agente viene svolto, in modalità chat, nel contesto principale, con
lo stesso formato di output e dichiarando che non è indipendente. Una skill non
si ferma e non chiede di cambiare ambiente.

Gli agenti esistono per una ragione sola: chi scrive un testo lo giudica con
indulgenza, quindi la revisione che conta avviene in un contesto che vede solo
il testo e i criteri (`docs/adr/0005`). La skill passa all'agente percorsi e
griglia, mai la conversazione.

Sopra tutto sta il vincolo che i testi prodotti non contengono dati inventati:
dove manca un'informazione va un segnaposto `[…]`. Vale anche per i valutatori
simulati, che non inventano punteggi senza griglia.

## Dove fare cosa

- **Qui, in Claude Code**: tutto ciò che tocca più di un file o la storia git.
  Build e validazione, rinomine, coerenza fra skill, il nucleo, i file
  condivisi, le decisioni. Anche costruire i profili di programma e di rivista,
  che vuole ricerca web e scrittura di file nello stesso posto.
- **Nell'app, nel progetto con le chat**: provare le skill come le userà chi
  scrive a CIMA, con il plugin installato e gli agenti che partono davvero;
  lavorare con materiali riservati (ESR, proposte, manoscritti) senza che
  tocchino il repository; limare il contenuto di una skill in conversazione
  lunga, quando serve il giudizio dell'utente riga per riga. La calibrazione
  del dominio proposte sugli ESR reali si fa lì.
- **In una chat singola con lo zip della skill**: solo la prova di accettazione
  in modalità chat, dove la skill deve consegnare tutto senza agenti.

Ogni aggiornamento si prova nei due ambienti prima di uscire, con la sua
cartella in `prove/`: versione nuova in `plugin.json`, voce nel `CHANGELOG`,
cartella `prove/<versione>-<slug>/` con le prove e i loro esiti. La build
avvisa quando la versione non ha la sua cartella.

In una riga: qui si costruisce il plugin, nell'app lo si prova e gli si danno
in pasto i materiali veri.

## Come si lavora

Si lavora su `main`. Per una modifica grossa o rischiosa, un branch breve con
pull request; un solo checkout, niente worktree (`docs/adr/0016`).

Chi scrive una skill non cambia il nucleo di sua iniziativa: il nucleo vale per
tutti i domini, quindi una modifica lì si propone e si decide a parte.

Una decisione presa diventa un file in `docs/adr/` più una riga nel suo
indice; un termine chiarito diventa una voce in `CONTEXT.md`. Il `CHANGELOG.md`
si aggiorna nella stessa modifica.

Messaggi di commit in italiano, minuscoli, nella forma `<ambito>: <cosa
cambia>`.

ESR, proposte, manoscritti e deliverable reali stanno in `materiali/`, che non
è versionato, e non entrano mai nel repository né negli esempi delle skill: nel
plugin vanno solo pattern anonimizzati.

## Dove guardare

| Per | Leggi |
|---|---|
| il significato preciso di dominio, nucleo, revisione, modalità, segnaposto | `CONTEXT.md` |
| scrivere o modificare una skill o un agente | `docs/scrivere-una-skill.md` |
| capire quale skill deve prendersi una richiesta | `docs/instradamento.md` |
| perché una scelta è stata fatta così | `docs/adr/README.md` |
| il dominio proposte, non ancora scritto | `docs/proposte.md` |
| provare un aggiornamento prima di rilasciarlo | `prove/README.md` |

`CONTEXT.md` è il glossario di chi sviluppa. Non confonderlo con
`nucleo/terminologia.md`, che è la terminologia dei testi prodotti (allerta,
early warning system, DEWETRA) e viaggia dentro le skill.
