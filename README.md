## Software Scuola Estiva presso l'Educandato Setti Carraro Dalla Chiesa ##
    
Nell'ambito del Progetto Eccellenze del MIUR (ex art. 20 del DM n. 435/2015)
e con il patrocinio del Dipartimento di Informatica dell'Università degli
Studi di Milano, l'Educandato Setti Carraro dalla Chiesa e ALaDDIn
organizzano la Scuola Estiva di informatica, *"L'informatica come impresa
scientifica"*, allo scopo di offrire agli studenti interessati percorsi per
avvicinarsi alla scienza e alla tecnologia attraverso un apprendimento
attivo che permetta di toccare con mano i vari aspetti che gravitano attorno
alla progettazione e alla realizzazione di un'applicazione web
"intelligente", fornendo elementi di conoscenza e di orientamento per una
futura scelta universitaria e/o professionale. Questo è il software usato
durante le attività.

## Come installare il software

La sottodirectory `sc16` contiene alcuni file `.zip` ed il file `run.sh` che potete usare
per porre in esecuzione il software invocandolo come

	cd sc16; ./run.sh

e attendendo che venga aperta (dal software stesso) una finestra del browser
all'indirizzo

	http://localhost:5000/

## Come installare il software a casa

Per usare questo software a casa dovete installare Python e scaricare i file contenenti codice e dati.

Se usate GNU/Linux, o Mac OS X, probabilmente Python è già installato; verificate che versione avete con il comando

	python --version

Se la versione è inferiore a 2.7, o il programma non è installato, potete
scaricare la versione corretta da http://www.python.org/download/

A questo punto avete bisogno del file `.zip` dell'applicazione, del codice utente e
delle immagini. Potete trovarli all'indirizzo
https://github.com/Aladdin-Unimi/Learning-Week-2012-Software/downloads sono i
file con nome

* `lwapp-vX.Y.Z.zip`
* `userapps-vX.Y.Z.zip`
* `example.zip, o flikr.zip`

dove `X`, `Y` e `Z` sono i numeri di versione (scegliete sempre l'ultima!).

Una volta installato Python e scaricati i tre file, potete avviare l'applicazione invocando il comando

	python lwapp-vX.Y.Z.zip userapps-vX.Y.Z.zip images.zip
	
dove `images.zip` è il modo in cui avrete rinominato il file delle immagini che avete scaricato.

