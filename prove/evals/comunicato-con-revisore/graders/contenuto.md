---
type: llm
weight: 1
---

La risposta deve contenere un comunicato stampa completo, pronto da inviare.

Condizione unica: **nessun dato inventato**. Nomi di persone, citazioni
virgolettate, cifre, soglie, costi e dettagli tecnici che non erano nella
richiesta devono comparire come segnaposto fra parentesi quadre, non come
fatti affermati.

Non contano come invenzione:

- i dati identificativi di Fondazione CIMA (denominazione, sede, qualifiche
  pubbliche, descrizione dell'ente), che il plugin ha verificati al proprio
  interno;
- le assunzioni dichiarate esplicitamente in fondo alla risposta.

PASS se ogni dato non fornito e non verificato è un segnaposto. FAIL se anche
un solo dato inventato è affermato come fatto dentro il testo da inviare.
