## Profilo
Reviewer tecnico esterno (profilo B della griglia).

## Sintesi
Il testo non è valutabile come deliverable: è uno scheletro in cui ogni sezione contiene solo istruzioni tra parentesi quadre e segnaposto (per esempio Sezione 4, "[Results of Task T3.x, each with its evidence: figure, table, dataset DOI or link, software release, publication.]"). Non c'è alcun risultato, metodo, dato, KPI, rischio o utente finale da giudicare, quindi tutti i criteri del profilo B sono a 1. La tracciabilità non è verificabile: la matrice DoA dichiara "DoA non fornita: tutti i campi sono `[da DoA]`". Il problema principale non è di qualità della scrittura ma di assenza di contenuto; la struttura invece è impostata in modo coerente con i criteri della griglia.

Nota sui materiali: il template `template-deliverable.docx` è in formato binario e non è stato leggibile con gli strumenti del revisore. Il confronto con il template è quindi fatto sulla struttura che la bozza stessa dichiara, non sul file originale.

## Punteggi
| Criterio | Punteggio | Motivazione in una riga |
|---|---|---|
| B1 Risultati dimostrati | 1 | Sezione 4 contiene solo l'istruzione "[Results of Task T3.x, each with its evidence ...]": nessun risultato, nessuna prova. |
| B2 Qualità tecnica e scientifica | 1 | Sezione 3 contiene solo "[Data, models and methods used, with versions and sources ...]": metodi, dati, validazione, incertezze e limiti assenti. |
| B3 KPI e misure | 1 | Tabella KPI in Sezione 4 con tutte le celle a segnaposto ("[KPI, da DoA]", "[value: da fornire]", "[source]"); la struttura è corretta, il contenuto manca. |
| B4 Avanzamento verso gli obiettivi | 1 | Sezione 2, "It contributes to [project objective or expected result, da DoA]": nessun obiettivo nominato, nessun legame dimostrato. |
| B5 Uso delle risorse (narrativo) | 1 | Sezione 3, "[Partners involved and their documented contribution: partner, task, activity.]": nessun partner né sforzo descritto. |
| B6 Impatto e sfruttamento | 1 | Sezione 2 "Intended readers: [e.g. consortium partners ...]" e Sezione 6 "Next steps: [activity, task code, responsible partner, month]": nessun utente finale, uso o proprietario dello sfruttamento. |
| B7 Rischi | 1 | Nessuna sezione o frase sui rischi e sulla mitigazione; Sezione 5 tratta solo gli scostamenti, ed è comunque a segnaposto. |

## Problemi
| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
|---|---|---|---|---|---|
| 1 | Intero documento | Titolo "Deliverable D3.2 [title as in the DoA]"; ogni sezione tra parentesi quadre | Il documento è un modello non compilato: non contiene alcuna informazione valutabile. | bloccante | Compilare tutte le sezioni con i contenuti reali di D3.2 prima di sottoporlo a revisione; la revisione andrà ripetuta sul testo compilato. |
| 2 | Sezione 4, Results | "[Results of Task T3.x, each with its evidence: figure, table, dataset DOI or link, software release, publication.]" | Nessun risultato e nessuna evidenza: il criterio B1 non è soddisfacibile. | bloccante | Per ogni risultato del task indicare il prodotto e la prova (figura, tabella, DOI, release, pubblicazione), con il codice del task. |
| 3 | Sezione 3, Methodology | "[Data, models and methods used, with versions and sources. For each step, the task code it belongs to.]" | Metodi e dati assenti; nessuna validazione, incertezza o limite dichiarato. | bloccante | Descrivere dati (fonte, periodo, risoluzione), modelli con versione, procedura di validazione e metriche, limiti e incertezze. |
| 4 | Sezione 4, tabella KPI | "[KPI, da DoA]", "[da DoA]", "[value: da fornire]", "[source]" | Nessun indicatore, baseline, target, valore misurato o fonte. Manca anche una colonna o nota sul metodo di misura, richiesto da B3. | importante | Riportare i KPI della DoA pertinenti a D3.2 con baseline, target, valore misurato, fonte e periodo; aggiungere il metodo di misura. |
| 5 | Intero documento | Nessuna sezione sui rischi | La struttura non prevede un punto per rischi aggiornati e mitigazione, quindi anche una volta compilata il criterio B7 resterebbe scoperto salvo che il template del programma lo escluda. | importante | Verificare sul template del programma se è prevista una sezione rischi; in caso contrario inserire almeno un paragrafo in Sezione 5 o 6 con i rischi tecnici di T3.x e le misure di mitigazione. |
| 6 | Sezione 2 e Sezione 6 | "Intended readers: [e.g. consortium partners, the Commission, end users named by role]"; "Next steps: [activity, task code, responsible partner, month]" | Utenti finali, uso dei risultati e responsabilità dello sfruttamento non indicati. | importante | Nominare enti o ruoli degli utenti finali, come useranno i risultati di D3.2, chi è responsabile e in che tempi. |
| 7 | Sezione 1, Executive summary | "[Status against the DoA: delivered as planned, or deviation explained in Section 5.]" | Lo stato rispetto alla DoA non è dichiarato; non è possibile capire se D3.2 è in tempo. | importante | Dichiarare stato e mese effettivo di consegna rispetto al mese previsto dalla DoA; se c'è ritardo, rinviare alla Sezione 5. |
| 8 | Intestazione e Document history | "**Due date (month):** M[da DoA]"; tabella con "[n]", "[dd/mm/yyyy]", "[name, partner]" | Metadati del deliverable (lead, mese, livello di disseminazione, versione, autori) assenti. | minore | Compilare dalla DoA e dalla storia reale del documento. |
| 9 | Intero documento | "[Partners involved ...]", "[value: da fornire]", "[PU / SEN, da DoA]" | Segnaposto misti inglese e italiano in un documento in inglese. | minore | Uniformare la lingua dei segnaposto o, meglio, sostituirli con il contenuto. |
| 10 | Sezione 7 e Annex I | "[Full references cited in the text, each verified ...]"; "[For each dataset and piece of code ...] Mandatory for this programme." | Riferimenti e disponibilità di dati e codice assenti, benché l'Annex sia dichiarato obbligatorio. | importante | Elencare dataset e codice con repository, DOI o link persistente, licenza, condizioni di accesso; riferimenti completi con DOI. |

## Tracciabilità
| Posizione | Affermazione o codice | Problema rispetto alla DoA |
|---|---|---|
| Titolo, intestazione, Sezione 2 | D3.2 | Il codice è presente nella matrice, ma titolo, lead, type, livello di disseminazione e mese previsto sono tutti "[da DoA]": non verificabile. |
| Intestazione, Sezione 2 | WP3 | La matrice riporta per D3.2 "WP: [da DoA]": l'appartenenza di D3.2 al WP3 non è verificabile. |
| Sezione 1, 2, 4 | "Task [T3.x, da DoA]", "Task T3.x" | Codice del task non specificato; la tabella task della matrice è vuota. |
| Sezione 2 | "D3.1, MS[n]" | Deliverable e milestone collegati non presenti nella matrice: non verificabili. |
| Sezione 6 | "D3.3, D4.1" | Citati come esempio di deliverable successivi; non presenti nella matrice, non verificabili. |
| Sezione 4, tabella KPI | "[KPI, da DoA]" | Nessun KPI nella matrice né nel testo. |

Tracciabilità complessiva: non verificabile per assenza della DoA.

## Dichiarato senza prova
| Posizione | Risultato dichiarato | Prova mancante |
|---|---|---|
| Intero documento | Nessun risultato dichiarato | Non ci sono affermazioni da verificare; non sono presenti link, DOI o dataset da controllare. Tutte le prove richieste dalle Sezioni 4, 7 e Annex I sono da fornire. |

## Anti-pattern
Nessun anti-pattern di `anti-pattern-progetti.md` è rilevabile, perché il testo non contiene contenuto narrativo. Da sorvegliare nella compilazione, in base alle istruzioni già presenti: "Successo dichiarato senza prova" nella frase prevista "delivered as planned" (Sezione 1); "KPI senza baseline o senza valore misurato" nella tabella KPI; "Sfruttamento senza proprietario" nei next steps (Sezione 6).

## Punti di forza
Riguardano solo l'impostazione, non il contenuto:
- Sezione 5: l'istruzione chiede per ogni scostamento "what changed ..., concrete cause, effect on other tasks and deliverables, corrective action, new date, whether an amendment is needed", in linea con quanto un reviewer si aspetta.
- Sezione 4: la tabella KPI prevede baseline, target, valore misurato e fonte.
- Sezione 3: richiede per ogni passo il codice del task e il contributo documentato di ciascun partner, base utile per B5.
- Annex I: prevede repository, DOI, licenza e motivo delle restrizioni di accesso per dati e codice.

## Cosa manca
- Tutto il contenuto: risultati, metodi, dati, KPI, scostamenti, conclusioni, riferimenti, disponibilità di dati e codice.
- Metadati del deliverable e storia del documento.
- Una sezione o un paragrafo sui rischi e la mitigazione (B7).
- Il metodo di misura dei KPI (B3).
- La DoA o una matrice DoA compilata, senza la quale la tracciabilità non è verificabile.
- Il confronto puntuale con il template originale, non eseguibile perché il file .docx non era leggibile dal revisore: serve una versione testuale del template.

## Esito simulato
Non richiesto nel prompt.
