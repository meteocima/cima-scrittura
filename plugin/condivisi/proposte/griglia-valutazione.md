# Griglia di valutazione del dominio proposte

Usata da `proposte-revisione`, dagli agenti `proposte-valutatore` e
`proposte-rapporteur`, e dall'autorevisione delle altre skill del dominio.

Questa griglia e' il **motore**: dice come si valuta. **Che cosa** si valuta,
con quali criteri, pesi e soglie, viene sempre da fuori: dalla matrice del
bando, e in subordine dal profilo del programma.

## 1. La scala non e' del plugin

Ogni programma ha la sua, e un punteggio senza la sua scala non vuol dire
niente:

| Programma | Scala | Soglie |
|---|---|---|
| Horizon Europe | 0-5 per criterio, mezzi punti | 3 per criterio, 10 su 15 |
| EIC | 0-5, con pesi per strumento, piu' passaggi a GO/NO GO | 4 / 3,5 / 3 secondo lo strumento |
| Interreg | 1-5 per domanda, con pesi x1 o x2 | per esempio 35 su 50, ma dipende dalla call |
| LIFE | 0-20 per criterio, peso 1,5 su Impact | 10 per criterio, 55 complessiva dopo la pesatura |
| UCPM | 0-40 e 0-30 per criterio, su 100 | 20 / 15 / 15 e 65 complessiva |

La scala si prende dalla matrice del bando. Se la matrice la marca
`[da bando]`, la scala non e' nota.

## 2. Quando non si danno punteggi

Due casi, e in tutti e due si scrive il rapporto lo stesso, senza numeri:

- **Non c'e' una griglia reale.** Criteri, scala o soglie non sono noti:
  nessun punteggio, e il rapporto dice quali informazioni servirebbero.
  Inventare una scala "realistica" e' il modo piu' efficace per far lavorare
  qualcuno contro un bersaglio che non esiste.
- **Il testo e' in gran parte segnaposto.** Vale la regola del nucleo
  (`protocollo-revisione.md`, sezione 5): un punteggio minimo su un testo che
  non esiste ancora sembra un giudizio e non lo e'. Si elenca che cosa serve
  perche' la valutazione abbia senso, e si segnalano lo stesso i problemi che
  si vedono gia'.

## 3. Come si assegna un punteggio

1. Leggere **tutta** la proposta prima di giudicare.
2. Elencare **prima** i problemi e i punti di forza, **poi** mettere il
   numero. Il numero viene dalle osservazioni, non le precede.
3. Ogni giudizio cita il passaggio: sezione, e frase o tabella. Un giudizio
   senza citazione non va nel rapporto.
4. Valutare la proposta **come e' scritta**, non per quello che potrebbe
   diventare: e' l'istruzione che hanno i valutatori veri. Una lacuna non
   diventa una richiesta di chiarimento, diventa un punto in meno.
5. Non raccomandare modifiche dentro il punteggio: la direzione della
   correzione sta nella colonna apposita, il punteggio riflette quello che
   c'e'.
6. Dire se la proposta e' **in ambito** rispetto al bando. Fuori ambito, anche
   in parte, pesa sul punteggio e va spiegato.
7. Applicare `anti-pattern-proposte.md` come una voce della valutazione, non
   come criterio principale.
8. Tarare il numero su `pattern-esr.md`: dice come i valutatori veri
   etichettano le debolezze e quanto costa ciascuna nel punteggio, e quali
   debolezze hanno trovato davvero nelle proposte CIMA.

## 4. Le soglie si dichiarano

Il rapporto non si ferma al punteggio: dice se la proposta **supera** o
**non supera**, criterio per criterio e complessivamente, con la scala a
fianco. Dove il programma pesa (LIFE, Interreg, EIC), il calcolo mostra il
punteggio pesato, perche' la soglia complessiva si misura su quello.

Dove il passaggio e' a GO/NO GO (EIC Transition e Accelerator), non si
inventa un numero: si da' GO o NO GO con la motivazione.

## 5. Formato del rapporto

Vale il formato comune del nucleo (`protocollo-revisione.md`, sezione 5), con
due aggiunte del dominio:

```
## Sintesi
[2-4 frasi: giudizio complessivo e problema principale]

## Ambito
[in ambito / in parte fuori ambito / fuori ambito, con il motivo]

## Punteggi
| Criterio | Punteggio | Scala | Soglia | Supera | Motivazione in una riga |

## Commenti in stile ESR
[per ciascun criterio, il commento come lo scriverebbe un valutatore:
prima quello che funziona, poi le debolezze, ciascuna con il passaggio]

## Problemi
| # | Posizione | Citazione | Problema | Gravita' | Direzione della correzione |

## Punti di forza
## Cosa manca
```

I commenti in stile ESR si scrivono nella lingua dell'utente, salvo richiesta
diversa; se l'utente chiede l'inglese, si scrivono come arriverebbero dalla
Commissione.

## 6. Divergenze

Il rapporteur **non fa la media**. Riporta come divergenza:

- una differenza **maggiore di un punto** sulla scala in uso, normalizzata
  alla scala del programma (su 0-20 di LIFE, un punto di Horizon Europe vale
  quattro: la soglia si traduce, non si copia);
- due giudizi opposti sullo stesso passaggio, anche a pari punteggio;
- un problema giudicato bloccante da un valutatore e non nominato dagli altri.

Ogni divergenza porta le posizioni di tutti, con il passaggio citato da
ciascuno. Una divergenza e' un segnale: dice che quel punto si legge in due
modi, e in valutazione vera capitera' lo stesso.

## 7. Che cosa il valutatore non fa

- Non riscrive il testo.
- Non ammorbidisce: il rapporto serve a chi scrive, non va a terzi.
- Non stima la probabilita' di finanziamento, e non dice "sarebbe finanziata":
  dice se supera le soglie, che e' un'altra cosa.
- Non vede la conversazione in cui la proposta e' nata, e non chiede di
  vederla.
