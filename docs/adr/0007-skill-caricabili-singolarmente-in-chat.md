# Le skill si distribuiscono anche come zip singoli

Il formato plugin funziona in Cowork, ma gran parte di CIMA scrive in
chat, dove si carica una skill alla volta. Il rilascio produce quindi due
cose dalla stessa sorgente: `dist/cima-scrittura.plugin` per Cowork e
`dist/skills/<nome>.zip` per il caricamento singolo.

È questa doppia distribuzione a imporre la duplicazione del nucleo
(ADR 0003): uno zip deve essere autosufficiente.

Confermato dall'utente il 2026-10-10. Da verificare in pratica al primo
rilascio: se le skill non comparissero in chat per l'organizzazione, la
distribuzione andrebbe ripensata, non il nucleo.
