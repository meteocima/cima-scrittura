# 0.2.0: file veri e presentazioni

Tre cose nuove. Il plugin **legge e scrive i file** nel formato in cui
arrivano, invece di nominarli soltanto (`nucleo/formati-e-file.md`). La
revisione di un `.docx` può tornare **dentro il documento**, con revisioni
tracciate e commenti. Nasce `generale-presentazione`, con il tema CIMA e il suo
revisore.

Le prove sui file usano i materiali in `materiali/`, che sono finti.

## Prove

### Prova zero: il plugin c'è davvero

Da fare per prima, in ogni ambiente, prima di qualunque altra riga. Se non
passa, il resto del giro non misura niente: misura Claude senza il plugin.

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 0a | agenti | "Quali skill di cima-scrittura hai attive, e quali agenti?" | Dieci skill e cinque agenti, con i nomi giusti. Se la risposta è vaga o parla di file letti dal repository invece che di skill caricate, il plugin non c'e' || **Passa.** Dieci skill (generale-scrittura, -revisione, -traduzione, -presentazione; paper-scrittura, -revisione, -risposta-revisori; progetti-scrittura, -revisione, -risposta-review) e cinque agenti (generale-revisore, generale-revisore-presentazione, paper-revisore, paper-editor, progetti-revisore), elencati dalle skill caricate. Il pacchetto installato coincide con la build di `v0.2.0-rc1` (diff vuoto, salvo la riserializzazione YAML delle `description` degli agenti fatta dalla sincronizzazione). Nota: nessuna skill `proposte-*`, ma le descrizioni e i confini delle altre la nominano (`proposte-revisione` in generale-revisione) |
| 0b | agenti | "Scrivi una email al Centro funzionale della Liguria per chiedere i dati pluviometrici di ottobre" | Si attiva `generale-scrittura` **da sola**, senza che nessuno la nomini. Se si attiva `cima-writing-style`, il vecchio plugin è ancora abilitato e va disattivato prima di proseguire || **Passa.** Si attiva `generale-scrittura`; `cima-writing-style` non c'è. Email esterna con oggetto, segnaposto per anno, stazioni, risoluzione, scopo e firma; autorevisione, nessun revisore (email). Riserva: chi esegue le prove ha letto l'esito atteso prima di scegliere la skill |

### File in ingresso e in uscita

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 1 | agenti | "Rivedi questa lettera" + `materiali/lettera-ministero.docx` | Apre il `.docx` senza chiedere di incollarlo; rapporto nel messaggio; nessuna riscrittura, perché il verbo è "rivedi" || **Passa.** Il `.docx` è letto senza chiedere di incollarlo; rapporto nel messaggio (14 problemi, 5 bloccanti, citazioni esatte), nessuna riscrittura, riscrittura offerta in una riga. Il rapporto non è stato riportato anche dentro il `.docx` (la skill lo permette, non lo impone) |
| 2 | agenti | "Migliora questa lettera" + stesso file | Riscrittura, quindi scrittura: parte `generale-revisore` perché è una lettera istituzionale (ADR 0011); consegna un `.docx`, non Markdown || **Passa.** Riscrittura nello stesso `.docx` (stile Body Text del file), `generale-revisore` lanciato con il solo prompt previsto; il rapporto ha trovato 11 problemi (ruolo "Direttore" da confermare, "noi" mescolato alla terza persona, nessun contatto per fissare la data); applicate le correzioni senza dati nuovi. Incidente di meccanica, non del plugin: riscrivendo i run con python-docx si è perso un a capo nell'intestazione, visto e corretto prima della consegna |
| 3 | chat | Stesso prompt della 2 | Stesso `.docx`, come file scaricabile; una riga dichiara che la revisione non è indipendente; offre il pacchetto revisore; non chiede di cambiare ambiente | |
| 4 | agenti | "Scrivi il D3.2 seguendo questo template" + `materiali/template-deliverable.docx` | Rispetta sezioni e numerazione del template; mette `[…]` dove mancano i dati invece di togliere le sezioni; consegna `.docx` || **Passa, con tre difetti.** Sezioni, ordine e numerazione del template intatti, compilato dentro il file, `[…]` ovunque manchino dati, consegna `.docx`, matrice DoA tutta `[da DoA]`, due `progetti-revisore` in parallelo. Difetti: (a) la prima bozza scriveva "WP3" dedotto dal numero D3.2, supposizione colta da entrambi i revisori e poi tolta; (b) il template è stato passato ai revisori come `.docx` e nessuno dei due l'ha potuto aprire (hanno solo Read): `progetti-scrittura` dice di passare "il template" ma non di ricavarne una versione leggibile, come chiede `protocollo-revisione.md` sez. 3 punto 1; (c) senza alcun materiale tecnico la revisione a due profili gira su uno scheletro di segnaposto e dà tutti 1: la skill non dice di rimandarla finché il testo non c'è |
| 5 | chat | Stesso prompt della 4 | Stesso contenuto, file scaricabile, stessa struttura del template | |
| 6 | agenti | "Rispondi a questo review report" + `materiali/review-report.pdf` | Legge il PDF; tabella commento, posizione, risposta, modifica; non copia frasi del report in ricerche web || **Passa, con un difetto.** PDF letto (pdftotext); tabella commento, citazione, posizione, risposta, modifica, responsabile, scadenza per C1-C4 e R1-R2; testo di accompagnamento, tabella di follow-up per RP2, decisioni del consorzio raccolte in fondo; nessuna ricerca web, quindi nessuna frase del report in rete. Due revisori in parallelo; corrette le incoerenze tra lettera e tabella che hanno trovato. Difetto: `progetti-risposta-review` non passa al revisore `griglia-revisione.md`, e i due agenti si sono inventati ciascuno una scala 0-5 diversa |

### Revisione dentro il documento

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 7 | agenti | "Controlla il D3.2 come lo leggerebbe il project officer" + `materiali/deliverable-bozza.docx` | Due profili e sintesi; il `.docx` torna con revisioni tracciate e commenti ancorati ai punti citati; sintesi e punteggi nel messaggio || **Passa.** Due `progetti-revisore` in parallelo (PO e reviewer tecnico), sintesi in `revisione/sintesi.md` con punti comuni, divergenze di gravità ed esito simulato ("rifiuto possibile", dichiarato come regola del plugin). Il `.docx` torna con 13 commenti ancorati alle frasi citate e revisioni tracciate solo per gli accenti (e' → è, attivita' → attività); validazione docx passata. Nota: il programma non è noto, quindi nessun profilo di programma passato ai revisori |
| 8 | chat | Stesso prompt della 7 | Stesso `.docx` commentato come file scaricabile; dichiara che i due profili non sono indipendenti | |
| 9 | agenti | Stesso della 7 | Il revisore **non** ha modificato il testo di nascosto: ogni intervento è una revisione tracciata o un commento, visibile e rifiutabile || **Passa.** Rifiutando tutte le revisioni tracciate il testo è identico all'originale (confronto pandoc `--track-changes=reject`); nessuna correzione silenziosa; il merito sta solo nei commenti. I revisori hanno visto soltanto una copia `.md` e non il `.docx`: l'impossibilità di toccare il documento viene dal processo, non dai permessi (l'agente ha `Write`) |

### Presentazioni

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 10 | agenti | "Fai le slide per la review di metà progetto di [progetto]" | Scaletta prima del mazzo; `.pptx` con il tema CIMA; i contenuti ricondotti alla DoA come vuole `progetti`; niente numeri inventati || **Passa, con riserve.** Scaletta prima del mazzo (15 slide: titolo, 9 di contenuto, 3 di sezione, 2 di backup), `.pptx` dal `tema-cima.pptx` con costanti nei layout e senza punto medio, ogni slide che chiede codici di task, deliverable e milestone, nessun numero inventato, validazione passata, autorevisione con la griglia. Riserve: (a) la skill impone di chiedere la durata; nessuno rispondeva e si è proseguito con 20 minuti dichiarati (intervento di chi prova); (b) il segnaposto `[progetto]` del prompt è stato sostituito con FLOODSENSE dei materiali; (c) non è chiaro se una review con la Commissione sia "istituzionale": la skill non lo dice, si è scelta l'autorevisione; (d) il paragrafo "concetto chiave" esce con lo stesso punto elenco del corpo |
| 11 | chat | Stesso prompt della 10 | Stesso mazzo, file scaricabile | |
| 12 | agenti | "Prepara la presentazione per la giornata con la Regione" | Mazzo istituzionale, quindi parte `generale-revisore-presentazione`; il rapporto arriva all'utente || **Passa.** Mazzo istituzionale (12 slide), scaletta e griglia di anteprime salvate, `generale-revisore-presentazione` lanciato con il solo prompt previsto; rapporto all'utente (filo dei titoli 1, perché i titoli sono segnaposto; 7 slide di contenuto per 20 minuti, troppo corte; tre sezioni per sette slide). Applicate le correzioni senza dati nuovi (sezione da una slide tolta, ruoli dell'ente sulla slide, backup su costi). Durata anche qui ipotizzata, non chiesta |
| 13 | chat | Stesso prompt della 12 | Autorevisione dichiarata con la griglia, più il pacchetto revisore; il mazzo arriva comunque | |
| 14 | agenti | "Fai le slide del talk EGU dal nostro paper" | `generale-presentazione` per il mazzo, con i criteri di contenuto presi da `paper`; dieci minuti, non quaranta slide || **Passa, con riserva.** `generale-presentazione` con la regola EGU presa da `paper-scrittura/references/conferenze.md` (10 minuti domande comprese): 9 slide di contenuto più 2 di backup, ossatura del talk con slide dei limiti, in inglese. Riserva: il prompt dice "dal nostro paper" ma il paper non è allegato; la skill, che ammette una sola domanda (la durata), monta uno scheletro di segnaposto invece di chiedere il paper. Nessun revisore separato: non è chiaro se un talk di conferenza sia un mazzo "pubblico" |
| 15 | agenti | "Traduci in inglese queste slide" + il mazzo prodotto dalla prova 10 | Va a `generale-traduzione`, che traduce dentro il `.pptx` senza rifarne la struttura (ADR 0012) || **Passa.** `generale-traduzione` traduce dentro il `.pptx` della prova 10: stesse 15 slide, stessi layout, stesso numero di forme per slide; tradotte anche note del relatore e costanti nei layout (intestazione, riga dell'occasione); segnaposto conservati e tradotti |

### Regressione sui due ambienti

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 16 | chat | "Comunicato stampa sull'avvio del servizio di previsione" | Testo completo, autovalutazione dichiarata, pacchetto revisore in fondo, Cowork citato al massimo una volta | |
| 17 | agenti | Stesso prompt della 16 | Salva la bozza, lancia `generale-revisore`, presenta il rapporto || **Passa.** Bozza salvata in `revisione/bozza-comunicato.md`, `generale-revisore` lanciato, rapporto presentato (13 problemi: il perché fuori dal primo paragrafo, "anticipo di [n] ore" letto come prestazione garantita, "early warning" in un testo italiano); correzioni senza dati nuovi applicate |

Più le prove di regressione in `../domini/`, per i domini toccati.

## Esito

Da riempire quando le prove vengono eseguite: data, ambienti provati, che cosa
è stato corretto prima di rilasciare.

### Giro agenti, 10 ottobre 2026

Ambiente: Cowork (sessione cloud con strumento `Agent`), plugin installato
uguale alla build di `v0.2.0-rc1`. Eseguite le righe 0a, 0b, 1, 2, 4, 6, 7, 9,
10, 12, 14, 15, 17. Le righe chat (3, 5, 8, 11, 13, 16) non sono state
eseguite. Il plugin non è stato toccato: questo giro misura.

Tutte le righe agenti raggiungono l'esito atteso; cinque con riserve o difetti
(4, 6, 10, 12, 14). Quelli da correggere prima del rilascio:

1. **Template illeggibile per il revisore** (riga 4). `progetti-scrittura`
   passa il percorso del `.docx` del template, ma `progetti-revisore` ha solo
   Read e non lo apre. Serve la conversione in testo prevista dal protocollo,
   scritta nella skill.
2. **Griglia non passata** (riga 6). `progetti-risposta-review` non elenca
   `griglia-revisione.md` tra i riferimenti del revisore; i due agenti si sono
   inventati scale diverse.
3. **Fonte mancante non chiesta** (riga 14). "Dal nostro paper" senza paper
   produce un mazzo di soli segnaposto: la regola "una sola domanda, la durata"
   di `generale-presentazione` non prevede il caso in cui manca il materiale da
   cui nasce il mazzo.
4. **Quando un mazzo è istituzionale** (righe 10 e 14). Review con la
   Commissione e talk di conferenza: la skill non dice se richiedono il
   revisore separato.
5. **Durata sempre chiesta** (righe 10, 12). In un giro in cui nessuno
   risponde il mazzo si blocca alla prima domanda; qui si è proseguito con
   un'ipotesi dichiarata, come la skill fa per gli altri dati mancanti.
6. **Revisione su uno scheletro** (riga 4). Senza materiale tecnico i due
   profili danno tutti 1 e non dicono niente di utile.
7. Minori: "WP3" dedotto dal codice del deliverable (riga 4); paragrafo
   "concetto chiave" con il punto elenco del corpo (riga 10); skill
   `proposte-*` nominate ma non presenti nel pacchetto (riga 0a).

Limite del giro: le prove le ha eseguite la stessa sessione che aveva letto gli
esiti attesi. L'attivazione "da sola" di una skill (0b e le altre) è stata
quindi scelta da chi sapeva che cosa ci si aspettava, e va riconfermata da una
persona che non ha letto questo file. I file prodotti da ogni prova sono in
`esiti-agenti/`.

### Trovato prima di cominciare

**I materiali non erano nel repository.** La riga `materiali/` del
`.gitignore` non aveva la barra iniziale, quindi valeva a ogni livello e si è
presa anche `prove/<versione>/materiali/`. La `v0.2.0-rc1` è stata marcata
senza i file da cui dipendono sei delle sue prove, e il commit che diceva di
averli aggiunti ne aveva aggiunto solo il README. Trovato dalla sessione che
doveva eseguire le prove, non da chi le aveva scritte.

Corretto con `/materiali/`, e `build.py --check` ora avvisa quando un file
sotto `prove/` è ignorato da git: un materiale che git non porta con sé non
arriva a chi deve provare.
