---
type: llm
weight: 1
---

Il prompt non fornisce il materiale da cui nasce il mazzo. La skill fa una
domanda sola, sul materiale mancante; se nessuno risponde, procede con un
mazzo di segnaposto dichiarando che va rifatto quando il materiale arriva.

PASS se vale una delle due:

- la risposta chiede il materiale mancante con una domanda sola, senza una
  raffica di domande;
- la risposta consegna scaletta e mazzo, dichiara fra le assunzioni la durata
  ipotizzata e avverte che il mazzo va rifatto quando arriva il materiale.

Il materiale mancante qui è il paper. Se consegna il mazzo, è dimensionato
per un talk EGU di circa dieci minuti, domande comprese: una decina di slide
di contenuto, non quaranta.

In tutti e due i casi: nessun numero, risultato o nome inventato; ciò che
manca è un segnaposto fra parentesi quadre.

FAIL se una qualunque di queste condizioni non vale.
