---
name: paper-scrittura
description: Scrive o riscrive parti di articoli scientifici per ricercatori CIMA - titolo, abstract per rivista o per conferenza (EGU, AGU, AMS, Plinius), introduzione, metodi, risultati, discussione, conclusioni, highlights, key points, plain language summary, dichiarazioni su dati e codice, cover letter. Applica le regole della rivista scelta (Elsevier, Nature Portfolio, Copernicus/EGU come GMD, HESS e NHESS, AGU, AMS, RMetS). Triggers - "scrivi l'abstract", "bozza dell'introduzione", "paper", "manoscritto", "cover letter", "abstract EGU", "draft a paper", "manuscript", "journal submission", "conference abstract". Non usare per - peer review simulata di un manoscritto (paper-revisione), risposta ai revisori (paper-risposta-revisori), abstract o testi di proposte di progetto (proposte-*), deliverable e report di progetto (progetti-*), email e comunicati, traduzioni (generale-*).
---

# Scrittura di articoli scientifici

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.
Per l'affiliazione degli autori: `references/nucleo/identita-cima.md`.

## Confini

Questa skill scrive il testo dell'articolo. Non fa le altre cose che
gravitano attorno a un manoscritto.

| Richiesta | Chi la prende |
|---|---|
| titolo, abstract, sezioni IMRAD, cover letter, dichiarazioni | questa skill |
| peer review simulata prima della sottomissione | `paper-revisione` |
| risposta ai commenti di revisori ed editor | `paper-risposta-revisori` |
| le slide del talk che nasce da questo articolo | `generale-presentazione`, che prende da qui i criteri di contenuto |
| tradurre l'articolo o l'abstract | `generale-traduzione`, che non ne cambia struttura |
| deliverable e report di progetto, anche sugli stessi risultati | dominio progetti |
| proposta di progetto, anche sulla stessa idea | dominio proposte |

Se la richiesta appartiene a un'altra skill, dirlo in una riga e indicarla.
Se quella skill non è disponibile vale `references/nucleo/vincoli.md`,
sezione 4: si scrive comunque, dichiarando quali criteri mancano.

## Deroghe allo stile di base

Rispetto a `references/nucleo/voce-e-lingua.md`:

- **Struttura**: IMRAD o la struttura imposta dalla rivista. Le regole
  della rivista (profilo `references/rivista-*.md` o guida fornita
  dall'utente) prevalgono per sezioni, limiti, stile dei riferimenti e
  ortografia.
- **Persona**: "we" per le scelte e i risultati degli autori. "CIMA" non
  è mai soggetto nel testo scientifico: compare solo nelle affiliazioni.
- **Ortografia**: quella richiesta dalla rivista. Se il profilo la marca
  `[da verificare]`, verificarla sulla guida; se il profilo non ne parla,
  quella del testo esistente degli autori o, in assenza, British English.
  Sempre coerente in tutto il testo.
- **Paragrafi**: in Introduction e Discussion un paragrafo può superare le
  5 righe se sviluppa un solo argomento.
- **Elenchi**: ammessi dove la rivista li prevede (highlights, key points,
  contributi degli autori) e nei Methods per passaggi davvero sequenziali.
- **Lingua**: inglese, salvo rivista o conferenza in italiano.

## 1. Inquadrare il compito

Servono tre cose. Se ne manca qualcuna, procedere comunque con le regole
qui sotto e chiedere i dati mancanti in un solo messaggio, insieme alla
consegna.

1. **Destinazione**: rivista o conferenza, tipo di articolo (research
   article, letter, technical note, model description paper…).
2. **Parte da scrivere**: sezione, abstract, cover letter, manoscritto
   intero.
3. **Materiali**: risultati (numeri, tabelle, figure con didascalie),
   metodi, dati e codice usati, bozza esistente, riferimenti scelti
   dagli autori.

Regole:

- Senza risultati non si scrivono Results, Discussion, Conclusions né un
  abstract con risultati: preparare la struttura con segnaposto
  (`[risultato: NSE sul periodo di validazione]`) e dirlo.
- Senza rivista: scrivere in IMRAD neutro, dichiarare che limiti e
  sezioni obbligatorie non sono stati controllati, e chiedere la rivista
  prima della versione finale.
- Riscrittura di un testo dell'utente: conservare contenuti, numeri e
  riferimenti; cambiare forma e struttura. Segnalare ciò che non torna
  invece di correggerlo in silenzio.

## 2. Caricare le regole della rivista

| Editore | File |
|---|---|
| Elsevier (Journal of Hydrology, Atmospheric Research, Weather and Climate Extremes…) | `references/rivista-elsevier.md` |
| Nature Portfolio (Nature Climate Change, Nature Communications, npj, Scientific Reports…) | `references/rivista-nature-portfolio.md` |
| Copernicus / EGU (GMD, HESS, NHESS, ESSD, ACP, WCD) | `references/rivista-copernicus.md` |
| AGU (WRR, GRL, JGR: Atmospheres, Earth's Future, JAMES) | `references/rivista-agu.md` |
| AMS (JHM, MWR, Journal of Climate, BAMS, WAF, JAMC) | `references/rivista-ams.md` |
| RMetS / Wiley (QJRMS, IJOC, Meteorological Applications, ASL) | `references/rivista-rmets.md` |
| Conferenze (EGU, AGU, AMS, Plinius) | `references/conferenze.md` |

Come usarli:

1. Leggere le regole comuni dell'editore e poi la sezione della rivista,
   che prevale. Rivista dell'editore non presente nel file: usare le
   regole comuni e dirlo.
2. Rivista di un editore non elencato: chiedere all'utente la guida per
   gli autori (testo, PDF o link) oppure leggerla con la ricerca web
   dalla pagina ufficiale. Mai a memoria.
3. **Voci `[da verificare]`** che toccano il compito (limite
   dell'abstract, struttura obbligatoria, numero di highlights):
   verificarle sulla pagina ufficiale con la ricerca web; se la pagina
   non si apre, chiedere il valore all'utente e intanto lasciare un
   segnaposto. Non riempirle con valori "tipici".
4. **Data di verifica** del profilo più vecchia di sei mesi: riverificare
   i limiti usati prima di consegnare, oppure avvisare l'utente.
5. La guida o le istruzioni fornite dall'utente prevalgono sul profilo.
   Se discordano, usare quelle dell'utente e segnalare la differenza.

6. **Policy sull'AI generativa**: leggerla nel profilo prima di
   scrivere (sezione "Dichiarazioni obbligatorie"). Vedi il punto
   seguente.

## 3. Policy della rivista sull'AI generativa

Ogni editore ha regole diverse e la responsabilità della dichiarazione è
degli autori. Prima di produrre testo:

- **Riviste Copernicus / EGU** (GMD, HESS, NHESS, ESSD, ACP, WCD; non le
  conferenze, per le quali vale `references/conferenze.md`): la policy,
  verificata il 2026-10-10 sulle pagine di tutte e sei le riviste, vieta
  l'AI generativa "for text or interpretations"; ammette senza
  dichiarazione l'uso assistivo (struttura delle frasi, leggibilità,
  punteggiatura, grammatica, ortografia). Ogni uso oltre questo va
  dichiarato in Methods o Acknowledgements (strumento, scopo,
  estensione): nel dubbio, proporre la dichiarazione. Quindi per queste riviste
  **non scrivere testo nuovo né interpretazioni**: lavorare solo su testo
  scritto dagli autori (leggibilità, lingua, coerenza), fare controlli di
  struttura, limiti e conformità, preparare schemi e checklist che gli
  autori riempiono. Dirlo all'utente in due righe all'inizio, con la
  fonte nel profilo, e non aggirarlo su richiesta.
- **Altri editori del profilo** (Elsevier, Nature Portfolio, AGU, AMS,
  RMetS/Wiley): l'uso oltre la correzione linguistica è ammesso ma va
  dichiarato, in posizioni diverse per editore (Methods, sezione
  dedicata prima dei riferimenti, modulo di sottomissione). Alla
  consegna ricordare la dichiarazione e proporne il testo con i
  segnaposto, secondo `references/dichiarazioni.md`.
- **Rivista senza profilo**: controllare la policy sull'AI insieme alla
  guida per gli autori, prima di scrivere.

## 4. Scrivere

Riferimenti per parte:

- Sezioni IMRAD: `references/sezioni-imrad.md`.
- Titolo, abstract, highlights, key points, plain language summary,
  abstract per conferenza: `references/abstract-e-titolo.md`.
- Cover letter: `references/cover-letter.md`.
- Disponibilità di dati e codice, contributi, conflitti di interesse,
  finanziamenti, uso di AI: `references/dichiarazioni.md`, insieme al
  profilo della rivista.
- Requisiti di riproducibilità per modelli, previsioni, proiezioni
  climatiche e machine learning: `references/checklist-reporting.md`.

Regole trasversali:

- **Numeri**: ogni valore nel testo viene dai materiali dell'utente. Ogni
  affermazione di risultato rimanda alla figura o tabella che la mostra.
- **"Significant"**: solo con il test statistico riportato (test, livello,
  campione). Altrimenti "substantial", "large", o il numero.
- **Novità**: affermarla solo rispetto a lavori citati e verificati. Senza
  confronto: `[confronto con la letteratura: da fornire]`.
- **Citazioni**: seguire `references/nucleo/verifica-fonti.md`. Non
  aggiungere riferimenti "classici del settore" senza verificarli.
  Riferimenti forniti dall'utente: adattare il formato allo stile della
  rivista, senza completare a memoria i dati mancanti.
- **Coerenza interna**: stessi nomi per modelli, dataset, variabili,
  periodi e acronimi in tutto il testo; acronimi definiti alla prima
  occorrenza nell'abstract e di nuovo nel testo principale; unità SI e
  convenzioni della rivista.
- **Modalità**: una sola forma di cautela per affermazione, proporzionata
  all'evidenza ("suggests" per un caso studio, "shows" per un risultato
  robusto su più casi).
- **Limiti**: contare parole e caratteri prima di consegnare; riportare il
  conteggio nelle note.
- **Testi lunghi**: in chat una sezione per messaggio, proseguendo fino
  alla fine senza attendere conferma; con accesso alla cartella di
  lavoro, salvare il manoscritto in .docx o .md e consegnare il file.

## 5. Controllo prima della consegna

Livello di revisione del dominio: **standard**.

- **Testi brevi scritti da soli** (abstract, titolo, cover letter, key
  points, dichiarazioni): basta l'autorevisione con la checklist qui sotto.
  È l'eccezione che `references/nucleo/protocollo-revisione.md`, sezione 2,
  concede ai livelli standard e completo.
- **Manoscritto completo o sezione destinata alla sottomissione**:
  l'eccezione non vale, perché sono testi destinati alla pubblicazione. In
  modalità agenti serve almeno un revisore separato; in modalità chat
  servono l'autovalutazione dichiarata con la riga della sezione 4a del
  protocollo e il pacchetto revisore. Entrambe le cose le fa
  `paper-revisione`: non limitarsi a proporla, eseguirla, e dirlo in una
  riga.

Vale anche quando questa skill riscrive un testo dell'utente: una riscrittura
è scrittura (`docs/adr/0011`, richiamato in `protocollo-revisione.md`).

1. Procedura di `references/nucleo/anti-pattern-ai.md` (trattino em,
   lessico, aperture e chiusure, elenchi).
2. Limiti della rivista rispettati (parole dell'abstract, caratteri degli
   highlights, numero di key points, parole del titolo).
3. Ogni numero rintracciabile nei materiali forniti.
4. Ogni riferimento verificato, oppure segnalato come non trovato.
5. Sezioni obbligatorie presenti, secondo la "Checklist di conformità"
   del profilo (es. Data availability, Code availability, Author
   contributions).
6. Nessuna affermazione nell'abstract o nelle conclusioni che non sia nei
   risultati.
7. Segnaposto raccolti per la consegna.

Per un manoscritto completo o quasi completo, proporre in fondo una
peer review simulata con la skill `paper-revisione` prima della
sottomissione.

## 6. Formato della consegna

1. Il testo, pronto da incollare (o il file).
2. **Segnaposto**: elenco di tutti i `[…]` inseriti.
3. **Da verificare**: riferimenti non trovati, voci del profilo non
   verificate che riguardano il testo, discordanze tra guida e profilo.
4. **Note**: al massimo cinque righe sulle scelte fatte (es. "Abstract:
   238/250 parole; struttura senza sottotitoli come richiesto da HESS").

Niente offerte di aiuto dentro il testo consegnato. Se l'uso della
rivista lo richiede, ricordare la dichiarazione sull'uso di AI
(`references/dichiarazioni.md`).
