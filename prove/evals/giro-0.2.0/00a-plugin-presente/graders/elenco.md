---
type: llm
weight: 1
---

La risposta elenca le skill e gli agenti del plugin come caricati nella
sessione, non come letti da file del repository.

Skill attese, dieci: generale-scrittura, generale-revisione,
generale-traduzione, generale-presentazione, paper-scrittura,
paper-revisione, paper-risposta-revisori, progetti-scrittura,
progetti-revisione, progetti-risposta-review.

Agenti attesi, cinque: generale-revisore,
generale-revisore-presentazione, paper-revisore, paper-editor,
progetti-revisore.

PASS se compaiono tutti e quindici i nomi e nessuna skill `proposte-*`
viene presentata come attiva. FAIL se ne manca anche uno, o se la
risposta resta vaga.
