# Profilo: Elsevier

> File condiviso del dominio paper di `cima-scrittura`. Fonte unica:
> `plugin/condivisi/paper/` nel repository; la build lo copia in
> `references/` di ogni skill `paper-*`. Non modificare la copia dentro
> una skill. Costruito da pagine ufficiali consultate con ricerca web
> (data di verifica qui sotto). Le voci `[da verificare]` non si
> riempiono a memoria: si verificano sulla fonte ufficiale o si chiedono
> all'utente.

Data di verifica: 2026-10-10
Fonti principali:
- https://www.elsevier.com/about/policies-and-standards/the-use-of-generative-ai-and-ai-assisted-technologies-in-writing-for-elsevier
- https://www.elsevier.com/about/policies-and-standards/research-data
- https://www.elsevier.com/about/policies-and-standards/publishing-ethics
- https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement
- https://www.elsevier.com/researcher/author/tools-and-resources/highlights
- https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement
- https://www.elsevier.com/reviewer/what-is-peer-review
- https://www.elsevier.com/subject/next/guide-for-authors (guide "Your Paper Your Way" per la famiglia di riviste Elsevier *Next*: usata solo come esempio del modello Elsevier, NON come guida delle riviste di questo profilo)
- https://media.journals.elsevier.com/content/files/editorialhydrologyregionalstudies-18134837.pdf (editoriale 2020, Journal of Hydrology: Regional Studies)

Nota per Claude: tutte le guide per autori delle singole riviste (www.sciencedirect.com/journal/<rivista>/publish/guide-for-authors e i vecchi indirizzi www.elsevier.com/journals/<rivista>/<issn>/guide-for-authors) non sono state lette perché il recupero automatico è bloccato dal robots.txt del sito. Le regole specifiche di rivista prevalgono sempre su quelle comuni: prima di dare per buono un limite, chiedi all'autore di confrontarlo con la guida della rivista.

## Regole comuni dell'editore

### Tipi di articolo
[da verificare: i tipi di articolo sono definiti nella guida di ciascuna rivista, non accessibile]. Nella guida della famiglia *Next* (fonte: https://www.elsevier.com/subject/next/guide-for-authors) compaiono Original Research Article, Review, Communication, Comment, Protocol, Replication Study, Video Article, Editorial; non vanno trasferiti automaticamente alle riviste di questo profilo.

### Struttura e sezioni obbligatorie
Fonte: https://www.elsevier.com/subject/next/guide-for-authors
- Modello di riferimento indicato da Elsevier: Introduction, Experimental/Methods, Theory/calculation, Results, Discussion, Conclusions, più Abstract, Graphical abstract, Keywords, Acknowledgements, Funding.
- Acknowledgements: sezione separata "at the end of the article before the references".
- Dichiarazione sull'AI: va "at the end of the manuscript, immediately above the references" (fonte: pagina policy AI, vedi sotto).
- CRediT: nella versione pubblicata compare "above the acknowledgment section" (fonte: pagina CRediT).
- Equazioni come testo editabile, non immagini; tabelle editabili, senza linee verticali né ombreggiature.
- Figure: vettoriali EPS o PDF; foto TIFF/JPG min. 300 dpi; line art bitmap min. 1000 dpi; combinazioni min. 500 dpi; font consigliati Arial/Helvetica, Times, Symbol, Courier.
- Ordine esatto delle sezioni finali (Data availability, Appendices) per le riviste del profilo: [da verificare: guida di rivista non accessibile].

### Abstract, highlights, graphical abstract, keywords
- Abstract: "A concise and factual abstract is required", deve reggersi da solo, senza riferimenti bibliografici (o con autore e anno se indispensabili), abbreviazioni non standard definite alla prima occorrenza. Fonte: https://www.elsevier.com/subject/next/guide-for-authors. Limite di parole per rivista: [da verificare].
- Highlights (fonte: https://www.elsevier.com/researcher/author/tools-and-resources/highlights): "three to five" bullet points, ciascuno "85 characters or fewer, including spaces"; file Word separato caricato come "Highlights"; descrivono risultati nuovi e metodi nuovi; evitare "jargon, acronyms, or abbreviations". Secondo la pagina generale non sono oggetto di valutazione editoriale e sono "not required until the final files stage"; la singola rivista può richiederli alla prima sottomissione [da verificare per rivista].
- Graphical abstract: "optional, its use is encouraged"; file separato; min. 531 × 1328 pixel (h × w), leggibile a 5 × 13 cm a 96 dpi; TIFF, EPS, PDF o file MS Office. Fonte: https://www.elsevier.com/subject/next/guide-for-authors.
- Keywords: "a maximum of 6 keywords, using American spelling and avoiding general and plural terms". Fonte: idem. Numero per rivista: [da verificare].

### Limiti (parole, figure, tabelle, riferimenti)
[da verificare: i limiti sono fissati nelle guide di rivista, non accessibili]. La guida *Next* dichiara "no formal length or formatting requirements" e solo intervalli indicativi; non usarli come limiti delle riviste di questo profilo.

### Stile dei riferimenti e citazioni
Fonte: https://www.elsevier.com/subject/next/guide-for-authors
- Modello "Your Paper Your Way": "There are no strict requirements on reference formatting at submission"; stile coerente, con autori, titolo, anno, volume, numero di articolo o pagine; DOI fortemente consigliato; lo stile della rivista è applicato in bozza.
- Dati citati nel testo e in bibliografia; identificatori di database nel testo (formato "Database: xxxx").
- LaTeX: "it is recommended that Authors use the Elsevier article class" (elsarticle.cls) con BibTeX.
- Stile specifico (author-year o numerico) per ciascuna rivista: [da verificare]. Per Journal of Hydrology: Regional Studies l'editoriale 2020 indica citazioni autore-anno (vedi sotto).

### Dichiarazioni obbligatorie
- Disponibilità di dati: Elsevier incoraggia la condivisione dei dati e supporta "data availability statements to enhance transparency" (https://www.elsevier.com/about/policies-and-standards/research-data). Il data statement si compila "directly in the submission flow" nella maggior parte delle riviste e, se i dati non sono accessibili, si deve "provide a reason if data is not available to access" (https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-statement). L'opzione di policy sui dati adottata da ciascuna rivista: [da verificare].
- Codice: la policy sui dati include esplicitamente "software, algorithms, protocols" tra i research data (fonte: research-data). Obblighi specifici per rivista: [da verificare].
- CRediT author statement (https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement): 14 ruoli (Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data Curation, Writing - Original Draft, Writing - Review & Editing, Visualization, Supervision, Project administration, Funding acquisition); da fornire "during the submission process"; formato: nome dell'autore, due punti, ruoli separati da virgole, punto finale; il corresponding author garantisce che le descrizioni siano "accurate and agreed by all authors". Obbligatorio o solo incoraggiato per rivista: [da verificare].
- Conflitti di interesse: gli autori "must disclose any financial and personal relationships with other people or organizations" che possano influenzare il lavoro; dichiarazione per tutti gli autori, anche se non c'è nulla da dichiarare, tramite il declaration tool, caricata nello step Attach Files (fonti: https://www.elsevier.com/subject/next/guide-for-authors; https://www.elsevier.com/about/policies-and-standards/publishing-ethics).
- Finanziamenti: indicare i finanziatori e il loro ruolo (disegno dello studio, dati, scrittura, decisione di sottomettere), oppure dichiararne l'assenza. Formula per assenza di fondi, come riportata dalla pagina consultata: "This research did not receive any specific grant from funding agencies" [da verificare: testo completo della formula sulla guida di rivista].
- Uso di AI generativa (https://www.elsevier.com/about/policies-and-standards/the-use-of-generative-ai-and-ai-assisted-technologies-in-writing-for-elsevier): consentito per sintesi della letteratura, organizzazione del contenuto, miglioramento di lingua e leggibilità, con supervisione umana; da dichiarare alla sottomissione indicando strumento, scopo ed entità del controllo umano; la dichiarazione va sotto il titolo "Declaration of Generative AI and AI-assisted technologies in the writing process", alla fine del manoscritto, subito prima dei riferimenti, e viene pubblicata; non serve per semplici controlli di grammatica, ortografia e punteggiatura; l'uso di AI nella ricerca va descritto nei metodi; vietato creare o alterare immagini con AI generativa salvo che faccia parte del disegno o dei metodi della ricerca; gli strumenti AI non possono essere autori; gli autori devono verificare ogni output, inclusi i riferimenti, che "can be incorrect or fabricated".
- Etica (https://www.elsevier.com/about/policies-and-standards/publishing-ethics): originalità ("entirely original works"); vietata la sottomissione simultanea a più riviste; preprint ammesso; "Elsevier journals do not allow authorship changes after acceptance"; vietato "enhance, obscure, move, remove, or introduce a specific feature within an image"; dati pronti per la revisione editoriale e conservati dopo la pubblicazione. Controllo di originalità con Crossref Similarity Check (fonte: guida *Next*).

### Lingua e ortografia (British/US)
Fonte: https://www.elsevier.com/subject/next/guide-for-authors
- "Please write your text in good English (American or British usage is accepted, but not a mixture of these)."
- Keywords in ortografia americana (vedi sopra).
- Raccomandati linguaggio inclusivo e linee guida SAGER per sesso e genere.

### Cover letter e sottomissione
- Cover letter: [da verificare: contenuti richiesti non indicati nelle pagine generali consultate].
- Revisori suggeriti (fonte: https://www.elsevier.com/subject/next/guide-for-authors): più nomi con email istituzionale; esclusi colleghi attuali, coautori o collaboratori degli ultimi tre anni e membri del comitato editoriale; gruppo diversificato per paese o regione, genere, etnia e fase di carriera. Numero richiesto per rivista: [da verificare].
- File e formato (fonte: idem): per la revisione basta un unico PDF o Word; alla revisione/accettazione servono file editabili (Word o LaTeX); file grafici sopra 10 MB caricati separatamente; materiale supplementare con didascalia; "Track Changes" disattivato nei file finali.
- Numerazione righe e doppia interlinea: [da verificare: non indicate nelle pagine generali]; richieste da Journal of Hydrology: Regional Studies secondo l'editoriale 2020 (vedi sotto).
- Preprint: possono essere condivisi "anywhere at any time" e non contano come pubblicazione precedente (fonte: guida *Next*).

### Revisione tra pari
- Modelli usati in Elsevier (https://www.elsevier.com/reviewer/what-is-peer-review): single anonymized (il più comune), double anonymized, triple anonymized, open review.
- Modello di ciascuna rivista del profilo: [da verificare]. Nel modello Elsevier tipico l'editor fa uno screening e invia ad almeno due revisori indipendenti (fonte: guida *Next*).
- Tempi: [da verificare].

## Riviste

### Journal of Hydrology
- Guida: https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors [da verificare: pagina bloccata da robots.txt, non letta]
- Ambito dichiarato: [da verificare: pagina non accessibile]
- Tipi di articolo e limiti: [da verificare]
- Differenze rispetto alle regole comuni (sezioni, limiti, highlights, dati/codice, stile riferimenti): [da verificare]

### Journal of Hydrology: Regional Studies
- Guida: https://www.sciencedirect.com/journal/journal-of-hydrology-regional-studies/publish/guide-for-authors [da verificare: pagina bloccata da robots.txt, non letta]
- Fonte secondaria ufficiale consultata: editoriale degli editor, 2020 (doi 10.1016/j.ejrh.2020.100717), https://media.journals.elsevier.com/content/files/editorialhydrologyregionalstudies-18134837.pdf. Il documento ha sei anni: le indicazioni vanno confermate sulla guida corrente.
- Ambito (dall'editoriale): ricerca originale che "enhancing the science of hydrology" su problemi specifici di una regione; benvenute review che sintetizzano casi regionali; fuori ambito i lavori non idrologici o senza giustificazione della rappresentatività regionale.
- Abstract strutturato in tre sezioni: Study Region, Study Focus, New Hydrological Insights for the Region.
- Struttura: Introduction, Materials and Methods, Results and Discussion, Conclusions; dichiarazione esplicita di novità alla fine dell'introduzione; Conclusions in almeno tre paragrafi brevi (risultati principali, limiti e ricerca futura, impatti più ampi).
- Formato: righe numerate, doppia interlinea, citazioni autore-anno (non numeriche).
- Dati e codice: dati e metodi completi, inclusi script o codice, resi pubblici o forniti alla sottomissione (Data in Brief citata come opzione).
- Sovrapposizione testuale oltre circa il 20% porta di norma alla restituzione del manoscritto.
- Highlights: l'editoriale rimanda ai requisiti della rivista senza indicarli [da verificare].
- Tipi di articolo e limiti di parole: [da verificare].

### Atmospheric Research
- Guida: https://www.sciencedirect.com/journal/atmospheric-research/publish/guide-for-authors [da verificare: pagina bloccata da robots.txt, non letta]
- Ambito dichiarato: [da verificare]
- Tipi di articolo e limiti: [da verificare]
- Differenze rispetto alle regole comuni: [da verificare]

### Weather and Climate Extremes
- Guida: https://www.sciencedirect.com/journal/weather-and-climate-extremes/publish/guide-for-authors [da verificare: pagina bloccata da robots.txt, non letta]
- Ambito dichiarato: [da verificare]
- Tipi di articolo e limiti: [da verificare]
- Differenze rispetto alle regole comuni (rivista open access: eventuale APC e licenza): [da verificare]

### Advances in Water Resources
- Guida: https://www.sciencedirect.com/journal/advances-in-water-resources/publish/guide-for-authors [da verificare: pagina bloccata da robots.txt, non letta]
- Ambito dichiarato: [da verificare]
- Tipi di articolo e limiti: [da verificare]
- Differenze rispetto alle regole comuni: [da verificare]

### Environmental Modelling & Software
- Guida: https://www.sciencedirect.com/journal/environmental-modelling-and-software/publish/guide-for-authors [da verificare: pagina bloccata da robots.txt, non letta]
- Ambito dichiarato: [da verificare]
- Tipi di articolo e limiti: [da verificare]
- Requisiti particolari (sezione di software/model availability, licenza, repository, dati di input): [da verificare: requisito atteso ma non confermato su fonte ufficiale corrente]

## Checklist di conformità
Solo regole verificate sulle pagine generali Elsevier; le regole di rivista possono essere più restrittive.
- Highlights: 3–5 punti, ciascuno max 85 caratteri spazi inclusi, file Word separato, senza gergo, acronimi o abbreviazioni.
- Keywords: max 6, ortografia americana, niente termini generici o plurali (salvo indicazione diversa della rivista).
- Abstract: autonomo, senza riferimenti bibliografici, abbreviazioni non standard definite.
- Graphical abstract (se presente): file separato, min. 531 × 1328 pixel.
- Lingua: inglese britannico o americano, mai misti.
- Declaration of competing interest presente per tutti gli autori, anche se negativa.
- Funding: finanziatori e loro ruolo, oppure dichiarazione di assenza di finanziamenti specifici.
- CRediT author statement: ruoli tra i 14 standard, formato "Nome: ruolo, ruolo."
- Data statement compilato; se i dati non sono disponibili, motivazione indicata.
- Se usata AI generativa nella scrittura: sezione "Declaration of Generative AI and AI-assisted technologies in the writing process" subito prima dei riferimenti, con strumento, scopo e controllo umano; nessuna immagine creata o alterata con AI fuori dai metodi; AI non tra gli autori.
- Riferimenti: stile coerente, con DOI ove possibile; dati citati in bibliografia.
- Equazioni e tabelle editabili; tabelle senza linee verticali.
- Figure alle risoluzioni minime (300/500/1000 dpi secondo il tipo).
- Acknowledgements in sezione separata prima dei riferimenti.
- Revisori suggeriti: email istituzionali, nessun collaboratore degli ultimi tre anni, nessun membro del comitato editoriale.
- Lista autori definitiva prima dell'accettazione.
- Solo Journal of Hydrology: Regional Studies (editoriale 2020, da confermare): abstract in tre sezioni (Study Region, Study Focus, New Hydrological Insights for the Region), novità dichiarata a fine introduzione, righe numerate, doppia interlinea, citazioni autore-anno, codice e dati disponibili.

## Punti non verificati
1. Tipi di articolo previsti dalle riviste del profilo (regole comuni).
2. Ordine delle sezioni finali (Data availability, Appendices) per le riviste del profilo.
3. Limite di parole dell'abstract per rivista.
4. Obbligo di highlights alla prima sottomissione per rivista.
5. Numero di keywords per rivista.
6. Limiti di parole, figure, tabelle, riferimenti.
7. Stile dei riferimenti specifico (author-year o numerico) per rivista.
8. Opzione di research data policy adottata da ciascuna rivista.
9. Obblighi su codice/software per rivista.
10. CRediT obbligatorio o solo incoraggiato per rivista.
11. Testo completo della formula per assenza di finanziamenti.
12. Contenuti richiesti nella cover letter.
13. Numero di revisori suggeriti richiesto.
14. Numerazione righe e interlinea (regole comuni).
15. Modello di peer review di ciascuna rivista.
16. Tempi di revisione.
17. Journal of Hydrology: guida, ambito, tipi di articolo, differenze.
18. Journal of Hydrology: Regional Studies: guida corrente, highlights, tipi di articolo e limiti (e conferma delle indicazioni dell'editoriale 2020).
19. Atmospheric Research: guida, ambito, tipi di articolo, differenze.
20. Weather and Climate Extremes: guida, ambito, tipi di articolo, differenze, APC e licenza.
21. Advances in Water Resources: guida, ambito, tipi di articolo, differenze.
22. Environmental Modelling & Software: guida, ambito, tipi di articolo, requisiti di software/model availability.
