# 10-valutazione-agenti e 11-valutazione-senza-file

Stessa proposta finta e stesso topic finto, strumenti diversi: il 10 puo'
scrivere file, l'11 no.

**I due casi non misurano la modalita'.** Misurato il 2026-10-10: la suite non
puo' togliere `Agent` e `Task` a una sessione figlia, perche' `allowed_tools`
non li governa. Una sessione senza `Write` puo' lanciare lo stesso i
valutatori, e in due esecuzioni su tre lo ha fatto. Quindi il caso 11 misura
che cosa succede **senza poter salvare file**, non la modalita' chat. La
modalita' chat resta una prova a mano, con lo zip della skill caricato in una
conversazione.

I grader sono scritti di conseguenza: chiedono che la consegna sia completa e
che dichiari **con verita'** se la valutazione e' stata indipendente oppure
no, senza premiare una delle due strade.

## Che cosa c'e' nella proposta finta

Sei difetti piantati: "beyond the state of the art" senza numeri; un KPI senza
baseline; la formazione di 200 operatori promessa e non prodotta da nessun
work package; un partner senza ruolo; rischi generici; tre casi di studio nel
testo contro due in tabella.

## Che cosa c'e' nel topic finto

Tre divergenze volute rispetto al profilo: soglia di Impact a 4 invece di 3,
limite di 30 pagine invece di 40, pesi non dichiarati.

## Perche' questo elenco non sta nel materiale

Fino al 2026-10-10 ci stava, e una sessione misurata lo ha fatto notare da
sola: aveva letto quali difetti doveva trovare, quindi trovarli non dimostrava
niente.
