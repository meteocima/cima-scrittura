# CIMA Writing Style Plugin

Plugin di scrittura condiviso per il gruppo CimaMeteoIdro.

## Cosa fa

Quando installi questo plugin, Claude conosce la voce ufficiale di
CIMA Research Foundation e la applica ogni volta che scrivi o revisioni
un testo — email, abstract, deliverable UE, comunicati, proposte.

Funziona **in italiano e in inglese** e rileva automaticamente la lingua
dalla richiesta.

## Tre vincoli fondamentali

1. **Niente invenzioni**: Claude non inventa dati, nomi, risultati o fonti.
   Dove mancano informazioni, inserisce segnaposto espliciti (`[da inserire]`)
   e te lo segnala.

2. **Verifica delle fonti**: Ogni riferimento bibliografico o normativo viene
   verificato con una ricerca web prima di essere inserito nel testo. Se non
   è verificabile, Claude te lo dice e non lo include.

3. **Anti-pattern AI**: Il testo viene controllato prima della consegna per
   eliminare i pattern tipici della scrittura generativa (aperture vuote,
   superlativi non supportati, listing compulsivo, vaghezze tecniche).

## Come usarla

Chiedi a Claude di scrivere o rivedere qualsiasi testo per CIMA:

- "Scrivi una email al DPC sul progetto X"
- "Draft an abstract for the paper on flood forecasting"
- "Rivedi questo paragrafo del report"
- "Prepara un comunicato stampa sui risultati del progetto Y"

Claude applica automaticamente lo stile CIMA nella lingua corretta.

## Struttura della skill

```
skills/writing-style/
├── SKILL.md                        # Istruzioni principali
└── references/
    ├── terminology.md              # Terminologia preferita IT/EN
    ├── audience-tones.md           # Tono per DPC, UE, stampa, ecc.
    └── good-bad-examples.md        # Esempi prima/dopo
```

## Personalizzazione individuale

Ogni membro del gruppo può salvare le proprie preferenze personali sopra
lo stile condiviso. Dopo ogni bozza, Claude offre in una riga di farlo.
Lo stile di gruppo rimane la base; le preferenze individuali lo affinano.

## Installazione

Aprire il file `.plugin` nel desktop app di Claude e premere il pulsante
di installazione. La skill sarà disponibile in tutte le sessioni.

---

*Versione 0.1.0 — CimaMeteoIdro*
