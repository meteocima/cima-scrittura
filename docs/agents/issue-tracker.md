# Issue tracker: GitHub

Le issue e le specifiche di questo repository vivono come issue GitHub su
`meteocima/cima-scrittura`. Tutte le operazioni passano dalla CLI `gh`, che
deduce il repository dal remoto quando viene eseguita dentro il clone.

## Convenzioni

- **Creare**: `gh issue create --title "..." --body "..."`. Per corpi su più
  righe usare un heredoc.
- **Leggere**: `gh issue view <numero> --comments`.
- **Elencare**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`, con i filtri `--label` e `--state` che servono.
- **Commentare**: `gh issue comment <numero> --body "..."`
- **Etichettare**: `gh issue edit <numero> --add-label "..."` oppure `--remove-label "..."`
- **Chiudere**: `gh issue close <numero> --comment "..."`

Titoli e corpi in italiano, come il resto del repository. Restano in inglese i
comandi, i nomi delle etichette e i termini tecnici che `CONTEXT.md` tiene in
inglese.

## Le pull request come superficie di triage

**PR come canale di richieste: no.** _(Mettere `sì` se questo repository
tratta le pull request esterne come richieste di funzionalità; `/triage` legge
questo valore.)_

Quando è `sì`, le PR passano per le stesse etichette e gli stessi stati delle
issue, con gli equivalenti `gh pr`. GitHub condivide la numerazione fra issue e
PR, quindi un `#42` può essere entrambe: si risolve con `gh pr view 42` e si
ripiega su `gh issue view 42`.

## Quando una skill dice "pubblica sull'issue tracker"

Crea una issue GitHub.

## Quando una skill dice "recupera il ticket"

Esegui `gh issue view <numero> --comments`.

## Operazioni di wayfinding

Usate da `/wayfinder`. La **mappa** è una singola issue con le issue **figlie**
come ticket.

- **Mappa**: una issue con etichetta `wayfinder:map`, che contiene Note,
  Decisioni prese e Nebbia. `gh issue create --label wayfinder:map`.
- **Ticket figlio**: una issue collegata alla mappa come sub-issue GitHub
  (`gh api` sull'endpoint delle sub-issue). Dove le sub-issue non sono
  abilitate, aggiungere il figlio a una task list nel corpo della mappa e
  mettere `Part of #<mappa>` in cima al corpo del figlio. Etichette:
  `wayfinder:<tipo>` (`research`, `prototype`, `grilling`, `task`).
- **Dipendenze**: le **issue dependencies** native di GitHub, che sono la
  rappresentazione canonica e visibile nell'interfaccia. Si aggiunge un arco
  con `gh api --method POST repos/<owner>/<repo>/issues/<figlio>/dependencies/blocked_by -F issue_id=<id-del-bloccante>`,
  dove l'id è il **database id** numerico (`gh api repos/<owner>/<repo>/issues/<n> --jq .id`,
  non il `#numero` né il `node_id`). Dove le dipendenze non sono disponibili,
  ripiegare su una riga `Blocked by: #<n>, #<n>` in cima al corpo. Un ticket è
  sbloccato quando ogni bloccante è chiuso.
- **Frontiera**: elencare le figlie aperte della mappa, togliere quelle con un
  bloccante aperto o con un assegnatario; vince la prima nell'ordine della
  mappa.
- **Prendere in carico**: `gh issue edit <n> --add-assignee @me`.
- **Risolvere**: `gh issue comment <n> --body "<risposta>"`, poi
  `gh issue close <n>`, poi aggiungere un rimando alle Decisioni prese della
  mappa.
