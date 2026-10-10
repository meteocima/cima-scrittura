# Il plugin lavora sui documenti, non solo sul testo

Fino alla versione 0.2.0 il plugin sapeva scrivere testo e nominare i file. Un
censimento delle nove skill lo mostrava netto: `.pptx`, `.xlsx` e i PDF da
leggere non comparivano da nessuna parte, e il `.docx` compariva solo come
formato in cui consegnare, mai come file da aprire. Gli agenti revisori avevano
`Read, Glob, Grep, Write`, con cui un `.docx`, che è uno zip di XML, non si
apre.

Intanto il mondo chiede file: Copernicus vuole l'author's response come PDF
separato più una versione marked-up, AGU vuole il file Word finale più un
"Article Tracked Changes" e rifiuta il PDF, Alpine Space fa ricaricare un
clarification form in Word. Il plugin li nominava e non ne produceva nessuno.

Da ora `nucleo/formati-e-file.md` stabilisce che si legge nel formato in cui
l'utente consegna e si restituisce nello stesso formato, che i template
imposti prevalgono sulla struttura suggerita dalla skill, e che un rapporto di
revisione su un `.docx` può tornare dentro il documento con modifiche tracciate
e commenti.

La meccanica non è nostra: la fanno le skill `docx`, `pptx`, `xlsx` e `pdf`,
sincronizzate sull'account e quindi presenti in tutti gli ambienti in cui il
plugin gira. Il plugin CIMA decide che cosa scrivere, quelle sanno come si
impacchetta un OOXML. Riscrivere quel pezzo qui sarebbe stato lavoro doppio e
peggiore.

Vincolo che resta: ogni intervento di un revisore dentro un documento è una
modifica tracciata o un commento, mai una correzione silenziosa. Il revisore
propone in modo visibile e rifiutabile, come vuole `adr/0005`.

Deciso il 2026-10-10.
