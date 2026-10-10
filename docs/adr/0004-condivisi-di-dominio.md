# Riferimenti comuni di dominio in `plugin/condivisi/<dominio>/`

Alcuni riferimenti servono a più skill dello stesso dominio ma non a
tutto il plugin: tipologie, destinatari e checklist per `generale`,
matrice DoA e griglia per `progetti`. Tenerne una copia per skill
significava modificarne tre e dimenticarne una.

Stessa soluzione del nucleo, un livello più in basso: fonte unica in
`plugin/condivisi/<dominio>/`, la build la copia in `references/` delle
sole skill di quel dominio, sottocartelle comprese. Il sorgente di una
skill non può contenerne copie: la build si ferma.

Proposto dalla sessione del dominio generale (PR #1), deciso il
2026-10-10. Supera l'istruzione precedente, che chiedeva di modificare
tutte le copie insieme.
