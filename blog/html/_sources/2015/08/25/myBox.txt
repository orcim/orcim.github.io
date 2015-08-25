myBox
=====

Bene oggi vedremo il nostro primo *template* per i *widgets*.

Non potevamo che iniziare dai contenitori! Lo chiameremo **my01Box**.
Vi chiederete perchè inserisco dei prefissi numerici ai nomi degli script.
E' una maniacale usanza che mi permette di tenere ordinati per importanza i vari files.

Inoltre quando devo richiamarli, da terminale, è sufficiente dare in genere le prime 4 lettere seguite da un **Tab** per avere velocemente la scelta del file interessato. Non fateci caso ma nel mondo **nix** succedono anche queste cose.

Per chi non lo sapesse **nix** sta ad indicare tutto quello che deriva da unix.

.. more::

**my01Box**

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 1-83

I metodi **myBox** e **myFrame** li abbiamo già visti nel post **Contenitori** per cui non li commenterò.

myViewObject
------------

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 25-31

E' una *utility* che serve in fase di **debug** per visualizzare le istanze degli oggetti creati. Normalmente viene richiamato, se necessario, dopo una istanza di un oggetto complesso per visualizzare la sua struttura. Un esempio d' uso lo vederemo nella istanza di liste di oggetti.

.. note:: Per visualizzare il risultato dovete avviare lo script da terminale.

Liste di oggetti
----------------

In questo modulo, *myBox.py*, sono presenti oltre che la definizione di metodi tradizionali anche la definizione di liste di oggetti. Questi metodi si riconosco dal post suffisso **List** dato al nome del metodo stesso. Sono molto utili quando si prevede l' utilizzo di un insieme di **oggetti** simili.

Vediamo un esempio concreto.

myBoxList
---------

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 84-125

E' un esempio di pura dimostrazione ma serve a comprendere la potenzialità di usare le liste nella programmazione in genere.

Come potete vedere dal codice del nostro template **myBoxList** passiamo una lista  dei nomi degli oggetti che vogliamo istanziare, nel nostro caso sono **box**. Subito dopo passiamo gli attributi **tbox** e **aBox** che andranno a caratterizzare gli stessi. Ed infine una funzione di supporto. 

Mi voglio soffermare su questa ultimo parametro passato. Questa funzione torna molto utile. Ci permette di integrare una ulteriore elaborazione durante l' istanza dell' oggetto. Nell' esempio di **testBoxList** viene utilizzata per inserire delle labes per enfatizzare lo scopo dell' esempio stesso.

.. figure:: myBoxList.png
	:align: center
	:alt: alternate text

	*testBoxList in esecuzione.*

.. note:: per maggiori informazioni dei contenitori consiglio di rivedere il post **Contenitori**

myFrameList
-----------

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 127-203

Questo è un'altro esempio di lista di oggetti. E' molto simile alla precedente cambiano solo gli attributi all' ingresso che rispecchiano quelli del nuovo oggetto frame. Per cui non li commenterò.

.. figure:: myBoxList.png
	:align: center
	:alt: alternate text

	*testBoxList in esecuzione.*

Package
-------

La struttura del nostro package ora è la seguente:

.. code-block:: rest

	l00_start.py
	l01_startGtk.py
	my00init.py
	myWidg/
	  __init__.py
	  my00init.py
	  my00initGtk.py
	  my01Box.py
	  myWind.py
	  myApp.py

Per scaricare la nuova versione :download:`20150825.zip </_static/20150825.zip>`

Saluti
------

Nel prossimo post vedremo una variante dell' oggetto **box**.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
