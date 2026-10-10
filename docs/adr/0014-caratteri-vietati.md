# Trattino em e punto medio sono errori di build

Il trattino em (quello lungo) e il punto medio usato come separatore sono due
dei marcatori più riconoscibili della scrittura generata, e sono nell'elenco
degli anti-pattern che il plugin insegna a evitare.

Vietarli nei testi prodotti non basta: il modello imita gli esempi che ha sotto
gli occhi, comprese le istruzioni che sta eseguendo. Per questo
`scripts/build.py` tratta come errore qualsiasi occorrenza nei file del plugin
e del nucleo, istruzioni e commenti compresi. Unica esenzione:
`anti-pattern-ai.md`, che li nomina per vietarli.

Il punto medio si è aggiunto al trattino em il 2026-10-10, su indicazione
dell'utente, dopo che il template delle presentazioni CIMA è risultato
suggerirlo nei propri segnaposto (riga degli autori, piè di pagina): un
segnaposto che suggerisce un carattere vietato è esattamente il modo in cui il
carattere rientra dalla finestra.

È una regola che sembra pedanteria e verrà tolta da qualcuno: questo ADR esiste
per spiegare perché non va tolta. Non vale per i file fuori dal plugin (README,
CONTEXT.md, ADR, prove).

Deciso il 2026-10-10.
