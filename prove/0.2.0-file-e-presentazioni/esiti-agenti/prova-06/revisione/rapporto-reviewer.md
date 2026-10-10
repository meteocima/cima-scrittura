## Profilo
Reviewer tecnico esterno. Criterio guida indicato nel prompt: le risposte tecniche sono sostenute da dati e modifiche reali o solo dichiarate? Non è stata fornita una griglia con scala di punteggio: i punteggi sotto usano una scala 0-5 definita in questo rapporto (0 = assente, 5 = pienamente soddisfatto) sui criteri del formato di risposta (`formato-risposta.md`) e degli anti-pattern di progetto. La DoA non è stata fornita: la matrice contiene solo campi `[da DoA]`, quindi la tracciabilità non è verificabile.

## Sintesi
La struttura è corretta e completa: tutti e sei i commenti (C1-C4, R1, R2) hanno una riga nella tabella, con citazione letterale, posizione, luogo della modifica e una tabella di follow-up per RP2. Nel merito, però, nessuna risposta tecnica è sostenuta da un dato o da una modifica effettivamente fatta: ogni valore di KPI, ogni dataset, la spiegazione dello scostamento MS4/D3.2 e le attività di disseminazione sono segnaposto, e tutte le modifiche sono `[da fare]`. Il testo stesso lo dichiara ("tutte le risposte di merito sono segnaposto", Notes for the user). Il problema principale è che la lettera di accompagnamento afferma posizioni e impegni ("We accept C1, C3 and C4 and will revise D3.2", "We accept R1 and R2 and will address them in the RP2 periodic report") che la tabella lascia aperti o non dimostra; in particolare C2 è dichiarato "Accepted with clarification" senza alcun chiarimento. Così com'è, il documento è uno schema di risposta, non una risposta inviabile.

## Punteggi
| Criterio | Punteggio | Motivazione in una riga |
|---|---|---|
| Copertura dei commenti (ogni commento ha una risposta) | 5 | C1-C4, R1, R2 tutti presenti in tabella e nel follow-up, numerazione del report mantenuta. |
| Pertinenza della risposta al commento | 4 | Le direzioni di risposta centrano le richieste (KPI con baseline/target/valore, annex dati, rischi); C2 non affronta l'affermazione "no significant deviations" come errore. |
| Sostanza: risposte sostenute da dati e modifiche reali | 0 | Nessun valore, nessun dataset, nessuna causa, nessuna sezione rivista: tutto `[...]` o `[da fare]`. |
| Coerenza interna (lettera di accompagnamento vs tabella) | 2 | La lettera dà per decise le sedi di C4 e R2 che la tabella lascia a "decisione del consorzio"; C2 "clarify" senza chiarimento. |
| Tracciabilità DoA (codici, mesi) | 1 | Codici D3.2 e MS4 coerenti con la matrice, ma mese previsto, WP e KPI non verificabili; riferimento a "Part B Section 1" basato su un template non confermato. |
| Tono e forma | 4 | Fattuale, un solo ringraziamento, nessuna enfasi; sezione interna in italiano da rimuovere prima dell'invio. |

## Problemi
| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
|---|---|---|---|---|---|
| 1 | Response table, C2 | "Accepted with clarification" / "[Explanation of the relation between MS4 and D3.2: ...]" | La posizione "accolto con chiarimento" richiede l'informazione e il punto del testo dove ora si trova (`formato-risposta.md`, Passo 2). Qui il chiarimento è interamente segnaposto: il reviewer riceve una posizione senza contenuto. | bloccante | Inserire mese di scadenza DoA di D3.2, causa concreta del ritardo, effetto su altri task/deliverable, azione correttiva, stato di MS4 confermato o corretto. Finché manca, la riga non può essere inviata. |
| 2 | Response table, C2 | "Section 5 will no longer state that there are no significant deviations [if confirmed]." | Risposta condizionale a un commento fondato: un deliverable consegnato a M20 con MS4 dichiarata a M12 è, salvo prova contraria, uno scostamento. Il condizionale "[if confirmed]" rende la risposta evasiva e non riconosce che la Section 5 originale era inesatta. Anti-pattern "Progress as planned con ritardi taciuti". | importante | Decidere la posizione sulla base della DoA: se il ritardo esiste, dirlo in modo esplicito e correggere la Section 5; se non esiste, dimostrarlo con il mese DoA e la definizione di MS4 (posizione "accolto con chiarimento" o "parzialmente accolto"). Valutare la posizione "Accepted" pura. |
| 3 | Covering text, par. 3 | "On C2 we accept the request and clarify the timing of MS4 and D3.2 in a revised Section 5 of D3.2." | La lettera afferma un chiarimento che non esiste né nella tabella né in una Section 5 rivista (contrassegnata `[da fare]`). | bloccante | Allineare la lettera allo stato reale: o fornire il chiarimento, o non dichiararlo fatto. |
| 4 | Covering text, par. 3 | "We accept R1 and R2 and will address them in the RP2 periodic report." | Contraddice la tabella, R2: "[Decisione del consorzio: send now as annex to this response, or in RP2.]". La lettera promette una scelta che il consorzio non ha preso (`formato-risposta.md`, Tono: "Non promettere ciò che l'utente non ha confermato"). | importante | Scrivere la sede di R2 solo dopo la decisione; fino ad allora lasciare il segnaposto anche nella lettera. |
| 5 | Covering text, par. 3 | "We accept C1, C3 and C4 and will revise D3.2 and the dissemination reporting accordingly." | Per C4 la tabella lascia aperto se integrare ora il report RP1 o rinviare a RP2 ("[decisione del consorzio: integrate now or in RP2]"); la lettera presenta come deciso un intervento sul reporting. Inoltre il tempo futuro "will revise" per tutto il pacchetto indica che nessuna modifica è stata fatta, mentre la posizione "Accolto" richiede "cosa è stato cambiato e dove". | importante | Se D3.2 rivisto viene allegato, scrivere al passato con versione e sezioni; se non viene allegato, indicare data di reinvio. Per C4 riflettere la decisione effettiva. |
| 6 | Response table, C1 | "[KPI 1: baseline, target, measured value, source], [KPI n: ...]" | Il commento chiede "quantitative evidence"; la risposta non contiene un solo numero. È il caso tipico di risultato dichiarato senza prova. | bloccante | Inserire per ogni KPI di DoA Annex 1, Table 3.2 baseline, target, valore misurato, fonte e periodo di misura, e riportare la stessa tabella in D3.2 Section 4. |
| 7 | Response table, C1 | "Where a KPI has not been measured yet, we state why and when it will be." | A M20, su un deliverable di risultati, un KPI non ancora misurato è uno scostamento, non una nota. La formula al futuro rischia l'anti-pattern "futuro per lavoro che doveva essere fatto". | importante | Per ogni KPI non misurato indicare se la misura era prevista entro RP1 secondo la DoA; se sì, trattarlo come scostamento anche nella risposta a C2/Section 5. |
| 8 | Response table, C1 | "baseline, target, measured value and source of the measured value" | Manca il periodo di riferimento della misura, richiesto dall'anti-pattern "KPI senza baseline o senza valore misurato" (indicatore, baseline, valore misurato, target, fonte e periodo). | minore | Aggiungere la colonna periodo/data della misura. |
| 9 | Response table, C3 | "[List of datasets and code: to be provided.]" | L'annex dati e codice è richiesto per verificare i risultati; la risposta non indica nemmeno un repository o un DOI. Nessuna verifica di esistenza è possibile. | bloccante | Elencare dataset e codice con DOI o link persistente, licenza, condizioni di accesso; se alcuni non sono pubblicabili, dire perché (es. dati di terzi, restrizioni) e come si accede. |
| 10 | Response table, C3 | "The data and code availability annex required by the programme is missing." (citazione) / "Assunzioni: programma non indicato nel report" | La risposta non dichiara a quale requisito di programma o di GA l'annex risponde, e il programma non è confermato. | minore | Citare la clausola del GA o il requisito del programma una volta confermato. |
| 11 | Response table, C4 | "[Progress against each dissemination KPI in the DoA: ...]" / "[Activities other than conferences carried out in RP1, if any: ...]" | Interamente segnaposto. Inoltre la struttura prevista ("publications, datasets, web, end-user events, with evidence") non chiede pubblico raggiunto (tipo e numero) ed esito: rischio di ripetere l'anti-pattern "Disseminazione come elenco di eventi" che il reviewer ha appena contestato. | importante | Per ogni KPI di disseminazione: baseline, target, valore a fine RP1, fonte. Per ogni attività: pubblico (ruolo e numero), messaggio, esito, prova. Se in RP1 non ci sono state attività oltre le conferenze, dirlo e indicare l'azione correttiva. |
| 12 | Response table, C4 | "Periodic report RP1 [section to be confirmed] or RP2 report" | Il luogo della modifica è alternativo e indeterminato: il reviewer non sa dove verificare. | importante | Fissare una sola sede dopo la decisione del consorzio. |
| 13 | Response table, R1 | "RP2 periodic report, Part B Section 1" | Il riferimento alla sezione presuppone il template Horizon Europe, che le note stesse dichiarano "non confermato". | minore | Verificare il template del programma e correggere il riferimento. |
| 14 | Response table, R1 e R2 | "[WP leaders]", "[Coordinator]", "[RP2 report due date]" | Responsabili ipotizzati dall'autore, non forniti; sono tra parentesi ma sembrano valori compilati. | minore | Usare segnaposto neutri `[partner / person]` finché il consorzio non assegna i responsabili. |
| 15 | Response table, C2 (citazione) | "MS4 was reported as achieved in month 12 while D3.2 is submitted in month 20." | La citazione omette la parte centrale della critica ("The report states there are no significant deviations"), che è proprio ciò su cui la risposta deve prendere posizione. | minore | Includere nella citazione breve il riferimento all'affermazione sugli scostamenti. |
| 16 | Covering text, par. 2 | "we send the consortium's observations within the 30 days requested" | Affermazione non verificabile: data della review e data di invio sono segnaposto. | minore | Indicare date reali o rimuovere l'affermazione. |
| 17 | Notes for the user | "Notes for the user (in italiano)" | Sezione interna nel documento destinato al PO. | minore | Rimuoverla prima dell'invio. |
| 18 | Anti-pattern (voce di valutazione) | Covering text e tabella, uso costante di "we" / "the consortium" | Voce del consorzio coerente, tono non difensivo né ossequioso, un solo ringraziamento: nessun anti-pattern di forma. Gli anti-pattern rilevati sono di sostanza (successo dichiarato senza prova, KPI senza valore, ritardo non riconosciuto in C2). | minore | Nessuna correzione di forma; correggere i punti 1, 2, 6, 9, 11. |

## Tracciabilità
| Posizione | Affermazione o codice | Problema rispetto alla DoA |
|---|---|---|
| C2, Covering text | D3.2 | Codice coerente con la matrice. Titolo, WP e mese previsto `[da DoA]`: non è verificabile se M20 sia un ritardo e di quanti mesi; la risposta stessa lascia "M[da DoA]" e "[n]-month gap". |
| C2, Notes for the user | MS4 "achieved at M12" | Codice coerente con la matrice; mese previsto e mezzo di verifica di MS4 `[da DoA]`. Non è verificabile se MS4 dipenda da D3.2 (che spiegherebbe l'incoerenza segnalata). |
| C1 | "DoA Annex 1, Table 3.2" | Riferimento ripreso dal review report; contenuto della tabella KPI non disponibile nella matrice. Nessun KPI nominato. |
| C4 | "each dissemination KPI in the DoA" | KPI di disseminazione non elencati né nella matrice né nella risposta. |
| R1 | "T[n].[n]" | Nessun task citato; struttura dei task non presente nella matrice. Non verificabile. |
| R1 | "Part B Section 1" | Sezione di template non riconducibile alla DoA e basata su un programma non confermato. |
| R2 | "each risk in the DoA risk table" | Tabella dei rischi non presente nella matrice; nessun rischio nominato. |
| C2, Notes for the user | "Possibile amendment" | Non valutabile senza le regole di scostamento del GA e il mese DoA di D3.2. |

## Dichiarato senza prova
| Posizione | Risultato dichiarato | Prova mancante |
|---|---|---|
| Covering text, par. 3 | "We accept C1, C3 and C4 and will revise D3.2" | Versione rivista di D3.2 non allegata, numero di versione `[n]`, data di reinvio `[date]`. |
| Covering text, par. 3 | "clarify the timing of MS4 and D3.2 in a revised Section 5" | Nessun chiarimento nel testo; Section 5 `[da fare]`. |
| C1 | KPI riportati "with baseline, target, measured value and source" | Nessun valore, nessuna fonte. |
| C2 | Relazione tra MS4 e D3.2 | Mese DoA, causa, effetto, azione correttiva: tutti assenti. |
| C3 | Annex I con repository, DOI, licenze | Nessun dataset, repository o DOI; nulla da verificare (nessun identificativo da controllare con ricerca esterna). |
| C4 | Progressi sui KPI di disseminazione e attività oltre le conferenze | Nessun KPI, nessuna attività, nessuna prova; non è nemmeno detto se esistano ("if any"). |
| R2 | Aggiornamento dei rischi | Nessun rischio aggiornato; sede non decisa. |
| Covering text, par. 2 | Invio "within the 30 days requested" | Date assenti. |

## Punti di forza
- Response table: tutti i commenti del report sono coperti con la numerazione originale (C1-C4, R1, R2) e citazioni letterali brevi; un reviewer ritrova subito ogni punto.
- Response table, colonna "Change and location": per C1, C2, C3 la sede della modifica è specifica (D3.2 v[n], Section 4, Section 5, Annex I), quindi verificabile una volta compilata.
- C1: la struttura richiesta (baseline, target, valore misurato, fonte, per ogni KPI della Table 3.2) risponde esattamente alla richiesta di "quantitative evidence".
- C3: l'annex previsto include repository, DOI o link persistente, licenza e condizioni di accesso, cioè gli elementi che rendono verificabili dati e codice.
- Follow-up table for the RP2 report: anticipa il follow-up richiesto dai template e collega ogni azione a una prova attesa.
- Uso corretto dei segnaposto `[decisione del consorzio: ...]` nella tabella invece di decisioni inventate (il problema è che la lettera non li rispetta, punti 3-5).
- Tono: fattuale, un solo ringraziamento, nessuna formula difensiva o ossequiosa.

## Cosa manca
- Qualsiasi dato quantitativo: valori dei KPI di Table 3.2 e dei KPI di disseminazione (C1, C4).
- La spiegazione dello scostamento MS4/D3.2: mese DoA, causa concreta, effetto, azione correttiva, nuova data, valutazione sulla necessità di amendment (C2), e il riconoscimento esplicito che la Section 5 originale ("no significant deviations") era inesatta, se lo era.
- L'elenco di dataset e codice con identificativi verificabili (C3).
- Le attività di disseminazione di RP1 con pubblico raggiunto ed esito (C4).
- La versione rivista di D3.2 o, in alternativa, una data di reinvio confermata.
- Le decisioni del consorzio che condizionano la lettera (sede di C4 e R2, stato di MS4).
- Responsabili e scadenze reali per ogni riga.
- Conferma del programma e del template, da cui dipendono i riferimenti "Annex 1" e "Part B Section 1".

## Esito simulato
Non richiesto nel prompt.
