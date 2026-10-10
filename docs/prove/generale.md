# Dominio generale: prove e note

Prompt di prova e note di sviluppo. Fuori dal plugin: non viene distribuito.

## Skill e agenti

| Nome | Ruolo |
|---|---|
| `generale-scrittura` | scrive email, lettere, comunicati, verbali (anche da trascrizione), report interni, testi web e social |
| `generale-revisione` | rivede testi dell'utente; ingresso per "rivedi questo testo" senza contesto |
| `generale-traduzione` | traduce e adatta IT/EN |
| `generale-revisore` (agente) | revisore separato: testi pubblici in `generale-scrittura`, su richiesta in `generale-revisione` |

## File condivisi

`tipologie.md`, `checklist.md` e `destinatari.md` servono a più skill del
dominio e stanno in `plugin/condivisi/generale/`. Regole in
`../scrivere-una-skill.md`, sezione "Riferimenti".

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
