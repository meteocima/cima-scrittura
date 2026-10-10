# Dichiarazioni del manoscritto

Titolo, posizione e obbligatorietà di ogni dichiarazione cambiano per
rivista: controllarli sempre nel profilo (`rivista-*.md`, sezioni
"Struttura e sezioni obbligatorie" e "Dichiarazioni obbligatorie").
Qui ci sono solo le tracce di contenuto, con segnaposto. Nessun dato
(repository, DOI, licenze, numeri di grant, ruoli) si deduce: tutto viene
dall'utente.

## Disponibilità dei dati (Data availability)

Per ogni dataset usato: cosa, dove, come accedervi, condizioni.

```
The [nome del dataset, versione] used in this study [is/are] available
from [repository o fornitore] at [DOI o URL] under [licenza].
[Per dati di terzi:] [Nome] data were obtained from [fornitore] and are
available [condizioni di accesso].
[Per dati non pubblici:] [Motivo] prevents public release; data are
available from [chi] upon [condizione].
```

Controlli: i dati necessari a riprodurre le figure sono indicati; i
dataset citati qui compaiono anche nei riferimenti se la rivista lo
richiede (Copernicus e AGU chiedono la citazione dei dataset).

## Disponibilità del codice (Code availability)

```
The [nome del modello o del codice] version [versione esatta] used in
this study is archived at [repository persistente] ([DOI]) under the
[licenza] licence. [Script di analisi e figure:] available at [DOI].
```

Per GMD le regole sono più strette (sezione "Code and data
availability", versione esatta, archivio persistente): vedere
`rivista-copernicus.md`.

## Contributi degli autori

Se la rivista usa la tassonomia CRediT, usare solo i ruoli che
l'utente indica per ciascun autore. Non attribuire ruoli per deduzione.

```
[Iniziali]: [ruolo CRediT], [ruolo CRediT]. [Iniziali]: …
```

## Conflitti di interesse

Formula della rivista, presa dal profilo (es. "The authors declare no
competing interests."). Se l'utente non ha detto nulla: segnaposto
`[conflitti di interesse: da confermare con tutti gli autori]`.

## Finanziamenti

```
This work was supported by [finanziatore] under [programma], grant
agreement No. [numero] ([acronimo del progetto]).
```

Numero di grant e acronimo solo se forniti. Alcuni finanziatori
impongono una formula esatta: chiederla all'utente.

## Uso di AI generativa

Posizione e regole nel profilo; sintesi delle differenze in SKILL.md,
sezione 3. Traccia per le riviste che chiedono la dichiarazione:

```
During the preparation of this work the authors used [strumento] for
[scopo: es. drafting of sections X and Y, language editing]. The
authors reviewed and edited the output and take full responsibility for
the content of the publication.
```

Lo scopo va descritto per com'è stato davvero: se il plugin ha scritto
bozze di sezioni, dirlo.

Riviste Copernicus: la scrittura di testo e interpretazioni con AI
generativa non è ammessa (il testo e la data di verifica stanno in
`references/rivista-copernicus.md`); l'uso assistivo su
lingua e leggibilità non si dichiara. Ogni altro uso (es. figure o
schemi generati) va dichiarato in Methods o Acknowledgements:

```
[Strumento] was used to [scopo, es. generate the schematic in Fig. n].
[Estensione e controllo degli autori.]
```
