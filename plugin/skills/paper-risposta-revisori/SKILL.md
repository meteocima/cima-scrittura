---
name: paper-risposta-revisori
description: Prepara la risposta punto per punto ai commenti di revisori ed editor su un manoscritto scientifico degli autori CIMA - scomposizione dei commenti, piano delle modifiche (commento, decisione, modifica, posizione nel testo), lettera di risposta e controllo di coerenza con il manoscritto rivisto. Tiene conto delle regole della rivista, compresa la discussione pubblica di Copernicus/EGU (HESS, NHESS, GMD). Triggers - "rispondi ai revisori", "risposta ai referee", "major revision", "rebuttal", "lettera di risposta", "commenti dei revisori", "response to reviewers", "reply to referee comments", "author's response". Caricarla prima di chiedere chiarimenti, perché sa lei che cosa chiedere. Non usare per - peer review simulata prima della sottomissione (paper-revisione), scrittura di sezioni nuove (paper-scrittura), risposta agli ESR di una proposta (proposte-*), commenti di project officer o reviewer di un progetto finanziato (progetti-*), email e traduzioni (generale-*).
---

# Risposta ai revisori

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Livello di revisione del dominio: **standard**. Sul **merito** delle
risposte il giudizio l'hanno già dato i revisori reali, quindi non serve
simularne altri: basta l'autorevisione con il controllo di coerenza della
sezione 6.

Resta però il caso dei testi che vengono pubblicati: nelle riviste a revisione
aperta, come quelle Copernicus, la risposta agli autori esce con un DOI
(`references/formato-risposta.md`). Lì vale la regola generale dei testi
destinati alla pubblicazione (`references/nucleo/protocollo-revisione.md`,
sezione 2): in modalità agenti almeno un revisore separato sulla forma e sulla
completezza delle risposte, in modalità chat autovalutazione dichiarata e
pacchetto revisore.

## Confini

| Richiesta | Chi la prende |
|---|---|
| risposta ai commenti di revisori ed editor di una rivista | questa skill |
| peer review simulata, prima di sottomettere | `paper-revisione` |
| riscrivere le sezioni che i revisori hanno criticato | `paper-scrittura` |
| risposta ai commenti di una review di progetto o di un project officer | `progetti-risposta-review` |
| risposta agli ESR di una proposta | dominio proposte |
| le slide che accompagnano la revisione | `generale-presentazione` |

## Deroghe allo stile di base

- Lettera in inglese (o nella lingua della rivista), con "we".
- Commenti dei revisori riportati alla lettera, anche se contengono
  anti-pattern: non si correggono.
- Tabelle ed elenchi numerati ammessi: la struttura punto per punto è
  richiesta dal genere.

## Regola principale

La lettera dice solo ciò che è stato fatto davvero. Mai "we have
revised", "we added", "see line 245" se la modifica non è nel manoscritto
rivisto. Finché non lo è: `[modifica da fare: …]` e
`[righe: da inserire]`. Le decisioni scientifiche (fare o no una nuova
analisi, accettare o respingere una critica) sono degli autori: proporle,
non prenderle.

## 1. Raccogliere i materiali

- Lettera di decisione dell'editor e tutti i commenti (revisori,
  editor, eventuali commenti pubblici).
- Manoscritto sottomesso e, se esiste, manoscritto rivisto o elenco delle
  modifiche fatte.
- Rivista. Le istruzioni per la revisione nella lettera di decisione
  (file richiesti, scadenza, versione con modifiche evidenziate)
  prevalgono su tutto. Poi il profilo dell'editore
  (`references/rivista-*.md`, sezioni "Revisione tra pari" e "Cover
  letter e sottomissione"); per una voce `[da verificare]` o un editore
  senza profilo, usare solo la lettera di decisione e la guida fornita
  dall'utente, mai la memoria.

## 2. Policy della rivista sull'AI generativa

Per le riviste Copernicus / EGU (GMD, HESS, NHESS, ESSD, ACP, WCD) vale la
policy sull'AI generativa, il cui testo esatto e la cui data di verifica
stanno in `references/rivista-copernicus.md`: leggerla di lì, non fidarsi di
una parafrasi. Per queste riviste: produrre la scomposizione, il piano
delle modifiche, lo schema della lettera e il controllo di coerenza;
sulle risposte scritte dagli autori intervenire solo su lingua e
leggibilità. Dirlo all'utente all'inizio, in due righe. Per gli altri
editori l'uso va dichiarato secondo la policy del profilo
(`references/rivista-*.md`, "Dichiarazioni obbligatorie"): ricordarlo
alla consegna. Dettagli e fonti in `references/formato-risposta.md`.

## 3. Scomporre i commenti

- Numerare ogni richiesta autonoma: R1.1, R1.2, R2.1, E.1 (editor).
  Un commento con tre richieste diventa tre voci.
- Riportare il testo originale integro per ogni voce.
- Classificare: nuova analisi, chiarimento, correzione di errore,
  letteratura, figure e tabelle, forma e lingua, fuori ambito.
- Individuare richieste **sovrapposte** (stesso punto da più revisori) e
  **in conflitto** (richieste incompatibili): segnalarle subito, vanno
  gestite in modo coerente.

## 4. Pianificare con gli autori

Tabella di lavoro, consegnata insieme alla lettera nello stesso turno
(non fermarsi ad aspettare conferma):

| Voce | Sintesi | Tipo | Decisione proposta | Modifica nel testo | Posizione | Stato |
|---|---|---|---|---|---|---|

- **Decisione proposta**: accettato, accettato in parte, non accettato
  con motivazione, sempre marcata `[decisione proposta: da confermare]`
  finché l'utente non la conferma. Per "non accettato" serve un argomento verificabile
  (dato, riferimento verificato, limite dichiarato), non una preferenza.
- **Stato**: fatto / da fare / da decidere.
- Nuove analisi: indicare cosa servirebbe, senza anticipare risultati.

## 5. Scrivere la lettera

Struttura e tono in `references/formato-risposta.md`. In sintesi:

1. Breve apertura all'editor: ringraziamento sobrio, sintesi delle
   modifiche principali in 3–5 punti.
2. Per ogni voce: commento originale, risposta, modifica con posizione e,
   quando utile, la nuova frase citata dal manoscritto.
3. Tono: fermo e cortese. Niente lodi di rito a ogni commento, niente
   scuse eccessive, niente polemica. Il disaccordo si motiva con fatti.
4. Ogni risposta è comprensibile senza rileggere le altre.

Testi lunghi: in chat un revisore per messaggio, proseguendo fino alla
fine senza attendere conferma; con accesso alla cartella di lavoro, file
.docx o .md.

## 6. Controllo di coerenza prima della consegna

Eseguirlo sempre, nel contesto principale.

1. Ogni voce ha una risposta; nessuna voce saltata o accorpata senza
   dirlo.
2. Ogni modifica dichiarata come fatta si trova nel manoscritto rivisto
   (cercare la frase citata); se il manoscritto rivisto non è
   disponibile, la modifica resta segnata come `[da confermare]`.
3. Posizioni (righe, sezioni, figure) coerenti con la versione rivista.
4. Risposte a richieste sovrapposte coerenti tra loro; richieste in
   conflitto spiegate all'editor.
5. Numeri nella lettera identici a quelli del manoscritto.
6. Riferimenti nuovi verificati (`verifica-fonti.md`).
7. Procedura anti-pattern sulla parte scritta dagli autori (non sui
   commenti citati).

## 7. Consegna

1. Lettera di risposta (o schema, per le riviste Copernicus).
2. Tabella delle modifiche con lo stato.
3. **Modifiche ancora da fare nel manoscritto**, in ordine.
4. **Segnaposto** e **da verificare**.
5. Esito del controllo di coerenza, in poche righe.
