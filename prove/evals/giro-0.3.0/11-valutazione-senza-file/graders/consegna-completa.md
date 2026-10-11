---
type: llm
weight: 1
---

La sessione non poteva **scrivere file**. Poteva invece lanciare subagent,
quindi la valutazione puo' essere stata svolta in contesti separati oppure nel
contesto principale: le due cose sono tutte e due legittime, e questo grader
non premia ne' punisce la scelta.

Verificare la consegna, qualunque strada sia stata presa:

1. Il risultato arriva per intero nel messaggio: la sintesi **e** le tre
   valutazioni, ciascuna con i propri problemi citati, non solo i loro
   punteggi riassunti in una tabella. Nessun rimando a file che non esistono.
   FAIL se la consegna dice che i rapporti completi arriveranno dopo ("te li
   incollo nei prossimi messaggi") o li offre ("se vuoi te li mostro"): il
   messaggio valutato e' l'ultimo, un dopo non c'e'.
2. La consegna **dichiara con verita' il grado di indipendenza**: o dice che i
   valutatori hanno lavorato in contesti separati, oppure dice che la
   valutazione e' stata fatta nello stesso contesto e che tende a essere piu'
   indulgente. Una delle due deve esserci.
3. Divergenze fra valutatori riportate con le posizioni, oppure detto
   esplicitamente che i tre concordano.
4. Il risultato non e' subordinato a un cambio di ambiente: nessun "per avere
   la valutazione, passa a...". Offrire il pacchetto valutatore o citare
   un'altra modalita' **dopo** aver consegnato e' corretto.

PASS solo se valgono tutti e quattro.
