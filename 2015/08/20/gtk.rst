Gtk
===

Perchè Gtk e non Qt o altro?

Quando ho iniziato a programmare in modalità grafica le Qt non erano ancora proprio libere. Ma non solo. In **linux** io preferisco Gnome a Kde perciò è venuto del tutto naturale la scelta. A distanza di anni non me ne pento. Anche se una volta compreso il loro funzionamento si scopre che passare da un ambiente ad un altro non è così difficile perchè i motori che girano sotto sono molto simili.

.. more::

Quando ho iniziato c' erano solo le gtk poi sono arrivate le gtk3.
Il passaggio è quasi immediato ma ci vuole un pò di pazienza su alcune ridefinizioni.
Non ho mai capito perchè hanno voluto rinominarle senza fare una retro compatibilità.

Visto che non c'è la facciamo noi.

Esempio

.. code-block:: python

	#-----------------------------------------------------------------------------
	# Gtk2 = Gtk3
	#-----------------------------------------------------------------------------
	Gtk.ICON_SIZE_MENU = Gtk.IconSize.MENU
	Gtk.ICON_SIZE_BUTTON = Gtk.IconSize.BUTTON

Un altro metodo che scelgo sempre di usare è quello di creare un file **my00init.py**
dove all' interno inserisco i richiami dei moduli più usati e inoltre aggiungo alcune definizioni che normalmente utilizzo spesso.

Esempio: **my00init.py**

.. literalinclude:: my00init.py
    :language: python

**link**

	:download:`download <my00init.py>`

Dopo di che non faccio altro che inserire la direttiva in tutti i miei files:

.. code-block:: python

	#-----------------------------------------------------------------------------
	# Modules
	#-----------------------------------------------------------------------------
	from my00init import *

Qualcuno avrà qualcosa da ridere in questo modo di fare.

Dialogs
-------

Nel file precedente ho introdotto il primo metodo che usa le **GTK**.
In particolare le **dialogs** servono quando dobbiamo interagire con l' utente.

Le **dialogs** sono un particolare oggetto che normalmente blocca l' esecuzione del programma principale per attendere una risposta dall' utente. 

In gergo chiamato **modale** o **non modale**.

.. note:: Da un pò di tempo si è deciso di non visualizzare più di default le icone degli oggetti. Per questo bisogna abilitarli tramite l' apposita funzione quando desiderato.

Windows
-------

Bene ora che abbiamo il nostro **init** passiamo alla prima applicazione.

Esempio: **myWind.py**

.. literalinclude:: myWind.py
    :language: python

**link**

	:download:`download <myWind.py>`

Per creare un' applicazione grafica di solito si parte ereditando dalla classe madre:

**Gtk.Window**

Subito dopo si definisce il metodo **__init__()** che serve ad inizializzare l' oggetto che stiamo definendo. La prima cosa da fare è richiamare l' inizializzazione del genitore col metodo **super** ed infine si inizia a definire gli attributi e le altre definizioni che caratterizzeranno la nostra classe.

Descrizione
-----------

Iniziamo col descrivere le cose più salienti.

Callback
--------

Le **callbacks** in python non sono altro che dei metodi richiamati da un evento ad essi associati.

Esempio

.. code-block:: python

	# callback di uscita da envento
	self.connect("delete-event", Gtk.main_quit)

Come si può leggere dal codice qui sopra la chiave **connect** lega l' evento definito come **delete-event** al metodo **Gtk.main_quit** che serve per uscire dall' esecuzione della nostra applicazione.

Start
-----

Si perchè in python l' applicazione principale va in esecuzione alla chiamata 

**Gtk.main** 

che altro non è che il loop principale della nostra applicazione. 

Stop
----

Invece viene interrotta dalla chiamata di 

**Gtk.main_quit**

Event/Signal
------------

**delete-event** invece è un evento che viene inviato quando l' utente richiede di chiudere la finestra cliccando col mouse sul pulsante [x] che di solito si trova in
alto a destra della finestra stessa.

.. note:: A volte si vuol differenziare eventi da segnali come messaggi emessi da soggetti diversi. 

**Event** => **Widgets** oggetto visibile (es: pulsante). 

**Signal** => **Objects** oggetto non visibile (es: tastiera).

Keyboard
--------

Noi da bravi programmatori diamo la possibilità di chiudere la finestra anche usando solo la tastiera. Il tasto principe per la fuga è nominato **Escape**. Questo perchè ritengo, e non solo io, che l' uso della tastiera in molti casi sia più veloce che l' uso del buon mouse.

In questo caso ho dovuto definire il metodo per intercettare l' avvenuta pressione del tasto interessato. E per altre eventuali intercettazioni ho previsto anche la verifica del tasto **Ctrl**.

Esempio

.. code-block:: python

	def doKeyPress(self, widget, event):
		# intercetto tasto speciale ctrl
		if (event.state == Gdk.ModifierType.CONTROL_MASK):
			#print "Ctrl", Gdk.keyval_name(event.keyval)
			pass
		else:
			# intercetto tasto normale
			keyname = Gdk.keyval_name(event.keyval)
			#print "the button %s was pressed" % keyname
			if keyname == "Escape":
				# richiesta di uscita dal programma
				Gtk.main_quit()

L'associazione della callback è la seguente.

.. code-block:: python

	# intercettiamo la tastiera
	self.connect("key_press_event", self.doKeyPress)

Saluti
------

Ok per oggi finiamo quì.

I commenti di **Box** e **Frame** li vediamo alla prossima**

Ciao alla prossima. (stay tune!)

.. author:: default
.. categories:: programming
.. tags:: programming, python, gtk
.. comments::
