---
type: llm
weight: 1
---

La consegna rispetta la regola del formato. PASS se vale una delle due:

- dice di aver prodotto un file `.docx` e ne dà il percorso;
- dichiara in una riga che la skill `docx` non è disponibile nell'ambiente e
  consegna il contenuto completo in Markdown strutturato.

FAIL se consegna solo Markdown senza dire perché, o se chiede all'utente di
incollare il testo del file invece di aprirlo.
