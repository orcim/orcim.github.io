Template base
=============

Dopo un pò di ciacole, come si dice a Venezia, iniziamo a vedere un aspetto della programmazione che a mio modesto avviso viene spesso sottovalutato.

Quando iniziamo a scrivere del codice ci dobbiamo ricordare di dare una struttura al nostro lavoro, nota bene sto sottolineando la parola **Lavoro** non codice.

.. more::

Come dicevo nel precedente post è importante dare una impronta al nostro modo di lavorare e cercare di seguirla senza modificarla il più possibile. Forse all'inizio ci ritroveremo a modificarla più frequentemente a causa della nostra inesperienza ma col passare del tempo la affineremo e apprezzeremo presto il suo utilizzo.

Qui vengono in aiuto i **Templates** che altro non sono dei modelli da cui partire per il nostro lavoro. Sono dei semplici files costruiti precedente che di danno le linee guida per il nostro futuro lavoro.

Vediamo un esempio concreto **l00_start.py**

.. literalinclude:: l00_start.py
    :language: python

Descrizione
-----------

Questo è un template base per uno script **Python**.

Commentiamo assieme la sua struttura.

Nella prima riga troviamo la classica direttiva per fare diventare uno script eseguibile da linea di comando senza anteporre l'interprete python.

.. code-block:: python

	#!/usr/bin/env python


Nella seconda indichiamo il coding che vogliamo utilizzare.

.. code-block:: python

	# -*- coding: utf-8 -*-

Il primo commento
-----------------

Segue la classica **Doc string** che nel nostro caso riassume cosa contiene il nostro file.

.. code-block:: python

	""" lista oggetti definiti:

		- myDefine
		- MyClass
	"""

La revisione
------------

E' bene inoltre definire un attributo che ricordi la revisione del nostro codice.

.. code-block:: python

	myRev = "(rev.20150811)"

Il metodo che ho scelto per indicare la revisione è la data Osi che ci permette di avere un ordinamento corretto in caso di indicizzazione. 

La forma è molto semplice AAAAMMGG. 

Se si avesse la necessità di avere più granularità nello stesso giorno io di solito aggiungo una lettera progressiva. Esempio

.. code-block:: rest

	20150811a
	20150811b

Qui una domanda sorge spontanea. Perchè mettere una revisione su singolo file?

Si perchè in python ogni file puo' diventare un modulo ed essere raggruppato in un package inserendolo in una directory dove sarà prensente il file col nome **__init__.py**.

Questo indica al nostro interprete che questa directory diventa un package in altre parole una libreria.


Commenti
--------

Come si diceva meglio abbondare di commenti. Questi ci aiutano sia a ricordare quello che facciamo ma anche ad aumentare la leggibilità. Come avrete potuto notare nell' esempio precedente io uso separare o meglio raggruppare zone di codice antecedendo
una intestazione che richiama a prima vista di cosa tratta il codice seguente.

.. code-block:: python

	#-----------------------------------------------------------------------------
	# Modules
	#-----------------------------------------------------------------------------
	import sys

Suddivisione
------------

La prima grande suddivisione separa i richiami dei moduli dalle definizioni di metodi e classi. E per finire i test del codice stesso con relativo richiamo tramite il **main** principale.

.. code-block:: python

	#-----------------------------------------------------------------------------
	# Main
	#-----------------------------------------------------------------------------
	if __name__=='__main__':

		# test arguments
		if len(sys.argv) == 1:
			# no arguments (scelgo io)
			choi = 1
		else:
			# get first argument (scelta esterna)
			choi = int(sys.argv[1])

E qui si scatenerà una guerra. Perchè non usare **unitest** con i metodi **assert** o **fail**.
E' solo una scelta personale. Ognuno è libero di scegliere come lavorare se non si hanno dei vincoli imposti ovvio.

Ricordo che in **python** uno script in esecuzione prende il nome di default **__main__** perciò si può sfruttare questa peculiarità per rendere eseguibili anche dei moduli che normalmente sarebbero solo richiamati da altri scripts. In questo modo possiamo testare tramite l' attributo **choi** vari pezzi di codice.

Test
----

Normalmente quando scrivo un nuovo metodo o una nuova classe subito dopo scrivo anche il metodo che li testa. 

.. code-block:: python

	#-----------------------------------------------------------------------------
	class MyClass(object):
		def __init__(self, name=""):
			self.name = name
	#-----------------------------------------------------------------------------
	def testMyClass():
		# (name="")
		self = MyClass("MyClass")
		print self.name

Questo mi permette a distanza di tempo:

* di vedere come utilizzare il codice 
* copiare e incollare le linee di codice come fosse un template.

Normalmente nel codice di prova scrivo un commento prima della chiamata dove riporto i vari parametri che si possono passare. 

Ricordate cosa dicono le regole di un buon programmatore:

* meglio esplicito che implicito.

Try
---

Nella sezione **try** scrivo dei metodi che simulano dei test più complessi dell' uso dei vari oggetti definiti. In questo caso nel nostro file campione gli oggetti definiti sono molto semplici e può risultare ridondante il codice scritto. Ma per un template questo va benissimo.

.. code-block:: python

	#-----------------------------------------------------------------------------
	# myTry
	#-----------------------------------------------------------------------------
	def myTry01():
		""" test myDefine
		"""
		testMyDefine()

Labels
------

Come avrete notato le **labels** che utilizzo sono acronimi composti. 

Se la definizione è un **metodo** o un **attributo** deve iniziare sempre in minuscolo.

.. code-block:: python

	def myDefine(name=""):

mentre se è una **classe** inizia sempre con una maiuscola. 

.. code-block:: python

	class MyClass(object):

Le lables composte da più acronimi seguono la regola di enfatizzare con una lettera maiuscola l' inizio di ogni acronimo a meno del primo che deve sottostare alle regole viste precedentemente.

Tendo ad accorciare le parole quasi sempre con 4 lettere mentre la finale la lascio integra se non troppo lunga. 

.. code-block:: python

	#-----------------------------------------------------------------------------
	def testMyDefine():

Le variabili locali interne sono lunghe 3 lettere, esempio **ind**,  mentre quelle di passaggio 4 lettere, esempio **name**,  per distinguerle meglio. 

.. code-block:: python

	#-----------------------------------------------------------------------------
	def myDefine(name=""):
		return name
	#-----------------------------------------------------------------------------
	def testMyDefine():
		# (name="")
		for ind in xrange(3):
			print ind, myDefine("la mia callback!")
		# end idle
		return False

Saluti
------

Nel prossimo post inizieremo a parlare di GTK.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python
.. comments::
