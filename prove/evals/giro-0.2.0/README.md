# Giro 0.2.0 come casi eval

Le righe di `prove/0.2.0-file-e-presentazioni/README.md` convertite in casi
per `claude plugin eval`. Il numero del caso è il numero della riga. Come si
esegue la suite: `prove/README.md`, sezione "La suite automatica".

I casi misurano l'esito atteso **di oggi**, cioè quello della riga corretto
dai rilievi chiusi dopo il giro (tabella "Correzioni applicate"): la riga 14
ora si aspetta la domanda sul paper mancante, non un mazzo di segnaposto.

## Righe convertite

| Riga | Caso | Che cosa misura | Serve |
|---|---|---|---|
| 0a | `00a-plugin-presente` | dieci skill e cinque agenti, con i nomi giusti | |
| 0b | `00b-email-cf-liguria` | `generale-scrittura` da sola, nessun revisore, segnaposto | |
| 1 | `01-rivedi-lettera` | rapporto nel messaggio, nessuna riscrittura | Bash |
| 2 | `02-migliora-lettera` | `generale-revisore` lanciato, lettera senza anti-pattern, formato | Bash, Write |
| 4 | `04-template-deliverable` | sezioni del template conservate, niente "WP3" dedotto, niente punteggi su uno scheletro | Bash, Write |
| 6 | `06-review-report` | tabella con C1-C4 e R1-R2 in `revisione/risposta.md`, `progetti-revisore` lanciato con la griglia | Write |
| 7 | `07-controlla-deliverable` | due `progetti-revisore`, sintesi, difetti della bozza trovati | Bash, Write |
| 10 | `10-slide-review` | una domanda sul materiale mancante, oppure mazzo con ipotesi dichiarate | Bash, Write |
| 12 | `12-slide-regione` | `generale-revisore-presentazione` lanciato, rapporto all'utente, formato | Bash, Write |
| 14 | `14-slide-egu` | domanda sul paper, oppure mazzo da dieci minuti con avvertenza | Bash, Write |
| 15 | `15-traduci-slide` | traduzione dentro il `.pptx`, struttura conservata | Bash, Write |
| 17 | `17-comunicato-agenti` | `generale-revisore` lanciato, nessun dato inventato, forma della consegna | Write |

I grader sugli agenti cercano nella traccia `"name":"(Agent|Task)"` insieme al
`subagent_type` atteso: lo strumento si chiama `Agent` in Claude Code e `Task`
altrove, e `tool_used` accetta un nome solo.

Tre scarti dalla riga, voluti:

- il prompt del 17 dice più della riga ("valle del Magra", "15 novembre"),
  perché viene dal primo caso eval, già misurato con quel testo;
- il 15 traduce il mazzo prodotto dalla riga 10 in Cowork
  (`esiti-agenti/prova-10/`), come dice il README dei materiali: se quella
  cartella cambia, cambia anche l'ingresso del caso;
- il 6 non misura "non copia frasi del report in ricerche web": la sessione
  figlia non ha strumenti web, quindi il controllo passerebbe sempre.

## Righe non convertite

**Le righe chat (3, 5, 8, 11, 13, 16).** `claude plugin eval` dà sempre lo
strumento `Agent` alla sessione figlia, anche quando `allowed_tools` non lo
elenca: è fra gli strumenti di sola lettura che concede comunque. La skill
vede quindi la modalità agenti e la modalità chat non si può provocare. Si
provano come dice `CLAUDE.md`, in una chat singola con lo zip della skill.

**La riga 9.** Chiede di rifiutare tutte le revisioni tracciate del `.docx`
restituito e confrontare il testo con l'originale. Un grader non legge il
contenuto di un `.docx` (è un archivio compresso) e il confronto andrebbe
fatto dopo la corsa. Si potrebbe far giudicare a un grader quello che la
sessione dice di aver fatto, ma la riga esiste proprio per non fidarsi di
quel racconto: resta una prova a mano.

## Che cosa cambia rispetto a Cowork

Nella sessione figlia le skill `docx` e `pptx` non ci sono: è caricato solo il
plugin sotto prova. Per i file Word e PowerPoint vale quindi la regola di
`nucleo/formati-e-file.md` sezione 3: o il file arriva lo stesso, o il
contenuto arriva in Markdown con una riga che dice perché. I grader del
formato accettano tutte e due le strade; lo scarto dal comportamento in
Cowork è voluto, non un difetto del plugin.

Read non apre i `.docx` e i `.pptx`: per leggerli la sessione figlia ha
bisogno di Bash. I casi marcati `bash` girano solo dove la sandbox di Bash
funziona (vedi `prove/README.md`).

## Prima misura, 10 ottobre 2026

Eseguiti qui i quattro casi che non hanno bisogno di Bash (`00a`, `00b`, `06`,
`17`), una corsa ciascuno, giudice opus: passano tutti i grader. In `06` i due
`progetti-revisore` ricevono la griglia, e in una delle corse di taratura
hanno rifiutato di dare punteggi su un testo fatto di segnaposto: i rilievi 2
e 6 del giro reggono.

Il comunicato (`17`) ha fatto sei corse durante la taratura dei grader, e
in due il giudice ha trovato dati davvero non forniti: "Savona"
come luogo di diffusione, scritto come fatto mentre la revisione stessa diceva
che andava concordato; e "il Magra scorre tra Liguria e Toscana" con gli
affluenti dati per coperti dal servizio. È il caso da guardare con
`--runs 3`.

I casi `bash` non sono stati eseguiti: su questa macchina la sandbox di Bash
non parte (vedi `prove/README.md`).
