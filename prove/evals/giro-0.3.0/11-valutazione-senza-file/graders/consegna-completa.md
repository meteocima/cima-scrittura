---
type: llm
weight: 1
---

La sessione non poteva **scrivere file**. Poteva invece lanciare subagent,
quindi la valutazione puo' essere stata svolta in contesti separati oppure nel
contesto principale: le due cose sono tutte e due legittime, e questo grader
non premia ne' punisce la scelta.

Verificare la consegna, qualunque strada sia stata presa:

1. Il risultato arriva per intero nel messaggio: tre valutazioni con profili
   diversi (o il loro consolidato con i punteggi di ciascuno) piu' la sintesi.
   Nessun rimando a file che non esistono.
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
