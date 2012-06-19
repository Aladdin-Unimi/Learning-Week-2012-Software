# Learning Week 2012 Software


Software utilizzato per l'edizione 2012 della Learning Week presso il
Dipartimento di Informatica @ Unimi.

## Come installare il software

Eseguite dall'interprete di comandi il comando

	curl -sL http://git.io/lw12 | bash

al termine dell'esecuzione sarà stata creata (nella directory dove avete
eseguito il comando precedente) la sottodirectory `lw12` al cui interno
verranno installati alcuni file `.zip` ed il file `run.sh` che potete usare
per porre in esecuzione il software invocandolo come

	cd lw12; ./run.sh

e attendendo che venga aperta (dal software stesso) una finestra del browser
all'indirizzo

	http://localhost:5000/

## Suggerimenti utili durante lo svolgimento delle lezioni in SILab

### Uso del proxy:

Prima di scaricare il software, date il comando

	export ALL_PROXY=www:8080

per consentire a `curl` di usare il proxy. Potete rendere "permanente" tale
modifica aggiungendo tale riga in coda al file `.bash_profile` contenuto nella
vostra home, ad esempio, tramite il comando

	echo "export ALL_PROXY=www:8080" >> ~/.bash_profile

(questa modifica avrà effetto al successivo login).

### Immagini con geo-tag

Potete scaricare un file `.zip` contenente alcune immagini con geo-tag
tramite il comando

	curl -sL http://git.io/lw12gt > flikr.zip
	
e quindi estrarre le immagini (nella directory corrente) con

	unzip flikr.zip -x metadata.kml
	
si tratta di alcune centinaia di immagini con geo-tag provenienti da http://flikr.com.
