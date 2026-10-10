# Documenti di dominio

Come le skill di engineering devono leggere la documentazione di dominio di
questo repository prima di esplorarlo.

## Da leggere prima di esplorare

- **`CONTEXT.md`** alla radice: il glossario del repository. Dominio, nucleo,
  revisione, modalità, segnaposto e gli altri termini che qui hanno un
  significato preciso.
- **`docs/adr/`**: le decisioni che toccano l'area su cui si sta per lavorare.
  L'indice è `docs/adr/README.md`.

Attenzione a non confondere `CONTEXT.md` con `nucleo/terminologia.md`: il primo
è il vocabolario di chi sviluppa il plugin, il secondo è la terminologia dei
testi che il plugin produce e viaggia dentro le skill.

Se uno di questi file non esistesse, **procedere in silenzio**: non segnalarne
l'assenza e non proporre di crearli in anticipo. `/domain-modeling` li crea
quando un termine o una decisione si risolve davvero.

## Disposizione

Contesto unico, che è la forma di quasi tutti i repository:

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── README.md
│   ├── 0001-decisioni-in-docs-adr.md
│   └── ...
├── nucleo/
└── plugin/
```

## Usare il vocabolario del glossario

Quando un risultato nomina un concetto del dominio, in un titolo di issue, in
una proposta di modifica, in una ipotesi, si usa il termine come lo definisce
`CONTEXT.md`. Niente sinonimi che il glossario elenca sotto "Evitare": dire
"mazzo" e non "pacchetto di slide", "modalità agenti" e non "Cowork".

Se il concetto che serve non è ancora nel glossario, è un segnale: o si sta
inventando un linguaggio che il progetto non usa, e allora conviene fermarsi,
oppure c'è un buco vero, e allora va annotato per `/domain-modeling`.

## Segnalare i conflitti con un ADR

Se un risultato contraddice un ADR esistente, dirlo invece di scavalcarlo in
silenzio:

> _Contraddice l'ADR 0019 (le presentazioni sono un formato, non un dominio),
> ma vale la pena riaprirlo perché…_

Vale anche al contrario: un ADR superato dai fatti si marca superato, non si
riscrive. Lo dice `docs/adr/README.md`.
