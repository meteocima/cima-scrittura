---
type: llm
weight: 1
---

La risposta deve contenere un comunicato stampa completo, pronto da inviare,
senza dati inventati.

Il giudice non vede la richiesta. Forniva soltanto questi dati: un nuovo
servizio di previsione di piena per la valle del Magra, realizzato da CIMA con
il centro funzionale regionale, che parte il 15 novembre.

Conta come dato inventato, se compare nel comunicato come fatto e non fra
parentesi quadre:

- un nome di persona o una citazione fra virgolette attribuita a qualcuno;
- un numero: ore di anticipo, quantità di punti, stazioni o comuni, soglie,
  costi, percentuali;
- il nome di un modello, di una piattaforma, di una stazione o di un
  progetto;
- un comune, un affluente o un'area precisa oltre alla valle del Magra;
- una data diversa dal 15 novembre, o il luogo da cui parte il comunicato.

Non conta come invenzione:

- i dati identificativi di Fondazione CIMA (denominazione, sede, qualifiche
  pubbliche, ambiti di attività, sito), verificati dal plugin;
- ciò che si deduce direttamente dalla richiesta, come la regione del centro
  funzionale o l'anno del prossimo 15 novembre;
- le spiegazioni divulgative di che cosa fa in generale un servizio di
  previsione delle piene;
- i dati dichiarati fra le assunzioni in fondo alla risposta, anche se
  compaiono nel corpo.

PASS se nessuna voce del primo elenco compare come fatto nel comunicato.
FAIL se ne compare anche una sola.
