# Matrice di tracciabilità dalla DoA

La matrice è il riferimento di ogni testo del dominio progetti: ogni
affermazione su attività, risultati e scostamenti deve potersi
ricondurre a una riga. Si costruisce una volta per progetto e si
riusa: se l'utente ne ha già una (file `matrice-doa.md` o tabella in
conversazione), usarla e chiedere solo se è aggiornata all'ultimo
amendment.

## Fonti, in ordine di precedenza

1. Grant Agreement firmato e ultimo amendment (Data Sheet, Annex 1).
2. Description of the Action (DoA, Annex 1 Part A e Part B) o, per
   Interreg, Application Form approvata.
3. Report precedenti, review report, lettere del project officer.
4. Informazioni date dall'utente in conversazione.

Una proposta non è una DoA: se l'utente fornisce la proposta e non il
GA, usarla ma dichiarare in una riga che task, deliverable e date
possono essere cambiati in fase di grant preparation o con amendment.

## Cosa estrarre

Estrarre solo ciò che il documento contiene. Mai completare a memoria
codici, mesi o lead: campo assente = `[da DoA]`.

### Intestazione

| Campo | Valore |
|---|---|
| Acronimo e numero del GA | |
| Programma e tipo di azione | |
| Durata e date (inizio, fine) | |
| Reporting period (numero, mesi) | |
| Ultimo amendment considerato | |
| Ruolo di CIMA (coordinatore, partner, WP leader di…) | |

### Work package e task

| WP | Titolo | Lead | Mesi | Task | Titolo del task | Lead del task | Mesi del task |
|---|---|---|---|---|---|---|---|

### Deliverable

| Codice | Titolo | WP | Lead | Type | Dissemination level | Mese previsto | Stato (dall'utente) |
|---|---|---|---|---|---|---|---|

### Milestone

| Codice | Titolo | WP | Mese previsto | Means of verification | Stato (dall'utente) |
|---|---|---|---|---|---|

### Obiettivi e indicatori

| Obiettivo o risultato atteso | Indicatore / KPI | Baseline | Target | Fonte del valore misurato | Valore misurato (dall'utente) |
|---|---|---|---|---|---|

### Rischi

| Rischio (dalla DoA o dal Portal) | WP | Misura di mitigazione prevista | Stato attuale (dall'utente) |
|---|---|---|---|

## Regole d'uso

- **Colonne "dall'utente"**: si riempiono solo con dati forniti
  dall'utente o dai suoi file. Le altre colonne vengono dalla DoA.
- **Aggancio nel testo**: ogni paragrafo su attività o risultati cita
  almeno un codice (T2.3, D4.1, MS5). Un'attività che non trova riga
  nella matrice è una delle due: lavoro aggiuntivo da presentare come
  tale, oppure uno scostamento da spiegare.
- **Dichiarato e dimostrato**: per ogni risultato annotare la prova
  (deliverable, dataset con DOI o link, software, pubblicazione,
  verbale, numero di partecipanti). Senza prova il risultato è
  "dichiarato" e il testo lo deve presentare come tale o chiedere la
  prova con un segnaposto.
- **Scostamenti**: confrontare mese previsto e stato. Ogni differenza
  diventa una voce nella sezione scostamenti del report.
- **Riservatezza**: la matrice contiene dati del consorzio. In modalità
  agenti salvarla nella cartella di lavoro dell'utente, mai altrove.

## Consegna della matrice

In modalità agenti: file `matrice-doa.md` nella cartella di lavoro.
In chat: tabelle nel messaggio, prima della bozza, con l'elenco dei
campi `[da DoA]` rimasti vuoti.
