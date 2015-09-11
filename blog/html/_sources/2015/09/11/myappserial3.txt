myAppSerial (III)
=================

Bene oggi introduciamo la possibilità di ripetere nel tempo l' invio del nostro comando in modo automatico.

.. more::

myTry02
-------

Per far questo aggiungiamo alla nostra **GUI** una **myEntFrame** dove inseriremo il tempo di ripetizione e un **myChkButton** per abilitare l' invio automatico.

Sempre per la filosofia dei **templates** selezioniamo e copiamo da riga 339 a riga 385 del nostro script **myAppSerial** e incolliamo alla fine della sezione **TX**, prima del **Main** incolliamo la precedente copia.

Dopo le modifiche descritte successivamente il risultato è il seguente:

.. literalinclude:: /_static/20150911/myAppSerial/myAppSerial.py
	:language: python
	:lines: 461-503

Abbiamo modificato quanto segue sulla nuova  **myEntFrame**:

* Eliminiamo il contenuto della callback **on_activate** e inseriamo l' istruzione **pass**. Questo perche' la nostra **callback** non deve fare nulla.

* Il valore iniziale di default da **name=''** in **name='100'**
* La lunghezza della entry da **numb=29** in **numb=5**
* La label da **cmd.Serial** in **mSec**
* Il riferimento della nostra entry da **self.entCmdSerial** in **self.ent_mSec**

Abbiamo modificato quanto segue sul nuovo **myChkButton**:

* Abbiamo Copiato dal precedente **myChkButton** il codice della callback **on_clicked** e modificato il contenuto come segue:

.. literalinclude:: /_static/20150911/myAppSerial/myAppSerial.py
	:language: python
	:lines: 486-491

Come potete vedere abbiamo sfruttato la chiamata differita **GLib.timeout_add** per regolare il tempo di ripetizione.

myRepeat
--------

Nella definizione del metodo **myRepeat** abbiamo sfruttato la variabile **self.enaRepeat**. Quando questa è uguale a **False** rimuove se stessa dalla lista che l' oggetto **GLib.timeout** usa per richiamare i metodi in modo differito.

.. literalinclude:: /_static/20150911/myAppSerial/myAppSerial.py
	:language: python
	:lines: 477-482


Proviamo ad avviare il nostro **script**.

Scriviamo qualcosa da inviare sulla myEntFrame **cmd.Serial**.

Attiviamo l'invio ripetuto cliccando sul nostro myChkButton **Repeat**.

Il risultato sarà il seguente:

.. figure:: myAppSerial3.png
	:align: center
	:alt: alternate text

	*myAppSerial* in esecuzione. 

Se vogliamo terminare l' invio automatico basterà cliccare di nuovo sul nostro myChkButton **Repeat**.

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

Per scaricare la nuova versione :download:`20150911.zip </_static/20150911.zip>`

Saluti
------

Bene nel prossimo post arricchiremo la nostra applicazione con altre caratteristiche.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk, application
.. comments::
