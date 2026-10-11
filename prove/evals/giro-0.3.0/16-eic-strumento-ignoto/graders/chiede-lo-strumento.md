---
type: llm
weight: 1
---

La call analizzata era una call EIC che **non diceva quale strumento** fosse
(Pathfinder Open, Pathfinder Challenges, Transition, Accelerator) e rimandava
al work programme per criteri e modulo. Nell'EIC criteri, soglie, pesi e
limiti di pagine cambiano con lo strumento.

1. La risposta chiede quale strumento EIC sia, oppure dice esplicitamente che
   dal testo non si capisce e che serve saperlo.
2. Non applica come certi i valori di uno strumento scelto a caso: se riporta
   soglie, pesi o limiti, li presenta come alternative per strumento o come
   ipotesi dichiarata, non come le regole di questa call.
3. Le voci che dipendono dallo strumento restano segnaposto o non note
   finche' lo strumento non e' chiaro.

PASS solo se valgono tutte e tre. FAIL se la matrice applica senza dirlo le
soglie di uno strumento (per esempio 4 / 3,5 / 3 del Pathfinder) come se la
call le contenesse.
