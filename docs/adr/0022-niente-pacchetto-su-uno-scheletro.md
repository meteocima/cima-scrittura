# Niente pacchetto revisore su un testo fatto di segnaposto

Il protocollo voleva il pacchetto revisore in fondo a ogni consegna in
modalità chat, e dal giro 0.2.0 (rilievo 6) toglieva i punteggi quando il
testo è in gran parte segnaposto. Del pacchetto, in quel caso, non diceva
niente.

Il 2026-10-11, nelle prove in chat della issue #7, Opus ha rimandato il
pacchetto tre volte su tre proprio su testi di quel tipo (righe 5, 11 e 13:
un deliverable da template senza dati, due mazzi senza materiale), dicendo
che lo avrebbe preparato a testo pieno. Il rinvio è giusto per la stessa
ragione per cui mancano i punteggi: un revisore esterno su uno scheletro non
ha niente da giudicare, e il blocco da copiare sarebbe una cerimonia.

Quindi, in `nucleo/protocollo-revisione.md`, sezione 4b e "Testo troppo
incompleto per essere valutato": su un testo in gran parte segnaposto il
pacchetto non si prepara, e una riga dice che va chiesto quando i segnaposto
sono riempiti. In ogni altro caso resta obbligatorio, e va scritto per
intero, non offerto (`0006`).
