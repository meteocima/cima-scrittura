# Profilo: Copernicus Publications / EGU

> File condiviso del dominio paper di `cima-scrittura`. Fonte unica:
> `plugin/condivisi/paper/` nel repository; la build lo copia in
> `references/` di ogni skill `paper-*`. Non modificare la copia dentro
> una skill. Costruito da pagine ufficiali consultate con ricerca web
> (data di verifica qui sotto). Le voci `[da verificare]` non si
> riempiono a memoria: si verificano sulla fonte ufficiale o si chiedono
> all'utente.

Data di verifica: 2026-10-10
Fonti principali:
- https://publications.copernicus.org/for_authors/manuscript_preparation.html
- https://publications.copernicus.org/services/data_policy.html
- https://publications.copernicus.org/services/publication_ethics.html
- https://www.geoscientific-model-development.net/submission.html
- https://www.geoscientific-model-development.net/policies/code_and_data_policy.html
- https://www.geoscientific-model-development.net/about/manuscript_types.html
- https://www.geoscientific-model-development.net/policies/ai_policy.html
- https://www.geoscientific-model-development.net/peer_review/interactive_review_process.html
- Pagine "about/manuscript_types", "peer_review/interactive_review_process", "about/aims_and_scope" di HESS, NHESS, ESSD, ACP, WCD (URL nelle sezioni delle riviste)

Nota d'uso: le regole comuni valgono per tutte le riviste salvo dove la sezione della rivista indica una differenza. Le pagine di preparazione del manoscritto delle singole riviste (es. GMD, HESS) riproducono il testo generale Copernicus con piccole aggiunte.

## Regole comuni dell'editore

### Tipi di articolo
Fonte: pagine `about/manuscript_types.html` di ciascuna rivista (vedi sezione Riviste).
- I tipi di articolo sono definiti rivista per rivista; non esiste un elenco unico Copernicus.
- Tipo ricorrente in tutte le riviste esaminate: Corrigenda, con titolo nel formato `Corrigendum to "TITLE" published in JOURNAL, VOLUME, PAGES, YEAR`, solo per articoli finali (non preprint), entro 3 anni dalla pubblicazione, inviati per email all'editor (non tramite il modulo di sottomissione).
- Molti tipi brevi richiedono un prefisso fisso nel titolo (es. "Brief communication:", "Technical note:", "Comment on", "Reply to").

### Struttura e sezioni obbligatorie
Fonte: https://publications.copernicus.org/for_authors/manuscript_preparation.html ; https://www.geoscientific-model-development.net/submission.html
Ordine della "Manuscript composition" (le voci marcate "added by Copernicus" non vanno scritte dagli autori):
1. Title page
2. Abstract
3. Copyright statement (added by Copernicus)
4. Introduction
5. Sections (numerate; "Three levels of sectioning are allowed")
6. Conclusions
7. Appendices (A, B, ...)
8. Code availability
9. Data availability
10. Interactive computing environment
11. Sample availability
12. Video supplement
13. Supplement link (added by Copernicus)
14. Team list (se un team compare tra gli autori)
15. Author contribution
16. Competing interests
17. Statement on inclusion in global research (opzionale, fino a 100 parole; riportato nella pagina GMD, non nella pagina generale Copernicus)
18. Disclaimer
19. Special issue statement (added by Copernicus)
20. Acknowledgements
21. Financial support
22. Review statement (added by Copernicus)
23. References

Regole testuali sulle sezioni finali:
- Code: "a section entitled "Code availability" or, in the case of data and code, "Code and data availability"". Il software va citato con DOI e incluso nella reference list.
- Data: "This must be placed in the section "Data availability" at the end of the manuscript before the acknowledgements." Se i dati non sono pubblici, va spiegato perché.
- Author contribution: "add a section "Author contribution" before the acknowledgements"; "We recommend using the CRediT contributor roles taxonomy."
- Competing interests: "a declaration of all potential conflicts of interest is required by Copernicus Publications". Formula senza conflitti: "The authors declare that they have no conflict of interest." Se alcuni autori sono membri dell'editorial board della rivista, va dichiarato; la frase sull'editor indipendente la aggiunge Copernicus in produzione.
- Statement on inclusion in global research (GMD): opzionale, per ricerche con viaggi in altri paesi, campioni da altri paesi, popolazioni o terre indigene.
- Acknowledgements: includere le infrastrutture di ricerca usate (es. stazioni di campo).
- Financial support: usa i dati di finanziamento inseriti alla registrazione (inviati a FundRef).
- Title page: titolo "concise but informative, avoidance of abbreviations", nomi e cognomi completi, indirizzi istituzionali completi, email del corresponding author; indicare eventuali coautori deceduti.

### Abstract, short summary, keywords
Fonte: https://publications.copernicus.org/for_authors/manuscript_preparation.html ; https://www.geoscientific-model-development.net/submission.html
- Abstract: "the abstract should be intelligible to the general reader without reference to the text"; "An abstract should be short, clear, concise, and written in English with correct spelling and good sentence structure." Niente citazioni salvo necessità urgente; abbreviazioni spiegate.
- Limite di parole dell'abstract: nessun limite generale; limiti solo per alcuni tipi di articolo (vedi Riviste, es. NHESS research article 100–200 parole, brief communication max 100).
- Short summary: "a 500-character (incl. spaces) non-technical text", in inglese, in forma di paragrafo (niente elenchi), senza abbreviazioni.
- Graphical abstract: nel preprint va "unnumbered and placed directly after the text abstract"; nell'articolo finale di solito è la key figure.
- Keywords: non richieste nel manoscritto; alla registrazione si scelgono subject areas e index terms per l'assegnazione dell'editor.

### Limiti (parole, figure, tabelle, riferimenti)
Fonte: https://publications.copernicus.org/for_authors/manuscript_preparation.html
- Nessun limite generale di parole, figure, tabelle o riferimenti per i research article; i limiti sono per tipo di articolo e per rivista (vedi Riviste).
- Limiti tecnici dei file: PDF del manoscritto max 50 MB; ogni figura PDF max 2 MB, altri formati max 5 MB; totale dei file (escluso supplement) max 30 MB; supplement max 50 MB (zip o PDF unico).

### Stile dei riferimenti e citazioni
Fonte: https://www.geoscientific-model-development.net/submission.html ; https://publications.copernicus.org/services/data_policy.html
- Sistema autore-anno. In testo: "Smith (2009)" o "(Smith, 2009)"; citazioni multiple separate da punto e virgola; niente grassetto o corsivo.
- Reference list in ordine alfabetico per primo autore, con elenco completo degli autori (cognome seguito da iniziali), abbreviazione della rivista, volume, intervallo di pagine, DOI, anno.
- Stesso primo autore: prima i lavori a autore singolo, poi a due autori (alfabetico per secondo autore), poi "et al.", ciascun gruppo in ordine cronologico.
- Citare letteratura formale; letteratura grigia solo se manca un'alternativa. Lavori "in review" ammessi in sottomissione, non nella versione finale salvo che siano pubblicati o disponibili come preprint con DOI.
- Dataset e software si citano come contributi autonomi nella reference list (DataCite: creators, title, publisher/repository, identifier, year); per il software seguire i FORCE11 Software Citation Principles.
- File di stile disponibili: BibTeX (copernicus.bst), EndNote, CSL.
- Evitare citazioni gratuite: la citation manipulation è "regarded as scientific malpractice" (publication ethics).

### Dichiarazioni obbligatorie
Fonti: https://publications.copernicus.org/services/data_policy.html ; https://www.geoscientific-model-development.net/policies/ai_policy.html ; https://www.hydrology-and-earth-system-sciences.net/policies/ai_policy.html ; https://publications.copernicus.org/services/publication_ethics.html
Data policy:
- "Authors are required to provide a statement on how their underlying research data can be accessed." Sezione "Data availability".
- Depositare dati e metadati in "FAIR-aligned reliable public data repositories" (registro suggerito: re3data.org), con DOI.
- Dati di terzi: spiegarlo e citarli.
- Dati non pubblici alla pubblicazione: indicare "where and when they will appear" e come ottenerli nel frattempo; dati sotto embargo resi disponibili ai revisori (accesso "limited to reviewers"); se il deposito pubblico è impossibile serve una spiegazione dettagliata.
- I dati necessari a riprodurre le figure devono essere comunque pubblici (database pubblico o supplement).
Uso di AI generativa (testo uguale nelle pagine `/policies/ai_policy.html` di GMD, HESS, NHESS, ESSD, ACP e WCD, tutte verificate il 2026-10-10):
- Uso assistivo leggero (grammatica, ortografia, punteggiatura, leggibilità) non va dichiarato.
- "Generative AI must not be used for text or interpretations."
- Ogni uso generativo va dichiarato "either in the Methods or in the Acknowledgements sections of the manuscript", nominando lo strumento, lo scopo e l'estensione; alla registrazione gli autori certificano la dichiarazione.
- Illustrazioni e schemi generati con AI sono ammessi se lo strumento è citato.
- Gli autori garantiscono l'assenza di dati allucinati o non verificabili.
- Referee: "Referee comments and reports should always be written by persons"; vietato caricare manoscritti su strumenti AI.
Etica:
- Ogni autore deve aver dato un contributo significativo; vanno dichiarate le fonti di finanziamento.
- Solo materiale originale; vietata la pubblicazione ridondante ("salami"); articoli da atti di congresso: contenuto nuovo significativo, proceedings max 60% del manoscritto, con dichiarazione e citazione.
- Controllo antiplagio con iThenticate; i report di similarità sono condivisi con i referee.

### Lingua e ortografia (British/US), editing linguistico, convenzioni Copernicus (unità, abbreviazioni, figure)
Fonte: https://www.geoscientific-model-development.net/submission.html (testo uguale alla guida generale Copernicus)
Lingua:
- Inglese con ortografia e grammatica corrette; editing professionale incoraggiato ma facoltativo.
- Oxford spelling (-z-) diffusa, ma è accettata una variante purché coerente; Oxford comma usato in modo coerente.
- "data" è plurale. Virgolette doppie, singole all'interno. Sentence case per titoli e intestazioni.
- Niente trattino dopo avverbi in "-ly" e con unità abbreviate ("3 m stick").
- Corsivo per specie, nomi di navi, parole straniere non nei dizionari inglesi; *et al.* e *in situ* in tondo.
Unità, numeri, date:
- SI; unità abbreviate con i numeri (es. "10 km h-1"), per esteso senza numeri; esponenti negativi per i denominatori.
- Date: dd month yyyy; CE/BCE invece di AD/BC; indicare UTC o LT quando serve.
- Numeri cardinali sotto dieci in lettere, tranne con unità o in espressioni scientifiche.
- Intervalli con trattino en senza spazi (1–10); coordinate con spazio (30° N).
Matematica:
- Variabili in corsivo; funzioni, formule chimiche e unità in tondo; matrici in grassetto, vettori in grassetto corsivo.
- In testo "Eq. (14)", a inizio frase "Equation (14)".
Abbreviazioni:
- Definite nell'abstract e alla prima occorrenza nel testo; evitate nel titolo; note (NASA, GPS) non vanno definite. "Ma" per punti nel tempo, "Myr" per durate.
Figure e tabelle:
- File f01, f02, ...; PDF, PS, EPS, JPG, PNG o TIF; 300 dpi; larghezza minima 8 cm; vettoriale preferito, un'unica famiglia di font.
- Legenda dentro la figura, non nella didascalia; pannelli etichettati (a), (b).
- Verifica per daltonismo (consigliati Coblis e le scientific colour maps di Crameri).
- Tabelle in Word o nel file LaTeX, mai come PDF o immagini; nessun colore; linee orizzontali solo sopra, sotto e sotto l'intestazione.
- Figure riprodotte: citazione e diritti; figure adattate: "adapted from" in didascalia.
- Mappe: convenzioni di denominazione ONU, evitare confini contesi.

### Cover letter e sottomissione
Fonte: https://publications.copernicus.org/for_authors/manuscript_preparation.html ; https://www.geoscientific-model-development.net/submission.html
- Flusso: registrazione del manoscritto (tipo di articolo, subject areas, finanziamenti, accettazione di termini, APC, licenza) e poi upload dei file.
- Template LaTeX: Copernicus LaTeX Package, versione 7.16 del 3 September 2026, classe *manuscript*; non aggiungere pacchetti né definire nuovi comandi; usare copernicus.bst.
- Template Word (.docx) con equation editor Microsoft. R Markdown via `rticles` (mantenuto dalla comunità).
- PDF a 1 colonna, verticale, font incorporati: "All pages must be numbered consecutively and line numbers must be included."
- URL scritti per esteso, non come testo con collegamento.
- Figure e tabelle vicino alla prima citazione nel testo.
- Revisione: author's response come "one separate *.pdf file" con riferimenti a pagine e righe, più versione marked-up con le modifiche.
- Cover letter: [da verificare: la pagina generale non la menziona; richiesta esplicita solo per i model evaluation paper di GMD, vedi sotto].
- Revisori suggeriti: [da verificare: non menzionati nelle pagine di preparazione e sottomissione consultate].
- ORCID: [da verificare: nessun requisito sul manoscritto nelle pagine consultate].

### Revisione tra pari
Fonte: pagine `peer_review/interactive_review_process.html` di ciascuna rivista
Processo interattivo in due fasi (comune):
1. Assegnazione a un topic editor (in WCD co-editor).
2. Access review: verifica di ambito e qualità scientifica di base; solo "technical corrections" prima della pubblicazione del preprint; le richieste di revisione scientifica sono rinviate alla discussione.
3. Open discussion: preprint citabile con DOI su EGUsphere (ESSD: in ESSDD). Commenti: referee comments (RC, anonimi o firmati), community comments (CC, firmati), editor comments (EC), author comments (AC, solo dal contact author per conto dei coautori). Tutti i commenti hanno un DOI. "Normally, every preprint receives at least two referee comments." Chiusa la discussione non si accettano nuovi RC o CC.
4. Final response: risposta a tutti i commenti nell'ordine "(1) comments from referees/community, (2) author's response, and (3) author's changes in manuscript."
5. Revised manuscript, poi decisione dell'editor (accettazione diretta, rifiuto, o nuova consultazione dei referee).
6. Pubblicazione con link a preprint e discussione; referee report, editor report e risposte degli autori vengono pubblicati.
Tempi per rivista (indicativi, "a guideline"):
| Rivista | Discussione | Risposta finale | Revisione |
|---|---|---|---|
| GMD | 8 settimane | entro 4 settimane | 4–8 settimane dopo la discussione |
| HESS | 6 settimane | entro 4 settimane | non indicato |
| NHESS | 6 settimane | entro 6 settimane | non indicato |
| ESSD | 5 settimane | 2 settimane (estendibili a 4) | non indicato |
| ACP | 6 settimane (ACP Letters: 4) | entro 6 settimane | 4–8 settimane |
| WCD | 6 settimane | entro 4 settimane | 4–8 settimane |

## Riviste

### Geoscientific Model Development (GMD)
URL guida: https://www.geoscientific-model-development.net/submission.html ; policy: https://www.geoscientific-model-development.net/policies/code_and_data_policy.html ; tipi: https://www.geoscientific-model-development.net/about/manuscript_types.html
Ambito: "dedicated to the publication and public discussion of the description, development, and evaluation of numerical models", per l'Earth system science nel suo insieme e per le sue componenti.

Tipi di manoscritto (nessun limite di lunghezza indicato):
| Tipo | Contenuto | Titolo | Requisiti specifici |
|---|---|---|---|
| Model description papers | Descrizione completa di un modello (componenti, moduli, tool) tale da permetterne la re-implementazione | Deve includere nome del modello e numero di versione (o altro identificativo univoco) | Archiviare il codice della "exact model version described in the paper"; testo con URL del sito del modello, requisiti hardware e software, licenza; manuale utente e codice sorgente |
| Development and technical papers | Sviluppi tecnici: schemi numerici, nuove parametrizzazioni, prestazioni su compilatori o architetture, data assimilation | Nome e versione se lo sviluppo riguarda un solo modello | Nuovo codice con le stesse regole delle model description; paragrafo code availability |
| Methods for assessment of models | Nuove metriche, metodi di confronto modello-dati, tecniche di analisi o visualizzazione, software tool | Nome e versione se si descrive un software tool | Codice fornito per la peer review; lavori teorici con implementazione di esempio nel supplement |
| Model experiment description papers | Esperimenti standard (es. intercomparison project), configurazioni, ensemble, dataset di supporto | Nessun requisito | Versione del protocollo sperimentale; condizioni al contorno con numero di versione e disponibili; paragrafo data availability; link al paper GMD sul sito dell'esperimento |
| Model evaluation papers | Valutazione autonoma di un modello, sviluppo o esperimento già descritto altrove | Deve includere nome del modello e numero di versione | Citare il description paper nel manoscritto e nella cover letter; fornire script di pre-processing, run control e post-processing; esclusi i lavori le cui conclusioni principali riguardano la geoscienza e non i modelli |
| Review and perspective papers | Stato delle conoscenze e direzioni future | Nessun requisito | Contattare gli executive editors prima; sezione code e/o data availability obbligatoria |
| Corrigenda | Correzione di errori | Formato standard | Esclusi errori nello sviluppo del modello |

Code and data policy (citazioni testuali):
- Sezione: "Every paper must include a section at the end of the paper before the "Acknowledgements"" ... "entitled "Code and data availability"." Nota: la pagina submission di GMD elenca nell'ordine generale "Code availability" e "Data availability" separate; la policy impone il titolo combinato.
- "This section must include citations for the persistent public archives of the precise versions of all of the code and data"; deve spiegare come accedere ad altre versioni e indicare la licenza del codice.
- "In every case, the citation from the paper must identify the exact version of the code and/or data used." Le versioni aggiornate durante la revisione vanno archiviate di nuovo: manoscritto sottomesso e finale possono riportare DOI diversi.
- Accesso garantito già alla sottomissione del preprint; non sono ammessi embarghi.
- Archivi: supporto istituzionale di lungo periodo, impossibilità di rimozione unilaterale da parte del depositante, identificativo persistente della versione (di solito DOI).
- "Project or institution websites and online revision control sites such as GitHub, GitLab or Bitbucket are made for code development but not suitable for archiving frozen code versions." Possono comparire solo come link aggiuntivo.
- "Many GMD authors find Zenodo a suitable archival location" (anche tramite l'integrazione GitHub).
- Licenza: "The licence should conform to the Open Source Definition" (esempi: GPL, MIT).
- Ambito, secondo il tipo: codice sorgente (obbligatorio per model description, development/technical, methods for assessment); manuali e documentazione (se l'editor lo ritiene applicabile); file di configurazione, condizioni al contorno, dati di input (obbligatori per experiment description e per ogni paper con simulazioni); dataset di forzante e di confronto; script di pre-processing, run control e post-processing per tutti i risultati riportati (se applicabile).
- Template della sezione: "The current version of model name is available from the project website url under the licence name licence." / "The exact version of the model used to produce the results used in this paper is archived on repository under DOI".
- Eccezioni: se parti di codice o dati non possono essere pubbliche per motivi indipendenti dagli autori, dichiarare le restrizioni e dare accesso confidenziale a editor e referee senza compromettere l'anonimato; il resto va comunque archiviato. I manoscritti che non rispettano la policy sono respinti.
- Codice e dati non sono revisionati formalmente, ma in revisione può essere valutata la facilità di download, compilazione ed esecuzione del modello e dei test case.
Titolo:
- Nome del modello e numero di versione obbligatori per model description e model evaluation; per development/technical e methods for assessment quando riferiti a un singolo modello o tool. Abbreviazioni da evitare nel titolo in generale. Formato esatto della versione (es. "v1.0"): [da verificare: le pagine consultate non prescrivono un formato].
Altre differenze: discussione di 8 settimane (vs 6 di HESS, NHESS, ACP, WCD).

### Hydrology and Earth System Sciences (HESS)
URL guida: https://www.hydrology-and-earth-system-sciences.net/submission.html ; tipi: https://www.hydrology-and-earth-system-sciences.net/about/manuscript_types.html
Ambito: "encourages and supports fundamental and applied research that advances the understanding of hydrological systems", incluso "their role in providing water for ecosystems and society" e "the role of the water cycle in the functioning of the Earth system."
Tipi di articolo:
- Research articles: nessun limite indicato.
- Review articles: contattare un editor e un executive editor prima.
- Brief communications: "2–4 journal pages", max 3 figure e/o tabelle, max 20 riferimenti, abstract max 100 parole; titolo che inizia con "Brief communication:".
- HESS Opinions: in genere su invito, titolo "HESS Opinions:".
- Technical notes: "a few pages only"; titolo "Technical note:"; codice e manuali nei supplement.
- LESSONS Reports: 1000–2000 parole nel testo principale, abstract 100 parole che spiega l'aderenza a LESSONS e scioglie l'acronimo; contattare gli executive editors prima.
- Education and communication; Comments ("Comment on", "Reply to"); Corrigenda.
Differenze: discussione 6 settimane; opzione di co-review (supervisor ed executor). Section order, data availability, line numbers come regole comuni.

### Natural Hazards and Earth System Sciences (NHESS)
URL guida: https://www.natural-hazards-and-earth-system-sciences.net/about/manuscript_types.html ; ambito: https://www.natural-hazards-and-earth-system-sciences.net/about/aims_and_scope.html
Ambito: "a not-for-profit interdisciplinary and international journal dedicated to the public discussion and open-access publication" della ricerca sui rischi naturali e le loro conseguenze, per ricercatori, professionisti e decisori.
Fuori ambito: temi ingegneristici senza un contesto di rischio naturale; temi di Solid Earth più adatti ad altre riviste Copernicus; "Localised case studies with no broader implications" (gli autori devono mostrare cosa possono imparare ricercatori di altre regioni).
Tipi di articolo:
| Tipo | Lunghezza | Figure/tabelle | Riferimenti | Abstract | Titolo |
|---|---|---|---|---|---|
| Research articles | circa 6–24 pagine di rivista | adeguate | non indicato | 100–200 parole | nessun prefisso |
| Review articles | nessun limite | adeguate | nessun massimo | 100–200 parole | "Review article:" |
| Brief communications | 2–4 pagine | max 3 | max 20 | max 100 parole | "Brief communication:" |
| Invited perspectives | non indicato | non indicato | non indicato | non indicato | "Invited perspectives:" |
| Book reviews | meno di 1000 parole | non indicato | non indicato | non indicato | "Book review" |
| Corrigenda | standard | | | | formato standard |
Differenze: discussione 6 settimane, risposta finale entro 6 settimane; i coautori possono postare solo community comments.

### Earth System Science Data (ESSD)
URL guida: https://www.earth-system-science-data.net/submission.html ; tipi: https://www.earth-system-science-data.net/about/manuscript_types.html ; repository: https://www.earth-system-science-data.net/policies/repository_criteria.html
Ambito: "an international, interdisciplinary journal for the publication of articles on original research data (sets)."
Tipi di articolo (nessun limite di lunghezza indicato):
- Data description articles: contesto di generazione, usi e limiti dei dati, sezione su incertezza e sua valutazione; validazione con dati di riferimento indipendenti o, in assenza, valutazione di plausibilità; esclusi interpretazione estesa e sviluppo di metodi o modelli.
- Data review articles: valore aggiunto per gli utenti; consultare un editor prima ("strongly recommended").
- ESSD Visions (contattare i chief editors); Brief communications (commenti, risposte, aggiornamenti); Corrigenda.
Requisiti particolari:
- Dati depositati prima della sottomissione in un repository con identificativo persistente (DOI), preferibilmente disciplinare.
- Licenza: CC BY 4.0 o CC0; respinte "CC BY SA, CC BY ND, ODbL"; licenze non commerciali solo in casi eccezionali concordati prima.
- Accesso anonimo per i revisori (niente registrazione, email o dati personali); link di terze parti (es. cloud privato) non accettati; consigliati repository con link temporanei "data-in-review".
- Versione finale: "a functional data set DOI and its in-text citation must be given in the abstract" (con molti DOI, rimando alla sezione Data availability).
- Data availability con DOI e citazioni; oltre 5 DOI: tabella. Link di revisione in questa sezione.
- Metadati e landing page del DOI disponibili in inglese.
Revisione: discussione 5 settimane; l'editor invita "at least 2 (typically 3-5) reviewers"; risposta finale 2 settimane (estendibili a 4); nell'access review si verifica anche l'accesso a dati e software.

### Atmospheric Chemistry and Physics (ACP)
URL guida: https://www.atmospheric-chemistry-and-physics.net/about/manuscript_types.html ; ambito: https://www.atmospheric-chemistry-and-physics.net/about/aims_and_scope.html
Ambito: "publishes studies investigating Earth's atmosphere from the surface to the mesosphere, including the lower thermosphere."
Tipi di articolo:
- Research articles: nessun limite indicato.
- ACP Letters: meno di 2500 parole nel testo principale, abstract 200 parole, discussione di 4 settimane.
- Review articles: contattare prima gli executive editors con una traccia di meno di due pagine.
- Measurement reports: titolo "Measurement report:"; dati aperti con DOI o link di revisione alla sottomissione e DOI alla pubblicazione.
- Opinions ("Opinion:", in genere su invito); Technical notes ("Technical note:"); LESSONS Reports (1000–2000 parole suggerite, abstract 100 parole); Perspectives ("Perspective on "TITLE":", non revisionati); Commentaries ("Comment on", "Reply to"); Overview articles ("Overview:"); Corrigenda (inviati agli executive editors).
Differenze: l'editor resta anonimo fino all'accettazione come preprint; risposta finale entro 6 settimane; opzione di co-review.

### Weather and Climate Dynamics (WCD)
URL guida: https://www.weather-climate-dynamics.net/about/manuscript_types.html ; ambito: https://www.weather-climate-dynamics.net/about/aims_and_scope.html
Ambito: "dedicated to the publication and public discussion of high-quality research on dynamical processes in the atmosphere", con "a seamless perspective on atmospheric flows, on scales from weather to climate."
Tipi di articolo:
- Research articles: implicazioni generali, non di interesse soprattutto locale; nessun limite indicato.
- Review articles: contattare prima gli executive editors.
- Meeting summaries: titolo "Meeting summary:"; max 3 figure e/o tabelle, max 20 riferimenti, abstract max 100 parole, 4–8 pagine preferite (formato preprint) esclusi i riferimenti.
- WCD Ideas: titolo "WCD Ideas:"; stessi limiti dei meeting summaries.
- Peer-reviewed comments ("Comment on", "Reply to"); Corrigenda (al co-editor).
Differenze: editor chiamati co-editor; discussione 6 settimane.

## Checklist di conformità
- [ ] PDF a 1 colonna, pagine numerate e numeri di riga continui, max 50 MB.
- [ ] Titolo conciso, senza abbreviazioni, in sentence case; prefisso corretto per i tipi brevi (Brief communication:, Technical note:, Measurement report:, ecc.).
- [ ] GMD: nome del modello e numero di versione nel titolo per model description, model evaluation, e development/technical o methods for assessment riferiti a un singolo modello o tool.
- [ ] Title page con nomi completi, indirizzi istituzionali completi, email del corresponding author.
- [ ] Abstract autonomo, senza citazioni, abbreviazioni definite; rispetto dei limiti di parole del tipo di articolo (es. NHESS 100–200; brief communication max 100).
- [ ] Short summary non tecnico di max 500 caratteri spazi inclusi, senza elenchi e abbreviazioni.
- [ ] Max tre livelli di sezioni.
- [ ] Sezioni finali presenti e nell'ordine: Appendices, Code availability / Data availability (o Code and data availability), ..., Author contribution, Competing interests, ..., Acknowledgements, Financial support, References.
- [ ] GMD: sezione "Code and data availability" prima degli Acknowledgements, con DOI di archivi persistenti per la versione esatta di codice e dati, licenza conforme alla Open Source Definition, nessun link solo a GitHub/GitLab/Bitbucket, nessun embargo.
- [ ] GMD model evaluation: citazione del description paper nel testo e nella cover letter; script di pre- e post-processing forniti.
- [ ] Dataset e software citati nella reference list con DOI.
- [ ] ESSD: dataset depositato con DOI e licenza CC BY 4.0 o CC0, accesso anonimo per i revisori, DOI e citazione nell'abstract (versione finale).
- [ ] Competing interests con la formula standard o con i conflitti specificati; dichiarazione se autori nell'editorial board.
- [ ] Author contribution, preferibilmente con ruoli CRediT.
- [ ] Uso di AI generativa dichiarato in Methods o Acknowledgements (strumento, scopo, estensione); nessun testo o interpretazione generati con AI.
- [ ] Unità SI con esponenti negativi (m s-1), date dd month yyyy, intervalli con trattino en senza spazi, numeri sotto dieci in lettere.
- [ ] Figure: 300 dpi, larghezza min 8 cm, legenda nella figura, pannelli (a), (b), palette accessibili ai daltonici; tabelle non a colori e non come immagini.
- [ ] URL scritti per esteso.
- [ ] Citazioni autore-anno, reference list alfabetica con tutti gli autori e DOI; nessun lavoro "in review" nella versione finale salvo preprint con DOI.
- [ ] In revisione: author's response in PDF separato (commento, risposta, modifica con pagine e righe) e versione marked-up.

## Punti non verificati
- [da verificare: requisiti su cover letter nelle regole comuni; trovata solo la richiesta per i model evaluation paper di GMD]
- [da verificare: possibilità o obbligo di indicare revisori suggeriti; non menzionati nelle pagine consultate]
- [da verificare: requisito ORCID per gli autori; nessuna indicazione nelle pagine consultate]
- [da verificare: formato prescritto del numero di versione del modello nel titolo GMD; le pagine richiedono "model name and version number" senza esempio di formato]
- [da verificare: la pagina generale Copernicus https://www.copernicus.org/data_policy.html non si è aperta; usata la versione https://publications.copernicus.org/services/data_policy.html]
- [da verificare: incoerenza tra pagina submission GMD (sezioni "Code availability" e "Data availability" separate nell'ordine generale) e code and data policy GMD (sezione unica "Code and data availability"); seguire la policy]
