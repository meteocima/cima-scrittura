## Profilo
Reviewer tecnico esterno (profilo B della griglia)

## Sintesi
La bozza di D3.2 non contiene alcun risultato verificabile: nessun dato, nessuna figura, nessuna tabella, nessuna metrica, nessun link o DOI. Ogni sezione dichiara un esito positivo ("validato con successo", "significativamente migliorate", "accuratezza elevata", "operativo sul bacino pilota") senza indicare come sia stato misurato. Un reviewer tecnico non può giudicare né la solidità né l'utilità del lavoro e chiederebbe di riscrivere il deliverable. La DoA non è stata fornita (la matrice ha tutti i campi `[da DoA]`), quindi la tracciabilità rispetto a task, mesi e KPI non è verificabile.

## Punteggi
| Criterio | Punteggio | Motivazione in una riga |
|---|---|---|
| B1 Risultati dimostrati | 1 | Sez. 4 "L'accuratezza delle previsioni risulta elevata" e sez. 1 "Il sistema e' stato validato con successo": nessun dato, figura, link o prodotto a supporto. |
| B2 Qualità tecnica e scientifica | 1 | Sez. 3 "catena modellistica che integra dati osservati e previsioni meteorologiche" e "tarato su un ampio insieme di eventi storici": modelli, dati, periodo, metodo di taratura e validazione non descritti; nessuna incertezza o limite. |
| B3 KPI e misure | 1 | Sez. 4 "significativamente migliorate rispetto alla configurazione precedente": nessun indicatore, baseline, valore misurato, target o metodo; matrice KPI vuota. |
| B4 Avanzamento verso gli obiettivi | 1 | Sez. 2 "Le attivita' sono proseguite secondo quanto pianificato": nessun obiettivo, task o milestone citato a cui collegare il lavoro. |
| B5 Uso delle risorse (narrativo) | 1 | Il testo non descrive sforzo, partner né attività svolte; la proporzione tra lavoro e prodotto non è valutabile. |
| B6 Impatto e sfruttamento | 1 | Sez. 4 "adeguato alle esigenze operative" e "operativo sul bacino pilota": nessun utente nominato, nessun uso documentato, nessun piano di sfruttamento. |
| B7 Rischi | 1 | Sez. 5 "Non si segnalano scostamenti significativi": nessun rischio aggiornato né misura di mitigazione. |

## Problemi
| # | Posizione | Citazione | Problema | Gravità | Direzione della correzione |
|---|---|---|---|---|---|
| 1 | Sez. 4 Results | "L'accuratezza delle previsioni risulta elevata e il tempo di anticipo e' adeguato alle esigenze operative." | Risultato centrale del deliverable senza alcuna metrica, valore o soglia. "Elevata" e "adeguato" non sono misure. | bloccante | Riportare le metriche di verifica usate (per esempio scores deterministici e/o probabilistici su portate o livelli), con valori, periodo, numero di eventi, sezioni di controllo e lead time in ore, in tabella o figura. |
| 2 | Sez. 4 Results | "Le prestazioni del sistema sono significativamente migliorate rispetto alla configurazione precedente." | Confronto senza baseline definita né test di significatività. "Significativamente" suggerisce un test statistico che non è descritto. | bloccante | Definire la configurazione di riferimento, riportare valori prima/dopo per ogni metrica e, se si usa "significativamente", il test e la soglia; altrimenti togliere il termine. |
| 3 | Sez. 1 Executive summary | "Il sistema e' stato validato con successo." | Validazione dichiarata ma non descritta in nessuna sezione: non si sa su quali dati, con quale procedura, contro quali criteri di successo. | bloccante | Descrivere la procedura di validazione (dati indipendenti dalla taratura, periodo, eventi, criteri di accettazione) e rinviare ai risultati della sez. 4. |
| 4 | Sez. 3 Methodology | "E' stata implementata una catena modellistica che integra dati osservati e previsioni meteorologiche." | Nessun componente della catena è nominato: modello idrologico/idraulico, prodotti NWP, fonti osservative, risoluzione, assimilazione. Non riproducibile. | bloccante | Descrivere ogni anello della catena (modello, versione, input, risoluzione spazio-temporale, frequenza delle corse), con schema a blocchi e riferimenti. |
| 5 | Sez. 3 Methodology | "Il modello e' stato tarato su un ampio insieme di eventi storici." | "Ampio" non quantificato; mancano numero di eventi, periodo, criteri di selezione, funzione obiettivo, separazione tra taratura e validazione. | importante | Indicare numero e periodo degli eventi, criterio di selezione, parametri tarati, funzione obiettivo e split taratura/validazione. |
| 6 | Sez. 4 Results | "Il sistema e' operativo sul bacino pilota." | Bacino non nominato; "operativo" non definito (catena in esercizio continuo? presso chi? da quando?). | importante | Nominare il bacino, l'ente che usa il sistema, la data di avvio dell'esercizio e la prova (log di esercizio, piattaforma, link). |
| 7 | Sez. 2 e sez. 5 | "Le attivita' sono proseguite secondo quanto pianificato." / "Non si segnalano scostamenti significativi." | Avanzamento dichiarato senza riferimento a task, mesi o milestone; "significativi" implica che scostamenti minori esistano ma non sono detti. | importante | Elencare i task di WP3 coperti dal deliverable con stato e mese; dichiarare ogni scostamento, anche minore, con causa, effetto, azione e nuova data. |
| 8 | Sez. 1 Executive summary | "I risultati ottenuti sono molto positivi e dimostrano l'efficacia dell'approccio proposto." | Executive summary senza alcuna informazione: non dice cosa è stato fatto, su quale bacino, con quali numeri. Tono promozionale. | importante | Riscrivere come sintesi fattuale: obiettivo del deliverable, cosa è stato prodotto, 2 o 3 risultati quantitativi, limiti principali. |
| 9 | Sez. 6 Conclusions | "Il lavoro svolto conferma la validita' dell'approccio. Nel prossimo periodo si proseguira' con le attivita' previste." | Conclusione circolare e next steps generici; nessun limite, nessuna attività successiva nominata. | importante | Indicare limiti emersi, attività successive con codice di task, responsabile e mese. |
| 10 | Intero testo | Assenza di incertezze e limiti | Nessuna discussione di incertezza delle previsioni (ensemble, errori di input, casi mancati, falsi allarmi). Per un sistema di previsione è una lacuna sostanziale. | importante | Aggiungere una sezione su incertezze e limiti: casi di insuccesso, dipendenza dalla qualità dei dati, sensibilità al lead time. |
| 11 | Intero testo | Nessun riferimento bibliografico, dataset, software o repository | Il lavoro non è collegato allo stato dell'arte né a prodotti verificabili. | importante | Citare modelli e dati con riferimenti verificati; indicare dove sono disponibili codice, dati e output (repository, DOI, DMP). |
| 12 | Intero testo | "attivita\'", "e\'", "dell\'approccio" | Apostrofi con backslash e accenti resi come apostrofo: artefatti di conversione visibili nel deliverable. | minore | Ripulire la codifica e usare le lettere accentate corrette. |
| 13 | Titoli di sezione | "Executive summary", "Introduction and scope", "Results" con corpo in italiano | Lingua mista tra titoli e testo; la lingua richiesta dal programma non è nota. | minore | Uniformare alla lingua richiesta dal grant agreement (di norma inglese per i deliverable). |
| 14 | Intestazione | "FLOODSENSE - Deliverable D3.2" | Mancano titolo del deliverable, lead, data, versione, livello di diffusione, autori. | minore | Aggiungere la scheda del documento richiesta dal template del programma. |

### Anti-pattern trovati (anti-pattern-progetti.md)
| Anti-pattern | Posizione | Citazione |
|---|---|---|
| Successo dichiarato senza prova | Sez. 1 | "Il sistema e' stato validato con successo." |
| KPI senza baseline o senza valore misurato | Sez. 4 | "significativamente migliorate rispetto alla configurazione precedente" |
| "Progress as planned" senza verifica | Sez. 2, sez. 5 | "proseguite secondo quanto pianificato"; "Non si segnalano scostamenti significativi." |
| Impatto generico / utenti finali senza ruolo | Sez. 4 | "adeguato alle esigenze operative" (quali esigenze, di chi?) |
| Tono promozionale | Sez. 1, sez. 6 | "molto positivi e dimostrano l'efficacia"; "conferma la validita' dell'approccio" |
| Futuro generico per il lavoro successivo | Sez. 6 | "si proseguira' con le attivita' previste" |

## Tracciabilità
DoA non fornita: tutti i campi della matrice sono `[da DoA]`. I controlli sotto segnalano ciò che non si può verificare, non errori accertati.

| Posizione | Affermazione o codice | Problema rispetto alla DoA |
|---|---|---|
| Titolo | "Deliverable D3.2" | Titolo, lead e mese previsto non verificabili (matrice: `[da DoA]`); il testo stesso non li riporta. |
| Sez. 2 | "Il WP3 si occupa della catena modellistica." | Titolo e obiettivi di WP3 non verificabili; nessun task di WP3 citato, quindi nessuna attività è collegabile a un T3.x. |
| Sez. 2 | "secondo quanto pianificato" | Non verificabile senza mese previsto di D3.2 e delle milestone collegate; il testo non dichiara il mese di consegna. |
| Sez. 4 | Prestazioni, accuratezza, lead time | Nessun KPI della DoA richiamato; matrice KPI vuota, quindi impossibile verificare se il deliverable risponde al target. |
| Sez. 4 | "operativo sul bacino pilota" | Non verificabile se il bacino pilota e l'esercizio operativo siano previsti dalla DoA in questo deliverable. |
| Sez. 5 | "Non si segnalano scostamenti significativi." | Non verificabile contro mesi e stato della DoA. |

## Dichiarato senza prova
| Posizione | Risultato dichiarato | Prova mancante |
|---|---|---|
| Sez. 1 | "I risultati ottenuti sono molto positivi" | Quali risultati, con quali valori. |
| Sez. 1 | "Il sistema e' stato validato con successo." | Procedura, dati e criteri di validazione; esito numerico. |
| Sez. 3 | "tarato su un ampio insieme di eventi storici" | Numero, periodo ed elenco degli eventi; parametri e funzione obiettivo. |
| Sez. 4 | "Le prestazioni del sistema sono significativamente migliorate" | Baseline, metriche prima/dopo, test di significatività. |
| Sez. 4 | "L'accuratezza delle previsioni risulta elevata" | Metriche di verifica con valori, tabelle o figure. |
| Sez. 4 | "il tempo di anticipo e' adeguato alle esigenze operative" | Lead time in ore e requisito operativo di riferimento (fonte: utente o DoA). |
| Sez. 4 | "Il sistema e' operativo sul bacino pilota." | Nome del bacino, ente utilizzatore, data di avvio, evidenza di esercizio (link, piattaforma, log). |
| Sez. 6 | "Il lavoro svolto conferma la validita' dell'approccio." | Nessuna evidenza oltre alle affermazioni delle sezioni precedenti. |

Il testo non cita link, DOI o dataset: non c'era nulla da verificare con ricerca web.

## Punti di forza
- La struttura delle sezioni (sez. 1 a 6) copre le parti attese da un deliverable tecnico, inclusa una sezione dedicata agli scostamenti (sez. 5): l'impianto è riutilizzabile.
- Sez. 3 dichiara l'integrazione di dati osservati e previsioni meteorologiche e sez. 4 l'esistenza di un bacino pilota: sono i due elementi su cui costruire la parte di metodo e risultati, una volta documentati.

Nessun altro punto di forza è citabile da un reviewer tecnico: il testo non contiene contenuto tecnico verificabile.

## Cosa manca
- Descrizione della catena modellistica: modelli, versioni, dati di input, risoluzione, schema a blocchi.
- Area di studio: nome e caratteristiche del bacino pilota, sezioni di controllo.
- Dataset di taratura e validazione: eventi, periodo, fonti, split.
- Metriche di verifica con valori, tabelle e figure; confronto con la baseline.
- Lead time quantificato e requisito operativo di riferimento.
- Incertezze, limiti, casi di insuccesso.
- KPI della DoA con baseline, valore misurato, target, metodo.
- Collegamento a task e milestone di WP3 con codici e mesi.
- Utenti finali per ruolo (per esempio centri funzionali, protezione civile), modalità d'uso, piano di sfruttamento con responsabilità e tempi.
- Rischi aggiornati e misure di mitigazione.
- Disponibilità di dati, codice e output (repository, DOI, riferimento al DMP).
- Riferimenti bibliografici.
- Scheda del documento: titolo del deliverable, lead, autori, data, versione, livello di diffusione.
- Partner coinvolti e contributo di ciascuno (necessario per B5).

## Esito simulato
**Rifiuto possibile.**

Regola applicata: B1 è a 1 con problemi bloccanti (problemi 1 a 4), condizione che la griglia associa a "Rifiuto possibile"; inoltre tutti i criteri B sono a 1. Regola del plugin, non previsione della decisione reale dell'agenzia o del reviewer.
