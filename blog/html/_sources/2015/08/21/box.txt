Contenitori
===========

Oggi parleremo dei contenitori **Box** e **Frame**. Ne esistono altri come Grid, Table, ecc. ma per il momento ci concentriamo su questi due.

Come ricorderete nel precedente post nelle definizioni erano presenti **myBox1** e **myFrame1**.

.. more::

Box
===

Esempio **myBox1**

.. code-block:: python

	#-----------------------------------------------------------------------------
	def myBox1(tBox='v', homo=False, spac=0):
		""" crea un contenitore del tipo richiesto
		
			-> tBox tipo di contenitore v/h 
			-> homo tipo omogeneita'
			-> spac spazio da mantenere all'esterno dell'oggetto
		"""
		if tBox == 'v':
			# creo un Vertical Box
			xBox = Gtk.VBox(homo,spac)
		elif tBox == 'h':
			# creo un Horizontal Box
			xBox = Gtk.HBox(homo,spac)
		xBox.show()
	# <-
		return xBox

Nel box di base esistono 2 tipi di contenitore:

* verticale
* orizzontale

Come si evince dai vocaboli i due box si differenziano dal modo in cui ordinano gli oggetti contenuti. 

Quando si approccia per la prima volta nelle **Gtk** si trova un pò di difficoltà ad adattarsi a una sua caratteristica che posiziona, in modo automatico, gli oggetti
a seconda di come impostiamo gli attributi dei nostri contenitori.

Normalmente negli altri **RAD** (Rapid Application Development) si decidono le dimensioni e il posizionamento degli oggetti stessi in base agli attributi **width**, **height**, **x** e **y**.

Nelle **Gtk** invece, di default, gli oggetti si auto dimensionano e prendono posizione in base ad attributi del tipo **expand**, **fill**.

Finchè non si comprende questo funzionamento non si apprezza invece la sua caratteristica principale che lo differenzia dagli altri. Proprio per questo motivo si può sviluppare progetti senza l'ausilio dei **RAD** in modo facile ed efficiente.
Una volta creati un pò di modelli base sarà sufficiente fare del **Cut** & **Paste** e modificare al volo se necessario alcuni attributi.

Come possiamo notare dal primo template, **myBox1** ci torna una istanza di un oggetto in base agli attributi passati durante la chiamata.

*Attributi*:

* **homogeneous**: definisce che gli oggetti contenuti avranno uguale spazio di allocazione
* **spacing**: indica lo spazio espresso in pixel che distanzierà in modo orizzontale gli oggetti.

Infine il metodo **show()** serve a rendere visibile l'oggetto che di default è sempre invisibile.

Frame
=====

Frame è un contenitore che aggiunge un bordo grafico con una label molto utile per indicare la tipologia degli oggetti che andremo ad inserire.

Analizziamo il nostro template **myFrame1**

.. code-block:: python

	#-----------------------------------------------------------------------------
	def myFrame1(name='myFrame', obje=None, colo='blue',
				bord=2, shad=Gtk.SHADOW_ETCHED_OUT, 
				tBox='v', aBox=[False, False, 1],
				xtBox='', xaBox=[False, False, 1],
				deb=False ):
		""" crea una cornice con un titolo
		
			-> name nome associato alla label della cornice
			-> obje oggetto da inserire
			-> colo colore label
			-> bord bordo riservato all'esterno
			-> shad tipo di cornice
				Gtk.SHADOW_NONE, Gtk.SHADOW_IN, Gtk.SHADOW_OUT, 
				Gtk.SHADOW_ETCHED_IN, Gtk.SHADOW_ETCHED_OUT
			-> tBox tipo di contenitore v/h interno 
			-> aBox attributi del contenitore interno
			-> xtBox tipo di contenitore v/h esterno 
			-> xaBox attributi del contenitore esterno
			-> show abilita la visione della cornice
		"""
	#frame
		if name != "":
			name = " "+name+" "

		# nasconde il bordo e il nome del frame
		if show==False:
			bord=0
			aBox=[False, False, 0]
			name = ""
			shad = Gtk.SHADOW_NONE

		fram = Gtk.Frame(label=name)
		# la rendo visibile
		fram.show()
		# imposto il bordo (esterno)
		fram.set_border_width(bord)
		fram.set_shadow_type(shad)
	#label
		# referenzio la label della Frame
		labe = fram.get_label_widget()
		# attivo il markup
		labe.set_markup("<b>%s</b>" %name)
		# imposto il colore
		labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse(colo))
	#myBox (interno)
		xBox = myBox1(tBox)
		fram.add(xBox)
	#object
		if obje != None:
			#(child, expand=False, fill=False, padding=1)
			xBox.pack_start(obje, *aBox)
	#myBox (esterno)
		if (xtBox == 'v') or (xtBox == 'h'):  
			yBox = myBox1(xtBox)
			#(child, expand=False, fill=False, padding=1)
			yBox.pack_start(fram, *xaBox)
	# <-
			return yBox, [labe, xBox, fram]
		else:    
	# <-
			return fram, [labe, xBox]

Il primo attributo **name** viene usato per impostare la label della cornice se presente. Inoltre per enfatizzare la label sfruttiamo la possibilità di attivare il **markup** e modificare il colore.

.. code-block:: python

	#label
		# referenzio la label della Frame
		labe = fram.get_label_widget()
		# attivo il markup
		labe.set_markup("<b>%s</b>" %name)
		# imposto il colore
		labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse(colo))

Il secondo attributo **obje** serve a passare un oggetto da inserire nel nostro contenitore. Questo comunque lo possiamo fare anche in un secondo momento.

Gli attributi **bord** e **shad** decidono rispettivamente lo spessore della cornice e la tipologia della stessa.

**xBox**

All' interno della nostra cornice inseriamo un contenitore per avere più flessibilità di gestione del suo comportamento. Qui passiamo come parametri il tipo di contenitore scelto e la lista dei parametri di inserimento dell' oggetto stesso.

.. code-block:: python

	#(child, expand=False, fill=False, padding=1)
	tBox='v', aBox=[False, False, 1],

**xtBox**

Nello stesso modo passiamo i parametri per un' altro contenitore che verrà istanziato solo se passiamo l' attributo valido 'v' o 'h'. Questo contenitore serve solo quando abbiamo la necessità che la nostra cornice non si espandi per tutta l' area orizzontale se si trova in un contenitore verticale, o per tutta l' area verticale se si trova in un contenitore orizzontale.

**show**

Per finire ho inserito l' attributo **show** che serve ad abilitare la visualizzazione della cornice. Vi chiederete ma che senso ha. Se faccio una cornice e poi la nascondo. Nel nostro caso serve solo di supporto per capire come funzionano i contenitori. Lo scopo finale che mi sono prefisso è quello di costruire un framework (una struttura) per sviluppare un template di una applicazione generica di base.

.. figure:: myWind.png
	:align: right

**myWind**

Se proviamo ad avviare lo script **myWind.py** vediamo la nostra prima applicazione con i contenitori visibili e riconoscibili dalle loro labels.

Saluti
------

Ok per oggi abbiamo finito.

Nel prossimo post vedremo la struttura completa di una applicazione base.

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
