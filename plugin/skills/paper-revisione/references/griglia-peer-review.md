# Griglia di revisione

Scala per criterio, da 1 a 5. Il punteggio si assegna **dopo** aver
elencato problemi e punti di forza, e ogni punteggio cita almeno un
passaggio del manoscritto.

| Punteggio | Significato |
|---|---|
| 5 | Nessun problema rilevante; al più ritocchi formali. |
| 4 | Problemi minori, correggibili senza nuove analisi. |
| 3 | Problemi importanti: servono chiarimenti sostanziali o analisi aggiuntive limitate. |
| 2 | Problemi gravi: servono nuove analisi o una riformulazione delle conclusioni. |
| 1 | Problema bloccante: il criterio non è soddisfatto e non si risolve con una revisione. |

## Criteri

1. **Domanda e contributo**: domanda chiara, lacuna specifica, contributo
   rispetto ai lavori citati.
2. **Metodi**: adatti alla domanda, descritti in modo riproducibile.
3. **Dati**: adeguati, indipendenti dove serve, fonti e versioni
   indicate.
4. **Risultati**: mostrati con incertezza, confrontati con un
   riferimento, coerenti con i metodi.
5. **Conclusioni**: sostenute dai risultati, senza estensioni oltre il
   campione o l'area.
6. **Letteratura**: pertinente, aggiornata, citata correttamente.
7. **Chiarezza**: struttura, lingua, figure e tabelle leggibili e
   necessarie, didascalie autonome.
8. **Riproducibilità e apertura**: disponibilità di dati e codice
   secondo la rivista.
9. **Adeguatezza alla rivista**: ambito, tipo di articolo, lettori.

Ogni revisore valuta tutti i criteri; può scrivere "fuori dal mio
profilo" per un criterio, con una riga di motivo, invece del punteggio.

## Dalla griglia alla raccomandazione

Orientamento, non regola automatica. I criteri segnati "fuori dal mio
profilo" non contano. Applicare la prima riga che corrisponde:

| Condizione | Raccomandazione di norma |
|---|---|
| almeno un criterio a 1 | reject |
| almeno un criterio a 2 | major revision |
| un 3 su un criterio tra 2 e 5 (metodi, dati, risultati, conclusioni) | major revision |
| tre o più criteri a 3 | major revision |
| uno o due 3 sui criteri 1, 6, 7, 8 o 9, gli altri a 4 o 5 | minor revision |
| tutti a 4 o 5 | minor revision, o accept se i 4 riguardano solo aspetti formali |

Il revisore può discostarsi motivandolo in una riga.

## Divergenze

Per l'editor: c'è divergenza quando due revisori differiscono di più di
1 punto sullo stesso criterio, o danno giudizi opposti sullo stesso
passaggio. Riportare entrambe le posizioni con le citazioni, senza fare
la media.

## Anti-pattern AI

Applicare `anti-pattern-ai.md` come voce del criterio 7 (Chiarezza),
non come criterio a sé: segnalare i pattern con la citazione come
problema di chiarezza, senza fare ipotesi su chi o cosa ha scritto il
testo.
