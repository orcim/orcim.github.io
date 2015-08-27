myLabel
=======

Il widget **Label** ci permette di visualizzare una stringa. 

Questo può essere posizionato vicino ad un' altro oggetto per identificarlo.

.. more::

.. warning:: Attenzione che ho dovuto correggere un piccolo bug sulla gestione dei css. Per cui sono stati aggiornati alcuni files. Consiglio sempre di scaricare l' ultima versione che trovate sempre alla fine del post.

myLabel
-------

.. literalinclude:: /_static/20150827/myWidg/my02Label.py
    :language: python
    :lines: 23-65

I parametri che differiscono dai soliti nostri **widgets** sono l' impostazione del font da usare per la nostra stringa e il colore da usare per la scrittura.

.. literalinclude:: /_static/20150827/myWidg/my02Label.py
    :language: python
    :lines: 50-53

Mentre altri 3 parametri **leng**, **prea** e **post** meritano una spiegazione. Se decidiamo che la nostra stringa debba occupare un certo spazio dobbiamo indicare la **lunghezza**, inoltre possiamo decidere il carattere da usare per identare a destra, e ultimo possiamo aggiungere un **post** fisso alla nostra stringa. Vedremo più avanti l' utilità di queste cose.

.. literalinclude:: /_static/20150827/myWidg/my02Label.py
    :language: python
    :lines: 44-47

Se proviamo ad avviare il **test** otterremo quanto segue.

.. figure:: testLabel.png
	:align: center
	:alt: alternate text

	*testLabel in esecuzione.*

myLabList
---------

Quello che segue è la solita lista di oggetti che non serve commentare.

Il codice segue la stessa filosofia delle altre liste già viste.

.. literalinclude:: /_static/20150827/myWidg/my02Label.py
    :language: python
    :lines: 67-107

Se proviamo ad avviare il **test** otterremo quanto segue.

Notate l' utilizzo dell' identazione a destra con **post** fisso.

.. figure:: testLabList.png
	:align: center
	:alt: alternate text

	*testLabList in esecuzione.*

myLabFrame
----------

Per finire uniamo il widget **myFrame** già visto con **myLabel**.

.. literalinclude:: /_static/20150827/myWidg/my02Label.py
    :language: python
    :lines: 109-155

.. note:: Osservate come vengono passati i parametri in uscita. C' è sempre l' oggetto principale seguito dalla lista di oggetti utili istanziati.

Se proviamo ad avviare il **test** otterremo quanto segue.

.. figure:: testLabFrame.png
	:align: center
	:alt: alternate text

	*testLabFrame in esecuzione.*

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
	  my02Label.py
	  myWind.py
	  myApp.py

Per scaricare la nuova versione :download:`20150827.zip </_static/20150827.zip>`

Saluti
------

Nel prossimo post vedremo l' oggetto **entry**.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
