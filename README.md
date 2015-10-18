# FakeLogin-Fuzzer #

Cerca il file con le password rubate da un fake login

## Sintassi #

ff fakelogin_root_url nome1 [nome2 nome3 ... nomen]

## Opzioni ##

* fakelogin_root_url: la root del fakelogin, deve essere in questa forma: http://foo.bar/fake/. Deve essere presente un http/https iniziale, ma soprattutto uno "/" finale.
* nome1 [nome2 nome3 ... nomen]: i possibili nomi del file, ovviamente non è necessario inserirli manualmente se sono molti; leggere la sezione "Miglioramenti di input/output".

## Funzionamento ##

FakeLogin-Fuzzer (ff) prende la root del fake login, aggiunge alla fine il nome di un possibile file e invia al server una richiesta http HEAD; quindi stampa il codice HTTP ricevuto.	

## Miglioramenti di input/output ##

* I nomi dei possibili file possono essere tenuti in un file separati da " ", per utilizzarli in input è possibile fare una cosa simile a questa:

```
cat nomi.txt | xargs ff fakelogin_root_url
```

* In output vengono visualizzati anche i file non trovati, se si volessero vedere solo i file trovati si potrebbe fare per es.:

```
cat nomi.txt | xargs ff fakelogin_root_url | grep 200
```

## Altre informazioni ##

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.  

Aggiornamenti: [GitHub] (https://github.com/matteoalessiocarrara)  
Email: sw.matteoac@gmail.com
