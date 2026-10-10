# Il nucleo viene duplicato dentro ogni skill a build time

In chat le skill si caricano una per volta: una skill non può leggere i
file di un'altra, né un file che sta fuori dalla propria cartella. Le
regole comuni (vincoli, anti-pattern, verifica fonti, voce, terminologia,
protocollo di revisione) devono però essere identiche ovunque.

`scripts/build.py` copia quindi `nucleo/*.md` dentro `references/nucleo/`
di ogni skill al momento della build. La fonte unica resta `nucleo/`: nel
sorgente le skill non contengono `references/nucleo/` e la build fallisce
se ce lo trovano.

La duplicazione è visibile in `dist/` e sembra un errore: non lo è. Chi
"mette ordine" accorpando quelle copie rompe il caricamento in chat, che
è il modo in cui il plugin arriva alla maggior parte di CIMA.

Deciso il 2026-10-10.
