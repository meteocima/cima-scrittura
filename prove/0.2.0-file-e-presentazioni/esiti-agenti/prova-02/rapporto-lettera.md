## Sintesi

Il testo non può partire così, e non solo per i segnaposto aperti: il ruolo del firmatario ("Direttore") e la denominazione del ministero sono scritti come fatti e vanno confermati prima dell'invio. Il problema principale è che la lettera non contiene ancora un motivo per cui la Direzione debba accettare l'incontro. Tutto il peso argomentativo sta nei segnaposto dei paragrafi 1 e 2, e l'unica frase di contenuto su CIMA ("lavora nella previsione idrologica e nel monitoraggio ambientale") è generica. Mancano anche un contatto operativo per fissare la data e la coerenza di persona (terza persona e "noi" mescolati).

## Problemi

| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
|---|---|---|---|---|---|
| 1 | Firma, riga 31 | "Direttore" | Il ruolo del firmatario è dato come fatto mentre il nome è un segnaposto. In una lettera al ministero il ruolo deve essere fornito ed esatto (checklist A1; tipologie, sezione 3, punto 7). Non è verificabile da qui chi firmi per Fondazione CIMA e con quale titolo. | bloccante finché non è confermato | Confermare il ruolo esatto del firmatario oppure sostituirlo con `[firmatario e ruolo]`. |
| 2 | Destinatario, riga 4 | "Ministero dell'Ambiente e della Sicurezza Energetica" | La denominazione dell'ente è un fatto da confermare. Un nome sbagliato in una lettera al ministero è bloccante (checklist, premessa). | bloccante finché non è confermata | Verificare la denominazione in vigore alla data di invio e l'esatta denominazione della Direzione Generale. |
| 3 | Paragrafo 2, riga 17 | "Fondazione CIMA lavora nella previsione idrologica e nel monitoraggio ambientale." | Frase che resta vera per qualsiasi centro di ricerca del settore (anti-pattern-ai.md, "Generalità che valgono per qualsiasi ente"). Da sola non dice alla Direzione perché l'incontro la riguarda. | importante | Collegare le attività a una competenza specifica della Direzione destinataria, con fatti forniti (servizio, convenzione, progetto). Se i fatti non ci sono, la frase va tolta piuttosto che lasciata generica. |
| 4 | Paragrafi 1 e 2, righe 13-20 | "e discutere [che cosa si vuole ottenere dall'incontro, es. possibili ambiti di collaborazione]" / "[Uno o due fatti verificabili che collegano queste attività alle competenze della Direzione …]" | Lo scopo per la Direzione e la giustificazione della richiesta sono interamente segnaposto. Riempiti con formule come "possibili ambiti di collaborazione", la lettera diventa una richiesta generica di visibilità, che un ufficio ministeriale tende a non accogliere. | importante | Fornire un obiettivo concreto dell'incontro (decisione, informazione o contributo atteso dalla Direzione) e almeno un fatto che leghi CIMA alle competenze della Direzione. |
| 5 | Paragrafo 1, riga 12 | "per illustrare le attività in corso su [tema]" | L'angolatura è centrata su CIMA (illustrare ciò che fa) e non su ciò che serve al destinatario (destinatari.md, ministeri: "richiesta esplicita"). | importante | Formulare lo scopo dal lato della Direzione: che cosa ottiene dall'incontro. |
| 6 | Paragrafi 3 e 4, righe 22-26 | "Proponiamo un incontro" / "Siamo disponibili ad adattarci" / "Restiamo a disposizione" | Uso di "noi" con un ministero, mentre destinatari.md lo ammette solo nelle comunicazioni interne e con i partner scientifici. Il passaggio dalla terza persona dei paragrafi 1-2 ("Fondazione CIMA chiede") alla prima plurale è incoerente. | importante | Tenere la terza persona istituzionale in tutta la lettera ("CIMA propone…"). |
| 7 | Paragrafi 3 e 4, righe 24-26 | "Siamo disponibili ad adattarci alle esigenze della Direzione." / "Restiamo a disposizione per concordare la data." | Due frasi di disponibilità consecutive che dicono la stessa cosa. Tipologie, sezione 3, punto 6 chiede una chiusura in una frase. "Restiamo a disposizione" è una formula di rito. | minore | Fondere in una sola frase che indichi anche chi contattare, per esempio: "Per concordare la data è possibile contattare [nome, email, telefono]." |
| 8 | Paragrafi 1 e 2, righe 12 e 17 | "Fondazione CIMA chiede" / "Fondazione CIMA lavora" | Forma estesa ripetuta: dopo la prima occorrenza la regola è "CIMA" (destinatari.md, regola generale; checklist D3). | minore | Usare "CIMA" dalla seconda occorrenza. |
| 9 | Destinatario, riga 4 | "Spett.le Ministero" | "Spett.le" è d'uso commerciale. Per un ministero l'indirizzo istituzionale è più adatto. | minore | Usare "Al Ministero dell'Ambiente e della Sicurezza Energetica" o la sola denominazione. |
| 10 | Paragrafo 3, riga 22 | "[in presenza a Roma / online]" | "Roma" presuppone la sede della Direzione. Va confermata, anche se è probabile. | minore | Confermare la sede oppure scrivere "presso la sede della Direzione". |
| 11 | Chiusura, riga 28 | "Distinti saluti," | La virgola dopo la formula di saluto non è d'uso nelle lettere formali italiane. | minore | Togliere la virgola o chiudere con il punto. |

Controllo anti-pattern (sezione B): nessun trattino em, punto medio, emoji o simbolo decorativo. Non ci sono "Con la presente", connettivi riempitivi né elenchi. Gli unici pattern trovati sono quelli segnalati ai punti 3 e 7. Al test finale la lettera suona da modulo, non da testo generato: è effetto dei segnaposto e della frase generica del punto 3.

## Punti di forza

- Paragrafo 1, riga 12: la lettera parte dalla richiesta ("Fondazione CIMA chiede un incontro con la Direzione…"), senza formule introduttive, come richiedono tipologie, sezione 3, punto 5 e destinatari.md, ministeri.
- Righe 1-8: l'ordine luogo e data, protocollo, destinatario, "alla c.a.", oggetto segue la struttura del tipo. I dati non forniti sono segnaposto e non sono stati inventati.
- Riga 8: l'oggetto è di una riga e dichiara la natura della richiesta ("richiesta di incontro su …").
- Paragrafo 3, riga 22: la proposta è operativa (modalità, finestra di date, partecipanti), quindi la Direzione può rispondere con un sì o un no.
- Riga 17: i termini sono quelli preferiti di terminologia.md ("previsione idrologica", "monitoraggio ambientale").

## Cosa manca

Parti richieste o utili e assenti:
- Un contatto operativo per il riscontro (nome, email, telefono). Senza contatto la richiesta di "concordare la data" non ha un destinatario.
- Un riferimento a contatti o atti precedenti (nota, convenzione, incontro, norma), se esistono. Per i ministeri destinatari.md chiede "riferimenti precisi". Se la lettera è un primo contatto va bene così, ma l'autore lo deve sapere.
- Eventuale allegato con i dettagli tecnici delle attività (destinatari.md, ministeri: i dettagli tecnici vanno in allegato e non nel corpo), con il riferimento nel testo.
- Intestazione su carta intestata di Fondazione CIMA, se prevista per l'invio (non è nel testo).

Segnaposto ancora aperti:
- riga 1: `[data]`
- riga 2: `[n. protocollo]`
- riga 5: `[denominazione]` (Direzione Generale)
- riga 6: `[nome, titolo e ruolo]`
- riga 8: `[tema delle attività da illustrare]`
- riga 10: `[Titolo Cognome]`
- righe 13-15: `[tema]`, `[attività o servizio]`, `[che cosa si vuole ottenere dall'incontro, …]`
- righe 18-20: `[Uno o due fatti verificabili …]`
- riga 22: `[in presenza a Roma / online]`
- riga 23: `[finestra di date]`, `[nomi e ruoli per CIMA]`
- riga 30: `[Nome Cognome]`

Fatti da confermare prima dell'invio: ruolo del firmatario ("Direttore"), denominazione del ministero, sede di firma ("Savona"), sede dell'eventuale incontro ("Roma").
