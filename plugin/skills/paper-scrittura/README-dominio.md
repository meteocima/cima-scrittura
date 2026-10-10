# Dominio paper: note per chi mantiene il plugin

Questo file non entra nel plugin costruito (`build.py` lo esclude).

## Componenti

| Tipo | Nome | Ruolo |
|---|---|---|
| Skill | `paper-scrittura` | sezioni, abstract (rivista e conferenza), cover letter, dichiarazioni |
| Skill | `paper-revisione` | peer review simulata: revisori A, B (C) + editor |
| Skill | `paper-risposta-revisori` | piano delle modifiche, lettera di risposta, controllo di coerenza |
| Agente | `paper-revisore` | revisore parametrizzato per profilo (cyan) |
| Agente | `paper-editor` | sintesi, conformità, decisione (cyan) |

Livello di revisione: standard.

## Profili delle riviste

- Editori: Elsevier, Nature Portfolio, Copernicus/EGU, AGU, AMS,
  RMetS/Wiley. Conferenze: EGU, AGU, AMS, Plinius.
- Costruiti il 2026-10-10 da pagine ufficiali con ricerca web.
- Stanno in `plugin/condivisi/paper/rivista-<editore>.md` (brief v5,
  decisione 5): `build.py` li copia in `references/` di tutte e tre le
  skill `paper-*`. Nessuna copia nel sorgente delle skill.
- `conferenze.md` serve solo a `paper-scrittura` e resta nella skill.
- Lacune note: le guide delle singole riviste Elsevier (sciencedirect.com)
  e RMetS (rmets.onlinelibrary.wiley.com) non erano leggibili dagli
  strumenti di ricerca; quei profili hanno molte voci `[da verificare]`.
  Si completano aprendo le guide da un browser o incollandone il testo.
- Aggiornare un profilo: modificare il file in `plugin/condivisi/paper/`
  e la sua data di verifica.

## Policy sull'AI generativa

Copernicus/EGU (GMD, HESS, NHESS, ESSD, ACP, WCD, verificato il
2026-10-10) vieta l'AI generativa "for text or interpretations". Le skill di scrittura e di risposta ai revisori, per
queste riviste, si limitano a interventi assistivi, controlli e schemi.
Fonte: https://www.geoscientific-model-development.net/policies/ai_policy.html
