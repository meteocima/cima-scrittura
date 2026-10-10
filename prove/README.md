# Prove

Il plugin viene usato in due modi, e deve funzionare in tutti e due:

- **modalità agenti**, dove lo strumento per lanciare subagent c'è (Cowork,
  Claude Code): la revisione la fa un contesto separato;
- **modalità chat**, dove non c'è: la skill svolge da sola ogni passaggio che
  avrebbe affidato a un agente, lo dichiara e consegna lo stesso il risultato
  completo.

Le due modalità non danno lo stesso risultato: danno lo stesso **prodotto** con
una garanzia di indipendenza diversa. Una regola scritta e mai provata si
sfilaccia, quindi ogni aggiornamento si prova in tutti e due prima di uscire.

## Com'è organizzata

- `domini/<dominio>.md`: le prove di regressione, stabili. Si rifanno quando si
  tocca quel dominio, e dicono quale skill deve attivarsi per quale richiesta.
- `<versione>-<slug>/`: una cartella per aggiornamento, con le prove nuove di
  quell'aggiornamento e i loro esiti. Resta nel repository: serve a sapere che
  cosa era stato provato, e come era andata.

## Fare un aggiornamento

1. Alzare `version` in `plugin/.claude-plugin/plugin.json`.
2. Creare `prove/<versione>-<slug>/README.md` dalla struttura qui sotto, con
   le prove che servono a quell'aggiornamento. Finché la cartella manca,
   `scripts/build.py --check` lo segnala.
3. Mettere in `materiali/` i file di ingresso che servono alle prove (un
   `.docx` finto, un template, un mazzo di slide). Mai materiale reale: niente
   deliverable veri, proposte, manoscritti o nomi di persone.
4. Fare la build, installare il pacchetto, eseguire le prove nei due ambienti e
   riempire la colonna degli esiti.
5. Committare la cartella con gli esiti dentro, insieme alla voce del
   `CHANGELOG`.

Un aggiornamento che tocca una skill ha **almeno una prova per ambiente**. Dove
l'ambiente cambia il comportamento (file salvato su disco contro file
scaricabile, agente separato contro autorevisione dichiarata), l'esito atteso
va scritto diverso per i due: se è identico, probabilmente la prova non sta
guardando la differenza che conta.

## Struttura del README di un aggiornamento

```markdown
# <versione>: <titolo>

Che cosa cambia, in tre righe.

## Prove

| # | Ambiente | Prompt | Esito atteso | Esito reale |
|---|---|---|---|---|
| 1 | agenti | ... | ... | |
| 2 | chat | ... | ... | |

## Esito

Data, ambiente provato, che cosa è stato corretto prima di rilasciare.
```

Un esito reale che non corrisponde all'atteso non si cancella: si scrive, si
corregge il plugin e si riprova, lasciando la riga vecchia. È la memoria di che
cosa si rompe facilmente.
