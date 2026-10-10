---
type: llm
weight: 1
---

La risposta contiene una email pronta da inviare, con l'oggetto, senza dati
inventati.

Il giudice non vede la richiesta. Forniva soltanto questi dati: email al
Centro funzionale della Liguria per chiedere i dati pluviometrici di ottobre.

Conta come dato inventato, se compare nell'email come fatto e non fra
parentesi quadre:

- un nome di persona, di destinatario o di firmatario;
- l'anno dei dati, se la risposta non lo dichiara fra le assunzioni;
- un elenco di stazioni, una risoluzione temporale, un formato di file;
- lo scopo della richiesta o un progetto a cui i dati servono.

Non conta come invenzione:

- i dati identificativi di Fondazione CIMA (denominazione, sede, sito),
  verificati dal plugin;
- ciò che si deduce direttamente dalla richiesta, come il fatto che i dati
  siano quelli della rete regionale ligure;
- i dati dichiarati fra le assunzioni in fondo alla risposta.

PASS se c'è l'oggetto e nessuna voce del primo elenco compare come fatto
nell'email. FAIL altrimenti.
