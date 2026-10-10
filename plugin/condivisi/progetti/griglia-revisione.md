# Griglia di revisione del dominio progetti

Usata da `progetti-revisione`, dall'autorevisione delle altre skill e
dal revisore separato. Due profili, stessa scala.

## Scala

| Valore | Significato |
|---|---|
| 1 | Insufficiente: il criterio non è trattato o è trattato in modo che il revisore chiederebbe di rifare |
| 2 | Debole: trattato, ma con lacune che il revisore segnalerebbe come richiesta di revisione |
| 3 | Adeguato: accettabile, con osservazioni minori |
| 4 | Buono: nessuna osservazione sostanziale |

Assegnare il punteggio dopo aver elencato problemi e punti di forza.
Ogni punteggio ha una riga di motivazione con il passaggio citato.
Criterio non applicabile al tipo di testo: "n.a." con il motivo.

## Profilo A: project officer

Chi è: funzionario dell'agenzia o del segretariato che segue il
progetto. Legge con il GA e la DoA aperti. Guarda la conformità, la
completezza e se il progetto sta facendo ciò per cui è pagato.

| # | Criterio | Domanda guida |
|---|---|---|
| A1 | Aderenza alla DoA | Ogni attività e risultato si collega a task, deliverable e milestone della DoA, con codici corretti? |
| A2 | Completezza rispetto al template | Ci sono tutte le sezioni richieste dal template del programma? Sono rispettati limiti di caratteri o pagine? |
| A3 | Scostamenti | Ritardi, task non svolti, cambi di approccio sono dichiarati, con causa, effetto, azione e nuova data? Serve un amendment? |
| A4 | Deliverable e milestone | Stato chiaro per ogni deliverable e milestone del periodo, con means of verification? |
| A5 | Follow-up | Le raccomandazioni di review o lettere precedenti hanno una risposta puntuale? |
| A6 | Disseminazione, comunicazione, open science | Attività con pubblico raggiunto; open access, DMP, dati FAIR dove il programma li richiede; obblighi di visibilità? |
| A7 | Leggibilità per un non specialista | Il PO capisce cosa è stato fatto senza conoscere il gergo del gruppo? Executive summary utile? |

## Profilo B: reviewer tecnico esterno

Chi è: esperto indipendente del settore incaricato della review del
progetto. Conosce lo stato dell'arte, non conosce il gruppo. Guarda se
i risultati sono reali, solidi e utili.

| # | Criterio | Domanda guida |
|---|---|---|
| B1 | Risultati dimostrati | I risultati sono provati (dati, figure, link, DOI, prodotti), non solo dichiarati? |
| B2 | Qualità tecnica e scientifica | Metodi, dati e validazione sono descritti a sufficienza e appropriati? Incertezze e limiti dichiarati? |
| B3 | KPI e misure | Indicatori con baseline, valore misurato, target e metodo di misura? |
| B4 | Avanzamento verso gli obiettivi | Il lavoro del periodo porta verso gli obiettivi della DoA, o devia senza motivo? |
| B5 | Uso delle risorse (narrativo) | Lo sforzo descritto è proporzionato a quanto prodotto? Squilibri tra partner? (Solo in base al testo: niente analisi finanziaria.) |
| B6 | Impatto e sfruttamento | Utenti finali, uso dei risultati, piano di sfruttamento con responsabilità e tempi? |
| B7 | Rischi | Rischi aggiornati, con misure di mitigazione realistiche? |

## Esito simulato

Solo per deliverable e report, e solo come stima dichiarata:

- **Accettabile**: nessun criterio a 1, al massimo due a 2.
- **Richiesta di revisione probabile**: un criterio a 1 oppure tre o più
  a 2.
- **Rifiuto possibile**: A1, A3 o B1 a 1 con problemi bloccanti.

La regola è del plugin, non dell'agenzia: dirlo sempre accanto
all'esito. Mai presentarlo come previsione della decisione reale.

## Voci obbligatorie del rapporto

Oltre al formato comune (protocollo di revisione, sezione 5):

- tabella "Tracciabilità": affermazioni su attività o risultati che non
  trovano corrispondenza nella DoA, o codici errati;
- tabella "Dichiarato senza prova": risultati presentati senza
  evidenza;
- anti-pattern di `anti-pattern-progetti.md` trovati, con citazione.
