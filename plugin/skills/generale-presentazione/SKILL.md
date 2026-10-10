---
name: generale-presentazione
description: "Costruisce presentazioni di Fondazione CIMA sul tema istituzionale, in italiano e in inglese: talk di conferenza, presentazioni di review di progetto, pitch di proposta, presentazioni istituzionali, seminari. Parte dal tempo a disposizione, costruisce la scaletta prima del mazzo, scrive titoli che affermano e note per chi parla, e produce un file .pptx. I criteri di contenuto restano del dominio: per un talk rimanda a paper, per una review a progetti. Usare per 'fai le slide', 'prepara la presentazione', 'mazzo per la review', 'slide per EGU', 'presentazione per la Regione', 'make the slides', 'prepare a deck', 'slides for the project review'. Non usare per: testo di articoli, abstract e cover letter (paper-); testo di proposte ed ESR (proposte-); deliverable e report (progetti-); email, lettere e comunicati (generale-scrittura); tradurre un mazzo esistente (generale-traduzione); rileggere un testo già scritto (generale-revisione)."
---

# Presentazioni CIMA

Questa skill costruisce i mazzi di slide di Fondazione CIMA, per qualsiasi
dominio. Livello di revisione: **leggero**
(`references/nucleo/protocollo-revisione.md`, sezione 2).

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Riferimenti di questa skill:

- `references/struttura.md`: quanto dura, quante slide, come si costruisce il
  discorso per occasione;
- `references/tema-cima.md`: il tema, i layout e come si monta il file;
- `references/tema-cima.pptx`: il template da cui si parte;
- `references/griglia-presentazione.md`: criteri di revisione;
- `references/destinatari.md`: tono per destinatario.

## Confini

Questa skill fa il **mazzo**. Il **contenuto** resta del dominio a cui
appartiene.

| Richiesta | Chi fa che cosa |
|---|---|
| slide di un talk di conferenza | questa skill per il mazzo; i criteri del contenuto e i limiti della conferenza da `paper` |
| slide di una review di progetto | questa skill; aderenza alla DoA e tracciabilità da `progetti` |
| slide di un pitch di proposta | questa skill; criteri e gergo del programma da `proposte` |
| presentazione istituzionale, giornata pubblica, seminario | questa skill, da sola |
| tradurre un mazzo che esiste già | `generale-traduzione`, che traduce dentro il file senza rifarne la struttura |
| rivedere un mazzo che esiste già | questa skill, con la griglia, senza rifarlo |
| il testo di un articolo, di un deliverable o di una proposta | la skill di quel dominio: le slide vengono dopo |

Se il contenuto appartiene a un altro dominio e quella skill non è
disponibile, costruire comunque il mazzo applicando il nucleo, e dire in una
riga quali criteri specifici del dominio non sono stati applicati.

## Che cosa serve sapere

Prima di costruire, servono quattro cose. Una sola merita una domanda.

1. **Quanto dura.** Se non è detto, chiedere: decide tutto il resto.
2. **Occasione e pubblico.** Dedurli dalla richiesta; per il tono vedere
   `references/destinatari.md`. Se non sono deducibili, procedere con l'ipotesi
   più probabile e dichiararla.
3. **Il contenuto.** Solo ciò che l'utente ha fornito: testo, file, risultati,
   il deliverable o il paper da cui nasce il mazzo. Niente altro.
4. **Lingua.** Dedurla secondo `voce-e-lingua.md`.

Ogni dato che serve e manca diventa un segnaposto nella slide, elencato nella
consegna. Non fare una raffica di domande: costruire il mazzo con i segnaposto.

## Flusso di lavoro

1. **Scaletta prima del mazzo.** Un elenco numerato: per ogni slide, layout,
   titolo che afferma, e in una riga che cosa sostiene. Seguire l'ossatura per
   occasione in `struttura.md`. Mostrare la scaletta all'utente e proseguire
   senza attendere conferma, salvo che l'utente abbia chiesto di approvarla.
2. **Fonti.** Se il mazzo cita studi, dati di terzi o norme, seguire
   `verifica-fonti.md` prima di scrivere.
3. **Testo delle slide.** Titoli che affermano, corpo breve, note del relatore
   con quello che si dice a voce. Regole in `struttura.md`.
4. **File.** Montarlo seguendo `tema-cima.md`.
5. **Autorevisione.** Sempre: `griglia-presentazione.md`, correggendo quello
   che si può correggere senza nuove informazioni.
6. **Revisione separata**, se serve: sezione sotto.
7. **Consegna.**

## Costruire il file

La procedura completa è in `references/tema-cima.md`. In breve: si copia il
template, si impostano una volta sola le costanti nei layout (autori,
occasione, intestazione), si duplica per ogni slide l'esempio del layout
giusto e se ne riempiono i segnaposto, si eliminano gli esempi rimasti, si
valida.

La meccanica del formato la fa la skill `pptx`
(`references/nucleo/formati-e-file.md`): questa skill decide che cosa va sulle
slide, non come si impacchetta un file PowerPoint.

Senza strumenti per produrre il file, consegnare il mazzo completo come testo
strutturato, una slide per blocco con layout, titolo, corpo e note, dicendolo
in una riga. Il lavoro non si ferma per un formato.

## Revisione separata

Serve per i mazzi **pubblici o istituzionali** (giornate pubbliche, eventi con
enti e istituzioni, presentazioni a nome di CIMA) e quando l'utente la chiede
per qualsiasi mazzo. Per i mazzi interni e di lavoro basta l'autorevisione con
la griglia. La modalità si deduce dagli strumenti disponibili
(`protocollo-revisione.md`, sezione 1).

## Modalità agenti

Strumento per lanciare subagent disponibile (`Agent` o `Task`):

1. Salvare nella cartella di lavoro il mazzo, la scaletta con le note del
   relatore in `revisione/mazzo.md` e la griglia di anteprime prodotta da
   `scripts/thumbnail.py` della skill `pptx`. Il revisore ha solo `Read`,
   `Glob`, `Grep` e `Write`: senza le anteprime non vedrebbe densità e
   leggibilità, e senza la scaletta non potrebbe giudicare il ritmo.
2. Costruire i percorsi assoluti a partire dalla cartella base di questa
   skill, indicata al caricamento.
3. Lanciare `generale-revisore-presentazione` con un prompt che contiene solo:
   percorso del file e della scaletta; occasione, pubblico e minuti a
   disposizione; percorsi di `references/griglia-presentazione.md`,
   `references/struttura.md`, `references/tema-cima.md` e dei file in
   `references/nucleo/` (vincoli, anti-pattern-ai, voce-e-lingua,
   terminologia, protocollo-revisione); formato del rapporto (sezione 5 del
   protocollo, con i punteggi della griglia); lingua del rapporto, quella in
   cui scrive l'utente; percorso del rapporto `revisione/rapporto-mazzo.md`.
   Niente riassunti della conversazione, scelte fatte o giudizi anticipati.
4. Leggere il rapporto. Non contestarlo per difendere il mazzo.
5. Applicare le correzioni che non richiedono nuove informazioni o scelte
   dell'utente; elencare le altre come proposte.

Se il lancio fallisce, passare alla modalità chat e dirlo in una riga.

## Modalità chat

Strumento per lanciare subagent non disponibile:

1. Svolgere la revisione nel contesto principale con la stessa
   `griglia-presentazione.md`, guardando il mazzo come chi sta in fondo alla
   sala e non ha seguito la conversazione.
2. Aprire il rapporto con la riga di `protocollo-revisione.md`, sezione 4a.
3. Stesso formato del revisore, con i punteggi della griglia, nella lingua in
   cui scrive l'utente.
4. Applicare le correzioni come al punto 5 della modalità agenti e consegnare
   il mazzo finale completo.
5. Per i mazzi pubblici o istituzionali, offrire in fondo il pacchetto
   revisore (sezione 4b del protocollo) in un unico blocco da copiare in una
   conversazione nuova.

Non fermarsi e non chiedere all'utente di cambiare ambiente: il mazzo arriva
comunque.

## Deroghe allo stile di base

Rispetto a `voce-e-lingua.md`:

- **Frasi senza verbo** ammesse nei titoli e nei punti elenco, dove la
  concisione vale più della forma distesa.
- **Elenchi puntati** ammessi come forma normale del corpo, non come
  eccezione.
- **Maiuscole e separatori imposti dal tema**: valgono le regole di
  `tema-cima.md`, comprese quelle sul trattino lungo nella riga
  dell'occasione e nella numerazione delle sezioni.
- **Sigle** ammesse senza scioglimento sulle slide, se sciolte nelle note del
  relatore o su una slide precedente.

Resta fermo tutto il resto del nucleo, a cominciare dal divieto di inventare
dati e dal divieto del punto medio.

## Consegna

- **Il file** del mazzo, nel formato richiesto, dove lo mette
  `formati-e-file.md`.
- **La scaletta** con le note del relatore, nel messaggio, così si legge senza
  aprire il file.
- Dopo, in quest'ordine e solo se presenti:
  1. **Segnaposto da completare**: elenco di tutti quelli inseriti, con la
     slide in cui stanno.
  2. **Slide di backup** preparate, in una riga.
  3. **Fonti**: verificate, corrette o non trovate.
  4. **Revisione**: sintesi del rapporto in 2 a 4 righe, correzioni applicate,
     proposte aperte. Per i mazzi senza revisione separata, una riga che dice
     che l'autorevisione è stata fatta.
  5. **Assunzioni**: occasione, pubblico, durata o lingua dedotti e non
     dichiarati dall'utente.
