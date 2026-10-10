# Instradamento misurato in cieco, 10 ottobre 2026

Otto casi in `prove/evals/instradamento/`, eseguiti da `claude plugin eval`:
sessioni figlie che non hanno letto né le prove né gli esiti attesi, e che
ricevono solo la frase. Misurano **quale** skill si attiva, non la qualità del
testo. Costo totale 1,94 dollari, 113 secondi con quattro in parallelo.

| Caso | Frase | Skill attivata | Atteso |
|---|---|---|---|
| 02 | "Il project officer ci ha mandato dei commenti sul report. Dobbiamo rispondere." | `progetti-risposta-review` | corretto |
| 03 | "Mi serve un abstract per EGU" | `paper-scrittura` | corretto |
| 04 | "Scrivi due righe al project officer per spostare la call di lunedì" | `generale-scrittura` | corretto |
| 05 | "Prepara le slide per il kickoff del progetto, mezz'ora" | `generale-presentazione` | corretto |
| 07 | "Traduci in inglese l'abstract" | `generale-traduzione` | corretto |
| 08 | "Rivedi questo testo" + testo di un deliverable | `generale-revisione`, poi `progetti-revisione` | corretto |
| 01 | "Scrivi il work package 3" | **nessuna** | ambigua di proposito |
| 06 | "Draft the impact section" | **nessuna** | ambigua di proposito |

## Che cosa dicono

**I confini tengono.** Sei casi su otto vanno dove devono, compreso il più
sottile: una email di routine al project officer va a `generale`, non a
`progetti`, che è la distinzione che la tabella di instradamento fa su "la
natura del testo, non il destinatario". E la porta d'ingresso senza contesto
funziona come progettata: `generale-revisione` riconosce il deliverable e
passa la mano a `progetti-revisione`.

**Il buco è nel mezzo ambiguo, e non è quello che temevamo.** Sulle due frasi
costruite per essere ambigue non si attiva la skill sbagliata: non si attiva
**nessuna** skill. Chi scrive riceve una risposta senza le regole CIMA, senza
il divieto di inventare, senza segnaposto, e non ha modo di accorgersene. Un
degrado silenzioso è peggio di un instradamento sbagliato, perché un
instradamento sbagliato si vede.

**Questo è un argomento a favore dell'unione, non contro.** "Scrivi il work
package 3" e "draft the impact section" sono ambigue fra proposta e progetto:
se le due fasi fossero un dominio solo, una skill le coprirebbe e scatterebbe.
La misura non conferma l'architettura attuale su questo punto.

La terza via, che non richiede di unire i domini: far rivendicare le frasi
ambigue a `progetti-scrittura`, che poi fa **una domanda sola** ("il Grant
Agreement è già firmato?") e passa la mano a `proposte` se siamo prima. Da
verificare con gli stessi casi, dopo averla scritta.
