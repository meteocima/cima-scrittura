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

## La suite automatica

`prove/evals/` contiene le prove convertite in casi per `claude plugin eval`,
che lancia sessioni figlie che non hanno letto né le prove né gli esiti
attesi e misura con grader separati. È il modo di sapere se una skill si
attiva **da sola**: chi esegue le prove a mano ha letto l'esito atteso prima
di cominciare.

- `instradamento/`: dieci frasi, misurano solo quale skill si attiva;
- `giro-0.2.0/`: le righe misurabili del giro 0.2.0, una per caso; il suo
  README dice quali righe sono rimaste fuori e perché;
- `_materiali/`: collegamenti ai file finti delle prove, che lo
  `scaffold_script` di ogni caso copia nella cartella di lavoro.

Si esegue su una copia, perché l'eval scrive i risultati dentro la cartella
del plugin e i collegamenti vanno risolti:

```bash
python3 scripts/build.py
R=$(mktemp -d)/run && cp -r dist/cima-scrittura "$R" && cp -rL prove/evals "$R/evals"
cd "$R" && claude plugin eval . --runs 1 -j 4 --ablation none --scaffold \
  --allow-tools Write Bash --judge-model opus --no-publish
```

I casi con il tag `senza-file` vanno lanciati **a parte, senza concedere
`Write`**: la concessione sulla riga di comando vale per tutti i casi e
scavalca la lista `allowed_tools` del caso, quindi una sessione che il caso
vuole senza file salva lo stesso. Scoperto il 2026-10-11 dalle tracce del caso
`giro-0.3.0/24-coerenza-senza-file`: con la concessione la sessione salvava il
rapporto e rimandava al file, senza la concessione lo consegnava intero.

Quindi due copie: in una si tolgono i casi `senza-file` e si lancia il
comando qui sopra, nell'altra si lanciano solo quelli, con `Bash` e basta.

```bash
R2=$(mktemp -d)/run && cp -r "$R" "$R2"
grep -rl 'senza-file' "$R/evals" --include=case.yaml | xargs -n1 dirname | xargs rm -rf
cd "$R2" && claude plugin eval . --tag senza-file --runs 1 -j 4 --ablation none \
  --scaffold --allow-tools Bash --judge-model opus --no-publish
```

Prima di quella data il comando documentato concedeva `Write` a tutta la
suite: gli esiti dei casi `senza-file` di quei giri vanno letti come presi con
i file a disposizione, salvo dove la traccia dice il contrario.

Le opzioni, una per una:

- `--allow-tools Write Bash`: l'eval tiene `Write`, `Bash` ed `Edit` dietro
  questa concessione anche quando il caso li elenca in `allowed_tools`. Senza
  `Write` la skill non salva la bozza e la revisione separata non parte; senza
  `Bash` i `.docx` e i `.pptx` non si aprono.
- `--scaffold`: senza, i casi con un file in ingresso girano senza il file.
- `--ablation none`: la suite verifica il plugin, non quanto migliora Claude
  senza plugin; il braccio senza plugin raddoppierebbe la spesa.
- `--judge-model opus`: il giudice risponde con una parola sola, senza
  ragionare, e vede solo la griglia e la risposta, non la richiesta. Su un
  comunicato pulito sonnet ha dato FAIL tre volte su tre, opus PASS; su un
  comunicato con un dato inventato tutti e due FAIL. Opus è anche il modello
  delle sessioni figlie, e un giudice uguale al giudicato tende a essere
  indulgente: le griglie sono scritte come elenchi chiusi di fatti per
  lasciargli meno margine.
- `--case '<glob>'` (uno solo, senza graffe) o `--tag <tag>` per una parte
  sola: i casi del giro si chiamano `giro-*` e hanno il tag `giro-0.2.0`;
  quelli che leggono o scrivono Word e PowerPoint anche `bash`, quelli che
  lanciano un revisore anche `agenti`.

**Quanto costa.** Misurato il 10 ottobre 2026 con `--runs 1`: gli otto casi
di instradamento 1,94 dollari in tutto; nel giro, `00a` 0,14, `00b` 0,39,
`06` 1,99 e `17` 1,22, giudice compreso, cioè 3,74 dollari in cinque minuti
lanciando i tre filtri in parallelo. Un caso con il revisore costa fra uno e due
dollari. I casi `bash` non sono ancora stati misurati: a quel prezzo la suite
intera dovrebbe stare fra i 20 e i 25 dollari. Il default di
`claude plugin eval` è tre esecuzioni per caso, cioè il triplo. Per un tetto
rigido, `--max-cost-usd`.

**Quando Bash non parte.** Su Ubuntu con
`kernel.apparmor_restrict_unprivileged_userns = 1` la sandbox di Bash fallisce
con `bwrap: loopback: Failed RTM_NEWADDR`, e i casi con il tag `bash` non
misurano niente. Lì si eseguono gli altri (`--case`), e i casi `bash` si fanno
girare su una macchina dove la sandbox funziona.

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
