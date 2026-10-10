# `BRIEF.md` sciolto nei file che hanno la sua materia

Il brief era arrivato a 404 righe e teneva insieme nove sezioni eterogenee:
obiettivi, principi, struttura delle cartelle, convenzioni, specifiche dei
quattro domini, instradamento, flusso di lavoro, decisioni, comandi di build.
Si leggeva per intero o non si leggeva.

Buona parte era diventata copia di una fonte più autorevole: le convenzioni
che `build.py` fa rispettare, la struttura che si vede guardando le cartelle,
le specifiche dei domini ormai scritti, che le skill definiscono meglio di
qualsiasi descrizione. Una regola in due posti diverge nei due posti.

Il brief è stato quindi sciolto, con il criterio di mettere ogni pezzo dove si
legge nel momento in cui serve: `CLAUDE.md` per ciò che vale a ogni turno,
`CONTEXT.md` per il vocabolario, `docs/scrivere-una-skill.md` per chi sta
scrivendo una skill, `docs/instradamento.md` per i confini fra domini,
`docs/proposte.md` per il dominio allora non ancora scritto (cancellato quando
il dominio è stato costruito), `docs/adr/` per il
perché.

Conseguenza da tenere a mente: non esiste più un file da "leggere per intero
prima di tutto". Il punto d'ingresso è `CLAUDE.md`, che si carica da solo e
rimanda al resto.

Deciso il 2026-10-10.
