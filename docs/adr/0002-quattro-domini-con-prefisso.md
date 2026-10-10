# Quattro domini, con il prefisso nel nome

Il plugin copre testi molto diversi (una email, un paper, una proposta
europea, un deliverable) che condividono le regole di fondo ma non i
criteri di qualità. Sono stati separati in quattro domini: `generale`,
`paper`, `proposte`, `progetti`.

Il prefisso non è una convenzione estetica: `scripts/build.py` lo usa per
decidere quali file condivisi iniettare in una skill, e le descrizioni lo
usano per l'instradamento fra skill che altrimenti si attiverebbero sulle
stesse parole ("scrivi", "review", "abstract"). Un nome senza prefisso
fa fallire la build.

Deciso il 2026-10-10.
