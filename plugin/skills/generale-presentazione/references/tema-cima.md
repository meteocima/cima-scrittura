# Tema CIMA per le presentazioni

Il template vero è `references/tema-cima.pptx`, nella stessa cartella. Questo
file dice come è fatto e come si usa. Il mazzo si costruisce **copiando il
template**, non ricostruendolo: l'identità CIMA non sta nello schema colori del
file, che è quello standard di Office, ma nei layout, nelle immagini di sfondo
e nel carattere che ogni forma impone sopra il tema.

Formato: 16:9, 13,333 x 7,5 pollici.

## Palette

| Colore | Codice | Dove |
|---|---|---|
| Blu notte | `1F3A66` | sfondi scuri, titoli sulle slide chiare, etichetta BACKUP |
| Arancio | `E87722` | sottotitoli e concetti chiave, indirizzo del sito, accenti |
| Quasi nero | `1A1A1A` | testo corrente |
| Azzurro chiaro | `B9C9DE` | testo secondario sulle slide scure, filetti |
| Grigio | `5A6675` | intestazione corrente, testo di servizio |
| Bianco | `FFFFFF` | testo sulle slide scure, fondo delle slide di contenuto |

Carattere: **Open Sans**, in tutte le forme. Lo schema del tema dice Calibri e
va ignorato: ogni forma lo sovrascrive. Se Open Sans manca sulla macchina che
apre il file, PowerPoint sostituisce da solo e il mazzo resta leggibile.

## I cinque layout

| Layout | Segnaposto | Fondo | Per |
|---|---|---|---|
| `CIMA_TITLE` | titolo `101`, sottotitolo `102` | scuro con texture di mappa, logo grande | la prima slide |
| `CIMA_SECTION` | titolo `101` | scuro, logo piccolo in alto a sinistra | aprire una sezione |
| `CIMA_CONTENT` | titolo `104`, corpo `105` | bianco | la slide normale |
| `CIMA_CONTENT_2COL` | titolo `104`, corpo `105`, corpo `106` | bianco | confronti, testo accanto a una figura |
| `CIMA_BACKUP` | titolo `106`, corpo `107` | bianco, etichetta BACKUP | appendice per le domande |

C'è anche un layout `DEFAULT` senza segnaposto: non usarlo.

Nel template ogni layout ha **una slide di esempio già pronta**: slide 1 titolo,
slide 2 sezione, slide 3 contenuto, slide 4 due colonne, slide 5 backup. Sono
le impalcature da duplicare.

## Che cosa si scrive dove

La distinzione che conta:

- **Nei segnaposto della slide** va il contenuto che cambia da slide a slide:
  titolo e corpo.
- **Nelle forme fisse del layout** vanno le costanti del mazzo, che compaiono
  su tutte le slide di quel layout: la riga degli autori e la riga
  dell'occasione sul layout titolo, l'intestazione corrente sui layout di
  contenuto. Non sono modificabili dalla singola slide.

Quindi le costanti si impostano **una volta sola per mazzo**, modificando i
layout dentro la copia del template. Siccome ogni mazzo è una copia a sé,
modificarne i layout non tocca niente altro.

| Dove | Testo di partenza | Che cosa metterci |
|---|---|---|
| `CIMA_TITLE`, forma autori | tre nomi di esempio | gli autori veri, separati da virgola |
| `CIMA_TITLE`, riga occasione | ente, evento, sessione, data | gli estremi veri dell'occasione |
| `CIMA_CONTENT` e simili, intestazione in alto a sinistra | titolo e sottotitolo di esempio | titolo breve del mazzo |
| ovunque | `www.cimafoundation.org`, icone social | lasciare come sono |

## Separatori

Il template usa due separatori che il nucleo vieta. Vanno trattati così:

- **Punto medio**: mai, da nessuna parte, nemmeno dove il segnaposto del
  template lo suggerisce (riga degli autori, intestazione corrente). Separare
  gli autori con la virgola e l'intestazione con la barra verticale, che è già
  il separatore usato nella riga dell'occasione.
- **Trattino lungo**: ammesso solo dove lo mette il template, cioè nella riga
  dell'occasione sulla slide titolo e nella numerazione delle slide di sezione
  (`1`, trattino lungo, `Introduzione`). In tutto il resto del mazzo, titoli e
  testo compresi, vale il divieto del nucleo.

## Procedura

1. Copiare `references/tema-cima.pptx` nel file del mazzo. Mai modificare il
   template in posto.
2. Scompattare la copia e impostare le costanti nei layout: autori, occasione,
   intestazione corrente.
3. Per ogni slide del mazzo, duplicare la slide di esempio del layout giusto e
   riempirne i segnaposto. La skill `pptx` ha `scripts/add_slide.py`, che
   duplica una slide con tutta la contabilità del pacchetto.
4. Eliminare le slide di esempio rimaste inutilizzate, poi passare
   `scripts/clean.py` per togliere media e relazioni non più riferiti.

   Attenzione al numero di righe: duplicando una slide di esempio si eredita
   il suo numero di paragrafi nel corpo (il layout di contenuto ne ha quattro:
   il concetto chiave e tre punti). Scrivere più righe di quelle non aggiunge
   paragrafi, le righe in più si perdono in silenzio. Per averne di più o di
   meno si duplica o si toglie il paragrafo nel corpo del segnaposto, non si
   aggiunge una casella di testo sopra il layout.
5. Ricompattare e verificare con `scripts/office/validate.py`, passando il
   template come `--original`: senza quel confronto gli errori propri del
   template vengono letti come errori del mazzo.

Nel corpo dei layout di contenuto il **primo paragrafo è il concetto chiave**,
in arancio e in grassetto, e non porta il punto elenco: è una riga che dice
che cosa sostiene la slide. I punti elenco cominciano dal secondo paragrafo.

Immagini e grafici nuovi si compongono sopra il layout, nei colori della
palette. Un grafico va inserito come grafico, non come immagine di un grafico,
così resta modificabile.
