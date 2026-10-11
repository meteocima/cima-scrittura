# Profilo: Elsevier

> File condiviso del dominio paper di `cima-scrittura`. Fonte unica:
> `plugin/condivisi/paper/` nel repository; la build lo copia in
> `references/` di ogni skill `paper-*`. Non modificare la copia dentro
> una skill. Costruito da pagine ufficiali consultate con ricerca web
> (data di verifica qui sotto). Le voci `[da verificare]` non si
> riempiono a memoria: si verificano sulla fonte ufficiale o si chiedono
> all'utente.

Data di verifica: 2026-10-11
Fonti principali:
- Guide for authors delle sei riviste, lette da browser il 2026-10-11 (www.sciencedirect.com/journal/<rivista>/publish/guide-for-authors; URL nella sezione di ogni rivista)
- Pagine "Open access information" delle sei riviste (www.sciencedirect.com/journal/<rivista>/publish/open-access-options), per APC e licenze
- https://www.elsevier.com/about/policies-and-standards/the-use-of-generative-ai-and-ai-assisted-technologies-in-writing-for-elsevier
- https://www.elsevier.com/about/policies-and-standards/research-data
- https://www.elsevier.com/about/policies-and-standards/publishing-ethics
- https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement
- https://www.elsevier.com/researcher/author/tools-and-resources/highlights
- https://www.elsevier.com/reviewer/what-is-peer-review

Nota per Claude: le sei guide seguono lo stesso modello Elsevier, con lo stesso testo per etica, file, figure, dati, CRediT e AI. Le regole comuni qui sotto vengono da quel testo condiviso; ciò che cambia da rivista a rivista (ambito, tipi, limiti, abstract, highlights, graphical abstract, stile dei riferimenti, requisiti particolari) sta nella sezione della rivista e prevale. Per una rivista Elsevier non elencata qui, le regole comuni sono un punto di partenza da confermare sulla sua guida.

## Regole comuni dell'editore

### Tipi di articolo
- Definiti rivista per rivista (vedi Riviste). Il tipo si sceglie nel sistema di sottomissione.
- Article Transfer Service: l'editor, un managing editor interno o uno strumento automatico possono proporre il trasferimento a un'altra rivista Elsevier; se l'autore accetta, la nuova rivista fa una revisione indipendente.

### Struttura e sezioni obbligatorie
Fonte: guide for authors.
- File modificabili: .doc/.docx o .tex; "A PDF is not an acceptable source file". Word a una colonna (le due colonne solo in LaTeX). Niente barrato o sottolineato salvo necessità scientifica.
- Title page: titolo conciso senza abbreviazioni e formule (salvo quelle consolidate); nomi degli autori nello stesso ordine del sistema di sottomissione; affiliazioni con lettera minuscola in apice e indirizzo postale completo con il paese; corresponding author con email, che viene pubblicata; eventuale present address in nota con numero arabo in apice.
- Sezioni numerate (1, 1.1, 1.1.1); l'abstract non è numerato; nei rimandi interni si usa il numero della sezione.
- Acknowledgements in una sezione separata "directly before the reference list", mai sulla title page o in nota. Nei ringraziamenti va anche chi ha aiutato con lingua, scrittura o correzione.
- Appendici A, B, …, con equazioni Eq. (A.1), tabelle Table A.1, figure Fig. A.1.
- Dichiarazione sull'AI: sezione nuova subito prima dei riferimenti (vedi sotto).
- Tabelle modificabili, non immagini, con didascalia e note sotto il corpo, senza linee verticali né ombreggiature.
- Figure in file separati (Figure_1, Figure_2…), tutte citate nel testo e con didascalia: vettoriali EPS o PDF con font incorporati; foto TIFF, JPG o PNG a 300 dpi minimi; disegni al tratto bitmap a 1000 dpi minimi; grafici e tabelle grandi in XLS/XLSX; immagini annotate in PPT/PPTX. Non unire più immagini in un file, salvo quelle da confrontare. Colori accessibili.
- Mappe: solo l'area studiata, con la nota "map lines delineate study areas and do not necessarily depict accepted national boundaries".
- Materiale supplementare: citato nel testo, con didascalia, inviato insieme al manoscritto, pubblicato così com'è senza impaginazione. Video fino a 150 MB per file e 1 GB in totale, con un fotogramma fisso e una descrizione nel testo.
- Numerazione delle righe e doppia interlinea: le guide non le chiedono.

### Abstract, highlights, graphical abstract, keywords
Fonte: guide for authors; https://www.elsevier.com/researcher/author/tools-and-resources/highlights.
- Abstract: "concise and factual", con scopo, metodi, risultati principali e conclusioni; autonomo; senza riferimenti (se indispensabili, autore e anno); abbreviazioni non standard definite alla prima occorrenza. Limite di parole per rivista: 250 nella maggior parte, 225 in J. Hydrol. Regional Studies, 150 in Environmental Modelling & Software.
- Keywords: da 1 a 7, in inglese, evitando parole chiave composte con "and" o "of"; abbreviazioni solo se consolidate.
- Highlights: da 3 a 5 punti, ciascuno di "a maximum of 85 characters, including spaces", in un file modificabile separato con "highlights" nel nome; descrivono risultati e metodi nuovi. **Obbligatori** alla sottomissione in J. Hydrol. Regional Studies, Atmospheric Research, Advances in Water Resources ed Environmental Modelling & Software; **incoraggiati** in Journal of Hydrology e Weather and Climate Extremes.
- Graphical abstract: file separato, 531 × 1328 pixel (h × w) o proporzionalmente di più, leggibile a 5 × 13 cm; TIFF, EPS, PDF o file MS Office. **Obbligatorio** in J. Hydrol. Regional Studies ed Environmental Modelling & Software; incoraggiato nelle altre.

### Limiti (parole, figure, tabelle, riferimenti)
- Le guide non fissano limiti per l'articolo di ricerca ordinario, salvo Weather and Climate Extremes ("usually up to 7,500 words"). Limiti ci sono per i tipi brevi (short communication, focussed review, perspective, lettere): vedi Riviste.

### Stile dei riferimenti e citazioni
Fonte: guide for authors.
- Tutte e sei usano lo stile **autore-anno**: (Allan, 2020a, 2020b; Allan and Jones, 2019), Kramer et al. (2023); lista in ordine alfabetico, poi cronologico, con a, b, c per stesso autore e anno.
- Journal of Hydrology, Weather and Climate Extremes e Advances in Water Resources: "no strict requirements on reference formatting at submission", purché lo stile sia coerente e completo; lo stile della rivista viene applicato in bozza. J. Hydrol. Regional Studies, Atmospheric Research ed Environmental Modelling & Software danno lo stile senza quella dispensa: conviene applicarlo già alla sottomissione.
- Formato in lista (esempio delle guide): Van der Geer, J., Handgraaf, T., Lupton, R.A., 2020. The art of writing a scientific article. J. Sci. Commun. 163, 51–59. https://doi.org/…; dataset con "[dataset]", software con "[software]" e versione; pagine web con URL e data di accesso.
- "Every reference included must correspond to a real, existing source." DOI dove disponibile. Riferimenti citati nell'abstract dati per esteso. "In press" solo se accettato. Comunicazioni personali e risultati non pubblicati: meglio solo nel testo; se in lista, nello stile della rivista con "unpublished results" o "personal communication" al posto della data.
- Dati citati in bibliografia; identificatori di database nel testo nel formato "Database: 12345".
- LaTeX: template Elsevier incoraggiato (elsarticle) con BibTeX.

### Dichiarazioni obbligatorie
- Dati (fonte: guide for authors, sezione Research data): nelle sei riviste si applica l'**Option C** delle linee guida Elsevier: depositare i dati in un repository pertinente, citarli e collegarli nell'articolo; se non è possibile, una dichiarazione che spiega perché. Per Elsevier i research data comprendono "software, code, models, algorithms, protocols, methods". Il data statement si compila nella sottomissione ed è pubblicato con l'articolo: obbligatorio in tutte, salvo Weather and Climate Extremes dove la guida lo dice "encouraged". Co-submission facoltativa di un articolo di dati o metodi su Data in Brief o MethodsX.
- Codice e software: rientrano nei research data dell'Option C. Environmental Modelling & Software chiede in più una sezione "Software and/or data availability" (vedi sotto).
- CRediT (fonte: guide for authors): "Corresponding authors are required to acknowledge co-author contributions using CRediT", in tutte e sei. 14 ruoli: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft, Writing – review and editing. Formato dell'esempio Elsevier: nome dell'autore, due punti, ruoli separati da virgole.
- Conflitti di interesse: tutti gli autori dichiarano relazioni finanziarie e personali (impiego, consulenze, azioni, compensi, perizie, brevetti, finanziamenti, ruoli nella rivista). Il declarations tool va sempre compilato; senza conflitti si sceglie "I have nothing to declare"; il documento Word risultante (.doc/.docx, senza firme) si carica nello step "attach/upload files". Chi ha un ruolo nella rivista usa la formula prevista dalla guida sotto "Other Activities".
- Finanziamenti: dichiarare i finanziatori e il loro ruolo (disegno dello studio, raccolta, analisi e interpretazione dei dati, scrittura, decisione di sottomettere), oppure dichiararne l'assenza di ruolo. Formato standard: "Funding: This work was supported by the National Institutes of Health [grant numbers xxxx, yyyy]; …". Senza finanziamento: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."
- Uso di AI generativa (fonti: guide for authors; pagina policy AI): consentito come supporto con supervisione umana, mai al posto del giudizio dell'autore; dichiarato alla prima sottomissione in una sezione nuova prima dei riferimenti, che viene pubblicata. Titolo nelle guide correnti: "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process." (la pagina generale della policy usa ancora "… in the writing process"; vale il titolo della guida della rivista). Testo: "During the preparation of this work the author(s) used [NAME OF TOOL / SERVICE] in order to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article." Non serve per strumenti di base di grammatica, ortografia e riferimenti, né per tecnologie assistive per disabilità; senza nulla da dichiarare, nessuna sezione. Gli autori verificano ogni output, compresi i riferimenti, che possono essere "incorrect or fabricated". L'AI non può essere autore. Immagini: AI ammessa per schemi esplicativi e per visualizzazioni di dati ottenute con metodi riproducibili; vietata per creare o alterare immagini di dati osservati o sperimentali; se usata per un'immagine, dichiararlo nella didascalia e nella sezione AI.
- Autorialità: contributo sostanziale, stesura o revisione critica, approvazione finale; un solo corresponding author. Cambi di autori solo prima dell'accettazione, con l'Authorship Change Request form, il consenso scritto di tutti e l'approvazione dell'editor; "This journal does not allow authorship changes after acceptance". Group authorship dichiarata sulla title page.
- Etica (fonte: guide for authors; publishing ethics): lavoro non pubblicato prima (salvo preprint, abstract, tesi) e non in valutazione altrove; controllo con strumenti di screening; vietato potenziare, oscurare, spostare, rimuovere o introdurre elementi in un'immagine; regolazioni non lineari dichiarate in didascalia. Studi con persone (questionari, dati personali): approvazione etica e consenso informato secondo la policy Elsevier (sezione "Studies in humans" in Atmospheric Research).
- Linguaggio inclusivo e linee guida SAGER per sesso e genere, dove pertinenti.

### Lingua e ortografia (British/US)
- "We recommend that you write in American or British English but not a combination of both." (J. Hydrol. Regional Studies, Atmospheric Research, Weather and Climate Extremes, Advances in Water Resources, Environmental Modelling & Software; Journal of Hydrology non ne parla). Keywords in inglese.
- Unità SI richieste in J. Hydrol. Regional Studies (altre unità con l'equivalente SI).

### Cover letter e sottomissione
- Cover letter: le guide non ne indicano i contenuti né la rendono obbligatoria.
- Revisori suggeriti: le guide non ne parlano; il sistema di sottomissione può chiederli.
- Sottomissione online su Editorial Manager; la corrispondenza avviene per email. Checklist della guida: corresponding author con contatti completi, tutti i file caricati con didascalie, controllo ortografico, riferimenti e citazioni allineati, permessi per il materiale protetto, consapevolezza dell'APC per l'open access.
- Preprint: condivisibili senza che contino come pubblicazione precedente; posting gratuito su SSRN offerto alla sottomissione (in Atmospheric Research, Weather and Climate Extremes, Advances in Water Resources ed Environmental Modelling & Software dopo il desk review iniziale).
- Bozze: correzioni entro due giorni.

### Revisione tra pari
- Journal of Hydrology: "single anonymized review process"; screening degli editor e poi "a minimum of two reviewers"; review e focussed review con almeno 3 revisori. Un solo ricorso per manoscritto, con decisione definitiva.
- Le altre cinque riviste hanno la stessa sezione della guida (single anonymized, almeno due revisori). Advances in Water Resources fa eccezione per le short communication, revisionate dall'Editorial Advisory Board entro circa 15 giorni con risposta degli autori entro 10.
- Tempi: le guide non li dichiarano.

### Accesso e APC
Fonte: pagine "Open access information" delle riviste, 2026-10-11 (prezzi tasse escluse, tutti i tipi di articolo).
- Open access senza abbonamento: J. Hydrol. Regional Studies USD 2820; Weather and Climate Extremes USD 3640. Entrambe aderiscono al Geographical Pricing for Open Access (GPOA).
- Ibride (in abbonamento, "Supports open access"): Journal of Hydrology USD 4500; Atmospheric Research USD 3560; Advances in Water Resources USD 3510; Environmental Modelling & Software USD 3570.
- Licenze: CC BY, CC BY-NC, CC BY-NC-ND. L'APC personalizzato si vede in sottomissione; gli accordi open access Elsevier con le istituzioni possono coprirlo.

## Riviste

### Journal of Hydrology
- Guida: https://www.sciencedirect.com/journal/journal-of-hydrology/publish/guide-for-authors
- Ambito: ricerca originale e review in tutti i campi delle scienze idrologiche, compresi gestione e politiche dell'acqua con impatti economici e sociali; idrologia superficiale e sotterranea, idrometeorologia, idrogeologia, idrogeofisica; analisi multi e interdisciplinari, anche con scienze sociali, economiche e comportamentali. La scienza pubblicata vale "to catchment scales rather than exclusively to a local scale or site"; ammessi gli studi urbani. I problemi specifici di una regione vanno a J. Hydrol. Regional Studies.
- Tipi: Research Article (tipo principale); Review Article (almeno 3 revisori); Focussed Review (max 3.000 parole escluse abstract, titolo, autori e riferimenti; max 80 riferimenti; componente didattica; almeno 3 revisori); Technical Note (contributo tecnico o metodologico conciso, rilevante oltre il sito); Discussion (su un articolo del Journal of Hydrology, di norma entro 12 mesi; risposta degli autori originali entro 21 giorni, pubblicate insieme).
- Limiti: abstract max 250 parole; keywords 1-7; nessun limite per i Research Article.
- Differenze: highlights e graphical abstract incoraggiati; formato dei riferimenti libero alla sottomissione; ibrida.

### Journal of Hydrology: Regional Studies
- Guida: https://www.sciencedirect.com/journal/journal-of-hydrology-regional-studies/publish/guide-for-authors
- Ambito: rivista sorella del Journal of Hydrology per i problemi idrologici specifici di una regione, passati e futuri, con analisi, review e soluzioni; benvenuti i nuovi elementi di conoscenza sui processi regionali e sulle risposte a condizioni che cambiano, l'interdisciplinarità e la translational science. Temi: idrologia di bacino superficiale e sotterranea; impatti di cambiamento climatico e uso del suolo; osservazione, modellistica e previsione; gestione dell'acqua in bacini transfrontalieri e falde; idrologia economica; acqua e mezzi di sussistenza; allocazione culturale e sociale; impatti sociali delle infrastrutture.
- Tipi: Research Paper; Review Paper (solo review critiche, formato e lunghezza flessibili); Comment (fino a 4 mesi dalla pubblicazione dell'articolo commentato).
- Abstract **strutturato**, max 225 parole, in tre paragrafi con sottotitoli: Study Region (area o bacino), Study Focus (scopo e metodo), New Hydrological Insights for the Region (la nuova comprensione dell'idrologia regionale).
- Requisiti particolari: highlights e graphical abstract obbligatori; **file .kmz o .kml obbligatorio** con almeno posizione e nome dei siti o delle stazioni usati; unità SI; Results e Discussion ben distinti (la guida rimanda all'editoriale della rivista: Results con figure e tabelle senza ripeterle nel testo, Discussion che confronta con la letteratura, risponde agli obiettivi e indica limiti e ricerca futura); stile autore-anno applicato già alla sottomissione.
- Rispetto all'editoriale del 2020 (doi 10.1016/j.ejrh.2020.100717, https://media.journals.elsevier.com/content/files/editorialhydrologyregionalstudies-18134837.pdf): la guida corrente conferma l'abstract in tre sezioni e lo stile autore-anno; non chiede più righe numerate e doppia interlinea. Dall'editoriale restano utili come indicazioni editoriali, non come regole della guida: dichiarazione di novità alla fine dell'introduzione; Conclusions in almeno tre paragrafi brevi (risultati, limiti e ricerca futura, impatti più ampi); sovrapposizione testuale oltre circa il 20% di norma porta alla restituzione del manoscritto.
- Accesso: open access, APC USD 2820.

### Atmospheric Research
- Guida: https://www.sciencedirect.com/journal/atmospheric-research/publish/guide-for-authors
- Ambito: "Clouds - Precipitation - Aerosols - Radiation - Climatology, Weather Modification". La parte di atmosfera dove avvengono i fenomeni meteorologici, dalla superficie alla tropopausa, con particolare attenzione a fisica delle nubi, meteorologia a mesoscala, inquinamento e aerosol, microfisica, dinamica e termodinamica delle nubi, simulazione numerica, climatologia, cambiamento climatico, modificazione del tempo. Benvenuti i contributi agli SDG 7 e 13.
- Tipi: Research paper, Review article, Short communication (l'ambito cita anche "letters and notes"). Limiti: non indicati.
- Differenze: highlights obbligatori; sezione "Studies in humans" su etica e consenso (rilevante per studi con questionari o dati personali); template LaTeX incoraggiato; stile autore-anno applicato già alla sottomissione; ibrida.

### Weather and Climate Extremes
- Guida: https://www.sciencedirect.com/journal/weather-and-climate-extremes/publish/guide-for-authors
- Ambito: estremi meteorologici e climatici per accademici, decisori, agenzie di sviluppo, ONG e società civile: tipi, dati, frequenza e intensità, cambiamenti osservati e proiettati; previsione a breve e medio termine e stagionale degli estremi; **monitoring and early warning systems**; modellistica degli impatti; vulnerabilità ed esposizione; gestione del rischio, preparedness, adattamento, resilienza, saperi tradizionali, strategie di informazione e comunicazione; casi di studio.
- Tipi e limiti: Research article di norma fino a 7.500 parole; Short Communication sotto le 4.000; Perspective max 6.000 (in Editorial Manager scegliere il tipo "discussion"); Letter to the Editor sotto le 800 parole e con al massimo tre riferimenti.
- Differenze: data statement "encouraged" invece che obbligatorio (ma Option C invariata: in pratica va fornito); formato dei riferimenti libero alla sottomissione; highlights e graphical abstract incoraggiati.
- Accesso: open access, APC USD 3640, licenze CC BY, CC BY-NC, CC BY-NC-ND.

### Advances in Water Resources
- Guida: https://www.sciencedirect.com/journal/advances-in-water-resources/publish/guide-for-authors
- Ambito: avanzamenti scientifici **fondamentali** nella comprensione dei sistemi di risorse idriche, con approcci teorici, computazionali o sperimentali, superficiali o sotterranei, e loro interazioni con atmosfera, geosfera, biosfera e società. Temi: idrologia superficiale e sotterranea, idrometeorologia, fluidodinamica ambientale, ecoidrologia, trasporto multifase nei mezzi porosi, flusso e trasporto reattivo.
- Fuori ambito: casi di studio senza conclusioni generali, progettazione ingegneristica, idraulica applicata, qualità e trattamento delle acque, applicazioni di conoscenze esistenti che non avanzano la comprensione dei processi.
- Tipi: Original research manuscript; Short communication; correzioni; Discussion su articoli pubblicati. Short communication: abstract di più di 100 parole, max 4.000 parole di testo (più riferimenti, tabelle e ringraziamenti), max tre figure, con una dichiarazione che spiega perché è una short communication; screening degli editor, revisione dell'Editorial Advisory Board entro circa 15 giorni, risposta degli autori entro 10.
- Differenze: highlights obbligatori; template LaTeX incoraggiato; formato dei riferimenti libero alla sottomissione; ibrida.

### Environmental Modelling & Software
- Guida: https://www.sciencedirect.com/journal/environmental-modelling-and-software/publish/guide-for-authors
- Ambito: rivista ufficiale della International Environmental Modelling & Software Society. Avanzamenti nella modellistica e nel software ambientale per rappresentare, capire, prevedere o gestire sistemi ambientali (aria, acqua, suolo) a tutte le scale: framework generici, sviluppo e valutazione di modelli con insight **generalizzabili** ad altri sistemi, software ambientale e sistemi di supporto alle decisioni, applicazioni reali con usabilità, affidabilità, verifica e validazione documentate con risultati quantitativi, costi di sviluppo e manutenzione, adozione da parte degli utenti, licenze e accesso open source dichiarati; valutazione integrata; analisi di sensibilità e incertezza; AI; GIS e telerilevamento.
- Requisiti di contenuto: obiettivi del modello o del software, passi essenziali di sviluppo con la ragione dell'approccio scelto, test e valutazione sostanziali (confronti con approcci alternativi incoraggiati), breve storia del problema in letteratura e valore aggiunto.
- Tipi: Research article (il più comune); review paper (con metodi della revisione documentati); position paper; introductory overview (solo su invito); commentary; book review. Per tutto ciò che non è un research article, contattare prima l'Editor-in-Chief. Opinion paper della serie EnviroFutures solo su invito (max 4.000 parole e 2 figure).
- Limiti: abstract **max 150 parole**; highlights e graphical abstract obbligatori.
- **Sezione "Software and/or data availability"**, attesa nella maggior parte degli articoli: nome del software o del dataset, sviluppatore e contatto, anno di prima disponibilità, hardware e software richiesti, disponibilità e costo; per il software linguaggio e dimensione del programma; per i dati forma del repository, dimensione dell'archivio, modalità di accesso. "Contact the author" non è accettabile: usare GitHub, BitBucket, FigShare, HydroShare o simili (ammessi i link a software commerciale). Se il software è essenziale, renderlo scaricabile per i revisori, eventualmente con una password comunicata agli editor.
- Differenze: stile autore-anno applicato già alla sottomissione; template LaTeX incoraggiato; ibrida.

## Checklist di conformità
Regole verificate sulle guide delle sei riviste:
- File sorgente modificabile (.docx o .tex, non PDF); Word a una colonna.
- Title page completa: titolo senza abbreviazioni, autori nell'ordine del sistema, affiliazioni con indirizzo e paese, email del corresponding author.
- Abstract entro il limite della rivista (250; 225 strutturato per J. Hydrol. Regional Studies; 150 per Environmental Modelling & Software), autonomo, senza riferimenti.
- Keywords da 1 a 7, in inglese.
- Highlights: 3–5 punti, max 85 caratteri spazi inclusi, file separato con "highlights" nel nome; obbligatori dove la rivista li richiede.
- Graphical abstract (obbligatorio per J. Hydrol. Regional Studies ed Environmental Modelling & Software): file separato, min. 531 × 1328 pixel.
- Sezioni numerate; abstract non numerato.
- Inglese britannico o americano, mai misti.
- Declaration of competing interest compilata con il declarations tool per tutti gli autori, anche se negativa.
- Funding nel formato standard, oppure la formula di assenza di finanziamenti specifici.
- CRediT per tutti gli autori, ruoli fra i 14 standard.
- Dati depositati in un repository, citati e collegati (Option C), oppure motivazione; data statement compilato nella sottomissione.
- Se usata AI generativa: sezione "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process" prima dei riferimenti; nessuna immagine di dati creata o alterata con AI; AI non tra gli autori.
- Riferimenti autore-anno, ognuno corrispondente a una fonte reale, con DOI dove disponibile; dataset e software citati con "[dataset]" e "[software]".
- Tabelle modificabili senza linee verticali; figure in file separati alle risoluzioni minime (300 dpi foto, 1000 dpi tratto bitmap).
- Acknowledgements in sezione separata subito prima dei riferimenti.
- Mappe limitate all'area di studio, con la nota sui confini.
- Lista autori definitiva alla sottomissione; nessun cambio dopo l'accettazione.
- Solo J. Hydrol. Regional Studies: abstract in tre sezioni (Study Region, Study Focus, New Hydrological Insights for the Region), file .kmz/.kml con i siti, unità SI.
- Solo Environmental Modelling & Software: sezione Software and/or data availability completa, senza "contact the author".
- Solo Advances in Water Resources, short communication: max 4.000 parole, max 3 figure, dichiarazione di motivazione.

## Punti non verificati
1. Contenuti della cover letter: le guide non li indicano.
2. Numero di revisori suggeriti: le guide non ne parlano.
3. Tempi di revisione: le guide non li dichiarano.
4. Limiti dei tipi brevi di Atmospheric Research (short communication, letters, notes): non indicati.
