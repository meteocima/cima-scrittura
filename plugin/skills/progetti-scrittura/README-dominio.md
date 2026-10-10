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

In chat ogni skill vede solo la propria cartella, e `build.py` copia
solo `nucleo/`. Per questo alcuni file sono duplicati. La fonte unica è
`progetti-scrittura/references/`; le copie vanno tenute identiche.

| File | scrittura | revisione | risposta-review |
|---|---|---|---|
| `matrice-doa.md` | fonte | copia | copia |
| `anti-pattern-progetti.md` | fonte | copia | copia |
| `griglia-revisione.md` | fonte | copia | |
| `programmi/*.md` | fonte | copia | copia |
| `tipi-documento.md` | solo qui | | |
| `formato-risposta.md` | | | solo in risposta-review |

Dopo ogni modifica, dalla radice del repository:

```
S=plugin/skills/progetti-scrittura/references
for d in progetti-revisione progetti-risposta-review; do
  cp $S/matrice-doa.md $S/anti-pattern-progetti.md plugin/skills/$d/references/
  cp $S/programmi/*.md plugin/skills/$d/references/programmi/
done
cp $S/griglia-revisione.md plugin/skills/progetti-revisione/references/
```

Controllo: `diff -r` tra fonte e copie non deve dare output per i file
elencati. Proposta alla chat hub: cartella `plugin/condivisi/<prefisso>/`
copiata dalla build nelle skill del prefisso, per eliminare le copie.

## Profili dei programmi

Costruiti il 2026-10-10 da fonti ufficiali con ricerca web. Ogni
profilo ha in fondo i "Punti da verificare". Aggiornarli almeno una
volta l'anno o quando cambia un template. Calibrazione con review
report reali di CIMA: non ancora fatta (nel plugin solo pattern
anonimizzati).
