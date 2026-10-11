# Le descrizioni dicono di caricare la skill prima di chiedere chiarimenti

Con Sonnet in Cowork le richieste brevi non attivavano le skill: su "Scrivi
il work package 3" `progetti-scrittura` partiva una volta su cinque, contro
quattro su quattro con Opus. Sonnet vedeva le skill e le attivava se nominate
o davanti a una richiesta precisa; su una richiesta vaga preferiva fare
domande sue nel riquadro di Cowork. In Claude Code il difetto non si vede,
perche' alle sessioni di `claude plugin eval` quel riquadro non e' offerto
(issue #35).

Una frase nella descrizione di `progetti-scrittura`, "caricarla prima di
chiedere chiarimenti, perche' la domanda giusta la fa lei", l'ha portata a
cinque su cinque. Il 2026-10-11 la stessa indicazione e' stata estesa alle
skill che ricevono richieste brevi e sanno da sole che cosa chiedere:
`generale-scrittura`, `generale-presentazione`, `paper-scrittura`,
`paper-risposta-revisori`, `proposte-scrittura`, `proposte-concept`,
`proposte-analisi-bando`, `progetti-risposta-review` (issue #36). Le skill
di revisione e di traduzione ne restano fuori: ricevono un testo, e la
richiesta non e' vaga.

Sulle otto skill dell'estensione l'effetto in Cowork non e' ancora misurato:
lo misura `prove/0.3.1-chiarimenti/`. Se per una skill la frase non cambia
niente, la si toglie da quella.

Conseguenza per chi scrive una skill nuova: `docs/scrivere-una-skill.md`.
