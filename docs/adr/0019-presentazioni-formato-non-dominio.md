# Le presentazioni sono un formato, non un dominio

Le slide servono a tutti i domini: il talk di conferenza nasce da un paper, la
presentazione di review nasce da un progetto, il pitch nasce da una proposta,
la giornata pubblica è testo istituzionale. La tentazione era un quinto dominio
`presentazioni-`, con scrittura e revisione proprie.

Sarebbe stato un dominio vuoto. I criteri di qualità del contenuto non sono
delle slide: sono del dominio che possiede quel contenuto, e li hanno già le
sue skill. Quello che le slide hanno in proprio è il mestiere del mazzo (quante
slide per quanti minuti, una idea per slide, titoli che affermano) e il tema
CIMA, e quelli non cambiano da un dominio all'altro. Tre skill per dominio
avrebbero divergito in tre modi sulla stessa impaginazione.

Quindi una skill sola, `generale-presentazione`, che costruisce il mazzo e
rimanda alla skill del dominio per i criteri di contenuto. È la stessa forma
della traduzione (`adr/0012`): un mestiere trasversale sta in un posto e non
invade i domini.

La revisione ha invece un agente suo, `generale-revisore-presentazione`, e non
riusa `generale-revisore`: un mazzo si giudica su cose che un revisore di testi
non guarda (tempo, leggibilità a distanza, filo dei titoli), e l'agente non ha
strumenti per aprire il file, quindi la skill gli prepara scaletta e anteprime
e lui legge quelle.

Il tema si è estratto dal PowerPoint reale di CIMA, non ricostruito: il tema
del file è lo stock di Office, mentre l'identità sta nei layout, nelle immagini
e nel carattere imposto sopra il tema. Un mazzo si costruisce quindi copiando
il template e duplicandone le slide di esempio, non rigenerando un tema da
zero.

Deciso il 2026-10-10.
