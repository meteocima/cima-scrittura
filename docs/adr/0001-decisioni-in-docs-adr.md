# Registrare le decisioni in `docs/adr/`

Le decisioni architetturali vivevano in `BRIEF.md` sezione 8, come elenco
numerato di righe. Funzionava finché erano poche, ma una riga non tiene il
perché di una scelta, le alternative scartate e lo stato (presa, aperta,
superata), e le sessioni di dominio citavano le decisioni per numero di
posizione nell'elenco, che cambia a ogni inserimento.

Da ora ogni decisione sta in `docs/adr/NNNN-slug.md` e la sezione 8 del
brief è solo un indice di rimandi. Il brief resta la fonte dell'architettura
corrente, gli ADR sono la memoria di come ci siamo arrivati: se i due
divergono, il brief descrive il presente e l'ADR va marcato superato.

Deciso il 2026-10-10.
