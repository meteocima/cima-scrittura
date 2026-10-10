# Ogni skill consegna il risultato completo anche senza agenti

Gli agenti esistono solo dove c'è lo strumento per lanciare subagent. La
maggior parte di CIMA usa il plugin in chat, dove non c'è. L'alternativa
scartata era far fermare la skill e chiedere all'utente di spostarsi su
Cowork.

Ogni passaggio che in modalità agenti farebbe un agente (revisione,
sintesi del rapporteur, verifica di coerenza, decisione dell'editor)
viene quindi svolto nel contesto principale, con lo stesso formato di
output, dichiarando in una riga che non è indipendente. La skill non si
ferma e non consegna a metà.

Conseguenza concreta: ogni SKILL.md che nomina un agente deve avere una
sezione `## Modalità chat`, e `scripts/build.py` blocca la build se
manca. La modalità si deduce dagli strumenti disponibili, non si chiede
all'utente.

Deciso il 2026-10-10 (brief v4).
