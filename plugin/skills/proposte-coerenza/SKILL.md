---
name: proposte-coerenza
description: "Controllo formale di una proposta europea prima di consegnarla: cerca le incoerenze fra sezioni (impatti che nessun work package produce, KPI presenti in un posto solo, numeri e date che si contraddicono, partner citati e assenti dalle tabelle) e conta pagine e caratteri contro i limiti del bando, con il margine o lo sforamento per sezione. Non da' punteggi e non entra nel merito. Dove l'ambiente lo permette lancia un verificatore indipendente; altrimenti svolge il controllo nel contesto principale e lo dichiara. Usare per: 'controlla la coerenza', 'ci stiamo nei limiti', 'quante pagine siamo', 'rileggi prima di consegnare', 'check consistency', 'are we within the page limit'. Non usare per: valutazione con punteggi e soglie (proposte-revisione); scrivere o correggere il testo (proposte-scrittura); criteri del bando (proposte-analisi-bando); ESR ricevuti (proposte-risposta-esr); deliverable e report (progetti-revisione); testi generici (generale-revisione)."
---

# Coerenza e limiti di una proposta

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Poi leggere `references/matrice-bando.md` e
`references/anti-pattern-proposte.md`, sezione "Coerenza fra sezioni".

Livello di revisione del dominio: **completo**. Questo controllo non e' una
valutazione: il merito lo giudica `proposte-revisione`, con tre valutatori e
un rapporteur.

## Che cosa fa, e che cosa non fa

Fa due cose, in modo esaustivo:

1. **Incoerenze fra sezioni.** Sono quello che i valutatori trovano per
   primo, perche' si vedono senza conoscere il tema: un impatto promesso che
   nessuna attivita' produce, un KPI che compare solo nell'impatto, due numeri
   diversi per la stessa cosa, un partner citato e assente dalle tabelle.
2. **Limiti.** Pagine e caratteri contro i limiti del bando, con il margine o
   lo sforamento, per sezione dove il bando pone limiti per sezione.

Non da' punteggi, non dice se la proposta e' buona, non riscrive. Se l'utente
vuole il giudizio, la skill lo dice in una riga e rimanda a
`proposte-revisione`; se vuole la correzione, a `proposte-scrittura`.

## Confini

| Richiesta | Chi la prende |
|---|---|
| incoerenze fra sezioni e sforamento dei limiti | questa skill |
| punteggi, soglie, giudizio di merito | `proposte-revisione` |
| correggere o riscrivere il testo | `proposte-scrittura` |
| criteri, pesi, soglie e limiti del bando | `proposte-analisi-bando` |

## Materiali

1. **Proposta** completa, con le tabelle: su una parte sola si controlla
   quella, e la consegna dice che le incoerenze con il resto non sono state
   cercate.
2. **Matrice del bando**, o il testo del topic: da li' vengono i limiti e le
   sezioni obbligatorie. Senza, i limiti restano `[da bando]` e non si
   stimano.

## Modalità agenti

1. Salvare nella cartella di lavoro `coerenza/proposta.md` (versione leggibile
   se arriva in Word o PDF) e `coerenza/matrice-bando.md`.
2. Lanciare l'agente `proposte-verificatore` con: percorsi della proposta,
   degli allegati e della matrice; il percorso del rapporto
   (`coerenza/rapporto.md`); la lingua. Niente altro: nessun riassunto della
   conversazione, nessuna indicazione su che cosa aspettarsi.
3. Presentare il rapporto all'utente, in ordine: prima le incoerenze
   bloccanti, poi i limiti, poi le voci mancanti.
4. Proporre le correzioni. Riscrivere solo su richiesta, con
   `proposte-scrittura`.

Se i file non si riescono a salvare, passare alla modalità chat e dirlo in
una riga.

## Modalità chat

Senza subagent la skill svolge da sola, nel contesto principale, il lavoro
del `proposte-verificatore`, con le stesse regole e lo stesso formato.
Dichiararlo in una riga all'inizio.

1. Aprire con la frase della sezione 4a del protocollo: il controllo e' fatto
   nella stessa conversazione, quindi tende a essere indulgente.
2. Confrontare le sezioni a coppie, nell'ordine: obiettivi contro piano di
   lavoro; impatti contro piano di lavoro; KPI dovunque compaiano; risorse e
   partner contro tabelle; date e durate contro diagrammi; riferimenti
   interni.
3. Contare i limiti e dichiarare l'approssimazione del conteggio.
4. Consegnare il rapporto completo nel formato previsto, non un riassunto.

## Consegna

- **Incoerenze**, ciascuna con **tutti e due** i passaggi citati e la sezione
  di ciascuno: senza la coppia non e' una incoerenza, e' un'opinione.
- **Limiti**: limite, conteggio, margine o sforamento, e la fonte del limite.
  Dove il limite non e' noto si scrive `[da bando]`: non si stima.
- **Voci mancanti** rispetto alla matrice: una sezione fatta di segnaposto
  vale come mancante.
- Nessun punteggio. Se nel rapporto ne compare uno, e' un errore di questa
  skill.

Il conteggio delle pagine e' per forza approssimativo finche' il testo non e'
nel modulo con il suo font e i suoi margini: dirlo in una riga invece di dare
un numero esatto che non puo' esserlo.
