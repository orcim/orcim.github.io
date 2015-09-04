myCheckButton
=============

Il modulo **my03ChkButton** contiene una serie di widgets per la gestione dei **check buttons** che sono degli oggetti che permettono la selezione (attiva/disattiva) attraverso un click sopra l' oggetto stesso.

.. more::

myChkButton
-----------

E' un oggetto che assume 2 stati come il nostro **button switch** ma con una grafica diversa.

Gli attributi passati durante l' istanza sono **valu** che decide se lo stato deve essere vero/falso. Altro attributo è **colo** che decide di che colore deve essere la **label** del nostro oggetto.

.. literalinclude:: /_static/20150903/myWidg/my03ChkButton.py
    :language: python
    :lines: 24-70

testChkButton
-------------

Come possiamo vedere dal codice del **test** abbiamo forzato il colore a **black** per rendere più visibile la nostra label. Inoltre abbiamo inserito il nostro **chkButton** all' interno di un **frame** per abbellire il tutto.

.. literalinclude:: /_static/20150903/myWidg/my03ChkButton.py
    :language: python
    :lines: 71-91

Se proviamo ad avviare il **test** vediamo:

.. figure:: testChkButton.png
	:align: center
	:alt: alternate text

	*testChkButton* in esecuzione. 

Se proviamo a cliccare sul nostro **chkButton** vedremo il segno di spunta apparire ed inoltre cambiare il colore della **label**. Questo è fatto dalla **callback** di default poichè abbiamo scelto di non passare nulla durante l' istanza **call=None** sebbene avvessimo ridefinito una nuova **callback** nell' esempio.

myChkButList
------------

Come al solito segue il metodo delle liste che ci torna utile nel caso dobbiamo definire una serie di widgets omogenei.

.. literalinclude:: /_static/20150903/myWidg/my03ChkButton.py
    :language: python
    :lines: 93-122

testChkButList
--------------

.. literalinclude:: /_static/20150903/myWidg/my03ChkButton.py
    :language: python
    :lines: 124-143

Se proviamo ad avviare il **test** vedremo:

.. figure:: testChkButList.png
	:align: center
	:alt: alternate text

	*testChkButList* in esecuzione. 

Se proviamo a modificare l' attributo **tBox='h'** in **tBox='v'** otteniamo la stessa lista ma con allineamento verticale:

.. figure:: testChkButList1.png
	:align: center
	:alt: alternate text

	*testChkButList* in esecuzione. 

myChkButLisLabel
----------------

Per finire ho realizzato la stessa lista ma con una **label** in testa che può tornare utile in alcune situazioni

.. literalinclude:: /_static/20150903/myWidg/my03ChkButton.py
    :language: python
    :lines: 145-192

testChkButLisLabel
------------------

.. literalinclude:: /_static/20150903/myWidg/my03ChkButton.py
    :language: python
    :lines: 172-186

Se proviamo ad avviare il **test** vediamo:

.. figure:: testChkButLisLabel.png
	:align: center
	:alt: alternate text

	*testChkButLisLabel* in esecuzione. 

.. note:: Vi invito per lo studio dei nostri **widgets** di avviarli sempre da terminale. Così potete visualizzare i messaggi in uscita fatti ad hoc per i nostri test.	

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

Per scaricare la nuova versione :download:`20150903.zip </_static/20150903.zip>`

Saluti
------

Per oggi mi fermo qui. 

Nel prossimo post vedremo i **radio buttons**.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
