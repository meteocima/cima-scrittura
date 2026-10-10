---
status: proposed
---

# Modello dei valutatori

Aperta. Il campo `model` degli agenti accetta `inherit`, `sonnet`, `opus`
e `haiku` (già validato da `scripts/build.py`), quindi si potrebbe far
girare i valutatori su un modello diverso da quello che ha scritto, per
aumentare la diversità di giudizio.

Limiti noti: vale solo in modalità agenti; i modelli sono della stessa
famiglia, quindi la diversità che se ne ricava è minore di quella data
da contesto separato e profili diversi (ADR 0005); la disponibilità
dipende dal piano dell'organizzazione.

Si decide con il test di accettazione del dominio proposte: stessa
proposta valutata con `inherit` e con un modello diverso, confronto fra i
due esiti e l'ESR reale. Fino ad allora: `inherit`.
