boxEvent
========

Oggi voglio fare una premessa per giustificare il mio modo di operare. Qualcuno mi suggerisce di usare glade o altri Rad. A mio modesto avviso prima di usare dei rad e cosa buona e giusta fare un pò di gavetta e scriversi il codice a mano. Perchè così facendo si impara a fondo l'ambiente e si fa pratica nella programmazione. Poi alla fine si sarà in grado di valutare meglio quale strada percorrere.

.. more::

myBoxEvent
----------

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 236-304

Questo oggetto l' ho costruito per avere la possibilità di avere un evento quando clicco col mouse sull' area del contenitore. Per fare questo ho istanziato l' oggetto EventBox che prevede questa caratteristica.

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 254-255

Inoltre ho gestito la possibilità di cambiare colore allo sfondo che può essere utile per enfatizzare l' evento stesso.

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 260-261

Ed infine ho inserito una **Label** per assegnare se necessario un nome all' area stessa.

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 267-269

Se avviate il test **testBoxEvent** dovreste vedere come nella figura seguente.

.. figure:: testBoxEvent.png
	:align: center
	:alt: alternate text

	*testBoxEvent in esecuzione.*

Se provate a cliccare sull' area colorata in giallo vedrete nel terminale il nome dello **stato** e nella **GUI** cambiare il **colore** in Verde o in Rosso in base allo stato dell' oggetto.

myBoxEveList
------------

Come per le altre tipologie di oggetti ho previsto la solita **lista di oggetti** omogenea.

.. literalinclude:: /_static/20150825/myWidg/my01Box.py
    :language: python
    :lines: 306-350

Il passaggio di parametri iniziale è molto simile alle altre liste già viste.
Per cui vi lascio alla meditazione leggendo e provando i 2 test possibili già previsti nel codice stesso.

Se avviate il test **testBoxEveList** dovreste vedere come nella figura seguente.

.. figure:: testBoxEveList.png
	:align: center
	:alt: alternate text

	*testBoxEveList in esecuzione.*

Se provate a cliccare nelle varie aree dovreste vedere nel terminale il nome dell' area cliccata.

Package
-------

La struttura e il link rimangono invariati rispetto al post **myBox**.

Per scaricare la versione :download:`20150825.zip </_static/20150825.zip>`

Saluti
------

Nel prossimo post inizieremo a vedere i widgets del tipo **Label**.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
