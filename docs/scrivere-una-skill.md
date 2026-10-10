# Scrivere o modificare una skill

Si legge quando si crea una skill o un agente, non prima. Le regole che
`scripts/build.py` fa rispettare da solo sono segnate con **[build]**: se le
violi la build si ferma e ti dice dove.

## Nomi

- Skill e agenti in kebab-case con il prefisso del dominio **[build]**:
  `generale-scrittura`, `paper-revisione`, `proposte-valutatore`.
- `name` nel frontmatter uguale al nome della cartella o del file **[build]**.
- Istruzioni in **italiano**, imperative, rivolte a Claude. Esempi e frammenti
  del testo prodotto nella lingua di quel testo.

## SKILL.md

Frontmatter: `name` e `description`. La descrizione è in italiano, terza
persona, sotto i 1024 caratteri **[build]** e in pratica intorno ai 900;
contiene frasi d'innesco in italiano e in inglese e una clausola
**"Non usare per…"** che rimanda alle skill degli altri domini, coerente con
`instradamento.md`. Niente parentesi angolari **[build]**.

Corpo sotto le 3.000 parole (oltre, la build avvisa): il resto va in
`references/`.

Prima sezione obbligatoria, identica in tutte le skill che producono o
rivedono testo:

```markdown
## Prima di tutto
Leggere `references/nucleo/vincoli.md` e `references/nucleo/anti-pattern-ai.md`.
Prima di citare fonti: `references/nucleo/verifica-fonti.md`.
Per voce e convenzioni di lingua: `references/nucleo/voce-e-lingua.md`
e `references/nucleo/terminologia.md`.
Per la revisione: `references/nucleo/protocollo-revisione.md`.
```

Poi, dove servono:

- `## Deroghe allo stile di base`: ogni scostamento da `voce-e-lingua.md` che
  il formato impone (IMRAD, template di deliverable, elenchi in un verbale).
  Fuori da questa sezione la deroga non esiste.
- `## Modalità chat`: obbligatoria **[build]** in ogni skill che nomina un
  agente del plugin. Dice passaggio per passaggio come la skill svolge da sola
  il lavoro di quell'agente, con lo stesso formato di output, dichiarando in
  una riga che non è indipendente.

Ogni file `references/…` citato nel corpo deve esistere **[build]**.

Mai il trattino em, nemmeno nelle istruzioni **[build]**: il modello imita gli
esempi che ha sotto gli occhi. Il perché sta in `adr/0014`.

## Riferimenti: dove mettere un file

Tre posti, in ordine di ampiezza:

| Serve a | Va in | Lo cita come |
|---|---|---|
| ogni skill di ogni dominio | `nucleo/` | `references/nucleo/<file>.md` |
| più skill dello stesso dominio | `plugin/condivisi/<dominio>/` | `references/<file>.md` |
| una skill sola | `plugin/skills/<skill>/references/` | `references/<file>.md` |

I primi due li copia la build dentro ogni skill interessata, sottocartelle
comprese. Nel sorgente la skill non deve contenerne copie **[build]**: si
modifica l'originale. `nucleo/` è un nome riservato dentro `condivisi/`
**[build]**.

## Agenti

Frontmatter: `name`, `description` con blocchi `<example>` **[build]**,
`model`, `color` **[build]**, `tools`.

- Colori: valutatori `cyan`, scrittori `magenta`.
- Strumenti minimi. Un valutatore ha `Read`, `Glob`, `Grep`, `Write` per il
  rapporto, più `WebSearch` se il dominio lo prevede. Mai strumenti che gli
  permettano di modificare il testo che valuta.
- `model: inherit` finché `adr/0015` resta aperto.
- **L'agente non conosce i percorsi delle skill.** Glieli passa nel prompt la
  skill che lo lancia, assoluti, a partire dalla propria cartella base. Il
  prompt segue `nucleo/protocollo-revisione.md`, sezione "Cosa passare al
  revisore": solo testo, criteri e formato, mai la conversazione.

## Output della skill

- Testi lunghi: in modalità agenti un file `.md` o `.docx` nella cartella di
  lavoro; in chat nel messaggio, una sezione alla volta.
- Segnaposto `[…]` per ogni dato mancante, elencati in fondo alla consegna.
- Il testo da inviare non contiene mai frasi rivolte all'utente.

## Prima di considerarla finita

1. `python3 scripts/build.py --check`.
2. I prompt di prova in `docs/prove/<dominio>.md`, nei due ambienti:
   chat senza subagent (deve consegnare tutto) e con gli agenti (deve
   lanciarli).
