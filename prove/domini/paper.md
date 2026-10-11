# Dominio paper: prove e note

Prompt di prova e note di sviluppo. Fuori dal plugin: non viene distribuito.

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
- Stanno in `plugin/condivisi/paper/rivista-<editore>.md` (`adr/0004`):
  `build.py` li copia in `references/` di tutte e tre le skill `paper-*`.
  Nessuna copia nel sorgente delle skill.
- `conferenze.md` serve solo a `paper-scrittura` e resta nella skill.
- Le guide Elsevier (sciencedirect.com) e RMetS
  (rmets.onlinelibrary.wiley.com) non si lasciano leggere dagli strumenti
  di ricerca: i due profili sono stati completati il 2026-10-11 aprendo le
  guide da un browser (issue #10). Per aggiornarli si fa lo stesso.
- Aggiornare un profilo: modificare il file in `plugin/condivisi/paper/`
  e la sua data di verifica.

## Policy sull'AI generativa

Copernicus/EGU (GMD, HESS, NHESS, ESSD, ACP, WCD, verificato il
2026-10-10) vieta l'AI generativa "for text or interpretations". Le skill di scrittura e di risposta ai revisori, per
queste riviste, si limitano a interventi assistivi, controlli e schemi.
Fonte: https://www.geoscientific-model-development.net/policies/ai_policy.html
