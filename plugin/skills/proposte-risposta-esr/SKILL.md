---
name: proposte-risposta-esr
description: "Lavora sull'Evaluation Summary Report di una proposta non finanziata: scompone i rilievi uno per uno, decide per ciascuno se accoglierlo o contestarlo con il motivo, dice che cosa cambia nella proposta e dove, e tiene separato cio' che e' gia' fatto da cio' che e' solo deciso. Vale anche a progetto avviato, perche' il confine con progetti e' la firma del Grant Agreement. Usare per: 'rispondiamo all'ESR', 'come rifacciamo la proposta dopo la valutazione', 'commenti dei valutatori sulla proposta', 'ESR', 'evaluation summary report', 'we were not funded, what now'. Non usare per: risposta a un review report o a un deliverable respinto di un progetto finanziato (progetti-risposta-review); risposta ai revisori di una rivista (paper-risposta-revisori); riscrivere il testo della proposta (proposte-scrittura); valutazione simulata prima della scadenza (proposte-revisione); capire i criteri del bando (proposte-analisi-bando)."
---

# Risposta a un ESR

## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
Se l'utente fornisce o chiede un file: `references/nucleo/formati-e-file.md`.

Poi leggere `references/formato-risposta-esr.md`,
`references/anti-pattern-proposte.md` e `references/pattern-esr.md`, che
aiuta a capire che cosa intende un rilievo e quanto e' costato.

Livello di revisione del dominio: **completo**. Sul merito della proposta
riscritta la revisione separata la fa `proposte-revisione`; su questo
documento basta l'autorevisione, dichiarata.

## La prima cosa da dire

A un ESR **non si replica**: nessun programma prevede una risposta di merito
al valutatore. L'ESR si usa per rifare la proposta. Dirlo in una riga, senza
farne un discorso, e poi fare il lavoro che serve davvero.

L'unica strada formale e' l'**evaluation review**, che riguarda solo gli
aspetti procedurali e mai il merito, con termini e limiti nel profilo del
programma. Se l'utente parla di contestare il punteggio, e' li' che va
indirizzato, sapendo che il merito non si riesamina.

## Confini

| Richiesta | Chi la prende |
|---|---|
| lavorare sull'ESR di una proposta | questa skill |
| risposta a un review report o a un deliverable respinto, dopo la firma | `progetti-risposta-review` |
| risposta ai revisori di una rivista | `paper-risposta-revisori` |
| riscrivere le sezioni della proposta | `proposte-scrittura` |
| valutazione simulata prima di consegnare | `proposte-revisione` |

Il confine con `progetti` e' la **firma del Grant Agreement**, non il momento:
l'ESR di una proposta resta qui anche se nel frattempo il consorzio ha un
altro progetto avviato (`adr/0009`, `adr/0020`).

## Materiali

Chiedere in un solo messaggio, poi procedere comunque:

1. **ESR**, per intero, con i punteggi per criterio.
2. La **proposta** presentata, o almeno le sezioni toccate dai rilievi.
3. Il bando a cui si ripresenta: se e' cambiato, alcuni rilievi cambiano
   senso.
4. Che cosa il consorzio ha gia' deciso (nuovi partner, cambi di ambito).

Senza la proposta si lavora lo stesso sui rilievi, dicendo che la colonna
"dove" resta da riempire.

## Riservatezza

L'ESR e la proposta sono riservati (`references/nucleo/vincoli.md`, sezione
"Riservatezza"). Non copiarne frasi nelle ricerche web: si cercano solo titoli
di bandi, identificativi di topic e documenti ufficiali. I file restano nella
cartella di lavoro indicata dall'utente.

## Procedura

1. **Scomporre** l'ESR secondo `references/formato-risposta-esr.md`: un
   numero per rilievo, il criterio, il tipo, se e' fondato. **Nessun rilievo
   resta fuori**, nemmeno quelli generici o quelli che sembrano ingiusti: un
   rilievo senza riga e' un rilievo che tornera' identico la prossima volta.
2. **Ordinare** per gravita': prima i criteri sotto soglia, poi il resto.
3. **Decidere la posizione** per ciascuno: accolto, accolto con chiarimento,
   parzialmente accolto, contestato. Contestare va bene, ma con un motivo
   verificabile: un dato, una fonte, un passaggio della proposta che il
   rilievo non ha considerato. Mai "il valutatore non ha capito".
4. **Dire che cosa cambia e dove**, nella proposta nuova. Se la modifica non
   c'e' ancora, lo stato e' `da fare`, non una descrizione al passato di una
   cosa non fatta.
5. **Autorevisione**: ogni rilievo ha una riga; ogni contestazione ha un
   motivo verificabile; nessuna modifica dichiarata che non esiste; i
   segnaposto sono elencati.

## Consegna

- La **tabella** rilievo per rilievo, nel formato del riferimento.
- I tre elenchi di chiusura: decisioni che mancano, criteri sotto soglia con
  quanto manca, punti apprezzati da non rompere.
- Se il programma prevede una sezione sui cambiamenti alla ripresentazione, il
  testo di quelle righe, pronto per entrare nella proposta nuova.
- I segnaposto, raggruppati.
- La nota di autorevisione.

Quando l'ESR porta punteggi, la consegna li riporta **con la scala e la
soglia** del programma, come fa `proposte-revisione`: un 3 non vuol dire
niente senza sapere su quanto e sotto quale soglia.
