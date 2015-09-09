myAppSerial
===========

Bene siamo arrivati alla nostra prima applicazione grafica.

Partiamo copiando la nostra prova **myTry01** del modulo **l01_startGtk**

.. more::

Modifichiamo la configurazione in **conf=0x0010** perchè non ci servono i box:

* application
* global
* main
* menu
* status

myTry01
-------

Aggiungiamo l' istanza del nostro **device** seriale con relativa configurazione.

Questa potete copiarla da **myTry01** del modulo **myProtocol**.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 34-87

**myTry01** la useremo come base di partenza per avere la struttura base della nostra applicazioen **Gtk**.

Per finire notare che abbiamo cambiato il titolo della nostra applicazione aggiungendo la **revisione** e la **configurazione** come promemoria.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 81-82

myTry02
-------

In **myTry02** viene definita la nostra **GUI** personale.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 90-341

Logger
^^^^^^

Il primo **widget** inserito è un **myTxtView** che lo useremo come **logger** della nostra applicazione. Qui vedremo i nostri **Tx** e **Rx**.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 99-121

Notate che abbiamo fatto un **redirect** per indirizzare lo **stdout** nel nostro **logger**. Questo avviene perchè abbiamo mantenuto la compatibilità delle chiamate.

Device
^^^^^^

La seconda **sezione** viene enfatizzata da un commento per aumentare la leggibilità.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 123-192

Qui abbiamo creato 2 metodi **devRx** e **devTx** per automatizzare l'aggiornamento.
Li abbiamo aggiunti al **loop** di **idle** così verranno richiamati quando non vi sono altre priorità.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 162-163


.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 191-192

Tx
^^

Per finire abbiamo aggiunto una **sezione** per la gestione delle nostre trasmissioni.

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 194-341

Come potete vedere abbiamo inserito la possibilità di abilitare il fine linea **LF** e il ritorno carrello **CR** nelle nostre TX.

Per test ho inserito anche la possibilità di modificare lo stato dei segnali **RTS** e **DTR**

Per finire ho aggiunto un contatore delle nostre trasmissioni **Tx.Data**

main
----

Il nostro **main** richiama le 2 definizioni **myTryXX** e per dimostrazione aggiunge 2 trasmissioni.


.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 367-376


Se proviamo ad avviare il nostro **script** vedremo:

.. figure:: myAppSerial.png
	:align: center
	:alt: alternate text

	*myAppSerial* in esecuzione. 

Come potete notare appaiono le 3 trasmissione Tx/Rx.

**Tx** viene enfatizzata dal colore verde.

**Rx** viene enfatizzata dal prepost **rx:**

Le prime 2 trasmissioni sono automatiche da codice. 

.. literalinclude:: /_static/20150909/myAppSerial/myAppSerial.py
	:language: python
	:lines: 372-376

La terza l' abbiamo fatta noi tramite il widget **cmd.Serial**.

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

Per scaricare la nuova versione :download:`20150909.zip </_static/20150909.zip>`

.. note:: Ricordatevi di fare il loop **TX<->Rx** sulla seriale e di impostare la porta giusta del vostro device su **myTry01**!

Saluti
------

Per oggi mi fermo qui. 

Nel prossimo post aggiungeremo alla nostra **GUI** altre caratteristiche.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk, application
.. comments::
