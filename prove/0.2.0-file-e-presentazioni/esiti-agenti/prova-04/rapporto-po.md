## Profilo
Project officer (profilo A della griglia)

## Sintesi
Il testo non è una bozza di deliverable ma lo scheletro del template: tutte le sezioni da 1 a 7 e l'Annex I contengono solo segnaposto e istruzioni per l'autore, senza alcuna attività, risultato, prova o stato. Un project officer non potrebbe verificare nulla e lo rimanderebbe indietro per intero. A questo si aggiunge che la matrice DoA è vuota ("DoA non fornita: tutti i campi sono `[da DoA]`"): la tracciabilità non è verificabile, neppure per i due soli codici presenti (D3.2, WP3). Il problema principale è quindi a monte della scrittura: mancano i contenuti tecnici del lavoro di WP3 e i dati della DoA.

Limite della revisione: il template `template-deliverable.docx` è un file binario che non ho potuto aprire con gli strumenti disponibili. La completezza rispetto al template (A2) è valutata sulla struttura della bozza stessa, che appare derivata da quel template; serve una versione leggibile del template per confermare sezioni e limiti di pagina.

## Punteggi
| Criterio | Punteggio | Motivazione in una riga |
|---|---|---|
| A1 Aderenza alla DoA | 1 | Nessun task, milestone o titolo è indicato: "Task \[T3.x, da DoA\]", "MS\[n\], da DoA"; matrice DoA vuota, quindi nessun collegamento verificabile. |
| A2 Completezza rispetto al template | 1 | I titoli delle sezioni ci sono, ma ogni sezione è un segnaposto (es. Sez. 3 "\[Data, models and methods used...\]"); l'executive summary è assente ("\[Limit: one page. To be written last...\]"). |
| A3 Scostamenti | 1 | Sez. 5 contiene solo l'istruzione "\[For each deviation: what changed...\]": non si dice né che ci sono scostamenti né che non ce ne sono. |
| A4 Deliverable e milestone | 1 | Mese di scadenza "M\[da DoA\]", stato "\[Status against the DoA: delivered as planned, or deviation...\]": lo stato di D3.2 non è dichiarato e non c'è means of verification. |
| A5 Follow-up | n.a. | Il testo è un deliverable e non sono stati forniti raccomandazioni di review o lettere precedenti a cui rispondere. |
| A6 Disseminazione, comunicazione, open science | 1 | Annex I, dichiarato "Mandatory for this programme", contiene solo l'istruzione "\[For each dataset and piece of code...\]": nessun dataset, licenza, DOI. |
| A7 Leggibilità per un non specialista | 1 | Non c'è testo da leggere: l'executive summary (Sez. 1) è composto solo da segnaposto. |

## Problemi
| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
|---|---|---|---|---|---|
| 1 | Intero documento, Sez. 1-7 e Annex I | "\[Two or three sentences on what was done in the period, with codes.\]"; "\[Results of Task T3.x, each with its evidence...\]" | Il documento non contiene alcun contenuto: è il template con le istruzioni. Non è valutabile nel merito e non è presentabile. | bloccante | Scrivere le sezioni a partire dal materiale tecnico del task (dati, metodi, risultati, prove) prima di sottoporlo a revisione. |
| 2 | Intestazione e matrice DoA | "**Lead beneficiary:** \[partner, da DoA\]"; "**Due date (month):** M\[da DoA\]"; "**Dissemination level:** \[PU / SEN, da DoA\]" | Titolo, lead, mese di scadenza e livello di diffusione mancano; la matrice DoA non li fornisce. Il PO controlla questi campi per primi contro il GA. | bloccante | Recuperare la DoA (Part A, tabella deliverable) e compilare i campi; aggiornare anche la matrice. |
| 3 | Sez. 1 e Sez. 2 | "under Task \[T3.x, da DoA\] of WP3"; "Task \[T3.x\] (\[task title, da DoA\], M\[x\]-M\[y\])" | Il task di riferimento non è identificato: impossibile collegare D3.2 al piano di lavoro. | bloccante | Indicare codice, titolo e mesi esatti del task (o dei task) dalla DoA. |
| 4 | Sez. 5 | "\[For each deviation: what changed ... If there is none: \"No deviations from the work plan...\"\]" | Nessuna dichiarazione sugli scostamenti. Se D3.2 è consegnato in ritardo o con contenuti diversi, il PO lo scopre da solo. | bloccante | Dichiarare esplicitamente o l'assenza di scostamenti o, per ciascuno, causa concreta, effetto su altri task e deliverable, azione, nuova data, necessità di amendment. |
| 5 | Sez. 4, tabella KPI | "\[KPI, da DoA\] \| \[da DoA\] \| \[da DoA\] \| \[value: da fornire\] \| \[source\]" | Nessun KPI, baseline, target o valore misurato. | importante | Riportare i KPI della DoA pertinenti a D3.2 con baseline, target, valore misurato, fonte e periodo; se nessun KPI riguarda D3.2, dirlo e togliere la tabella. |
| 6 | Annex I | "\[For each dataset and piece of code ... Mandatory for this programme.\]" | Allegato obbligatorio vuoto: per il PO è una non conformità formale. | importante | Elencare ogni dataset e codice con repository, DOI o link persistente, licenza, condizioni di accesso e motivo di eventuali restrizioni, coerentemente con il DMP. |
| 7 | Intestazione | Campi presenti: Work Package, Lead beneficiary, Due date, Dissemination level, Version | Mancano campi che la matrice DoA stessa prevede o che un PO si aspetta in copertina: numero del GA ("Acronimo e numero del GA" nella matrice), tipo di deliverable ("Type" nella matrice), data effettiva di consegna. | importante | Aggiungere numero del GA, tipo (es. R, DATA, DEC, secondo la DoA) e data di consegna effettiva accanto alla scadenza contrattuale. |
| 8 | Sez. 3 | "\[Partners involved and their documented contribution: partner, task, activity.\]" | Nessun partner e nessun contributo documentato: il PO non può vedere chi ha fatto cosa. | importante | Per ogni partner coinvolto: task, attività svolta, prodotto. |
| 9 | Sez. 7 | "\[Full references cited in the text, each verified...\]" | Nessun riferimento; non verificabile nulla con DOI. | minore (dipende dal contenuto) | Compilare con i riferimenti effettivamente citati, ciascuno con DOI. |
| 10 | Document history | "\[n\] \| \[dd/mm/yyyy\] \| \[name, partner\] \| \[e.g. first draft for internal review\]" | Storia del documento vuota; manca traccia della revisione interna di qualità. | minore | Compilare versioni, date, autori e indicare chi ha fatto la revisione interna. |
| 11 | Sez. 1, Sez. 2, Sez. 4, Annex I | "\[Object of D3.2, from the DoA\]"; "\[value: da fornire\]"; "da DoA" | Istruzioni e segnaposto in italiano dentro un documento in inglese, e istruzioni per l'autore ("To be written last", "Mandatory for this programme") nel corpo: se restassero nella versione finale sarebbero visibili al PO. | minore | Prima della consegna rimuovere tutte le istruzioni e verificare che nessun segnaposto `[...]` resti nel testo. |
| 12 | Sez. 1 | "\[Status against the DoA: delivered as planned, or deviation explained in Section 5.\]" | La formula suggerita invita all'anti-pattern "Progress as planned" con ritardi taciuti: "delivered as planned" senza prova non basta al PO. | minore | Accompagnare lo stato con la data effettiva di consegna e la prova (link al deliverable, dataset, release). |

## Tracciabilità
| Posizione | Affermazione o codice | Problema rispetto alla DoA |
|---|---|---|
| Titolo e intestazione | D3.2 | Il codice esiste nella matrice ma con tutti i campi "\[da DoA\]": titolo, WP, lead, tipo, livello di diffusione e mese non verificabili. |
| Intestazione, Sez. 2 | WP3 | La matrice non assegna D3.2 a un WP ("WP: \[da DoA\]"): l'appartenenza a WP3 non è confermabile. |
| Sez. 1, 2, 4 | Task T3.x | Codice non definito nel testo né nella matrice (tabella task vuota). |
| Sez. 2 | D3.1, MS\[n\] | Citati come esempio di collegamento; nessuno dei due è nella matrice. |
| Sez. 6 | D3.3, D4.1 | Citati come esempio di uso successivo dei risultati; non presenti nella matrice. |
| Sez. 4 | KPI | Tabella KPI della matrice vuota; nessun KPI verificabile. |

## Dichiarato senza prova
| Posizione | Risultato dichiarato | Prova mancante |
|---|---|---|
| Intero documento | Nessun risultato dichiarato | Non ci sono risultati da verificare: mancano figure, tabelle, dataset, DOI, release software, pubblicazioni richiesti dalle stesse istruzioni della Sez. 4. Nessun link o DOI da controllare. |

## Anti-pattern
Sul contenuto non sono rilevabili anti-pattern perché il contenuto non c'è. L'unico rischio visibile è nella struttura dell'executive summary: "\[Status against the DoA: delivered as planned...\]" (Sez. 1) predispone il pattern "Progress as planned con ritardi taciuti" se compilato senza data e prova (problema 12). I segnaposto misti italiano e inglese (problema 11) non sono un anti-pattern della lista ma un rischio di forma alla consegna.

## Punti di forza
- La struttura (Sez. 1-7 e Annex I) copre ciò che un PO cerca in un deliverable: scopo e collegamenti alla DoA (Sez. 2), metodi con codice del task (Sez. 3), risultati con prova (Sez. 4), sezione dedicata agli scostamenti (Sez. 5), disponibilità di dati e codice (Annex I).
- La tabella KPI della Sez. 4 prevede già baseline, target, valore misurato e fonte, cioè tutti gli elementi che un PO chiede.
- Le istruzioni della Sez. 5 elencano correttamente causa, effetto, azione, nuova data e necessità di amendment.

Questi sono punti di forza del modello, non del deliverable: non incidono sui punteggi.

## Cosa manca
- Tutto il contenuto del deliverable: oggetto, attività del periodo, metodi, risultati, KPI, conclusioni, passi successivi, riferimenti, dataset e codice.
- La DoA o almeno la sua Part A per D3.2 e per i task di WP3: senza di essa nessun codice, mese o titolo è verificabile.
- Dati di copertina: numero del GA, tipo di deliverable, data di consegna effettiva, titolo ufficiale.
- Dichiarazione esplicita sugli scostamenti (anche se nulli).
- Stato di D3.2 e delle milestone collegate con means of verification.
- Contributo documentato dei partner.
- Da verificare sul template e sul GA, che non ho potuto leggere: eventuali elementi obbligatori di copertina o di visibilità (dichiarazione di finanziamento ed emblema del finanziatore, disclaimer), indice, lista delle abbreviazioni, limiti di pagina oltre a quello dell'executive summary.
- Una versione leggibile (markdown o testo) del template `template-deliverable.docx`, per confermare il giudizio sul criterio A2.

## Esito simulato
Non richiesto nel prompt.
