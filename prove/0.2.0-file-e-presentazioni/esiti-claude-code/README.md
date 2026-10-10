# Giro Claude Code, 10 ottobre 2026

Cartella separata da `esiti-agenti/`, che contiene il giro eseguito in Cowork:
i due ambienti vanno confrontati, non mescolati.

Questo giro è diverso anche nel metodo. In Cowork le prove le ha eseguite una
sessione che aveva letto gli esiti attesi, e lo ha dichiarato come limite. Qui
sono state eseguite da `claude plugin eval`, che lancia una sessione figlia
**che non ha letto né le prove né gli esiti attesi**, carica il plugin da un
percorso e misura con grader separati. L'attivazione della skill è quindi una
misura, non una scelta di chi sapeva.

La suite sta in `prove/evals/`. Si esegue così:

```
python3 scripts/build.py
cp -r dist/cima-scrittura /tmp/evalrun && cp -r prove/evals /tmp/evalrun/evals
cd /tmp/evalrun && claude plugin eval . --runs 1 --trust-plugin --keep-temp
```

Gli esiti costano: circa un dollaro per esecuzione di un caso.

## Che cosa è stato misurato

Un solo caso finora, equivalente alla riga 17 (comunicato stampa in modalità
agenti). Le altre righe non sono state convertite in casi.

| Grader | Esito | Misura |
|---|---|---|
| `skill-attivata` | **passa** | `Skill` invocato 1 volta: `generale-scrittura` si attiva da sola, senza che nessuno la nomini |
| `revisore-agent` | **passa** | `Agent` invocato 3 volte, una delle quali su `cima-scrittura:generale-revisore` |
| `revisore-task` | fallisce | `Task` invocato 0 volte: in questo ambiente lo strumento si chiama `Agent`, non `Task`. Non è un difetto del plugin |
| `contenuto` | fallisce | grader sbagliato, corretto dopo: trattava come invenzione i dati verificati di `identita-cima.md` |
| `consegna` | **fallisce davvero** | vedi sotto |

## Risposte alle due domande aperte

**Gli agenti vengono usati?** Sì, in tutti e due gli ambienti. In Claude Code
la sessione figlia ha invocato `generale-revisore` del plugin; in Cowork sono
stati lanciati i revisori di `progetti` e il revisore dei mazzi. Lo strumento
però si chiama `Agent` qui e `Task` altrove: chi scrive un grader sugli agenti
deve prevedere entrambi i nomi.

**I due ambienti danno lo stesso risultato?** Sulle righe confrontabili sì,
con una differenza di comportamento sotto stress, descritta qui sotto.

## Difetti trovati da questo giro

1. **Trattino lungo come riempitivo di cella.** Nella tabella dei problemi del
   rapporto, una cella vuota è stata riempita con il trattino lungo. Il
   divieto del nucleo c'è, ma in una tabella quel segno non sembra
   punteggiatura. Corretto in `anti-pattern-ai.md`, che ora vieta anche quell'uso
   e indica di lasciare la cella vuota o scrivere "n.a.".

2. **Il revisore usato come scrivano.** Senza il permesso di scrivere file, la
   skill ha provato tre volte a far salvare la bozza da un agente, e al terzo
   tentativo ha lanciato `generale-revisore` con un prompt che diceva
   "Compito preliminare, NON una revisione: usa il tool Write per creare il
   file". Il revisore ha `Write` solo per il proprio rapporto: usarlo come
   scrivano svuota la separazione che `adr/0005` esiste per garantire. La
   skill dovrebbe passare alla modalità chat quando non riesce a salvare la
   bozza, non arruolare il revisore.
   Da notare che alla fine il ripiego è avvenuto, e correttamente: "non sono
   riuscito a lanciare il revisore separato, ho fatto la revisione qui".

3. **Limite del banco di prova, non del plugin.** `claude plugin eval` tiene
   `Write` dietro `--allow-tools` anche quando il caso lo elenca fra gli
   strumenti ammessi. Il percorso con gli agenti va riprovato con
   `--allow-tools Write` per misurarlo in condizioni normali.

## Che cosa è andato bene

Il testo prodotto ha 24 segnaposto e nessun dato inventato, elenca i
segnaposto in fondo, dichiara l'autovalutazione con la riga prevista dal
protocollo, offre il pacchetto revisore e chiude con le assunzioni. La
descrizione istituzionale di CIMA nelle note ai redattori viene da
`identita-cima.md`, cioè i dati verificati sono stati usati come previsto.
