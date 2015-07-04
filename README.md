# FakeLogin-Fuzzer

Cerca il file con le password rubate da un fake login

### Sintassi

ff fakelogin_root_url nome1 [nome2 nome3 ... nomen]

### Descrizione 

FakeLogin-Fuzzer (ff) prende la root del fake login, aggiunge alla fine il nome di un possibile file e invia al server una richiesta http HEAD; quindi stampa la risposta.
Questo software può anche essere usato per creare una lista dei file presenti in una generica directory.

### Opzioni

* fakelogin_root_url	La root del fakelogin, deve essere in questa forma: http://foo.bar/fake/. Deve essere presente un http/https iniziale, ma soprattutto uno "/" finale.
* nome1 [nome2 nome3 ... nomen]		I possibili nomi del file, ovviamente non è necessario inserirli manualmente se sono molti; leggere sotto.		

### Miglioramenti di input/output

* I nomi dei file possono essere tenuti in un file separati da " ", per utilizzarli in input è possibile fare una cosa simile a questa:
cat nomi.txt | xargs ff fakelogin_root_url
* In output vengono visualizzati anche i file non trovati, se si volessero vedere solo i file trovati si potrebbe fare per es.:
cat nomi.txt | xargs ff fakelogin_root_url | grep 200

