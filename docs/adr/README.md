# Decisioni

Una per file, con il contesto e le alternative scartate. Chi prende una
decisione nuova scrive il file e aggiunge la riga qui. Se una decisione
cambia, il file vecchio si marca superato invece di riscriverlo: `CLAUDE.md`
dice che cosa vale oggi, questi dicono come ci siamo arrivati.

| ADR | Decisione |
|---|---|
| [0001](0001-decisioni-in-docs-adr.md) | Le decisioni si registrano in `docs/adr/` |
| [0002](0002-quattro-domini-con-prefisso.md) | Quattro domini, con il prefisso nel nome |
| [0003](0003-nucleo-iniettato-a-build-time.md) | Il nucleo viene duplicato dentro ogni skill a build time |
| [0004](0004-condivisi-di-dominio.md) | Riferimenti comuni di dominio in `plugin/condivisi/<dominio>/` |
| [0005](0005-chi-scrive-non-valuta.md) | Chi scrive non valuta: la revisione sta in un contesto separato |
| [0006](0006-risultato-completo-senza-agenti.md) | Ogni skill consegna il risultato completo anche senza agenti |
| [0007](0007-skill-caricabili-singolarmente-in-chat.md) | Le skill si distribuiscono anche come zip singoli |
| [0008](0008-progetti-dominio-separato.md) | `progetti` è un dominio separato da `generale` |
| [0009](0009-confini-del-dominio-progetti.md) | Confini del dominio progetti |
| [0010](0010-generale-revisore-solo-testi-pubblici.md) | `generale-revisore` solo per i testi pubblici, e su richiesta in revisione |
| [0011](0011-una-riscrittura-e-scrittura.md) | Una riscrittura è scrittura |
| [0012](0012-traduzione-a-generale-traduzione.md) | La traduzione di qualsiasi testo va a `generale-traduzione` |
| [0013](0013-riviste-di-riferimento-paper.md) | Riviste di riferimento del dominio paper |
| [0014](0014-caratteri-vietati.md) | Trattino em e punto medio sono errori di build |
| [0015](0015-modello-dei-valutatori.md) | Modello dei valutatori (**aperta**) |
| [0016](0016-un-solo-tronco.md) | Un solo tronco: via il modello hub e dominio |
| [0017](0017-brief-sciolto.md) | `BRIEF.md` sciolto nei file che hanno la sua materia |
| [0018](0018-i-file-sono-cittadini-di-prima-classe.md) | Il plugin lavora sui documenti, non solo sul testo |
| [0019](0019-presentazioni-formato-non-dominio.md) | Le presentazioni sono un formato, non un dominio |
| [0020](0020-proposte-resta-un-dominio-separato.md) | `proposte` resta un dominio separato da `progetti` |
| [0021](0021-agenti-senza-file.md) | Senza file la revisione resta agli agenti, con i materiali nel prompt |
| [0022](0022-niente-pacchetto-su-uno-scheletro.md) | Niente pacchetto revisore su un testo fatto di segnaposto |
| [0023](0023-caricare-la-skill-prima-di-chiedere.md) | Le descrizioni dicono di caricare la skill prima di chiedere chiarimenti |
