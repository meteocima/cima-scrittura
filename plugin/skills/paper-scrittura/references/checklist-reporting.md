# Checklist di reporting per tipo di studio

Due livelli:

- **Requisiti della rivista**: vengono dal profilo (`rivista-*.md`) e sono
  vincolanti. Esempi verificati: GMD chiede codice archiviato con
  versione esatta e DOI; Copernicus chiede che i dati delle figure siano
  pubblici; Nature Portfolio chiede Data availability e Code
  availability; AGU chiede una sezione Open Research con dataset e
  software citati.
- **Buona pratica** (questo file): voci che un revisore di metodo
  controlla. Non sono requisiti formali: se mancano, segnalarlo come
  rischio in revisione, non come violazione.

Gravità, per leggere le due colonne allo stesso modo delle altre checklist
del plugin: le voci del primo livello sono **bloccanti**, perché la rivista
rifiuta il manoscritto senza; quelle del secondo sono **importanti**, perché
un revisore le nota e ne scrive, ma non fermano la sottomissione.

"Checklist di reporting" è il nome che il mestiere dà a questi elenchi
(CONSORT, PRISMA e simili): si tiene quello, anche se il file non ha una
gravità scritta voce per voce.

Usare la checklist nei Methods e nel controllo finale. Per ogni voce
assente scrivere un segnaposto, non un valore.

## Modelli numerici (idrologici, idraulici, meteorologici)

- [ ] Nome, versione, configurazione, riferimento verificato.
- [ ] Dominio, risoluzione, passo temporale, periodo simulato, spin-up.
- [ ] Forzanti e condizioni al contorno, con fonte e versione.
- [ ] Parametri modificati rispetto ai default e come sono stati scelti.
- [ ] Calibrazione: periodo, funzione obiettivo, algoritmo, numero di
      parametri calibrati.
- [ ] Validazione su un periodo o luogo indipendente dalla calibrazione.
- [ ] Codice e file di configurazione disponibili secondo la rivista.

## Verifica di previsioni (deterministiche ed ensemble)

- [ ] Previsioni e osservazioni di riferimento, con fonte.
- [ ] Riferimento di confronto per gli skill score (climatologia,
      persistenza, altro sistema).
- [ ] Lead time, inizializzazioni, numero di casi per classe.
- [ ] Soglie degli eventi e come sono state scelte.
- [ ] Metriche definite (formula o riferimento), adatte al tipo di
      previsione (es. probabilistiche per ensemble).
- [ ] Incertezza delle metriche (bootstrap o altro) e dimensione del
      campione.

## Proiezioni climatiche

- [ ] Modelli, membri, scenari, periodo di riferimento e periodi futuri.
- [ ] Downscaling e correzione del bias: metodo, periodo di
      calibrazione, verifica.
- [ ] Incertezza rappresentata (spread tra modelli, membri, scenari).
- [ ] Indici climatici definiti (formula, soglie).

## Machine learning

- [ ] Suddivisione training / validation / test, indipendente nel tempo o
      nello spazio quando i dati sono autocorrelati.
- [ ] Architettura, iperparametri e come sono stati scelti.
- [ ] Baseline fisica o statistica per il confronto.
- [ ] Prestazioni sul test set riportate una sola volta, senza scelta a
      posteriori.
- [ ] Codice, pesi del modello e dati di addestramento disponibili o
      motivo dell'indisponibilità.

## Analisi statistiche

- [ ] Test, ipotesi, livello di significatività, dimensione del campione.
- [ ] Correzione per test multipli se pertinente.
- [ ] "Significant" usato solo per risultati di test.
