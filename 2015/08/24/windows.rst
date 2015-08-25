Windows
=======

Per scrupolo ho provato ad eseguire gli scripts in **Windows** ma mi sono accorto che c' era qualche problema. Così ho preso l' occasione per suddividere ulteriormente il file **my00init.py** per aumentare la leggibilità. 

.. more::

Visto che ci sono spiego velocemente come installare le **GTK3** in *Windows*.

Scaricate dal seguente `link <http://sourceforge.net/projects/pygobjectwin32/files/latest/download?source=files>`_  che punta all' ultima versione dell' installer. Attende qualche secondo che vi appaia la dialog di download. 

Avviate l' eseguibile e seguite le istruzioni; vi ritroverete **Python GTK3** installato.

La struttura è cambiata come segue:

.. code-block:: rest

	l00_start.py
	l01_startGtk.py
	my00init.py
	myWidg/
	  __init__.py
	  my00init.py
	  my00initGtk.py
	  myWind.py
	  myApp.py

Il motivo del non funzionamento su **Windows** era dovuto che non supporta l' import diretto a causa del modo differente tra **Linux** e **Windows** di gestite il percorso dei files.

.. code-block:: python

	#-----------------------------------------------------------------------------
	from myWidg.my00init import *

	#-----------------------------------------------------------------------------
	from myWidg.myApp import MyApp

Perciò l' ho modificato in 

.. code-block:: python

	#-----------------------------------------------------------------------------
	from my00init import *

	#-----------------------------------------------------------------------------
	from myApp import MyApp

Dando il compito al seguente codice, che si trova in **my00init.py**, di risolvere il percorso assoluto di dove si trovano i files del nostro **package**.

.. code-block:: python

	#-----------------------------------------------------------------------------
	# ricavo l'ambiente
	myRoot = module_path()
	myFath, myHome = os.path.split(myRoot)
	# inseriamo i nostri packages che vogliamo usare
	insLib(myRoot+'/myWidg',True)

Per scaricare la nuova versione :download:`20150824.zip </_static/20150824.zip>`

Saluti
------

Se vi fossero errori fatemelo sapere.

Nel prossimo post inizieremo a creare il template dei contenitori.

Ciao alla prossima. (stay tune!)


.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
