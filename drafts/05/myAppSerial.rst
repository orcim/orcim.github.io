mySerial
========

Adesso abbiamo la base di una piccola libreria di widgets **GTK** pronta per essere usata nelle nostre applicazioni.

Andremo a realizzare la nostra prima appliazione reale!

Ho scelto di realizzare un terminale seriale poichè, nelle applicazioni industriali, la comunicazione per lo sviluppo è quasi sempre basata su questo tipo di comunicazione.

.. more::

mySerial
--------

Creiamo la struttura della nostra applicazione.

Per fare questo dobbiamo creare una directory di lavoro a cui assegneremo il nome di **myAppSerial**.

Iniziamo col definire un nuovo **package** (libreria) a cui assegneremo il nome **myLib**. Per fare questo creiamo la directory **myLib**. Qui aggiungiamo un file vuoto di nome **__init__.py**. 

Ora decomprimiamo la nostro base di partenza **20150904.zip**, che trovate nel post del 4/set/2015, dentro la directory **mySerial**. 

Alla fine dovremo la seguente struttura:

.. code-block:: rest

	myAppSerial/
	  l00_start.py
	  l01_startGtk.py
	  my00init.py
	  myLib/
		__init__.py
	  myWidg/
		__init__.py
		my00init.py
		my00initGtk.py
		my01Box.py
		my02Label.py
		my02Entry.py
		my02TxtView.py
		my03Button.py
		my03ChkButton.py
		myWind.py
		myApp.py

myLib
-----

Ora iniziamo a popolare la nostra libreria. Partiamo dalle librerie di basso livello senza interfaccia grafica **GUI**.

Creiamo un'altro package che conterrà al suo interno tutti i moduli che hanno a che fare con le comunicazioni seriali. Lo chiameremo **myProtocol**. Come prima creiamo la directory di nome **myProtocol** e al suo interno creiamo un file vuoto di nome **__init__.py**.

struttura aggiornata
^^^^^^^^^^^^^^^^^^^^

.. code-block:: rest

	myAppSerial/
	  l00_start.py
	  l01_startGtk.py
	  my00init.py
	  myLib/
	    __init__.py
	    myProtocol/
	      __init__.py

Ora copiamo dentro la directory **myProtocol** lo stesso file che troviamo alla base **myAppSerial/my00init**. Questo ci serve come init inziale del nostro micro ambiente **myProtocol**. Apriamolo ed eliminiamo le linee da 24 a 33 che sono quelle che riguardavano le **GTK**.

struttura aggiornata
^^^^^^^^^^^^^^^^^^^^

.. code-block:: rest

	myAppSerial/
	  l00_start.py
	  l01_startGtk.py
	  my00init.py
	  myLib/
	    __init__.py
	    myProtocol/
	      __init__.py
	      my00init.py













.. literalinclude:: /_static/20150904/myWidg/mySerial.py
	:language: python
	:lines: 24-60

Se proviamo ad avviare il **test** vedremo:

.. figure:: mySerial.png
	:align: center
	:alt: alternate text

	*mySerial* in esecuzione. 

Package
-------

La struttura aggiornata del nostro package è la seguente:

.. code-block:: rest

	l00_start.py
	l01_startGtk.py
	my00init.py
	myWidg/
	  __init__.py
	  my00init.py
	  my00initGtk.py
	  my01Box.py
	  my02Label.py
	  my02Entry.py
	  my02TxtView.py
	  my03Button.py
	  my03ChkButton.py
	  myWind.py
	  myApp.py

Per scaricare la nuova versione :download:`20150905.zip </_static/20150905.zip>`

Saluti
------

Per oggi mi fermo qui. 

Nel prossimo post vedremo ...

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
