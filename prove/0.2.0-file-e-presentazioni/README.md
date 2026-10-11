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
| 3 | chat | Stesso prompt della 2 | Stesso `.docx`, come file scaricabile; una riga dichiara che la revisione non è indipendente; offre il pacchetto revisore; non chiede di cambiare ambiente || **Non passa** (2026-10-11, claude.ai con Sonnet, `esiti-chat/prova-03/`). Il `.docx` è buono: anti-pattern tolti, nessun fatto nuovo, segnaposto dove la lettera era vaga. Ma la consegna si ferma all'elenco delle modifiche: nessuna riga 4a, nessuna autorevisione della nuova versione, nessun pacchetto revisore; l'autorevisione arriva solo su richiesta. Il trattino em, vietato, compare cinque volte (oggetto e segnaposto) e l'autorevisione l'avrebbe trovato. Causa in `generale-revisione`: la revisione della riscrittura non è un passo numerato del flusso, e la consegna rimanda alle regole di `generale-scrittura`, che una skill non può leggere. Minore: documento nuovo invece del file ricevuto, stile Body Text perso Rifatta lo stesso giorno con Opus (`esiti-chat/prova-03-opus/`, zip allegato e applicato a mano, nessuna skill installata): **passa con riserve**. Lavora dentro il file con lo stile originale, nessun trattino em, riga 4a presente, autorevisione dichiarata. Ma l'autorevisione è una frase e non il rapporto nel formato del protocollo, e il pacchetto revisore è solo offerto, non consegnato come blocco. Aggiunge la qualifica di CIMA presa dal nucleo (D.Lgs. 1/2018) dove la skill dice di non aggiungere fatti: dato vero e dichiarato, ma la regola va chiarita. Il modello attenua il difetto della skill, non lo toglie Rifatta ancora con Sonnet dopo le correzioni (`esiti-chat/prova-03-sonnet-2/`): **passa**. Riscrive dentro il file con gli stili originali, dichiara i dati presi da `identita-cima.md`, apre la revisione con la riga 4a, consegna il rapporto con sintesi e tabella dei problemi e scrive per intero il pacchetto revisore. Nessun trattino em. Minore, sfuggito alla sua autorevisione: "Fondazione CIMA" ripetuto per esteso nella chiusura |
| 4 | agenti | "Scrivi il D3.2 seguendo questo template" + `materiali/template-deliverable.docx` | Rispetta sezioni e numerazione del template; mette `[…]` dove mancano i dati invece di togliere le sezioni; consegna `.docx` || **Passa, con tre difetti.** Sezioni, ordine e numerazione del template intatti, compilato dentro il file, `[…]` ovunque manchino dati, consegna `.docx`, matrice DoA tutta `[da DoA]`, due `progetti-revisore` in parallelo. Difetti: (a) la prima bozza scriveva "WP3" dedotto dal numero D3.2, supposizione colta da entrambi i revisori e poi tolta; (b) il template è stato passato ai revisori come `.docx` e nessuno dei due l'ha potuto aprire (hanno solo Read): `progetti-scrittura` dice di passare "il template" ma non di ricavarne una versione leggibile, come chiede `protocollo-revisione.md` sez. 3 punto 1; (c) senza alcun materiale tecnico la revisione a due profili gira su uno scheletro di segnaposto e dà tutti 1: la skill non dice di rimandarla finché il testo non c'è |
| 5 | chat | Stesso prompt della 4 | Stesso contenuto, file scaricabile, stessa struttura del template || **Passa** (2026-10-11, claude.ai con Opus, `esiti-chat/prova-05/`). Template compilato dentro il file: stili, sezioni, ordine e numerazione intatti, allegato su dati e codice conservato, `[…]` ovunque manchino dati, segnaposto evidenziati. I tre difetti della rc1 non si ripetono: nessun "WP3" dedotto (lo dice da sé), revisione dichiarata non indipendente e rimandata perché il testo è quasi tutto segnaposto, nessun punteggio. Nessun trattino em. Il pacchetto revisore è rimandato al testo vero: la skill lo vuole sempre in fondo, e il protocollo ("Testo troppo incompleto") toglie i punteggi ma non dice nulla del pacchetto; il rinvio è ragionevole, la lacuna è nelle regole. Non verificato con la prova zero quale skill fosse attiva, ma la consegna è quella di `progetti-scrittura` |
| 6 | agenti | "Rispondi a questo review report" + `materiali/review-report.pdf` | Legge il PDF; tabella commento, posizione, risposta, modifica; non copia frasi del report in ricerche web || **Passa, con un difetto.** PDF letto (pdftotext); tabella commento, citazione, posizione, risposta, modifica, responsabile, scadenza per C1-C4 e R1-R2; testo di accompagnamento, tabella di follow-up per RP2, decisioni del consorzio raccolte in fondo; nessuna ricerca web, quindi nessuna frase del report in rete. Due revisori in parallelo; corrette le incoerenze tra lettera e tabella che hanno trovato. Difetto: `progetti-risposta-review` non passa al revisore `griglia-revisione.md`, e i due agenti si sono inventati ciascuno una scala 0-5 diversa |

### Revisione dentro il documento

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 7 | agenti | "Controlla il D3.2 come lo leggerebbe il project officer" + `materiali/deliverable-bozza.docx` | Due profili e sintesi; il `.docx` torna con revisioni tracciate e commenti ancorati ai punti citati; sintesi e punteggi nel messaggio || **Passa.** Due `progetti-revisore` in parallelo (PO e reviewer tecnico), sintesi in `revisione/sintesi.md` con punti comuni, divergenze di gravità ed esito simulato ("rifiuto possibile", dichiarato come regola del plugin). Il `.docx` torna con 13 commenti ancorati alle frasi citate e revisioni tracciate solo per gli accenti (e' → è, attivita' → attività); validazione docx passata. Nota: il programma non è noto, quindi nessun profilo di programma passato ai revisori |
| 8 | chat | Stesso prompt della 7 | Stesso `.docx` commentato come file scaricabile; dichiara che i due profili non sono indipendenti || **Passa** (2026-10-11, claude.ai con Opus, solo `progetti-revisione`, `esiti-chat/prova-08/`). Riga 4a in apertura, due profili e sintesi nel formato del protocollo con `n.v.` dove mancano DoA e programma, esito simulato dichiarato come regola del plugin, profili dichiarati non indipendenti, pacchetto revisore completo, Cowork citato una volta. Il `.docx` torna scaricabile con 13 commenti ancorati alle frasi citate e i segnaposto come modifiche tracciate; il testo originale è intatto, apostrofi compresi, che diventano un rilievo invece di una correzione silenziosa. Nessun trattino em. Minore: il messaggio conta 7 segnaposto, nel file sono 6 |
| 9 | agenti | Stesso della 7 | Il revisore **non** ha modificato il testo di nascosto: ogni intervento è una revisione tracciata o un commento, visibile e rifiutabile || **Passa.** Rifiutando tutte le revisioni tracciate il testo è identico all'originale (confronto pandoc `--track-changes=reject`); nessuna correzione silenziosa; il merito sta solo nei commenti. I revisori hanno visto soltanto una copia `.md` e non il `.docx`: l'impossibilità di toccare il documento viene dal processo, non dai permessi (l'agente ha `Write`) |

### Presentazioni

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 10 | agenti | "Fai le slide per la review di metà progetto di [progetto]" | Scaletta prima del mazzo; `.pptx` con il tema CIMA; i contenuti ricondotti alla DoA come vuole `progetti`; niente numeri inventati || **Passa, con riserve.** Scaletta prima del mazzo (15 slide: titolo, 9 di contenuto, 3 di sezione, 2 di backup), `.pptx` dal `tema-cima.pptx` con costanti nei layout e senza punto medio, ogni slide che chiede codici di task, deliverable e milestone, nessun numero inventato, validazione passata, autorevisione con la griglia. Riserve: (a) la skill impone di chiedere la durata; nessuno rispondeva e si è proseguito con 20 minuti dichiarati (intervento di chi prova); (b) il segnaposto `[progetto]` del prompt è stato sostituito con FLOODSENSE dei materiali; (c) non è chiaro se una review con la Commissione sia "istituzionale": la skill non lo dice, si è scelta l'autorevisione; (d) il paragrafo "concetto chiave" esce con lo stesso punto elenco del corpo |
| 11 | chat | Stesso prompt della 10 | Stesso mazzo, file scaricabile || **Passa** (2026-10-11, claude.ai con Opus, zip in chat, `esiti-chat/prova-11/`). `.pptx` scaricabile dal tema CIMA: 12 slide più 2 di backup, layout del tema, titoli che affermano, note in ogni slide, nessun trattino em né punto medio; concetto chiave senza punto elenco, quindi il difetto (d) della rc1 non torna. Una domanda sola, sulla durata, perché il materiale c'era (rilievo 3). Ogni numero è segnaposto, elencato per slide; dichiarato che senza `progetti` l'aderenza alla DoA non è controllata. Autorevisione con riga 4a e senza punteggi; pacchetto revisore rimandato ai dati veri, come nella riga 5. Da notare: i titoli delle slide 3, 6, 7 e 9 affermano ciò che il D3.2 dichiara senza provarlo; la sessione lo segnala e nelle note dice come riscriverli. Durata data da chi provava (15 minuti), quindi il ripiego senza risposta non è misurato qui |
| 12 | agenti | "Prepara la presentazione per la giornata con la Regione" | Mazzo istituzionale, quindi parte `generale-revisore-presentazione`; il rapporto arriva all'utente || **Passa.** Mazzo istituzionale (12 slide), scaletta e griglia di anteprime salvate, `generale-revisore-presentazione` lanciato con il solo prompt previsto; rapporto all'utente (filo dei titoli 1, perché i titoli sono segnaposto; 7 slide di contenuto per 20 minuti, troppo corte; tre sezioni per sette slide). Applicate le correzioni senza dati nuovi (sezione da una slide tolta, ruoli dell'ente sulla slide, backup su costi). Durata anche qui ipotizzata, non chiesta |
| 13 | chat | Stesso prompt della 12 | Autorevisione dichiarata con la griglia, più il pacchetto revisore; il mazzo arriva comunque || **Passa con riserva** (2026-10-11, claude.ai con Opus, `esiti-chat/prova-13/`). Il mazzo arriva come `.pptx` dal tema CIMA, dichiarato di impianto e da rifare con i documenti, come vuole il ripiego senza materiale: 27 slide, durata di 30 minuti assunta dentro la forbice di `struttura.md` per una giornata istituzionale, note in ogni slide. Dati reali solo con fonte (file di identità, DEWETRA verificato sul sito del DPC). Trattino lungo solo nella numerazione delle sezioni, dove `tema-cima.md` lo ammette. Riserva: autorevisione con riga 4a ma in tre righe, e pacchetto revisore rimandato al mazzo compilato, mentre l'esito atteso lo vuole subito. È la terza volta (righe 5, 11, 13): su un testo quasi tutto segnaposto Opus rimanda sempre il pacchetto, e il protocollo non dice se può |
| 14 | agenti | "Fai le slide del talk EGU dal nostro paper" | `generale-presentazione` per il mazzo, con i criteri di contenuto presi da `paper`; dieci minuti, non quaranta slide || **Passa, con riserva.** `generale-presentazione` con la regola EGU presa da `paper-scrittura/references/conferenze.md` (10 minuti domande comprese): 9 slide di contenuto più 2 di backup, ossatura del talk con slide dei limiti, in inglese. Riserva: il prompt dice "dal nostro paper" ma il paper non è allegato; la skill, che ammette una sola domanda (la durata), monta uno scheletro di segnaposto invece di chiedere il paper. Nessun revisore separato: non è chiaro se un talk di conferenza sia un mazzo "pubblico" |
| 15 | agenti | "Traduci in inglese queste slide" + il mazzo prodotto dalla prova 10 | Va a `generale-traduzione`, che traduce dentro il `.pptx` senza rifarne la struttura (ADR 0012) || **Passa.** `generale-traduzione` traduce dentro il `.pptx` della prova 10: stesse 15 slide, stessi layout, stesso numero di forme per slide; tradotte anche note del relatore e costanti nei layout (intestazione, riga dell'occasione); segnaposto conservati e tradotti |

### Regressione sui due ambienti

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 16 | chat | "Comunicato stampa sull'avvio del servizio di previsione" | Testo completo, autovalutazione dichiarata, pacchetto revisore in fondo, Cowork citato al massimo una volta || Tolta dal giro il 2026-10-11: non produce file, e il testo in chat lo misurano gia' le prove dei domini (issue #7) |
| 17 | agenti | Stesso prompt della 16 | Salva la bozza, lancia `generale-revisore`, presenta il rapporto || **Passa.** Bozza salvata in `revisione/bozza-comunicato.md`, `generale-revisore` lanciato, rapporto presentato (13 problemi: il perché fuori dal primo paragrafo, "anticipo di [n] ore" letto come prestazione garantita, "early warning" in un testo italiano); correzioni senza dati nuovi applicate |

Più le prove di regressione in `../domini/`, per i domini toccati.

Il 2026-10-11, con la 0.2.0 assorbita nella 0.3.0, le righe agenti 4, 6, 10,
12, 14 e 17 **non** vengono rieseguite sulla rc2 (issue #6 chiusa): restano gli
esiti della rc1. Delle righe chat restano da fare solo quelle che producono un
file, 3, 5, 8, 11 e 13 (issue #7).

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

### Correzioni applicate dopo il giro, 10 ottobre 2026

Nove rilievi dai due ambienti, tutti chiusi. Il plugin va riprovato: le righe
4, 6, 10, 12, 14 e 17 misurano ora un plugin diverso da quello della rc1.

| # | Rilievo | Dove è stato corretto |
|---|---|---|
| 1 | template `.docx` illeggibile per il revisore | `progetti-scrittura` lo converte in testo; il protocollo lo dice per ogni materiale |
| 2 | griglia non passata ai revisori | `progetti-risposta-review` la passa; il protocollo dice perché |
| 3 | fonte mancante non chiesta | `generale-presentazione`: la domanda singola va al materiale mancante, non alla durata |
| 4 | quando un mazzo è istituzionale | tabella per occasione: se esce dal gruppo che lo ha scritto, va dal revisore |
| 5 | durata sempre chiesta, giro bloccato | senza risposta si procede con l'ipotesi dichiarata |
| 6 | revisione su uno scheletro di segnaposto | il protocollo vieta i punteggi quando non c'è testo da valutare |
| 7 | "WP3" dedotto da "D3.2" | `progetti-scrittura`: un codice non ne deduce un altro |
| 7 | concetto chiave con il punto elenco | `tema-cima.md`: il primo paragrafo del corpo non porta il punto |
| 7 | skill `proposte-*` nominate e assenti | `vincoli.md` sezione 4: si consegna comunque, dicendo quali criteri mancano |
| 8 | trattino lungo come cella vuota | `anti-pattern-ai.md`: vietato anche lì, si usa "n.a." |
| 9 | revisore arruolato come scrivano | il protocollo: se non si riesce a salvare, si passa alla modalità chat |

### Correzioni dopo le righe in chat, 11 ottobre 2026

Righe 3, 5, 8, 11 e 13 eseguite in claude.ai (issue #7). Tre correzioni.

| Riga | Rilievo | Dove è stato corretto |
|---|---|---|
| 3 | riscrittura senza autorevisione né pacchetto revisore | `generale-revisione`: passi 8 e 9 del flusso, consegna scritta per esteso |
| 3 | qualifica di CIMA aggiunta dove la skill vietava fatti nuovi | `generale-revisione`: i dati di `identita-cima.md` sono ammessi, dichiarati |
| 5, 11, 13 | pacchetto revisore rimandato su testi di soli segnaposto | `protocollo-revisione.md`: niente pacchetto in quel caso (ADR 0022); il rinvio delle tre righe diventa conforme |

La riga 3, rifatta con Sonnet sul pacchetto corretto, passa.

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
