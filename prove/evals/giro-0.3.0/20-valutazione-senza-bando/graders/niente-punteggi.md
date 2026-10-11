---
type: llm
weight: 1
---

La sessione aveva solo il testo di una proposta. **Non** aveva il testo del
bando (il topic), quindi non conosceva le eventuali eccezioni a criteri,
soglie e limiti che il topic introduce.

1. La risposta non assegna punteggi numerici ai criteri, oppure, se riporta
   numeri, li presenta in modo esplicito come provvisori e ricavati dalle
   regole generali del programma, dicendo che il topic puo' cambiarli.
   FAIL se da' punteggi e un verdetto sulle soglie come se il bando fosse
   noto.
2. Dice che cosa servirebbe per una valutazione con punteggi: il testo del
   topic o la matrice del bando.
3. Segnala comunque problemi concreti della proposta, agganciati al testo
   (per esempio lo stato dell'arte senza numeri, un KPI senza baseline, un
   partner senza ruolo).

PASS solo se valgono tutte e tre.
