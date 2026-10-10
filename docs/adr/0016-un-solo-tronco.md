# Un solo tronco: via il modello hub e dominio

Il plugin è nato sull'app di Claude, dove più conversazioni lavoravano in
parallelo senza vedersi. Per tenerle separate si erano introdotti un branch e
un worktree per dominio, una sessione "hub" che integrava le pull request, e
un `BRIEF.md` che faceva da memoria condivisa fra sessioni cieche l'una
all'altra.

Quella macchina serviva al parallelismo, non al repository. Con un solo autore,
nessuna CI e file di Markdown, costava più di quanto rendesse, e lasciava
residui pericolosi: il dominio paper è rimasto per giorni su un branch locale
mai pushato, e un worktree puntava a una sessione cloud che non esisteva più.

Da ora: un solo checkout, si lavora su `main`, e un branch breve con pull
request solo per una modifica grossa o rischiosa. Niente worktree, niente
branch permanenti per dominio.

Il principio che il modello proteggeva (chi scrive una skill non tocca il
nucleo di sua iniziativa) non dipendeva dai branch: resta come regola in
`CLAUDE.md`.

Deciso il 2026-10-10.
