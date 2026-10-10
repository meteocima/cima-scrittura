# Esempi prima/dopo: stile CIMA

Questi esempi mostrano in pratica i tre vincoli della skill:
anti-pattern AI, no invenzioni, verifica fonti.

---

## 1. Anti-pattern AI

### Trattino em (—)

❌ **Prima (pattern AI)**
> I risultati mostrano un miglioramento significativo — soprattutto
> nei bacini non strumentati — rispetto al modello precedente.

✅ **Dopo (stile CIMA)**
> I risultati mostrano un miglioramento significativo nei bacini non
> strumentati rispetto al modello precedente.

oppure, se la virgolatura rende meglio:

> I risultati mostrano un miglioramento significativo (in particolare
> nei bacini non strumentati) rispetto al modello precedente.

*Regola*: sostituire con virgola, punto e virgola, due punti o
parentesi a seconda del contesto. Non usare mai il trattino em.

---

### Apertura vuota

❌ **Prima (pattern AI)**
> Certamente! Sono felice di aiutarti a scrivere questa email. Ecco una
> bozza che potrebbe fare al caso tuo…

✅ **Dopo (stile CIMA)**
> [Bozza email, direttamente:]
> Oggetto: Risultati validazione modello CONTINUUM, bacino Arno
> …

---

### Superlativi non supportati

❌ **Prima**
> CIMA ha sviluppato una soluzione all'avanguardia e altamente innovativa
> per il monitoraggio idrologico in tempo reale.

✅ **Dopo**
> CIMA ha sviluppato DEWETRA, una piattaforma operativa per il monitoraggio
> e la previsione idrologica in tempo reale, in uso presso il Dipartimento
> della Protezione Civile dal [inserire anno].

*(Se l'anno non è fornito dall'utente, lasciare il segnaposto.)*

---

### Chiusura formulaica

❌ **Prima**
> In conclusione, emerge chiaramente che il sistema sviluppato da CIMA
> rappresenta un contributo fondamentale per la gestione del rischio
> idrologico a livello nazionale e internazionale.

✅ **Dopo**
> I risultati di validazione sul periodo [periodo] mostrano un indice
> di Nash-Sutcliffe di [valore] per i bacini analizzati, in linea con
> i benchmark definiti nel Grant Agreement.

*(Se il valore non è stato fornito, inserire `[inserire NSE]`.)*

---

### Listing compulsivo

❌ **Prima**
> I principali vantaggi dell'approccio sono:
> - Maggiore accuratezza delle previsioni
> - Migliore gestione del rischio
> - Ottimizzazione delle risorse
> - Approccio multidisciplinare integrato

✅ **Dopo**
> L'approccio consente di integrare dati satellitari e stazioni a terra
> nella stessa catena modellistica, riducendo l'incertezza previsionale
> sui bacini non strumentati.

*(Specificare solo con dati reali. Se i dati non ci sono, non scrivere
la frase.)*

---

### Vaghezza tecnica

❌ **Prima**
> CIMA adotta un approccio olistico e multidisciplinare che integra
> diverse metodologie innovative per affrontare le sfide del cambiamento
> climatico in modo sostenibile.

✅ **Dopo**
> CIMA integra modelli idrologici distribuiti (CONTINUUM), telerilevamento
> (SAR Sentinel-1) e reti di osservazione a terra per la previsione delle
> piene nei bacini alpini e appenninici.

*(Solo se queste informazioni sono state fornite o sono di dominio
pubblico verificabile.)*

---

## 2. No invenzioni: segnaposto invece di dati inventati

### Abstract con dati mancanti

❌ **Prima (dati inventati)**
> The model was validated on 15 catchments across northern Italy, achieving
> a Nash-Sutcliffe Efficiency of 0.82 on average, which is comparable to
> state-of-the-art benchmarks in the literature.

✅ **Dopo (segnaposto)**
> The model was validated on [N] catchments across [region], achieving a
> Nash-Sutcliffe Efficiency of [value] on average, [compared to / in line
> with] [reference benchmark: da fornire].

*(L'utente fornisce i numeri reali; Claude non li inventa.)*

---

### Citazione parziale

❌ **Prima**
> As shown by Smith et al. (2021), flood frequency has increased
> significantly in Mediterranean catchments over the past three decades.

*(Se Smith et al. 2021 non è stato fornito dall'utente o non è
verificabile con WebSearch, questa citazione non va inserita.)*

✅ **Dopo (verifica o segnaposto)**
> [Verificare: Smith et al. (2021). Se non trovato con WebSearch,
> sostituire con: "Studies have shown that flood frequency has increased
> in Mediterranean catchments [inserire riferimento verificato]."]

---

### Firma email con ruolo inventato

❌ **Prima**
> Dr. Mario Rossi
> Senior Researcher, Hydrological Forecasting Unit
> CIMA Research Foundation
> mario.rossi@cimafoundation.org | +39 019 123456

*(Se l'utente non ha fornito ruolo, unità o telefono, non inventarli.)*

✅ **Dopo**
> [Nome]
> [Ruolo: inserire]
> CIMA Research Foundation
> [email: inserire]

---

## 3. Verifica fonti: workflow in pratica

**Scenario**: l'utente scrive "cita il Sendai Framework nella proposta".

**Procedura corretta:**
1. Cercare con WebSearch: "Sendai Framework for Disaster Risk Reduction"
2. Verificare: Sendai Framework 2015-2030, adottato a Sendai (Giappone)
   il 18 marzo 2015, quarta conferenza mondiale UNDRR. Verificato.
3. Citare: "the Sendai Framework for Disaster Risk Reduction 2015-2030
   (UNDRR, 2015)"

**Scenario**: l'utente scrive "cita l'articolo di Berne et al. 2004
sui radar X-band".

**Procedura corretta:**
1. Cercare con WebSearch il titolo o DOI.
2. Se trovato con i dati corrispondenti: citare.
3. Se non trovato o dati discordanti: segnalare "Non ho trovato riscontro
   per 'Berne et al. 2004' su radar X-band. Puoi fornire il DOI o il titolo
   completo?"
4. Non completare la citazione con titolo o rivista inventati.
