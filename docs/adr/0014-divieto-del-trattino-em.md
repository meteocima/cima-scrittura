# Il trattino em è un errore di build

Il trattino em (quello lungo) è uno dei marcatori più riconoscibili
della scrittura generata, ed è nell'elenco degli anti-pattern che il
plugin insegna a evitare.

Vietarlo nei testi prodotti non basta: il modello imita gli esempi che
ha sotto gli occhi, comprese le istruzioni che sta eseguendo. Per questo
`scripts/build.py` tratta come errore qualsiasi trattino em nei file del
plugin e del nucleo, istruzioni e commenti compresi. Unica esenzione:
`anti-pattern-ai.md`, che lo nomina per vietarlo.

È una regola che sembra pedanteria e verrà tolta da qualcuno: questo
ADR esiste per spiegare perché non va tolta. Non vale per i file fuori
dal plugin (brief, README, CONTEXT.md, ADR).

Deciso il 2026-10-10.
