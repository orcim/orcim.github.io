mySerial
========

Adesso abbiamo la base di una piccola libreria di widgets **GTK** pronta per essere usata nelle nostre applicazioni.

Andremo a realizzare la nostra prima applicazione reale!

Ho scelto di realizzare un terminale seriale poichè, nelle applicazioni industriali, la comunicazione per lo sviluppo è quasi sempre basata su questo tipo di comunicazione.

.. more::

myAppSerial
-----------

Creiamo la struttura della nostra applicazione.

Per fare questo dobbiamo creare una **directory** di lavoro a cui assegneremo il nome di **myAppSerial**.

Iniziamo col definire un nuovo **package** (libreria) a cui assegneremo il nome **myLib**. 

Per fare questo creiamo la directory **myLib**. Qui aggiungiamo un file vuoto di nome **__init__.py**. 

Ora decomprimiamo la nostro base di partenza **20150904.zip** dentro la directory **mySerial**.

La libreria la trovate nel post del 4/set/2015 come si deduce anche dal nome della stessa . 

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

Creiamo un' altro package che conterrà al suo interno tutti i moduli che hanno a che fare con le comunicazioni seriali. Lo chiameremo **myProtocol**. Creiamo la directory di nome **myProtocol** e al suo interno creiamo un file vuoto di nome **__init__.py**.

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

Ora copiamo dentro la directory **myProtocol** lo stesso file che troviamo alla base **myAppSerial/my00init**. Questo ci serve come init iniziale del nostro micro ambiente **myProtocol**. Apriamolo ed eliminiamo le linee da 24 a 33 che sono quelle che interessano le **GTK**. In questo micro ambiente non ne abbiamo bisogno.

Inoltre aggiungiamo la variabile **printable** che ci sarà utile per verificare se un carattere è stampabile nel prossimo modulo che andremo a definire. 

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/my00init.py
	:language: python
	:lines: 87-88

mySerial
--------

Fa uso del *package* **pySerial** che dovrete installarlo nel vostro ambiente.
Vi rimando al `link <http://pyserial.sourceforge.net/>`_ del sito in cui troverete ampia documentazione.

Questo modulo **mySerial** sarà il responsabile della gestione delle nostre **seriali**. 

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/mySerial.py
	:language: python
	:lines: 49-274

Il codice è stato scritto per non essere **bloccante**. Questo ci permetterà di lavorare in modo asincrono se ne avessimo bisogno.

Inoltre nel caso volessimo lavorare in modo sincrono ho sfruttato il timer del nostro **PC** per creare un **time out** oltre il quale comunque usciremo dal codice bloccante.

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/mySerial.py
	:language: python
	:lines: 233-267

Vi lascio allo studio del rimanente codice.

myTry01
-------

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/mySerial.py
	:language: python
	:lines: 276-310

Qui vediamo il modo di selezionare l' inizializzazione in base al **S.O.** sistema operativo in cui gira il codice. Può tornare utile anche in altre applicazioni multi piattaforma. 

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/mySerial.py
	:language: python
	:lines: 281-291

Inoltre ho aggiunto del codice di esempio per fare vedere come sollecitare l' handshake.

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/mySerial.py
	:language: python
	:lines: 298-303

myTry02
-------

.. literalinclude:: /_static/20150905/myAppSerial/myLib/myProtocol/mySerial.py
	:language: python
	:lines: 313-324

Qui sfruttiamo il codice di prima per l' inizializzazione. Poi facendo un **loop** hardware sui segnali **Tx** e **Rx** del nostro dispositivo seriale proviamo ad inviare e ricevere una stringa col nostro codice.

Se proviamo ad avviare il **test** da terminale **$ python mySerial.py** vedremo:

.. figure:: mySerial.png
	:align: center
	:alt: alternate text

	*mySerial* in esecuzione. 

Package
-------

La struttura aggiornata del nostro package è la seguente:

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
	      mySerial.py

Per scaricare la nuova versione :download:`20150905.zip </_static/20150905.zip>`

Saluti
------

Per oggi mi fermo qui. 

Nel prossimo post vedremo il lato del protocollo.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
