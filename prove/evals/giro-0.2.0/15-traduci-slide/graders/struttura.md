---
type: llm
weight: 1
---

La risposta dice di aver tradotto dentro il `.pptx`, in un file nuovo che non
sovrascrive l'originale, conservandone la struttura: stesso numero di slide,
stessi layout, segnaposto conservati e tradotti.

Se la skill `pptx` non è disponibile, è accettabile anche il testo tradotto
slide per slide, purché la risposta lo dichiari in una riga.

FAIL se dice di aver rifatto il mazzo da capo, o se consegna solo testo senza
dire perché.
