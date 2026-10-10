# Dominio generale: note per chi sviluppa

File escluso dalla build (`scripts/build.py` ignora `README-dominio.md`).

## Skill e agenti

| Nome | Ruolo |
|---|---|
| `generale-scrittura` | scrive email, lettere, comunicati, verbali (anche da trascrizione), report interni, testi web e social |
| `generale-revisione` | rivede testi dell'utente; ingresso per "rivedi questo testo" senza contesto |
| `generale-traduzione` | traduce e adatta IT/EN |
| `generale-revisore` (agente) | revisore separato: testi pubblici in `generale-scrittura`, su richiesta in `generale-revisione` |

## File duplicati

In chat una skill non legge i file di un'altra, quindi questi file sono
copiati. Le copie devono restare identiche:

| File | Copie in |
|---|---|
| `references/tipologie.md` | generale-scrittura, generale-revisione |
| `references/checklist.md` | generale-scrittura, generale-revisione |
| `references/destinatari.md` | generale-scrittura, generale-revisione, generale-traduzione |

Fonte da modificare: la copia in `generale-scrittura`. Poi:

```
cd plugin/skills
for f in tipologie checklist; do cp generale-scrittura/references/$f.md generale-revisione/references/; done
for s in generale-revisione generale-traduzione; do cp generale-scrittura/references/destinatari.md $s/references/; done
```

Controllo:

```
cd plugin/skills
for f in tipologie checklist destinatari; do for s in generale-revisione generale-traduzione; do
  [ -f $s/references/$f.md ] && diff -q generale-scrittura/references/$f.md $s/references/$f.md; done; done
```

Proposta all'hub: `build.py` copia `plugin/condivisi/[dominio]/*.md` in
`references/` di ogni skill del dominio (come fa con `nucleo/`) e
controlla che il sorgente non contenga copie. Così le duplicazioni
spariscono.

## Prompt di prova

Instradamento (la skill attesa è indicata a destra):

| Prompt | Atteso |
|---|---|
| Scrivi una email al Centro funzionale della Liguria per chiedere i dati pluviometrici di ottobre | generale-scrittura |
| Draft a letter to UNDRR proposing a joint webinar on early warning | generale-scrittura |
| Fai il verbale di questa riunione (trascrizione allegata) | generale-scrittura |
| Comunicato stampa sull'avvio del nuovo servizio di previsione | generale-scrittura (+ revisore in Cowork) |
| Post LinkedIn per annunciare il nostro workshop | generale-scrittura (+ revisore in Cowork) |
| Rivedi questo testo (email incollata) | generale-revisione |
| Rivedi questo testo (Introduction di un manuscript) | generale-revisione, che rimanda a paper |
| Migliora questa email, è troppo lunga | generale-revisione |
| Traduci in inglese questo comunicato per i partner europei | generale-traduzione |
| Traduci in inglese l'abstract del paper | generale-traduzione (struttura invariata) |
| Scrivi l'abstract per EGU | paper, non generale |
| Scrivi il deliverable D3.2 | progetti, non generale |
| Rispondi agli ESR della proposta | proposte, non generale |

Ambienti:

1. **Chat senza subagent**: comunicato stampa completo; deve arrivare il
   testo finale con la riga di autovalutazione dichiarata e il pacchetto
   revisore, senza fermarsi.
2. **Cowork**: stesso comunicato; deve salvare `revisione/bozza-comunicato.md`,
   lanciare `generale-revisore` con il solo prompt previsto e presentare
   il rapporto.
3. **Cowork, email esterna**: niente revisore, solo autorevisione.
4. **Verbale da trascrizione** con un punto ambiguo: deve comparire
   `[da verificare: …]` e nessuna scadenza dedotta.
