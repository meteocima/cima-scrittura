# Instradamento fra domini

Le descrizioni delle skill si sovrappongono su parole come "scrivi", "draft",
"review", "proposal", "abstract". Questa tabella è la fonte unica dei confini:
la clausola "Non usare per…" di ogni `description` e le tabelle "Confini"
dentro le skill ne sono viste, e devono concordare.

| Richiesta | Va a |
|---|---|
| proposta, bando, call, topic, Part B, ESR, work package, consorzio (pre-finanziamento) | proposte |
| deliverable, periodic report, technical report, review di un progetto in corso, Grant Agreement, DoA | progetti |
| risposta di merito a project officer o reviewer di progetto (review report, deliverable respinto, chiarimenti su un report) | `progetti-risposta-review` |
| email di routine al project officer (date, riunioni, logistica, invio di documenti) | generale |
| paper, manuscript, articolo, journal, revisori, rebuttal, cover letter | paper |
| abstract per conferenza o rivista | paper |
| abstract di una proposta | proposte |
| email, lettera, comunicato, post, verbale, testo web | generale |
| slide, presentazione, talk, deck, mazzo (di qualsiasi dominio) | generale (`generale-presentazione`): costruisce il mazzo con il tema CIMA e prende i criteri di contenuto dalla skill del dominio |
| "rivedi questo testo" senza contesto | generale, che rimanda se riconosce un paper o una proposta |
| traduci, translate (qualsiasi testo) | generale (`generale-traduzione`): per abstract, paper, proposte e deliverable traduce lingua e terminologia senza cambiare struttura e contenuto; per adattarli ai limiti del dominio rimanda alla skill di quel dominio |

Due confini che si sbagliano facilmente:

- fra **proposte** e **progetti** decide la firma del Grant Agreement, non
  l'argomento: la risposta agli ESR di una proposta resta in `proposte` anche
  a progetto avviato (`adr/0009`);
- fra **generale** e **progetti** decide la natura del testo, non il
  destinatario: al project officer si scrive da entrambi i domini;
- le **presentazioni** sono un formato, non un dominio: il mazzo lo fa sempre
  `generale-presentazione`, il contenuto resta di chi lo possiede.

**Il dominio `proposte` non è ancora scritto.** Le righe che lo riguardano
indicano dove andrà, non dove va oggi: finché quelle skill non esistono, vale
la regola di `nucleo/vincoli.md`, sezione 4, cioè si svolge comunque il
compito dichiarando quali criteri del dominio mancano.

Prima di un rilascio l'instradamento si prova con i prompt in `prove/`.
