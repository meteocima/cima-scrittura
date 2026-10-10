---
type: llm
weight: 1
---

La risposta deve contenere la matrice di un bando. Il bando analizzato
dichiarava esplicitamente queste cose, e la matrice deve riportarle tutte e
quattro:

1. La soglia del criterio Impact e' **4**, non 3, e la soglia complessiva
   resta 10. Se la matrice riporta 3 per Impact, e' FAIL.
2. Il limite della proposta e' **30 pagine**. Se riporta 40 o 45, e' FAIL.
3. I tre expected outcome del bando hanno ciascuno la propria riga: capacita'
   di anticipazione delle autorita' di protezione civile, servizi di
   previsione basata sugli impatti validati in almeno due contesti operativi,
   maggiore uso di dati idrologici aperti e prodotti di allertamento
   interoperabili. Riassunti in una riga sola o fusi insieme: FAIL.
4. Fra i requisiti obbligatori compare il work package dedicato alle attivita'
   di clustering con gli altri progetti della call.

PASS solo se valgono tutte e quattro.
