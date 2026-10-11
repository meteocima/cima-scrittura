# Senza file la revisione resta agli agenti, con i materiali nel prompt

Il protocollo diceva: se i file non si riescono a salvare, la modalità
agenti non è praticabile e si passa alla modalità chat. La regola era nata
nel giro 0.2.0 (rilievo 9) contro un difetto preciso, il revisore arruolato
come scrivano per salvare la bozza al posto della skill. La cura scelta era
più larga del difetto: per non far scrivere il revisore, si rinunciava al
revisore.

Il 2026-10-10 il caso `giro-0.3.0/11-valutazione-senza-file` ha mostrato che
le sessioni non la seguono: in due esecuzioni su tre hanno lanciato lo
stesso i valutatori passando la proposta nel prompt, e lo hanno dichiarato.
Quella strada non viola `0005`, perché il valutatore vede testo e criteri e
non la conversazione; e garantisce più della modalità chat, dove il giudizio
viene dallo stesso contesto che ha scritto il testo.

I rischi che giustificavano il divieto sono due: nel prompt può scivolare
il contesto dell'autore, e un materiale lungo non ci sta. Sono ragioni per
regolare la strada, non per vietarla. Quindi, in
`nucleo/protocollo-revisione.md`, sezione 3, "Senza file":

- ciò che ha già un percorso leggibile si passa per percorso;
- ciò che non ce l'ha va nel prompt per intero e tale e quale, mai
  riassunto o a estratti;
- se per farlo stare bisogna tagliare, o se un materiale non si può dare
  come testo (la griglia di anteprime di un mazzo), si passa alla modalità
  chat come prima;
- il revisore restituisce il rapporto come risposta e la consegna lo porta
  per intero nella stessa risposta, senza offrirlo né prometterlo per dopo
  (`0006`).

Alternative scartate: rinforzare il divieto, che toglie indipendenza dove
si poteva avere; fissare una soglia in parole per "troppo lungo", che
invecchia con i modelli e non dice niente su ciò che conta, cioè che il
materiale arrivi intero.

Resta il divieto da cui tutto era partito: nessun agente salva file per
conto della skill, e meno che mai il revisore.

Deciso il 2026-10-11 (issue #29).
