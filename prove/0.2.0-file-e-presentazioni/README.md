# 0.2.0: file veri e presentazioni

Tre cose nuove. Il plugin **legge e scrive i file** nel formato in cui
arrivano, invece di nominarli soltanto (`nucleo/formati-e-file.md`). La
revisione di un `.docx` può tornare **dentro il documento**, con revisioni
tracciate e commenti. Nasce `generale-presentazione`, con il tema CIMA e il suo
revisore.

Le prove sui file usano i materiali in `materiali/`, che sono finti.

## Prove

### File in ingresso e in uscita

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 1 | agenti | "Rivedi questa lettera" + `materiali/lettera-ministero.docx` | Apre il `.docx` senza chiedere di incollarlo; rapporto nel messaggio; nessuna riscrittura, perché il verbo è "rivedi" | |
| 2 | agenti | "Migliora questa lettera" + stesso file | Riscrittura, quindi scrittura: parte `generale-revisore` perché è una lettera istituzionale (ADR 0011); consegna un `.docx`, non Markdown | |
| 3 | chat | Stesso prompt della 2 | Stesso `.docx`, come file scaricabile; una riga dichiara che la revisione non è indipendente; offre il pacchetto revisore; non chiede di cambiare ambiente | |
| 4 | agenti | "Scrivi il D3.2 seguendo questo template" + `materiali/template-deliverable.docx` | Rispetta sezioni e numerazione del template; mette `[…]` dove mancano i dati invece di togliere le sezioni; consegna `.docx` | |
| 5 | chat | Stesso prompt della 4 | Stesso contenuto, file scaricabile, stessa struttura del template | |
| 6 | agenti | "Rispondi a questo review report" + `materiali/review-report.pdf` | Legge il PDF; tabella commento, posizione, risposta, modifica; non copia frasi del report in ricerche web | |

### Revisione dentro il documento

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 7 | agenti | "Controlla il D3.2 come lo leggerebbe il project officer" + `materiali/deliverable-bozza.docx` | Due profili e sintesi; il `.docx` torna con revisioni tracciate e commenti ancorati ai punti citati; sintesi e punteggi nel messaggio | |
| 8 | chat | Stesso prompt della 7 | Stesso `.docx` commentato come file scaricabile; dichiara che i due profili non sono indipendenti | |
| 9 | agenti | Stesso della 7 | Il revisore **non** ha modificato il testo di nascosto: ogni intervento è una revisione tracciata o un commento, visibile e rifiutabile | |

### Presentazioni

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 10 | agenti | "Fai le slide per la review di metà progetto di [progetto]" | Scaletta prima del mazzo; `.pptx` con il tema CIMA; i contenuti ricondotti alla DoA come vuole `progetti`; niente numeri inventati | |
| 11 | chat | Stesso prompt della 10 | Stesso mazzo, file scaricabile | |
| 12 | agenti | "Prepara la presentazione per la giornata con la Regione" | Mazzo istituzionale, quindi parte `generale-revisore-presentazione`; il rapporto arriva all'utente | |
| 13 | chat | Stesso prompt della 12 | Autorevisione dichiarata con la griglia, più il pacchetto revisore; il mazzo arriva comunque | |
| 14 | agenti | "Fai le slide del talk EGU dal nostro paper" | `generale-presentazione` per il mazzo, con i criteri di contenuto presi da `paper`; dieci minuti, non quaranta slide | |
| 15 | agenti | "Traduci in inglese queste slide" + il mazzo prodotto dalla prova 10 | Va a `generale-traduzione`, che traduce dentro il `.pptx` senza rifarne la struttura (ADR 0012) | |

### Regressione sui due ambienti

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 16 | chat | "Comunicato stampa sull'avvio del servizio di previsione" | Testo completo, autovalutazione dichiarata, pacchetto revisore in fondo, Cowork citato al massimo una volta | |
| 17 | agenti | Stesso prompt della 16 | Salva la bozza, lancia `generale-revisore`, presenta il rapporto | |

Più le prove di regressione in `../domini/`, per i domini toccati.

## Esito

Da riempire quando le prove vengono eseguite: data, ambienti provati, che cosa
è stato corretto prima di rilasciare.
