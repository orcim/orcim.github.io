#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myBox1
	- myFrame1
	- myWind
"""

myRev = "(rev.150820)"
# modificato deb in show
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# myDefines
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

#-----------------------------------------------------------------------------
def myFrame1(name='myFrame', obje=None, colo='blue',
			bord=2, shad=Gtk.SHADOW_ETCHED_OUT, 
			tBox='v', aBox=[False, False, 1],
			xtBox='', xaBox=[False, False, 1],
			show=False ):
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

#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------
class MyWind(Gtk.Window):
	""" + window (self)                         .------------------------.
	"     - vBox                                | vertical               |
	"       - hBox                              |   .--------------------.
	"                                           |   | horizontal         |
	"                                           |   |                    |
	"                                           .---.--------------------.
	"""
	def __init__(self, width=None, height=400, title="myWind", center=True, color=""):
		# inizializzo l'ogetto da cui derivo
		super(MyWind, self).__init__()

		# referenzio gli attributi passati
		self.title = title
		self.width = width
		self.height = height

		# imposto il nome dell'oggetto uguale al titolo
		self.set_name(title)
		# imposta il titolo dell'applicazione
		self.set_title(self.title)

		# dimensiono se viene passato almeno l'ampiezza
		if width != None:
			self.resize(width, height)
		# se richiesto centro la posizione
		if center:
			self.set_position(Gtk.WindowPosition.CENTER)

		# callback di uscita da envento
		self.connect("delete-event", Gtk.main_quit)
		# intercettiamo la tastiera
		self.connect("key_press_event", self.doKeyPress)

		#vBox (istanza un contenitore verticale)
		self.vBox = Gtk.VBox(homogeneous=False, spacing=0)
		self.add(self.vBox)
		#hBox (istanza un contenitore orizzontale)
		self.hBox = Gtk.HBox(homogeneous=False, spacing=0)
		self.vBox.pack_start(child=self.hBox, expand=False, fill=False, padding=0)

		# se passato cambio colore
		if color:
			# change background color to Class
			chaBackColor(obj=self, css=title, col=color)
		# visualizza il tutto
		self.show_all()

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

#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01():
	# istanza l'applicazione 
	#  (width=None, height=400, title="myWind", center=True, color="")
	self = MyWind(title="myWind", color="#aaa")

	# attributes
	colo="#333333"
	bord=2 			# external
	expa=False
	fill=False
	padd=1 			# internal
	show=True

#aBox (application)
	# fram,[labe,xBox]
	aObj, oth1 = myFrame1(name='application', obje=None, colo=colo,
						bord=bord, shad=Gtk.SHADOW_IN,
						tBox='h', aBox=[expa, fill, padd],
						#xtBox='h', xaBox=[expa, fill, padd],
						show=show )
	self.aBox = oth1[1]

	# inserimento nel contenitore
	self.vBox.pack_start(child=aObj, expand=False, fill=False, padding=0)

#gBox (aBox/global)
	# fram,[labe,xBox]
	gObj, oth1 = myFrame1(name='global', obje=None, colo=colo,
						bord=bord, shad=Gtk.SHADOW_IN,
						tBox='h', aBox=[expa, fill, padd],
						#xtBox='h', xaBox=[expa, fill, padd],
						show=show )
	self.gBox = oth1[1]

	# inserimento nel contenitore
	self.vBox.pack_start(child=gObj, expand=False, fill=False, padding=0)

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	# test arguments
	if len(sys.argv) == 1:
		# no arguments (scelgo io)
		choi = 1
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	if choi == 1:   # (MyWind)
		# draw window
		myTry01()

	# avvia applicazione
	Gtk.main()
