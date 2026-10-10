# Dominio progetti: note per chi mantiene le skill

File non incluso nel plugin (escluso da `scripts/build.py`).

## Skill e agente

- `progetti-scrittura`: deliverable, parte tecnica dei report, technical
  report, summary, DMP.
- `progetti-revisione`: revisione simulata con profili project officer e
  reviewer tecnico esterno, sintesi nel contesto principale.
- `progetti-risposta-review`: risposta a review report, rifiuti di
  deliverable, richieste di chiarimento.
- Agente `progetti-revisore` (in `plugin/agents/`), parametrizzato per
  profilo.

## File condivisi tra le skill del dominio

Stanno in `plugin/condivisi/progetti/` (BRIEF §3). `scripts/build.py` li
copia in `references/` di ogni skill `progetti-*`; nel SKILL.md si
citano come `references/<file>.md`. Il sorgente delle skill non deve
contenerne copie: la build si ferma.

| File | Usato da |
|---|---|
| `matrice-doa.md` | tutte e tre le skill |
| `anti-pattern-progetti.md` | tutte e tre le skill, agente (percorso passato nel prompt) |
| `griglia-revisione.md` | scrittura, revisione, agente |
| `programma-horizon-europe.md`, `programma-interreg.md`, `programma-life.md`, `programma-ucpm.md` | tutte e tre le skill |

La build copia anche le sottocartelle di `condivisi/progetti/` (brief
v6); i profili restano `programma-<nome>.md` finché la sessione di dominio
non decide di spostarli. Nuovo programma: aggiungere il file e la riga
nell'elenco dei profili delle tre SKILL.md.

File di una sola skill, restano nella skill: `tipi-documento.md`
(scrittura), `formato-risposta.md` (risposta-review).

## Profili dei programmi

Costruiti il 2026-10-10 da fonti ufficiali con ricerca web. Ogni
profilo ha in fondo i "Punti da verificare". Aggiornarli almeno una
volta l'anno o quando cambia un template. Calibrazione con review
report reali di CIMA: non ancora fatta (nel plugin solo pattern
anonimizzati).
