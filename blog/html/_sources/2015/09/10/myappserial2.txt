myAppSerial (II)
================

Bene continuamo la nostra **GUI**

Oggi creiamo la **sezione** Rx Buffer.

.. more::

myTry02
-------

In **myTry02** aggiungiamo la sezione di ricezione dati.

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 208-310

Rx
^^

Come potete vedere abbiamo inserito:

	* Il contatore dei dati ricevuti

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 222-233

Qui referenziamo l' oggetto **self.labRcv** che ci servirà per aggiornare il contatore.

	* La possibilità di abilitare/disabilitare la ricezione dati

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 235-250

Con la referenza **self.chkEna** abilitiamo/disabilitiamo la ricezione dati nel metodo **devRx**

	* Un pulsante per la pulizia del nostro logger che resetta anche i contatori Rx/Tx

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 252-270

Qui definiamo una nuova **callback** per il nostro pulsante che esegue tutte le operazioni richieste.

	* La possibilità di visualizzare i caratteri non stampabili

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 272-290

Anche qui definiamo una nuova **callback** che attiva/disattiva il flag **self.dev.hid** presente nel modulo del protocollo per rendere visibili i caratteri non stampabili.

	* La possibilità di visualizzare i caratteri ricevuti in formato esadecimale

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 292-310

Allo stesso modo definiamo una nuova **callback** che attiva/disattiva il flag **self.dev.hex** presente nel modulo del protocollo per visualizzare i caratteri ricevuti nella codifica esadecimale.

Parser
------

Abbiamo ridefinito il parser per le nuove necessità.

.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 33-54

Notare che adesso richiede in ingresso l' attributo **app** che ci serve come riferimento per poter scrivere nel **logger** e aggiornare il **contatore** dei bytes ricevuti.

Main
----

Il nostro **main** adesso invia un messaggio di prova attende 3 secondi e pulisce il nostro **logger**.


.. literalinclude:: /_static/20150910/myAppSerial/myAppSerial.py
	:language: python
	:lines: 488-497


Se proviamo ad avviare il nostro **script** vedremo:

.. figure:: myAppSerial2.png
	:align: center
	:alt: alternate text

	*myAppSerial* in esecuzione. 

Come potete notare adesso ci sono le sezioni **Rx** e **Tx** con i relativi widgets.

Package
-------

La struttura aggiornata del nostro package è la seguente:

.. code-block:: rest

	myAppSerial/
	  l00_start.py
	  l01_startGtk.py
	  my00init.py
	  myAppSerial.py
	  myLib/
	    __init__.py
	    myProtocol/
	      __init__.py
	      my00init.py
	      myProtocol.py
	      mySerial.py

Per scaricare la nuova versione :download:`20150910.zip </_static/20150910.zip>`

Saluti
------

Bene nel prossimo post arricchiremo la nostra applicazione con altre caratteristiche.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk, application
.. comments::
